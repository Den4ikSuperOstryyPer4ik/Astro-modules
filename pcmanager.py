__version__ = (1, 0, 0)
#               _             __  __           _       _
#     /\       | |           |  \/  |         | |     | |
#    /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___
#   / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|
#  / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \
# /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/
#
#               © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules

from .. import loader, utils

from telethon.tl.types import Message
from ..inline.types import InlineCall

class PCManagerMod(loader.Module):
	'''Управление вашим компьютером через юзербота'''
	strings = {"name": "PC-Manager"}

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				'bot_username',
				None,
				doc=lambda: "Введите юзернейм вашего бота для управления ПК"
			)
		)

	async def client_ready(self):
		self.lib = await self.import_lib(
			'https://raw.githubusercontent.com/ToXic2290/Hikka-moduless/main/AstroModules_Library.py',
			suspend_on_error=False,
		)


	@loader.command()
	async def addbot(self, message: Message):
		'''- добавить бота

 💎 Основные команды:'''
		await self.allmodules.commands["config"](
					await utils.answer(message, f"{self.get_prefix()}config PC-Manager")
				)
	@loader.command()
	async def tutor(self, message: Message):
		"""- туториал по подключению"""
		await utils.answer(message, "<emoji document_id=5787237370709413702>⚙️</emoji> <b>Туториал по настройке модуля:</b>\n\n@PC_AM_Tutor\n\nЕсли возникли трудности с установкой, пожалуйста, обратитесь в чат AstroModules ")

	@loader.command()
	async def pcoff(self, message: Message):
		"""- выключить компьютер""" 
		bot = self.config["bot_username"]
		call = await self.lib.message_g(f'🛑 Shutdown',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\n{call.text}')

	@loader.command()
	async def pcreboot(self, message: Message):
		"""- перезагрузить компьютер"""
		bot = self.config["bot_username"]
		call = await self.lib.message_g(f'🔄 Reboot',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\n{call.text}')

	@loader.command()
	async def pcinfo(self, message: Message):
		"""- просмотреть характеристики системы"""
		bot = self.config["bot_username"]
		call = await self.lib.message_q(f'💻 System Info',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\n{call.text}')

	@loader.command()
	async def pcip(self, message: Message):
		"""- просмотреть информацию об айпи адресе"""
		bot = self.config["bot_username"]
		call = await self.lib.message_q(f'🌐 IP Info',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\n{call.text}')

	@loader.command()
	async def pcscrin(self, message: Message):
		"""- сделать скриншот экрана"""
		bot = self.config['bot_username']
		call = await self.lib.message_g(f'/screenshot',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\nОтправка скриншота...')
		await message.respond(call)

	@loader.command()
	async def pcweb(self, message: Message):
		"""<ссылка> - открыть ссылку в браузере"""
		bot = self.config['bot_username']
		args = utils.get_args_raw(message)
		call = await self.lib.message_q(f'/browse {args}',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\n{call.text}\n\nСсылка: {args}')

	@loader.command()
	async def pcwebscrin(self, message: Message):
		"""- сделать снимок с веб-камеры

🔑 Дополнительно:"""
		bot = self.config['bot_username']
		call = await self.lib.message_g(f'/photo',
			bot,
			mark_read=True,
			delete=True
		)
		await utils.answer(message, f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\nОтправка снимка...')
		await message.respond(call)

	@loader.command()
	async def pcalert(self, message: Message):
		"""<сообщение> - вывести на экран сообщение"""
		bot = self.config['bot_username']
		args = utils.get_args_raw(message)
		call = await self.lib.message_q(f'/alert {args}',
			bot,
			mark_read=True,
			delete=True
		)
		await message.respond(f'<emoji document_id=5787544344906959608>ℹ️</emoji> <b>[PC_Manager]</b> <emoji document_id=5787544344906959608>ℹ️</emoji>\n\n{call.text}')
		await message.delete()
	
	@loader.command()
	async def pcvol(self, message: Message):
		"""- управление звуком"""
		await self.inline.form(
			text="ℹ️ <b>[PC_Manager]</b> ℹ️\n\n<b>Мишкер громкости</b>",
			reply_markup=[
				[
					{
						"text": "10%",
						"callback": self.vol10
					},
					{
						"text": "20%",
						"callback": self.vol20
					},
					{
						"text": "30%",
						"callback": self.vol30
					},
				],
				[
					{
						"text": "40%",
						"callback": self.vol40
					},
					{
						"text": "50%",
						"callback": self.vol50
					},
					{
						"text": "60%",
						"callback": self.vol60
					},
				],
				[	
					{
						"text": "70%",
						"callback": self.vol70
					},
					{
						"text": "80%",
						"callback": self.vol80
					},
					{
						"text": "90%",
						"callback": self.vol90
					},
				],
				[	
					{
						"text": "⬆️",
						"callback": self.volUp
					},			
					{
						"text": "100%",
						"callback": self.vol100
					},
					{
						"text": "⬇️",
						"callback": self.volDown
					},
				],
				[{"text": "🚫 Закрыть", "action": "close"}],
			],
			message=message,
		)

	@loader.command()
	async def pcmedia(self, message: Message):
		"""- управление музыкой"""
		await self.inline.form(
			text="ℹ️ <b>[PC_Manager]</b> ℹ️\n\n<b>Управление медиа</b>",
			reply_markup=[
				[
					{
						"text": "⏪",
						"callback": self.nazad
					},
					{
						"text": "⏯",
						"callback": self.pausa
					},
					{
						"text": "⏩",
						"callback": self.vpered
					},
				],
				[{"text": "🚫 Закрыть", "action": "close"}],
			],
			message=message,
		)

	async def nazad(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/key__prev')
		return await call.answer("Успешно!", show_alert=False)
	async def pausa(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/key__play')
		return await call.answer("Успешно!", show_alert=False)
	async def vpered(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/key__next')
		return await call.answer("Успешно!", show_alert=False)
	async def vol10(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 10')
		return await call.answer("Успешно!", show_alert=False)
	async def vol20(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 20')
		return await call.answer("Успешно!", show_alert=False)
	async def vol30(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 30')
		return await call.answer("Успешно!", show_alert=False)
	async def vol40(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 40')
		return await call.answer("Успешно!", show_alert=False)
	async def vol50(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 50')
		return await call.answer("Успешно!", show_alert=False)
	async def vol60(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 60')
		return await call.answer("Успешно!", show_alert=False)
	async def vol70(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 70')
		return await call.answer("Успешно!", show_alert=False)
	async def vol80(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 80')
		return await call.answer("Успешно!", show_alert=False)
	async def vol90(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 90')
		return await call.answer("Успешно!", show_alert=False)
	async def vol100(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume 100')
		return await call.answer("Успешно!", show_alert=False)
	async def volUp(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume up')
		return await call.answer("Успешно!", show_alert=False)
	async def volDown(self, call: InlineCall):
		bot = self.config['bot_username']
		await self.client.send_message(f'{bot}', '/volume down')
		return await call.answer("Успешно!", show_alert=False)

																			# Tx...