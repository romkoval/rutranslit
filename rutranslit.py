# -*- coding: utf-8 -*-

import sys

translate_tab = {
u'А': 'A',
u'Б': 'B',
u'В': 'V',
u'Г': 'G',
u'Д': 'D',
u'Е': 'E',
u'З': 'Z',
u'И': 'I',
u'Й': 'Y',
u'К': 'K',
u'Л': 'L',
u'М': 'M',
u'Н': 'N',
u'О': 'O',
u'П': 'P',
u'Р': 'R',
u'С': 'S',
u'Т': 'T',
u'У': 'U',
u'Ф': 'F',
u'Ы': 'Y',
u'Э': 'E',
u'Ь': '',
u'Ъ': '',
u'Ж':'ZH',
u'Х':'KH',
u'Ц':'TS',
u'Ч':'CH',
u'Ш':'SH',
u'Щ':'SH',
u'Ю':'YU',
u'Я':'YA',
u'Ё':'YO'
u'а': 'a',
u'б': 'b',
u'в': 'v',
u'г': 'g',
u'д': 'd',
u'е': 'e',
u'з': 'z',
u'и': 'i',
u'й': 'y',
u'к': 'k',
u'л': 'l',
u'м': 'm',
u'н': 'n',
u'о': 'o',
u'п': 'p',
u'р': 'r',
u'с': 's',
u'т': 't',
u'у': 'u',
u'ф': 'f',
u'ы': 'y',
u'э': 'e',
u'ь': '',
u'ъ': '',
u'ж':'zh',
u'х':'kh',
u'ц':'ts',
u'ч':'ch',
u'ш':'sh',
u'щ':'sh',
u'ю':'yu',
u'я':'ya',
u'ё':'yo'}

def main(filename) :
    f = open(filename)
    for line in f:
        line = line.decode('cp866')
        for ch in line:
            if ch in translate_tab:
                ch = translate_tab.get(ch)
            sys.stdout.write(ch.encode('utf8')) 

    f.close()

if __name__ == '__main__':
    main(sys.argv[1])
