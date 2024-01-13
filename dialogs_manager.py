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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/DialogsManager.jpg

import random

from telethon import functions
from telethon.tl.types import Message

from .. import loader
from ..utils import answer, get_args_raw

premium_emojies = [
	"<emoji document_id=5807752501042089473>⭐️</emoji>",
	"<emoji document_id=5809735165320104963>⭐️</emoji>",
	"<emoji document_id=5807791714093502248>⭐️</emoji>",
	"<emoji document_id=5807432062122070581>⭐️</emoji>",
	"<emoji document_id=5807657096933543955>⭐️</emoji>",
	"<emoji document_id=5809782942536306227>⭐️</emoji>",
	"<emoji document_id=5807952178366648233>⭐️</emoji>",
	"<emoji document_id=5807529673843805138>⭐️</emoji>",
	"<emoji document_id=5807678760748584365>⭐️</emoji>",
	"<emoji document_id=5807434488778591925>⭐️</emoji>",
	"<emoji document_id=5807779713954876564>⭐️</emoji>",
	"<emoji document_id=5834463121699245596>⭐️</emoji>",
	"<emoji document_id=5832542373669769430>⭐️</emoji>",
	"<emoji document_id=5782804629452492061>⭐️</emoji>"
]

@loader.tds
class DialogsManagerMod(loader.Module):
	'''
	Check your all info for dialogs, chats, PMs
	Delete definite dialog,
	delete all dialogs by arguments,
	leave the chats, ids/usernames which you specify
	Dialogs Manager!
	'''
	
	strings = {
		'name': 'DialogsManager',
		'dialogs_info': "<b>All Dialogs info:\n\n<emoji document_id=6048540195995782913>👤</emoji> All users PM ➪ {}\n<emoji document_id=6037355667365300960>👥</emoji> All chats ➪ {}\n<emoji document_id=5764623873974734153>📢</emoji> All channels ➪ {}\n<emoji document_id=6037190220930092878>🤖</emoji> All bots PM ➪  {}\n\n<emoji document_id=6048540195995782913>👤</emoji> Users(PM):\n\n  <emoji document_id=5805597488316419570>🚫</emoji> Fake ➪  {}\n  <emoji document_id=5805441297535733440>🚫</emoji> Scam ➪  {}\n  {} Premium ➪  {}\n  <emoji document_id=5850654130497916523>✅️</emoji> Verified ➪  {}\n  <emoji document_id=6050677771154231040>🗑</emoji> Deleted ➪  {}\n\n<emoji document_id=6037355667365300960>👥</emoji> Chats:\n\n  <emoji document_id=6323524880121726602>✅</emoji> Megagroups ➪  {}\n\n  <emoji document_id=6323380805443782200>☑️</emoji> Gigagroups ➪  {}\n\n  <emoji document_id=5805597488316419570>🚫</emoji> Fake ➪  {}\n  <emoji document_id=5805441297535733440>🚫</emoji> Scam ➪  {}\n  <emoji document_id=5850654130497916523>✅️</emoji> Verified ➪  {}\n\n<emoji document_id=5764623873974734153>📢</emoji> Channels:\n  <emoji document_id=5805597488316419570>🚫</emoji> Fake ➪  {}\n  <emoji document_id=5805441297535733440>🚫</emoji> Scam ➪  {}\n  <emoji document_id=5850654130497916523>✅️</emoji> Verified ➪  {}\n\n<emoji document_id=6037190220930092878>🤖</emoji> Bots(PM):\n  <emoji document_id=5805597488316419570>🚫</emoji> Fake ➪  {}\n  <emoji document_id=5805441297535733440>🚫</emoji> Scam ➪  {}\n<emoji document_id=5850654130497916523>✅️</emoji> Verified ➪  {}",
		"waiting_dinfo": "<b>Please wait, loading information...</b>",
	}
	
	strings_ru = {
		"waiting_dinfo": "<b>Пожалуйста подождите, идёт загрузка данных...</b>",
	}
	
	@loader.command(
		ru_doc="➪  полная информация о ваших диалогах, чатах лс и т.д.",
		alias='dinfo'
	)
	async def dialogsinfo(self, message: Message):
		"""➪  all info for your dialogs, chats, PMs..."""
		msg = await answer(message, self.strings('waiting_dinfo'))
		chats, users, scam_bots, scam_users, scam_chats, scam_channels, fake_users, fake_chats, fake_bots, fake_channels, bots, channels, premium, deleted, verified_users, verified_chats, verified_bots, verified_channels, gigagroups, megagroups = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
		async for dialog in self._client.iter_dialogs():
			ent = dialog.entity
			if dialog.is_user:
				if ent.bot:
					bots += 1
					if ent.scam:
						scam_bots += 1
					elif ent.verified:
						verified_bots += 1
					elif ent.fake:
						fake_bots += 1
				elif not ent.bot:
					users += 1
					if ent.deleted:
						deleted += 1
					elif ent.scam:
						scam_users += 1
					elif ent.verified:
						verified_users += 1
					elif ent.fake:
						fake_users += 1
					elif ent.premium:
						premium += 1
			elif dialog.is_group:
				chats += 1
			elif dialog.is_channel:
				if ent.megagroup or ent.gigagroup:
					if ent.megagroup:
						megagroups += 1
					elif ent.gigagroup:
						gigagroups += 1

					if ent.fake:
						fake_chats += 1
					elif ent.scam:
						scam_chats += 1
					elif ent.verified:
						verified_chats += 1
				elif not ent.megagroup and not ent.gigagroup:
					channels += 1

					if ent.fake:
						fake_channels += 1
					elif ent.scam:
						scam_channels += 1
					elif ent.verified:
						verified_channels += 1
		textik = self.strings('dialogs_info').format(
			users, chats, channels, bots,
			fake_users, scam_users,
			random.choice(premium_emojies),
			premium, verified_users, deleted,
			megagroups, gigagroups, fake_chats,
			scam_chats, verified_chats, fake_channels,
			scam_channels, verified_channels, fake_bots,
			scam_bots, verified_bots
		)
		await answer(msg, textik)
	
	@loader.command(
		ru_doc="<id or @username> ➪  удалить чат(диалог) с юзером"
	)
	async def dialog_clear(self, message: Message):
		"""<id or @username> ➪  delete dialog with user"""
		args = get_args_raw(message)
		try:
			await self._client.delete_dialog(args)
		except:
			await answer(message, '<b>Кажется произошла ошибка...</b>')
			return
		await answer(message, f'<b>Чат с юзером «{args}» был удален успешно!</b>')
		
	@loader.command(
		ru_doc="➪  алиас для команды 'dialogs_clear'"
	)
	async def dclear(self, message: Message):
		"""➪  alias for command 'dialog_clear'"""
		await self.dialog_clear(message)
	
	@loader.command(
		ru_doc="""Аргументы:
		-deleted ➪  очистить все ЛС с удаленными аккаунтами
		-fake ➪  очистить все ЛС с аккаунтами с пометкой "FAKE"
		-scam ➪  очистить все ЛС со скам аккаунтами
		-bots ➪  очистить все ЛС с ботами
		-allpms ➪  очистить ВСЕ АБСОЛЮТНО ЛС(ОПАСНО)
		-prem ➪  очистить все ЛС с юзерами, обладающими Premium⭐️
		"""
	)
	async def all_dialogs_clear(self, message: Message):
		"""
		Arguments:
		-deleted ➪  delete all dialogs PM with deleted accounts
		-fake ➪  delete all dialogs PM with fake accounts
		-scam ➪  delete all dialogs PM with scam accounts
		-bots ➪  delete all dialog with bots
		-allpms ➪  delete all dialogs PM
		-prem ➪  delete all dialogs PM with PREMIUM⭐️ users
		"""
		await self.clear_dialogs(message)
	
	async def clear_dialogs(self, message):
		msg = await answer(message, "<b>Пожалуйста подождите, выполняется очистка...</b>")
		args = get_args_raw(message)
		deleted_dialogs = 0
		async for chat in self._client.iter_dialogs():
			if chat.is_user:
				ent = chat.entity
				if args == '-deleted' and ent.deleted:
					await self._client.delete_dialog(chat.id)
					deleted_dialogs += 1
				elif args == '-fake' and ent.fake:
					await self._client.delete_dialog(chat.id)
					deleted_dialogs += 1
				elif args == '-scam' and ent.scam:
					await self._client.delete_dialog(chat.id)
					deleted_dialogs += 1
				elif args == '-bots' and ent.bot:
					await self._client.delete_dialog(chat.id)
					deleted_dialogs += 1
				elif args == '-allpms' and chat.id != (await self._client.get_me()).id:
					await self._client.delete_dialog(chat.id)
					deleted_dialogs += 1
				elif args == '-prem' and ent.premium:
					await self._client.delete_dialog(chat.id)
					deleted_dialogs += 1
				#else:
				#	await answer(message, self.strings('args-wrong'))
				#	return
		await answer(msg, f"<b>Было успешно удалено {deleted_dialogs} чатов ЛС.</b>")
			
	@loader.command(
		ru_doc="@chat_username1, @chat_username2, ... ➪  покинуть чаты, с определенными @username"
	)
	async def leave_chats(self, message: Message):
		"""@chat_username1, @chat_username2, ... ➪  leave chats, with usernames in arguments"""
		args = get_args_raw(message)
		if not args:
			await answer(message, 'Не было указано аргументов.')
			return
		msg = await answer(message, '<b>Пожалуйста подождите, процесс выполняется...</b>')
		dd = args.split(', ')
		leave_chatsss = 0
		for id in dd:
			await self._client(functions.channels.LeaveChannelRequest(channel=id))
			leave_chatsss += 1
		await answer(msg, f'<b>Работа завершена.\nВы успешно покинули {leave_chatsss} чата(-ов)!</b>')
