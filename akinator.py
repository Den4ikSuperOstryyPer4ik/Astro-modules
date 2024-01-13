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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/Akinator.jpg
# meta developer: @AstroModules

import random

import akinator
import deep_translator

from .. import loader, utils
from ..inline.types import InlineCall

aki_photo = "https://graph.org/file/3cc8825c029fd0cab9edc.jpg"
aki_failed = "https://0x0.st/H1rk.jpg"
emojies = ["😏", "🫢", "🤔", "🫣", "🫤", "😉", "😒"]

@loader.tds
class AkinatorGame(loader.Module):
	"""
	Akinator will guess any character you have in mind,
	You just need to answer a couple of questions)
	"""

	strings = {
		"name": "Akinator",
		"child_mode": "Child mode. If enabled, it will be easier to guess 18+ heroes",
		"failed": "❌ Failed",
		"start": "🔮 Start",
		"text": "🔮 <b>Guess any character you have in mind, and click on the Start button</b>",
		"target_lang": "Target language",
		"yes": "Yes",
		"no": "No",
		"idk": "I don't know",
		"probably": "Probably",
		"probably_not": "Probably not",
		"this_is": "<b>This is {name}\n{description}</b>",
		"not_right": "Not right",
	}

	strings_ru = {
		"_cls_doc": "Акинатор угадает любого вами загаданного персонажа, стоит лишь ответить на пару вопросов)",
		"child_mode": "Детский режим. Если включен, то будет сложнее отгадать 18+ героев",
		"failed": "🚫 Не удалось угадать персонажа",
		"start": "🔮 Начать",
		"text": "🔮 <b>Задумайте реального или вымышленного персонажа, и нажмите начать</b>",
		"target_lang": "Язык для перевода",
		"yes": "Да",
		"no": "Нет",
		"idk": "Не знаю",
		"probably": "Возможно",
		"probably_not": "Скорее нет",
		"this_is": "<b>Это {name}\n{description}</b>",
		"not_right": "Это не он",
	}

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"child_mode",
				True,
				lambda: self.strings("child_mode"),
				validator=loader.validators.Boolean()
			),
			loader.ConfigValue(
				"target_lang",
				"en",
				lambda: self.strings("target_lang"),
				validator=loader.validators.String()
			)
		)


	async def client_ready(self):
		self.games = {}


	@loader.command(
			ru_doc="- начать игру",
	)
	async def akinator(self, message):
		"""- start the game"""

		sta = akinator.Akinator()
		self.games.update({message.chat_id: {message.id: sta}})

		await self.inline.form(
			message=message,
			photo=aki_photo,
			text=self.strings("text"),
			reply_markup={
				"text": self.strings("start"),
				"callback": self.doai,
				"args": (message,),
			}
		)


	async def doai(self, call: InlineCall, message):
		chat_id = int(message.chat_id)
		mid = int(message.id)

		qu = self.games[chat_id][mid].start_game(child_mode=self.config["child_mode"])
		
		text = deep_translator.GoogleTranslator(
			source="auto", 
			target=self.config["target_lang"]
		).translate(qu)
		
		emo = random.choice(emojies)
		await call.edit(
			f"{emo} <b>{text}</b>",
			reply_markup=[
				[
					{
						"text": self.strings("yes"),
						"callback": self.cont,
						"args": ("Yes", message,),
					},
					{
						"text": self.strings("no"),
						"callback": self.cont,
						"args": ("No", message,),
					},
					{
						"text": self.strings("idk"),
						"callback": self.cont,
						"args": ("Idk", message,),
					}
				],
				[
					{
						"text": self.strings("maybe"),
						"callback": self.cont,
						"args": ("Probably", message,),
					},
					{
						"text": self.strings("maybe_not"),
						"callback": self.cont,
						"args": ("Probably Not", message,),
					}
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
				text = self.strings("this_is").format(name=gs["name"], description=gs["description"])
				await call.edit(
					text, 
					photo=gs["absolute_picture_path"],
					reply_markup=[
						{
							"text": self.strings("not_right"),
							"callback": self.cont,
							"args": ("No", message,),
						},
					]
				)
			else:
				text = deep_translator.GoogleTranslator(
					source="auto", 
					target=self.config["target_lang"]
				).translate(text)
				emo = random.choice(emojies)
				await call.edit(
					text=f"{emo} <b>{text}</b>",
					photo=aki_photo,
					reply_markup=[
						[
							{
								"text": self.strings("yes"),
								"callback": self.cont,
								"args": ("Yes", message,),
							},
							{
								"text": self.strings("no"),
								"callback": self.cont,
								"args": ("No", message,),
							},
							{
								"text": self.strings("idk"),
								"callback": self.cont,
								"args": ("Idk", message,),
							}
						],
						[
							{
								"text": self.strings("maybe"),
								"callback": self.cont,
								"args": ("Probably", message,),
							},
							{
								"text": self.strings("maybe_not"),
								"callback": self.cont,
								"args": ("Probably Not", message,),
							}
						]
					]
				)
		except akinator.exceptions.AkinatorQuestionOutOfRangeException:
			await call.edit(
				text=self.strings("failed"),
				photo=aki_failed
			)
