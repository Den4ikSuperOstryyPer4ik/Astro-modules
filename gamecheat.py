#               _             __  __           _       _
#     /\       | |           |  \/  |         | |     | |
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#               © Copyright 2023
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# old source: https://github.com/norouzy/Gamee-Cheat
# meta developer: @astromodules
# support: @visionavtr
# requirements: certifi==2022.6.15, charset-normalizer==2.1.0, idna==3.3, requests==2.28.1, urllib3==1.26.10

import re
import random
import hashlib
import requests
from .. import loader, utils
from telethon.tl.types import Message
from requests.structures import CaseInsensitiveDict

@loader.tds
class GameeCheatMod(loader.Module):
	"""Cheat for @gamee"""

	strings = {
		"name": "GameeCheats",
		"result": "<b>Successfully boosted your score. Current score:</b> <code>{}</code>",
		"err_args": "<b>Not enough arguments</b>",
		"banned": (
			"<emoji document_id=5228963597291363997>😣</emoji> <b>Unfortunately, "
			"you have been blocked. Please try again in 24 hours.</b>"
		)
	}

	strings_ru = {
		"result": "<b>Успешно накрутил вам рекорд. Нынешний рекорд:</b> <code>{}</code>",
		"err_args": "<b>Недостаточно аргументов</b>",
		"banned": (
			"<emoji document_id=5228963597291363997>😣</emoji> <b>К сожалению, "
			"вы были заблокированы. Повторите попытку через 24 часа.</b>"
		),
		"error_link": (
			' <emoji document_id=5228963597291363997>😣</emoji> <b>Эй, ты чего?'
			' Это не та ссылка) Смотри туториал по получению правильной ссылки ниже:</b>'
			' \n\nhttps://t.me/help_code/15'
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

	async def get_time(self, score: int):
		a = random.choice(['t', 'n'])
		if a == 't':
			return(random.randint(278, 1987))
		else:
			return(random.randint(78, 987))

	async def get_checksum(self, score, playTime, url):
		str2hash = f"{score}:{playTime}:{url}::crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen"
		result = hashlib.md5(str2hash.encode())
		checksum = result.hexdigest()
		return checksum

	@loader.command(ru_doc="<ссылка> <рекорд> - запустить чит")
	async def chg(self, message: Message):
		"""<game link> <score> <time> - run cheat"""
		args = utils.get_args_raw(message)
		if not args:
			await utils.answer(message, self.strings('err_args'))

		game, score = args.split(' ')

		game_url = await self.game_link(game)
		if game_url == False:
			await utils.answer(message, self.strings('error_link'))
			return

		time = await self.get_time(score)
		checksum = await self.get_checksum(score, time, game_url)

		token = await self.lib.get_token(game_url)
		Game_number = await self.lib.game_id(game_url)
		result = await self.lib.send_score(score, time, checksum, token, game_url, Game_number)

		if result == 'ban':
			await utils.answer(message, self.strings('banned'))
			return

		await utils.answer(message, self.strings("result").format(score))