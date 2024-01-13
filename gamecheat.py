__version__ = (1, 0, 5)
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
# old source: https://github.com/norouzy/Gamee-Cheat
# meta developer: @astromodules
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/GameeCheat.jpg
# meta designer: @XizurK
# requirements: certifi==2022.6.15, charset-normalizer==2.1.0, idna==3.3, requests==2.28.1, urllib3==1.26.10

import hashlib
import random
import re

from telethon.tl.types import Message

from .. import loader, utils


class GameeCheatMod(loader.Module):
	'''Читы для игр в @gamee'''

	strings = {
		"name": "GameeCheats",
		"result": (
			"<emoji document_id=6334592388073260525>🪄</emoji> <b>Рекорд накручен</b>!\n"
			"<emoji document_id=6334649330749671032>✨</emoji> Новый рекорд: <code>{}</code>"
		),
		"err_args": (
			'<emoji document_id=6334664779747034990>🚫</emoji> <b>Введите нужные аргументы</b>!\n'
			'<emoji document_id=6334638004920911460>ℹ️</emoji> Пример: <code>{}chg <ссылка> <рекорд></code>'
		),
		"banned": (
			"<emoji document_id=6334363088359262569>⛔️</emoji> <b>Вы были заблокированы в боте</b>!\n"
			"<emoji document_id=6334638004920911460>ℹ️</emoji> <code>Вы не можете ставить новые рекорды в течении 24 часов</code>"
		),
		"banned_perm": (
			"<emoji document_id=6334363088359262569>⛔️</emoji> <b>Вы были заблокированы в боте навсегда</b>!\n"
			"<emoji document_id=6334638004920911460>ℹ️</emoji> <code>Вы не можете ставить новые рекорды в @gamee</code>"
		),
		"error_link": (
			"<emoji document_id=6334664779747034990>🚫</emoji> <b>Вы ввели неправильную ссылку</b>!\n"
			"<emoji document_id=6334638004920911460>ℹ️</emoji> <code>Введите правильную ссылку или же"
			' посмотрите</code> <a href="https://t.me/help_code/15">туториал</a>'
		)
	}

	async def client_ready(self):
		self.lib = await self.import_lib('https://raw.githubusercontent.com/ToXic2290/Hikka-moduless/main/GameCheatsLib.py')

	async def game_link(self, url):
		pattern = r"https:\/\/prizes\.gamee\.com(\/game-bot\/.*)#tg"
		result = re.match(pattern, url)
		if result:
			return result.groups(0)[0]
		else:
			return False

	async def get_checksum(self, score, playTime, url):
		str2hash = f"{score}:{playTime}:{url}::crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen"
		result = hashlib.md5(str2hash.encode())
		checksum = result.hexdigest()
		return checksum

	@loader.command()
	async def chg(self, message: Message):
		"""<ссылка> <рекорд> - запустить чит"""
		args = utils.get_args_raw(message)
		if not args:
			await utils.answer(message, self.strings('err_args').format(self.get_prefix()))

		try:
			game, score = args.split(' ')
		except ValueError:
			await utils.answer(message, self.strings('err_args').format(self.get_prefix()))
			return

		game_url = await self.game_link(game)
		if not game_url:
			await utils.answer(message, self.strings('error_link'))
			return

		time = random.randint(308, 19187)
		checksum = await self.get_checksum(score, time, game_url)

		token = await self.lib.get_token(game_url)
		Game_number = await self.lib.game_id(game_url)
		result = await self.lib.send_score(score, time, checksum, token, game_url, Game_number)

		if result == 'ban':
			await utils.answer(message, self.strings('banned'))
			return
		if result == 'ban_permanent':
			return await utils.answer(message, self.strings('banned_perm'))

		await utils.answer(message, self.strings("result").format(score))
