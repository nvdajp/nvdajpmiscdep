# -*- coding: utf-8 -*-


try:
    from ._nvdajp_unicode import unicode_normalize
except (ImportError, ValueError):
    from _nvdajp_unicode import unicode_normalize  # type: ignore
import re

romadic = [
    # third item is number of morae
    ["ccha", "ッチャ", 2],
    ["cchi", "ッチ", 2],
    ["cchu", "ッチュ", 2],
    ["cche", "ッチェ", 2],
    ["ccho", "ッチョ", 2],
    #
    ["bba", "ッバ", 2],
    ["bbi", "ッビ", 2],
    ["bbu", "ッブ", 2],
    ["bbe", "ッベ", 2],
    ["bbo", "ッボ", 2],
    #
    ["dda", "ッダ", 2],
    ["ddi", "ッジ", 2],
    ["ddu", "ッヅ", 2],
    ["dde", "ッデ", 2],
    ["ddo", "ッド", 2],
    #
    ["ffa", "ッファ", 2],
    ["ffi", "ッフィ", 2],
    ["ffu", "ッフ", 2],
    ["ffe", "ッフェ", 2],
    ["ffo", "ッフォ", 2],
    #
    ["gga", "ッガ", 2],
    ["ggi", "ッギ", 2],
    ["ggu", "ッグ", 2],
    ["gge", "ッゲ", 2],
    ["ggo", "ッゴ", 2],
    #
    ["hha", "ッハ", 2],
    ["hhi", "ッヒ", 2],
    ["hhu", "ッフ", 2],
    ["hhe", "ッヘ", 2],
    ["hho", "ッホ", 2],
    #
    ["jja", "ッジャ", 2],
    ["jji", "ッジ", 2],
    ["jju", "ッジュ", 2],
    ["jje", "ッジェ", 2],
    ["jjo", "ッジョ", 2],
    #
    ["kka", "ッカ", 2],
    ["kki", "ッキ", 2],
    ["kku", "ック", 2],
    ["kke", "ッケ", 2],
    ["kko", "ッコ", 2],
    #
    ["ppa", "ッパ", 2],
    ["ppi", "ッピ", 2],
    ["ppu", "ップ", 2],
    ["ppe", "ッペ", 2],
    ["ppo", "ッポ", 2],
    #
    ["ssa", "ッサ", 2],
    ["ssi", "ッシ", 2],
    ["ssu", "ッス", 2],
    ["sse", "ッセ", 2],
    ["sso", "ッソ", 2],
    #
    ["tta", "ッタ", 2],
    ["tti", "ッチ", 2],
    ["ttu", "ッツ", 2],
    ["tte", "ッテ", 2],
    ["tto", "ット", 2],
    #
    ["zza", "ッザ", 2],
    ["zzi", "ッジ", 2],
    ["zzu", "ッズ", 2],
    ["zze", "ッゼ", 2],
    ["zzo", "ッゾ", 2],
    #
    ["cha", "チャ", 1],
    ["chu", "チュ", 1],
    ["cho", "チョ", 1],
    #
    ["tsu", "ツ", 1],
    #
    ["tya", "チャ", 1],
    ["tyu", "チュ", 1],
    ["tyo", "チョ", 1],
    #
    ["jya", "ジャ", 1],
    ["jyu", "ジュ", 1],
    ["jyo", "ジョ", 1],
    #
    ["kya", "キャ", 1],
    ["kyu", "キュ", 1],
    ["kyo", "キョ", 1],
    ["gya", "ギャ", 1],
    ["gyu", "ギュ", 1],
    ["gyo", "ギョ", 1],
    #
    ["shi", "シ", 1],
    #
    ["sya", "シャ", 1],
    ["syu", "シュ", 1],
    ["syo", "ショ", 1],
    #
    ["sha", "シャ", 1],
    ["shu", "シュ", 1],
    ["sho", "ショ", 1],
    #
    ["chi", "チ", 1],
    #
    ["nya", "ニャ", 1],
    ["nyu", "ニュ", 1],
    ["nyo", "ニョ", 1],
    #
    ["hya", "ヒャ", 1],
    ["hyu", "ヒュ", 1],
    ["hyo", "ヒョ", 1],
    #
    ["pya", "ピャ", 1],
    ["pyu", "ピュ", 1],
    ["pyo", "ピョ", 1],
    #
    ["mya", "ミャ", 1],
    ["myu", "ミュ", 1],
    ["myo", "ミョ", 1],
    #
    ["rya", "リャ", 1],
    ["ryu", "リュ", 1],
    ["ryo", "リョ", 1],
    #
    ["sa", "サ", 1],
    ["si", "シ", 1],
    ["ka", "カ", 1],
    ["ki", "キ", 1],
    ["ku", "ク", 1],
    ["ke", "ケ", 1],
    ["ko", "コ", 1],
    #
    ["ga", "ガ", 1],
    ["gi", "ギ", 1],
    ["gu", "グ", 1],
    ["ge", "ゲ", 1],
    ["go", "ゴ", 1],
    ["su", "ス", 1],
    ["se", "セ", 1],
    ["so", "ソ", 1],
    #
    ["za", "ザ", 1],
    ["zi", "ジ", 1],
    ["ji", "ジ", 1],
    ["zu", "ズ", 1],
    ["ze", "ゼ", 1],
    ["zo", "ゾ", 1],
    #
    ["ja", "ジャ", 1],
    ["ju", "ジュ", 1],
    ["jo", "ジョ", 1],
    #
    ["ta", "タ", 1],
    ["ti", "チ", 1],
    ["tu", "ツ", 1],
    ["te", "テ", 1],
    ["to", "ト", 1],
    #
    ["da", "ダ", 1],
    ["di", "ヂ", 1],
    ["du", "ヅ", 1],
    ["de", "デ", 1],
    ["do", "ド", 1],
    #
    ["na", "ナ", 1],
    ["ni", "ニ", 1],
    ["nu", "ヌ", 1],
    ["ne", "ネ", 1],
    ["no", "ノ", 1],
    #
    ["nn", "ン", 1],
    #
    ["ha", "ハ", 1],
    ["hi", "ヒ", 1],
    ["hu", "フ", 1],
    ["he", "ヘ", 1],
    ["ho", "ホ", 1],
    #
    ["fa", "ファ", 1],
    ["fi", "フィ", 1],
    ["fu", "フ", 1],
    ["fe", "フェ", 1],
    ["fo", "フォ", 1],
    #
    ["ba", "バ", 1],
    ["bi", "ビ", 1],
    ["bu", "ブ", 1],
    ["be", "ベ", 1],
    ["bo", "ボ", 1],
    #
    ["pa", "パ", 1],
    ["pi", "ピ", 1],
    ["pu", "プ", 1],
    ["pe", "ペ", 1],
    ["po", "ポ", 1],
    #
    ["ma", "マ", 1],
    ["mi", "ミ", 1],
    ["mu", "ム", 1],
    ["me", "メ", 1],
    ["mo", "モ", 1],
    #
    ["ya", "ヤ", 1],
    ["yu", "ユ", 1],
    ["yo", "ヨ", 1],
    #
    ["ra", "ラ", 1],
    ["ri", "リ", 1],
    ["ru", "ル", 1],
    ["re", "レ", 1],
    ["ro", "ロ", 1],
    #
    ["wa", "ワ", 1],
    ["wi", "ウィ", 1],
    ["wo", "オ", 1],
    #
    ["a", "ア", 1],
    ["i", "イ", 1],
    ["u", "ウ", 1],
    ["e", "エ", 1],
    ["o", "オ", 1],
    #
    ["n", "ン", 1],
]


def getKanaFromRoma(roma):
    kana = unicode_normalize(roma)
    if kana in ("youtube",):
        return None
    for item in romadic:
        kana = kana.replace(item[0], item[1])
    if all([re.search("[ァ-ヾ]", c) for c in kana]):
        return kana
    return None
