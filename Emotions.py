__version__ = (1, 0, 1)
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
# meta developer: @AstroModules, @hikarimods

from .. import loader, utils
import grapheme
from telethon.tl.types import Message

@loader.tds
class EmotionsMod(loader.Module):
	'''Выражение эмоций в чате'''

	strings = {
		"name": "Emotions",
		'delete_msg': "Удалять сообщение которое вызывает эмоцию?",
		'on': "<emoji document_id=5373230475022179039>🥺</emoji> Emotions успешно активирован в этом чате.",
		'off': "<emoji document_id=5373230475022179039>🥺</emoji> Emotions успешно деактивирован в этом чате",
		'ok': "<emoji document_id=5188315103384050849>☑️</emoji>Эмоция успешно добавлена",
		'list': "<emoji document_id=5373230475022179039>🥺</emoji> Доступные эмоции:\n\n{}\n\n<emoji document_id=5467928559664242360>❗️</emoji> Для добавления своих эмоций введите команду:\n    <code>.emo</code> <символ/слово> <эмоция>",
	}

	async def client_ready(self):
		self.emo = self.get(
			"emo",
			{
				')': '😊 улыбается',
				'(': '🙁 грустит',
				'😭': '😭 плачет',
				'😃': "😃 радуется",
				"😏": "😏 думает о кое-чем)))",
				"🤔": "🤔 призадумался",
				"😂": "😂 смеется",
				"🤣": "🤣 ржет",
				"😞": "😞 расстроен",
				"😔": "😔 сильно расстроен",
				"😍": "😍 что-то нравится",
				"😤": "😤 зол",
				"😡": "😡 сильно зол",
				"🤬": "🤬 матерится",
				"😎": "😎 типа крутой",
				"😳": "😳 шокирован",
				"🤢": "🤢 думает что это противно",
				"🫠": "🫠 весь течет",
				"🥺": "🥺 считает что это мило",
			},
		)
		self.chats = self.get("active", [])

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				'delete',
				True,
				doc=lambda: self.strings("delete_msg"),
				validator=loader.validators.Boolean(),)
		)

	async def emogocmd(self, message: Message):
		"""- вкл/выкл эмоции в данном чате"""

		cid = str(utils.get_chat_id(message))

		if cid in self.chats:
			self.chats.remove(cid)
			await utils.answer(message, self.strings("off"))
		else:
			self.chats += [cid]
			await utils.answer(message, self.strings("on"))

		self.set("active", self.chats)


	async def emoclearcmd(self, message: Message):
		"""<y> - сбросить список эмоций"""

		args = utils.get_args_raw(message)

		if args == "y":
			await self.allmodules.commands["e"](
				await utils.answer(message, f"{self.get_prefix()}e db.pop('EmotionsMod')")
			)
			await utils.answer(message, "<emoji document_id=5370842086658546991>☠️</emoji> <b>Список эмоций успешно сброшен до зоводских настроек\nПожалуйста, загрузите модуль еще раз.</b>")
		else:
			await utils.answer(message, '<emoji document_id=5370842086658546991>☠️</emoji> <b>Вы не подтвердили удаление!</b>')


	async def emolistcmd(self, message: Message):
		"""- список доступных эмоций"""

		await utils.answer(
			message,
			self.strings("list").format(
				"\n".join(
					[f" ▪️ {simvol} - {emotion}" for simvol, emotion in self.emo.items()]
				)
			),
		)


	async def emocmd(self, message: Message):
		"""<символ|слово> <эмоция> - добавить эмоцию в базу модуля"""
		args = utils.get_args_raw(message)
		try:
			simvol = args.split(" ", 1)[0]
			emotion = args.split(" ", 1)[1]

		except Exception:
			if not args or simvol not in self.emo:
				await utils.answer(message, '<emoji document_id=5467928559664242360>❗️</emoji> Вы ввели неверное значение. Попробуйте снова')
			else:
				del self.emo[simvol]
				self.set("emo", self.emo)
				await utils.answer(message, self.strings("ok"))

			return

		self.emo[simvol] = emotion
		self.set("emo", self.emo)
		await utils.answer(message, self.strings("ok"))


	async def watcher(self, message: Message):
		cid = str(utils.get_chat_id(message))
		try:
			if (
				cid not in self.chats
				or not isinstance(message, Message)
				or not hasattr(message, "raw_text")
				or message.raw_text.split(maxsplit=1)[0].lower() not in self.emo
			):
				return
		except IndexError:
			return

		try:
			cmd = message.raw_text.split(maxsplit=1)[0].lower()
		except IndexError:
			return

		msg = self.emo[cmd]
		sender = await self._client.get_entity(message.sender_id)

		if utils.emoji_pattern.match(next(grapheme.graphemes(msg))):
			msg = list(grapheme.graphemes(msg))
			emoji = msg[0]
			msg = "".join(msg[1:])
		else:
			emoji = "<emoji document_id=5373230475022179039>🥺</emoji>"

		if self.config['delete'] == True and not message.out:
			await message.delete()
		await utils.answer(
			message, 
			f'{emoji} <a href="tg://user?id={sender.id}">{utils.escape_html(sender.first_name)}</a> <b>{utils.escape_html(msg)}</b> {emoji}')
