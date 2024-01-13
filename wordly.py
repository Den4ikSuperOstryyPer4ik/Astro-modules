# 	
# 	 @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
# 	@@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
# 	@@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
# 	!@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
# 	@!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
# 	!!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
# 	!!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
# 	:!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
# 	::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
# 	 :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
# 	
#                                             © Copyright 2024
#
#                                    https://t.me/Den4ikSuperOstryyPer4ik
#                                                  and
#                                          https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/WordlyHelper.jpg

import re

import requests

from .. import loader, utils


@loader.tds
class WordlyHelper(loader.Module):
    '''Помощник для игры "Вордли на Русском"'''
    
    strings = {
        "name": "WordlyHelper",
        "not_args": "<emoji document_id=5352594935281360755>🚫</emoji> | <b>Аргументы где?</b>",
        "search": "<emoji document_id=5310041868191407556>🔸</emoji> | Поиск слов...",
        "result": (
            '<emoji document_id=5276288708054624909>🔹</emoji>'
            ' <b>Слова по вашему запросу</b>:\n\n<code>{}</code>\n\n'
            '<emoji document_id=5841711707939933938>🔸</emoji>'
            ' Запрос: <code>{}</code>'
        ),
        "not_found": "<emoji document_id=6334578700012488415>❌</emoji> Не найдено",
        "not_in_db": "<emoji document_id=5352594935281360755>🚫</emoji> | <b>В базе нету слов из {} букв</b> 😠",
    }
    
    async def client_ready(self):
        self.slova = {}
        for i, o in requests.get("https://0x0.st/HNeQ.json").json().items():
            self.slova[i] = [
                word + " "
                for word in o
            ]

    def letters_in_word(self, word: str, letters: list[str]):
        for letter in letters:
            if letter not in word:
                return False
        return True

    def letters_not_in_word(self, word: str, letters: list[str]):
        for letter in letters:
            if letter in word:
                return False
        return True
    
    def get_word(self, marking, _not: list[str] = [], _yes: list[str] = []):
        return [
            i
            for i in utils.array_sum(list(self.slova.values()))
            if re.match(marking.replace("*", "(.)").replace("$", "(.*)") + " ", i)
            and self.letters_in_word(i, _yes)
            and self.letters_not_in_word(i, _not)
        ]
    
    @loader.command()
    async def wordly(self, message):
        """<маркировка слова> [-not <буквы подряд, которых точно нету в слове>] [-yes <буквы подряд, которые точно есть в слове] - Найти слова по маркировке:
        * - одна любая буква
        $ - любое кол-во любых букв
        пример: *т**т -yes оч -not абвгд : отчет
        """
        
        args = utils.get_args(message)
        if not args:
            return await utils.answer(message, self.strings("not_args"))
        
        markirovka = args[0]
        if str(len(markirovka)) not in self.slova:
            return await utils.answer(message, self.strings("not_in_db").format(len(markirovka)))
        
        _not = []
        _yes = []
        
        msg = await utils.answer(message, self.strings("search"))
        
        for arg in args:
            if arg == "-not":
                _not = list(args[args.index(arg)+1])
            if arg == "-yes":
                _yes = list(args[args.index(arg)+1])
        
        return await utils.answer(msg, self.strings("result").format(
            "</code>\n<code>".join(
                self.get_word(markirovka, _not, _yes)
            ) or self.strings("not_found"), " ".join(args)
        ))
    