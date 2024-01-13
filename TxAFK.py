__version__ = (1, 4, 2)
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

import datetime
import logging
import time

from telethon import types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest

from .. import loader, utils
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)


@loader.tds
class TxAFKMod(loader.Module):
	'''Афк модуль от AstroModules с изменением био и имени'''
	async def client_ready(self, client, db):
		self._db = db
		self._me = await client.get_me()

	strings = {
		"name": "TxAFK",

		"lname": "| afk.",
		"lname0": " ",

		"bt_off_afk": "⚠️ АФК режим отключен",
		"bt_on_afk": "💤 АФК режим снова активен",

		"_cfg_cst_btn": "Ссылка на чат которая будет отоброжаться вместе с уведомлением. (Чтобы вообще убрать напишите None)",
		"standart_bio_text": "Кастомное описание профиля",
		"feedback_bot__text": "Юзер вашего фидбэк бота (если имеется)",
		"button__text": "Добавить инлайн кнопку отключения АФК режима?",
		"custom_text__afk_text": "Кастомный текст афк. Используй {time} для вывода последнего времени нахождения в сети",
	}

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"feedback_bot",
				"None",
				doc=lambda: self.strings("feedback_bot__text"),
			),
			loader.ConfigValue(
				"custom_text__afk",
				"None",
				doc=lambda: self.strings("custom_text__afk_text"),
			),
			loader.ConfigValue(
				"standart_bio",
				"None",
				doc=lambda: self.strings("standart_bio_text"),
			),
			loader.ConfigValue(
				"custom_button",
				[
					"🦄 AstroModules 🦄",
					"https://t.me/AstroModulesChat",
				],
				lambda: self.strings("_cfg_cst_btn"),
				validator=loader.validators.Union(
					loader.validators.Series(fixed_len=2),
					loader.validators.NoneType(),
				),
			),
			loader.ConfigValue(
				"ignore_chats",
				[],
				lambda: "Чаты, в которых при упоминании TxAFК не будет срабатывать",
				validator=loader.validators.Series(
                    validator=loader.validators.Union(
                        loader.validators.TelegramID(),
                        loader.validators.RegExp("[0-9]"),
                    ),
                ),
			),
			loader.ConfigValue(
				"button",
				True,
				doc=lambda: self.strings("button__text"),
				validator=loader.validators.Boolean(),
			)

		)


	async def txcfgcmd(self, message):
		"""- открыть конфиг модуля"""
		await self.allmodules.commands["config"](
					await utils.answer(message, f"{self.get_prefix()}config TxAFK")
				)

	async def goafkcmd(self, message):
		"""- войти в AFK режим"""
		try:
			user_id = (
				(
					(
						await self._client.get_entity(
							args if not args.isdigit() else int(args)
						)
					).id
				)
				if args
				else reply.sender_id
			)
		except Exception:
			user_id = self._tg_id

		user = await self._client(GetFullUserRequest(user_id))
		
		self._db.set(__name__, "afk", True)
		self._db.set(__name__, "gone", time.time())
		self._db.set(__name__, "ratelimit", [])
		a_afk_bio_nofb = "В афк."
		lastname = self.strings("lname")
		if self.config['feedback_bot'] == None:
			await message.client(UpdateProfileRequest(about=a_afk_bio_nofb, last_name=lastname))
		else:
			a_afk_bio = 'На данный момент в АФК. Связь только через '
			feedback = self.config['feedback_bot']
			aaa = a_afk_bio + feedback
			await message.client(UpdateProfileRequest(about=aaa))
		await self.allmodules.log("goafk")
		await utils.answer(message, '<emoji document_id=5215519585150706301>👍</emoji> <b>АФК режим включен!</b>')
		await message.client(UpdateProfileRequest(last_name=lastname))

	async def ungoafkcmd(self, message):
		"""- выйти из режима AFK"""
		msg = await utils.answer(message, '<emoji document_id=5213107179329953547>⏰</emoji> <b>Отключаю режим АФК...</b>')
		sbio = self.config['standart_bio']
		lastname0 = self.strings('lname0')
		self._db.set(__name__, "afk", False)
		self._db.set(__name__, "gone", None)
		self._db.set(__name__, "ratelimit", [])
		await self.allmodules.log("unafk")
		if sbio == None:
			await message.client(UpdateProfileRequest(about='', last_name=lastname0))
		else:
			await message.client(UpdateProfileRequest(about=sbio, last_name=lastname0))
		time.sleep(1)
		await utils.answer(msg, '<emoji document_id=5220108512893344933>🆘</emoji> <b>Режим AFK отключен!</b>')


	def _afk_custom_text(self) -> str:
		now = datetime.datetime.now().replace(microsecond=0)
		gone = datetime.datetime.fromtimestamp(
			self._db.get(__name__, "gone")
		).replace(microsecond=0)

		time = now - gone

		return (
			"<b> </b>\n"
			+ self.config["custom_text__afk"].format(
				time=time,
			)
		)


	async def watcher(self, message):
		if not isinstance(message, types.Message):
			return
		if utils.get_chat_id(message) in self.config['ignore_chats']: 
			return
		if message.mentioned or getattr(message.to_id, "user_id", None) == self._me.id:
			afk_state = self.get_afk()
			if not afk_state:
				return
			logger.debug("tagged!")
			ratelimit = self._db.get(__name__, "ratelimit", [])
			if utils.get_chat_id(message) in ratelimit:
				return
			else:
				self._db.setdefault(__name__, {}).setdefault("ratelimit", []).append(
					utils.get_chat_id(message)
				)
				self._db.save()
			user = await utils.get_user(message)
			if user.is_self or user.bot or user.verified:
				logger.debug("User is self, bot or verified.")
				return
			if self.get_afk() is False:
				return
			now = datetime.datetime.now().replace(microsecond=0)
			gone = datetime.datetime.fromtimestamp(
				self._db.get(__name__, "gone")
			).replace(microsecond=0)
			time = now - gone
			if self.config['custom_button'] == None:
				if self.config["button"] == False:
					if self.config["custom_text__afk"] == None:
						await self.inline.form(message=message, text=f"<b>🔅 Я сейчас нахожусь в АФК.</b>\n\nПоследний раз был в сети <code>{time}</code> назад.")
					else:
						await self.inline.form(message=message, text=self._afk_custom_text())
				
				elif self.config['button'] == True:
					if self.config["custom_text__afk"] == None:
						await self.inline.form(
							message=message, 
							text=f"<b>🔅 Я сейчас нахожусь в АФК.</b>\n\nПоследний раз был в сети <code>{time}</code> назад.", 
							reply_markup=[
								[
									{
										"text": "🚫 Выйти с афк 🚫", 
										"callback": self.button_cancel,
									}
								]
							]
						)

					else:
						await self.inline.form(
							message=message, 
							text=self._afk_custom_text(), 
							reply_markup=[
								[
									{
										"text": "🚫 Выйти с афк 🚫", 
										"callback": self.button_cancel,
									}
								]
							]
						)
			else:
				if self.config["button"] == False:
					if self.config["custom_text__afk"] == None:
						await self.inline.form(message=message, text=f"<b>🔅 Я сейчас нахожусь в АФК.</b>\n\nПоследний раз был в сети <code>{time}</code> назад.", reply_markup=[{"text": self.config['custom_button'][0], "url": self.config['custom_button'][1]}])
					else:
						await self.inline.form(message=message, text=self._afk_custom_text(), reply_markup=[{"text": self.config['custom_button'][0], "url": self.config['custom_button'][1]}])
				
				elif self.config['button'] == True:
					if self.config["custom_text__afk"] == None:
						await self.inline.form(
							message=message, 
							text=f"<b>🔅 Я сейчас нахожусь в АФК.</b>\n\nПоследний раз был в сети <code>{time}</code> назад.", 
							reply_markup=[
								[
									{
										"text": self.config['custom_button'][0],
										"url": self.config['custom_button'][1],
									}
								],
								[
									{
										"text": "🚫 Выйти с афк 🚫", 
										"callback": self.button_cancel,
									}
								]
							]
						)

					else:
						await self.inline.form(
							message=message, 
							text=self._afk_custom_text(), 
							reply_markup=[
								[
									{
										"text": self.config['custom_button'][0],
										"url": self.config['custom_button'][1],
									}
								],
								[
									{
										"text": "🚫 Выйти с афк 🚫", 
										"callback": self.button_cancel,
									}
								]
							]
						)

	async def button_cancel(self, call: InlineCall):
		self._db.set(__name__, "afk", False)
		self._db.set(__name__, "gone", None)
		self._db.set(__name__, "ratelimit", [])
		await self.allmodules.log("unafk")
		if self.config['standart_bio'] == None:
			lastname = self.strings("lname0")
			about = self.strings("lname0")
			await self._client(UpdateProfileRequest(about=about, last_name=lastname))
		else:
			aboutt = self.config['standart_bio']
			lastname = self.strings("lname0")
			await self._client(UpdateProfileRequest(about=aboutt, last_name=lastname))
		await call.edit(
		self.strings["bt_off_afk"],
		reply_markup=[
			{
				"text": "🔰 Войти в афк 🔰",
				"callback": self.button_cancel_on,
			}
		]
	)

	async def button_cancel_on(self, call: InlineCall):
		self._db.set(__name__, "afk", True)
		self._db.set(__name__, "gone", time.time())
		self._db.set(__name__, "ratelimit", [])
		a_afk_bio_nofb = "В афк."
		lastname = self.strings("lname")
		if self.config['feedback_bot'] == None:
			await self._client(UpdateProfileRequest(about=a_afk_bio_nofb, last_name=lastname))
		else:
			a_afk_bio = 'На данный момент в АФК. Связь только через '
			feedback = self.config['feedback_bot']
			aaa = a_afk_bio + feedback
			await self._client(UpdateProfileRequest(about=aaa))
		await call.edit(
		self.strings["bt_on_afk"],
		reply_markup=[
			{
				"text": "🚫 Выйти с афк 🚫",
				"callback": self.button_cancel,
			}
		]
	)

	def get_afk(self):
		return self._db.get(__name__, "afk", False)
