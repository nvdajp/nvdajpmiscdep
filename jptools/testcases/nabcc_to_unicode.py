# py -3.7-32 nabcc_to_unicode.py BRL.txt unicode.txt
import sys

# from liblouis text_nabcc.dis
table_text = """
display \x0000 478      #   0 ^@   NULL
display \x0001 178      #   1 ^A   START OF HEADING
display \x0002 1278     #   2 ^B   START OF TEXT
display \x0003 1478     #   3 ^C   END OF TEXT
display \x0004 14578    #   4 ^D   END OF TRANSMISSION
display \x0005 1578     #   5 ^E   ENQUIRY
display \x0006 12478    #   6 ^F   ACKNOWLEDGE
display \x0007 124578   #   7 ^G   BELL
display \x0008 12578    #   8 ^H   BACKSPACE
display \x0009 2478     #   9 ^I   HORIZONTAL TABULATION
display \x000a 24578    #  10 ^J   LINE FEED
display \x000b 1378     #  11 ^K   VERTICAL TABULATION
display \x000c 12378    #  12 ^L   FORM FEED
display \x000d 13478    #  13 ^M   CARRIAGE RETURN
display \x000e 134578   #  14 ^N   SHIFT OUT
display \x000f 13578    #  15 ^O   SHIFT IN
display \x0010 123478   #  16 ^P   DATA LINK ESCAPE
display \x0011 1234578  #  17 ^Q   DEVICE CONTROL ONE
display \x0012 123578   #  18 ^R   DEVICE CONTROL TWO
display \x0013 23478    #  19 ^S   DEVICE CONTROL THREE
display \x0014 234578   #  20 ^T   DEVICE CONTROL FOUR
display \x0015 13678    #  21 ^U   NEGATIVE ACKNOWLEDGE
display \x0016 123678   #  22 ^V   SYNCHRONOUS IDLE
display \x0017 245678   #  23 ^W   END OF TRANSMISSION BLOCK
display \x0018 134678   #  24 ^X   CANCEL
display \x0019 1345678  #  25 ^Y   END OF MEDIUM
display \x001a 135678   #  26 ^Z   SUBSTITUTE
display \x001b 24678    #  27 ^[   ESCAPE
display \x001c 125678   #  28 ^\   FILE SEPARATOR
display \x001d 1245678  #  29 ^]   GROUP SEPARATOR
display \x001e 4578     #  30 ^^   RECORD SEPARATOR
display \x001f 45678    #  31 ^_   UNIT SEPARATOR
display \x0020 0        #  32      SPACE
display \x0021 2346     #  33 !    EXCLAMATION MARK
display \x0022 5        #  34 "    QUOTATION MARK
display \x0023 3456     #  35 #    NUMBER SIGN
display \x0024 1246     #  36 $    DOLLAR SIGN
display \x0025 146      #  37 %    PERCENT SIGN
display \x0026 12346    #  38 &    AMPERSAND
display \x0027 3        #  39 '    APOSTROPHE
display \x0028 12356    #  40 (    LEFT PARENTHESIS
display \x0029 23456    #  41 )    RIGHT PARENTHESIS
display \x002a 16       #  42 *    ASTERISK
display \x002b 346      #  43 +    PLUS SIGN
display \x002c 6        #  44 ,    COMMA
display \x002d 36       #  45 -    HYPHEN-MINUS
display \x002e 46       #  46 .    FULL STOP
display \x002f 34       #  47 /    SOLIDUS
display \x0030 356      #  48 0    DIGIT ZERO
display \x0031 2        #  49 1    DIGIT ONE
display \x0032 23       #  50 2    DIGIT TWO
display \x0033 25       #  51 3    DIGIT THREE
display \x0034 256      #  52 4    DIGIT FOUR
display \x0035 26       #  53 5    DIGIT FIVE
display \x0036 235      #  54 6    DIGIT SIX
display \x0037 2356     #  55 7    DIGIT SEVEN
display \x0038 236      #  56 8    DIGIT EIGHT
display \x0039 35       #  57 9    DIGIT NINE
display \x003a 156      #  58 :    COLON
display \x003b 56       #  59 ;    SEMICOLON
display \x003c 126      #  60 <    LESS-THAN SIGN
display \x003d 123456   #  61 =    EQUALS SIGN
display \x003e 345      #  62 >    GREATER-THAN SIGN
display \x003f 1456     #  63 ?    QUESTION MARK
display \x0040 47       #  64 @    COMMERCIAL AT
display \x0041 17       #  65 A    LATIN CAPITAL LETTER A
display \x0042 127      #  66 B    LATIN CAPITAL LETTER B
display \x0043 147      #  67 C    LATIN CAPITAL LETTER C
display \x0044 1457     #  68 D    LATIN CAPITAL LETTER D
display \x0045 157      #  69 E    LATIN CAPITAL LETTER E
display \x0046 1247     #  70 F    LATIN CAPITAL LETTER F
display \x0047 12457    #  71 G    LATIN CAPITAL LETTER G
display \x0048 1257     #  72 H    LATIN CAPITAL LETTER H
display \x0049 247      #  73 I    LATIN CAPITAL LETTER I
display \x004a 2457     #  74 J    LATIN CAPITAL LETTER J
display \x004b 137      #  75 K    LATIN CAPITAL LETTER K
display \x004c 1237     #  76 L    LATIN CAPITAL LETTER L
display \x004d 1347     #  77 M    LATIN CAPITAL LETTER M
display \x004e 13457    #  78 N    LATIN CAPITAL LETTER N
display \x004f 1357     #  79 O    LATIN CAPITAL LETTER O
display \x0050 12347    #  80 P    LATIN CAPITAL LETTER P
display \x0051 123457   #  81 Q    LATIN CAPITAL LETTER Q
display \x0052 12357    #  82 R    LATIN CAPITAL LETTER R
display \x0053 2347     #  83 S    LATIN CAPITAL LETTER S
display \x0054 23457    #  84 T    LATIN CAPITAL LETTER T
display \x0055 1367     #  85 U    LATIN CAPITAL LETTER U
display \x0056 12367    #  86 V    LATIN CAPITAL LETTER V
display \x0057 24567    #  87 W    LATIN CAPITAL LETTER W
display \x0058 13467    #  88 X    LATIN CAPITAL LETTER X
display \x0059 134567   #  89 Y    LATIN CAPITAL LETTER Y
display \x005a 13567    #  90 Z    LATIN CAPITAL LETTER Z
display \x005b 2467     #  91 [    LEFT SQUARE BRACKET
display \x005c 12567    #  92 \    REVERSE SOLIDUS
display \x005d 124567   #  93 ]    RIGHT SQUARE BRACKET
display \x005e 457      #  94 ^    CIRCUMFLEX ACCENT
display \x005f 456      #  95 _    LOW LINE
display \x0060 4        #  96 `    GRAVE ACCENT
display \x0061 1        #  97 a    LATIN SMALL LETTER A
display \x0062 12       #  98 b    LATIN SMALL LETTER B
display \x0063 14       #  99 c    LATIN SMALL LETTER C
display \x0064 145      # 100 d    LATIN SMALL LETTER D
display \x0065 15       # 101 e    LATIN SMALL LETTER E
display \x0066 124      # 102 f    LATIN SMALL LETTER F
display \x0067 1245     # 103 g    LATIN SMALL LETTER G
display \x0068 125      # 104 h    LATIN SMALL LETTER H
display \x0069 24       # 105 i    LATIN SMALL LETTER I
display \x006a 245      # 106 j    LATIN SMALL LETTER J
display \x006b 13       # 107 k    LATIN SMALL LETTER K
display \x006c 123      # 108 l    LATIN SMALL LETTER L
display \x006d 134      # 109 m    LATIN SMALL LETTER M
display \x006e 1345     # 110 n    LATIN SMALL LETTER N
display \x006f 135      # 111 o    LATIN SMALL LETTER O
display \x0070 1234     # 112 p    LATIN SMALL LETTER P
display \x0071 12345    # 113 q    LATIN SMALL LETTER Q
display \x0072 1235     # 114 r    LATIN SMALL LETTER R
display \x0073 234      # 115 s    LATIN SMALL LETTER S
display \x0074 2345     # 116 t    LATIN SMALL LETTER T
display \x0075 136      # 117 u    LATIN SMALL LETTER U
display \x0076 1236     # 118 v    LATIN SMALL LETTER V
display \x0077 2456     # 119 w    LATIN SMALL LETTER W
display \x0078 1346     # 120 x    LATIN SMALL LETTER X
display \x0079 13456    # 121 y    LATIN SMALL LETTER Y
display \x007a 1356     # 122 z    LATIN SMALL LETTER Z
display \x007b 246      # 123 {    LEFT CURLY BRACKET
display \x007c 1256     # 124 |    VERTICAL LINE
display \x007d 12456    # 125 }    RIGHT CURLY BRACKET
display \x007e 45       # 126 ~    TILDE
display \x007f 4567     # 127 ^?   DELETE
""".split("\n")

table_dict = {}
for line in table_text:
    items = line.split(" ")[1:3]
    if items:
        ch = int(items[0][1:], 16)
        cell = items[1]
        val = 0
        if '1' in cell: val |= 1
        if '2' in cell: val |= 2
        if '3' in cell: val |= 4
        if '4' in cell: val |= 8
        if '5' in cell: val |= 0x10
        if '6' in cell: val |= 0x20
        if '7' in cell: val |= 0x40
        if '8' in cell: val |= 0x80
        if val:
            val |= 0x2800
        else:
            val = 0x20
        table_dict[chr(ch).swapcase()] = chr(val)

table = str.maketrans(table_dict)

with open(sys.argv[1]) as f:
    with open(sys.argv[2], "w", encoding="utf-8") as wf:
        for line in f.readlines():
            line = line.rstrip().translate(table) + "\n"
            wf.write(line)
