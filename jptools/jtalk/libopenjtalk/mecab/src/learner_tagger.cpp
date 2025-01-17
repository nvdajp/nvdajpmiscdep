//  MeCab -- Yet Another Part-of-Speech and Morphological Analyzer
//
//
//  Copyright(C) 2001-2006 Taku Kudo <taku@chasen.org>
//  Copyright(C) 2004-2006 Nippon Telegraph and Telephone Corporation
#include <functional>
#include <algorithm>
#include <iterator>
#include <iostream>
#include <vector>

#include "learner_node.h"
#include "learner_tagger.h"
#include "utils.h"
#include "common.h"

namespace MeCab {
namespace {
char *mystrdup(const char *str) {
  size_t l = std::strlen(str);
  char *r = new char[l + 1];
  std::strncpy(r, str, l+1);
  return r;
}

char *mystrdup(const std::string &str) {
  return mystrdup(str.c_str());
}
}

bool EncoderLearnerTagger::open(LearnerTokenizer      *p0,
                                FreeList<LearnerPath> *p1,
                                FeatureIndex          *p2,
                                size_t eval_size,
                                size_t unk_eval_size) {
  close();
  tokenizer_      = p0;
  path_freelist_  = p1;
  feature_index_  = p2;
  eval_size_     = eval_size;
  unk_eval_size_ = unk_eval_size;
  return true;
}

bool DecoderLearnerTagger::open(const Param &param) {
  close();
  path_freelist__.reset(new FreeList<LearnerPath>(BUF_SIZE));
  tokenizer__.reset(new LearnerTokenizer());
  feature_index__.reset(new DecoderFeatureIndex);
  path_freelist_ = path_freelist__.get();
  tokenizer_ = tokenizer__.get();
  feature_index_ = feature_index__.get();

  CHECK_CLOSE_FALSE(tokenizer_->open(param)) << tokenizer_->what();

  CHECK_CLOSE_FALSE(feature_index_->open(param)) << feature_index_->what();

  return true;
}

bool EncoderLearnerTagger::read(std::istream *is,
                                std::vector<double> *observed) {
  char line[BUF_SIZE];
  char *column[8];
  std::string sentence = "";
  std::vector<LearnerNode *> corpus;
  ans_path_list_.clear();

  bool eos = false;

  for (;;) {
    if (!is->getline(line, sizeof(line))) {
      is->clear(std::ios::eofbit|std::ios::badbit);
      return true;
    }

    eos = (std::strcmp(line, "EOS") == 0 || line[0] == '\0');

    LearnerNode *m = new LearnerNode;
    std::memset(m, 0, sizeof(LearnerNode));

    if (eos) {
      m->stat = MECAB_EOS_NODE;
    } else {
      size_t _size = tokenize(line, "\t", column, 2);
      CHECK_FALSE(_size == 2) << "format error: " << line;
      m->stat    = MECAB_NOR_NODE;
      m->surface = mystrdup(column[0]);
      m->feature = mystrdup(column[1]);
      m->length  = m->rlength = std::strlen(column[0]);
    }

    corpus.push_back(m);

    if (eos) break;

    sentence += std::string(column[0]);
  }

  CHECK_FALSE(!sentence.empty()) << "empty sentence";

  CHECK_FALSE(eos) << "\"EOS\" is not found";

  begin__.reset_string(sentence);
  begin_ = begin__.get();

  initList();

  size_t pos = 0;
  for (size_t i = 0; corpus[i]->stat != MECAB_EOS_NODE; ++i) {
    LearnerNode *found = 0;
    for (LearnerNode *node = lookup(pos); node; node = node->bnext) {
      if ( node_cmp_eq(*(corpus[i]), *node, eval_size_, unk_eval_size_) ) {
        found = node;
        break;
      }
    }

    // cannot find node even using UNKNOWN WORD PROSESSING
    if (!found) {
      LearnerNode *node = tokenizer_->getNewNode();
      node->surface  = begin_ + pos;
      node->length   = node->rlength = std::strlen(corpus[i]->surface);
      node->feature  = feature_index_->strdup(corpus[i]->feature);
      node->stat     = MECAB_NOR_NODE;
      node->fvector  = 0;
      node->wcost    = 0.0;
      node->bnext    = beginNodeList_[pos];
      beginNodeList_[pos] = node;
      std::cout << "adding virtual node: " << node->feature << std::endl;
    }

    pos += corpus[i]->length;
  }

  buildLattice();

  LearnerNode* prev = endNodeList_[0];  // BOS
  prev->anext = 0;
  pos = 0;

  for (size_t i = 0; i < corpus.size(); ++i) {
    LearnerNode *rNode = 0;
    for (LearnerNode *node = beginNodeList_[pos]; node; node = node->bnext) {
      if (corpus[i]->stat == MECAB_EOS_NODE ||
          node_cmp_eq(*(corpus[i]), *node, eval_size_, unk_eval_size_) )
        rNode = node;  // take last node
    }

    LearnerPath *lpath = 0;
    for (LearnerPath *path = rNode->lpath; path; path = path->lnext)
      if (prev == path->lnode) {
        lpath = path;
        break;
      }

    CHECK_DIE(lpath->fvector) << "lpath is NULL";
    for (const int *f = lpath->fvector; *f != -1; ++f) {
      if (*f >= static_cast<long>(observed->size()))
        observed->resize(*f + 1);
      ++(*observed)[*f];
    }

    if (lpath->rnode->stat != MECAB_EOS_NODE) {
      for (const int *f = lpath->rnode->fvector; *f != -1; ++f) {
        if (*f >= static_cast<long>(observed->size()))
          observed->resize(*f + 1);
        ++(*observed)[*f];
      }
    }

    ans_path_list_.push_back(lpath);

    prev->anext = rNode;
    prev = rNode;

    if (corpus[i]->stat == MECAB_EOS_NODE) break;

    pos += std::strlen(corpus[i]->surface);
  }

  prev->anext = beginNodeList_[len_];  // connect to EOS
  beginNodeList_[len_]->anext = 0;

  for (size_t i = 0 ; i < corpus.size(); ++i) {
    delete [] corpus[i]->surface;
    delete [] corpus[i]->feature;
    delete corpus[i];
  }

  return true;
}

int EncoderLearnerTagger::eval(size_t *crr,
                               size_t *prec, size_t *recall) const {
  int zeroone = 0;

  LearnerNode *res = endNodeList_[0]->next;
  LearnerNode *ans = endNodeList_[0]->anext;

  size_t resp = 0;
  size_t ansp = 0;

  while (ans->anext && res->next) {
    if (resp == ansp) {
      if (node_cmp_eq(*ans, *res, eval_size_, unk_eval_size_)) {
        ++(*crr);  // same
      } else {
        zeroone = 1;
      }
      ++(*prec);
      ++(*recall);
      res = res->next;
      ans = ans->anext;
      resp += res->rlength;
      ansp += ans->rlength;
    } else if (resp < ansp) {
      res = res->next;
      resp += res->rlength;
      zeroone = 1;
      ++(*recall);
    } else {
      ans = ans->anext;
      ansp += ans->rlength;
      zeroone = 1;
      ++(*prec);
    }
  }

  while (ans->anext) {
    ++(*prec);
    ans = ans->anext;
  }

  while (res->next) {
    ++(*recall);
    res = res->next;
  }

  return zeroone;
}

bool DecoderLearnerTagger::parse(std::istream* is, std::ostream *os) {
  path_freelist_->free();
  feature_index_->clear();
  tokenizer_->clear();

  if (!begin_) {
    begin__.reset(new char[BUF_SIZE * 16]);
    begin_ = begin__.get();
  }

  if (!is->getline(const_cast<char *>(begin_), BUF_SIZE * 16)) {
    is->clear(std::ios::eofbit|std::ios::badbit);
    return false;
  }

  initList();
  buildLattice();
  viterbi();

  for (LearnerNode *node = endNodeList_[0]->next;
       node->next; node = node->next) {
    os->write(node->surface, node->length);
    *os << '\t' << node->feature << '\n';
  }
  *os << "EOS\n";

  return true;
}

LearnerNode *LearnerTagger::lookup(size_t pos) {
  if (beginNodeList_[pos]) return beginNodeList_[pos];
  LearnerNode *m = tokenizer_->lookup(begin_ + pos, end_);
  beginNodeList_[pos] = m;
  return m;
}

bool LearnerTagger::connect(size_t pos, LearnerNode *_rNode) {
  for (LearnerNode *rNode = _rNode ; rNode; rNode = rNode->bnext) {
    for (LearnerNode *lNode = endNodeList_[pos]; lNode;
         lNode = lNode->enext) {
      LearnerPath *path   = path_freelist_->alloc();
      std::memset(path, 0, sizeof(Path));
      path->rnode   = rNode;
      path->lnode   = lNode;
      path->fvector = 0;
      path->cost    = 0.0;
      path->rnode   = rNode;
      path->lnode   = lNode;
      path->lnext   = rNode->lpath;
      rNode->lpath  = path;
      path->rnext   = lNode->rpath;
      lNode->rpath  = path;
      CHECK_FALSE(feature_index_->buildFeature(path))
          << feature_index_->what();
      CHECK_DIE(path->fvector);
    }
    size_t x = rNode->rlength + pos;
    rNode->enext  = endNodeList_[x];
    endNodeList_[x] = rNode;
  }

  return true;
}

bool LearnerTagger::initList() {
  if (!begin_) return false;

  len_ = std::strlen(begin_);
  end_ = begin_ + len_;

  endNodeList_.resize(len_ + 2);
  std::fill(endNodeList_.begin(), endNodeList_.end(),
            reinterpret_cast<LearnerNode *>(0));

  beginNodeList_.resize(len_ + 2);
  std::fill(beginNodeList_.begin(), beginNodeList_.end(),
            reinterpret_cast<LearnerNode *>(0));

  endNodeList_[0] = tokenizer_->getBOSNode();
  endNodeList_[0]->surface = begin_;
  beginNodeList_[len_] = tokenizer_->getEOSNode();

  return true;
}

bool LearnerTagger::buildLattice() {
  for (int pos = 0; pos <= static_cast<long>(len_);  pos++) {
    if (!endNodeList_[pos]) continue;
    connect(pos, lookup(pos));
  }

  if (!endNodeList_[len_]) {
    beginNodeList_[len_] = lookup(len_);
    for (size_t pos = len_; static_cast<long>(pos) >= 0;  pos--) {
      if (endNodeList_[pos]) {
        connect(pos, beginNodeList_[len_]);
        break;
      }
    }
  }

  return true;
}

bool LearnerTagger::viterbi() {
  for (int pos = 0;   pos <= static_cast<long>(len_);  ++pos) {
    for (LearnerNode *node = beginNodeList_[pos]; node; node = node->bnext) {
      double bestc = -1e37;
      LearnerNode *best = 0;
      feature_index_->calcCost(node);
      for (LearnerPath *path = node->lpath; path; path = path->lnext) {
        feature_index_->calcCost(path);
        double cost = path->cost + path->lnode->cost;
        if (cost > bestc) {
          bestc = cost;
          best  = path->lnode;
        }
      }

      node->prev = best;
      node->cost = bestc;
    }
  }

  LearnerNode *node = beginNodeList_[len_];  // EOS
  for (LearnerNode *prev; node->prev;) {
    prev = node->prev;
    prev->next = node;
    node = prev;
  }

  return true;
}

double EncoderLearnerTagger::gradient(double *expected) {
  viterbi();

  for (int pos = 0;   pos <= static_cast<long>(len_);  ++pos)
    for (LearnerNode *node = beginNodeList_[pos]; node; node = node->bnext)
      calc_alpha(node);

  for (int pos = static_cast<long>(len_); pos >=0;    --pos)
    for (LearnerNode *node = endNodeList_[pos]; node; node = node->enext)
      calc_beta(node);

  double Z = beginNodeList_[len_]->alpha;  // alpha of EOS

  for (int pos = 0;   pos <= static_cast<long>(len_);  ++pos)
    for (LearnerNode *node = beginNodeList_[pos]; node; node = node->bnext)
      for (LearnerPath *path = node->lpath; path; path = path->lnext)
        calc_expectation(path, expected, Z);

  for (size_t i = 0; i < ans_path_list_.size(); ++i)
    Z -= ans_path_list_[i]->cost;

  return Z;
}

double EncoderLearnerTagger::online_update(double *expected) {
  viterbi();

  LearnerNode *prev = endNodeList_[0];
  for (LearnerNode *node = prev->next; node; node = node->next) {
    for (LearnerPath *path = node->lpath; path; path = path->lnext) {
      if (prev == path->lnode) {
        calc_online_update(path, expected);
        break;
      }
    }
    prev = node;
  }

  return 0.0;
}
}
