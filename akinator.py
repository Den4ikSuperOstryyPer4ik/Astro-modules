__version__ = (1, 0, 5)
#                _             __  __           _       _
#      /\       | |           |  \/  |         | |     | |
#     /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#    / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#   / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
#  /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#                         © Copyright 2023
#
#                https://t.me/Den4ikSuperOstryyPer4ik
#                              and
#                      https://t.me/ToXicUse
#
#                 🔒 Licensed under the GNU AGPLv3
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: https://0x0.st/HQ7s.jpg
# meta developer: @AstroModules

import random
import akinator
import deep_translator
from .. import loader, utils
from ..inline.types import InlineCall

aki_photo = "https://graph.org/file/3cc8825c029fd0cab9edc.jpg"
aki_failed = 'https://0x0.st/H1rk.jpg'
emojies = ['😏', '🫢', '🤔', '🫣', '🫤', '😉', '😒']

@loader.tds
class AkinatorGame(loader.Module):
	'''
	Акинатор угадает любого вами загаданного персонажа, 
	стоит лишь ответить на пару вопросов)
	'''

	strings = {'name': 'Akinator'}

	async def client_ready(self):
		self.games = {}

	@loader.command()
	async def akinator(self, message):
		'''- начать игру'''
		sta = akinator.Akinator()
		self.games.update({message.chat_id: {message.id: sta}})
		await self.inline.form(
			message=message,
			photo=aki_photo,
			text='🔮 <b>Задумайте реального или вымышленного персонажа, и нажмите начать</b>',
			reply_markup={'text': 'Начать','callback': self.doai,'args': (message,),}
		)

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				'child_mode',
				True,
				lambda: 'Детский режим. Если включен, то будет сложнее отгадать 18+ героев',
				validator=loader.validators.Boolean()
			)
		)

	async def doai(self, call: InlineCall, message):
		chat_id = int(message.chat_id)
		mid = int(message.id)
		if self.config['child_mode']:
			qu = self.games[chat_id][mid].start_game(child_mode=True)
		else:
			qu = self.games[chat_id][mid].start_game(child_mode=False)
		text = deep_translator.GoogleTranslator(
			source="auto", 
			target='ru'
		).translate(qu)
		emo = random.choice(emojies)
		await call.edit(
			f'{emo} <b>{text}</b>',
			reply_markup=[
				[
					{'text': 'Да', 'callback': self.cont, 'args': ('Yes', message,),},
					{'text': 'Нет', 'callback': self.cont, 'args': ('No', message,),},
					{'text': 'Не знаю', 'callback': self.cont, 'args': ('Idk', message,),},
				],
				[
					{'text': 'Возможно', 'callback': self.cont, 'args': ('Probably', message,),},
					{'text': 'Скорее нет', 'callback': self.cont, 'args': ('Probably Not', message,),},
				]
			]
		)

	async def cont(
		self, 
		call: InlineCall, 
		args: str, 
		message
	):
		chat_id = message.chat_id
		mid = message.id
		gm = self.games[chat_id][mid]
		text = gm.answer(args)
		try:
			if gm.progression >= 85:
				gm.win()
				gs = gm.first_guess
				text = f"<b>Это {gs['name']}\n{gs['description']}</b>"
				await call.edit(
					text, 
					photo=gs["absolute_picture_path"],
					reply_markup=[
						{'text': 'Это не он', 'callback': self.cont, 'args': ('No', message,),},
					]
				)
			else:
				text = deep_translator.GoogleTranslator(
					source="auto", 
					target='ru'
				).translate(text)
				emo = random.choice(emojies)
				await call.edit(
					text=f'{emo} <b>{text}</b>',
					photo=aki_photo,
					reply_markup=[
						[
							{'text': 'Да', 'callback': self.cont, 'args': ('Yes', message),},
							{'text': 'Нет', 'callback': self.cont, 'args': ('No', message),},
							{'text': 'Не знаю', 'callback': self.cont, 'args': ('Idk', message),},
						],
						[
							{'text': 'Возможно', 'callback': self.cont, 'args': ('Probably', message),},
							{'text': 'Скорее нет', 'callback': self.cont, 'args': ('Probably Not', message),},
						]
					]
				)
		except akinator.exceptions.AkinatorQuestionOutOfRangeException:
			await call.edit(text='<b>К сожалению, я не смог угадать данного героя(</b>', photo=aki_failed)
