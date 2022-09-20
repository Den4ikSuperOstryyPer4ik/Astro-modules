#                _             __  __           _       _                
#      /\       | |           |  \/  |         | |     | |               
#     /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___      
#    / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|     
#   / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \     
#  /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/     
#                                                                        
#                         © Copyright 2022                               
#                                                                        
#                https://t.me/Den4ikSuperOstryyPer4ik                    
#                              and                                       
#                      https://t.me/ToXicUse                             
#                                                                         
#                 🔒 Licensed under the GNU AGPLv3                       
#             https://www.gnu.org/licenses/agpl-3.0.html                 
#                                                                                                                 
# meta developer: @AstroModules
from .. import loader, utils
from telethon.tl.types import Message


class AntiMatMod(loader.Module):
	'''Модуль, который не даст вам сматериться)'''

	strings = {
		"name": "Анти-Мат",
		"am_on": "🤬 <b>Antimat enabled.</b>",
		"am_off": "🤬 <b>Antimat disabled.</b>",
		"action_text": "What action should be taken when a swear word is found in a message?",
		"list_txt": 'Here you can add your mats.\np.s.: add one mat at a time',
	}

	strings_ru = {
		"am_on": "🤬 <b>Антимат включен.</b>",
		"am_off": "🤬 <b>Антимат отключен.</b>",
		"action_text": "Какое действие выполнять при обнаружении мата в сообщении?",
		"list_txt": "Здесь вы можете добавить свои маты.\np.s.: добавляйте по одному мату",
	}


	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"list",
				"хер, хрен, хуй, пизда, бля, пох, нах, еблан, еба, шлюха, сука, уебан, пздц, пиздец, пиздос, хую, долбоеб, пидор, гандон, хуя",
				doc=lambda: self.strings("list_txt"),
				validator=loader.validators.Series()
			),
		)


	@loader.command()
	async def antimat(self, message: Message):
		'''- активировать или диактивировать режим АнтиМат'''
		antimat = self.db.get(
			"am_status",
			"antimat",
		)
		if antimat == "":
			self.db.set("am_status", "antimat", False)
		if antimat == False:
			self.db.set("am_status", "antimat", True)
			await utils.answer(message, self.strings("am_on"))
		else:
			self.db.set("am_status", "antimat", False)
			await utils.answer(message, self.strings("am_off"))

	@loader.command()
	async def matlist(self, message: Message):
		"""- дополнить список матов

		🤫 Автор модуля не очень любит материться. В связи с этим в конфиге может не быть некоторых матов которые вы часто используете."""
		await self.allmodules.commands["config"](
					await utils.answer(message, f"{self.get_prefix()}config Анти-Мат")
				)

	@loader.watcher(out=True)
	async def watcher(self, message: Message):
		txt = message.text
		antimat = self.db.get(
			"am_status",
			"antimat",
		)
		mats = self.config['list']
		if antimat == False:
			return
		if antimat == True:
			for mat in mats:
				m = txt.lower().find(mat)
				if m != -1:
					await message.edit("<emoji document_id=5213285132709929474>🤬</emoji> <b>Не матерись!</b>")

