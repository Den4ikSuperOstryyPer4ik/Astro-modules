# meta developer: @ToXicUse and @Den4ikSuperOstryyPer4ik

import os
from asyncio import sleep

from telethon import functions
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest

from .. import loader, utils


@loader.tds
class UserMod(loader.Module):
	"""Управление профилем в Telegram"""
	strings = {'name': 'User'}
	
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self.client = client
		self.db = db
		self.me = await client.get_me()
		self.db.set(__name__, "first_copy", True)
		self.db.set(__name__, "avatar_copy", 0)


	async def avacmd(self, message):
		"""—> Получить все аватарки пользователя"""
		id = utils.get_args_raw(message)
		user = await message.get_reply_message()
		chat = message.input_chat
		if user:
			photos = await self.client.get_profile_photos(user.sender)
			u = True
		else:
			photos = await self.client.get_profile_photos(chat)
			u = False
		if id.strip() == "":
			if len(photos) > 0:
				await self.client.send_file(message.chat_id, photos)
			else:
				try:
					if u:
						photo = await self.client.download_profile_photo(
							user.sender)
					else:
						photo = await self.client.download_profile_photo(
							message.input_chat)
					await self.client.send_file(message.chat_id, photo)
				except:
					await message.edit("<code>У этого пользователя нету аватарок</code>")
					return
		else:
			try:
				id = int(id)
				if id <= 0:
					await message.edit(
						"<code>ID номер неправильный</code>")
					return
			except:
				await message.edit(
					"<code>ID номер неправильный</code>")
				return
			if int(id) <= (len(photos)):
				send_photos = await self.client.download_media(photos[id - 1])
				await self.client.send_file(message.chat_id, send_photos)
			else:
				await message.edit("<code>No photo found with that id</code>")
				return
		await message.delete()

	async def setavacmd(self, message):
		"""—> Загрузить автарку"""
		reply = await check_mediaa(message)
		if not reply:
			try:
				reply = await message.get_reply_message()
				if not reply:
					return await message.edit(
						"No reply on gif / animated sticker / video message .")
				await message.edit("Загрузкп...")
				if reply.video:
					await message.client.download_media(reply.media,
					                                    "ava.mp4")
					await message.edit("Конвертация...")
					os.system(
						"ffmpeg -i ava.mp4 -c copy -an gifavaa.mp4 -y")
					os.system(
						"ffmpeg -i gifavaa.mp4 -vf scale=360:360 gifava.mp4 -y")
				else:
					await message.client.download_media(reply.media,
					                                    "tgs.tgs")
					await message.edit("Converting...")
					os.system(
						"lottie_convert.py tgs.tgs tgs.gif; mv tgs.gif gifava.mp4")
				await message.edit("Загрузка аватарки...")
				await message.client(
					functions.photos.UploadProfilePhotoRequest(
						video=await message.client.upload_file("gifava.mp4"),
						video_start_ts=0.0))
				await message.edit("Аватарка загружена.")
				os.system("rm -rf ava.mp4 gifava.mp4 gifavaa.mp4 tgs*")
			except:
				await message.edit(
					"Damn, what a fool I am, I don't know a gif/animated sticker/video from any other file.\n\n" +
					"<b>THIS FILE IS NOT SUPPORTED!!!</b>(or just some tech.error c: )")
				try:
					os.system("rm -rf ava.mp4 gifava.mp4 gifavaa.mp4 tgs*")
				except:
					pass
				return
		else:
			reply = await message.get_reply_message()
			try:
				reply.media.photo
			except:
				await message.edit("Дайте фоторафию пожалуйста.")
				return
			await message.edit("Загрузка...")
			photo = await message.client.download_media(message=reply.photo)
			up = await message.client.upload_file(photo)
			await message.edit("Uploading avatar...")
			await message.client(functions.photos.UploadProfilePhotoRequest(up))
			await message.delete()
			os.remove(photo)

	async def delavacmd(self, message):
		"""—> Удаление аватарки"""
		ava = await message.client.get_profile_photos('me', limit=1)
		if len(ava) > 0:
			await message.edit("Удаление аватарки...")
			await message.client(functions.photos.DeletePhotosRequest(ava))
			await message.edit("Автарка удалена!")
		else:
			await message.edit(
				"У тебя нету аватарки!")

	async def delavascmd(self, message):
		"""—> Удалить все аватарки"""
		ava = await message.client.get_profile_photos('me')
		if len(ava) > 0:
			await message.edit("Удаление аватарок...")
			await message.client(functions.photos.DeletePhotosRequest(
				await message.client.get_profile_photos('me')))
			await message.edit("Все аватарки удалены!")
		else:
			await message.edit(
				"У вас нету аватарок!")

	async def setnamecmd(self, message):
		"""—> Изменить имя"""
		args = utils.get_args_raw(message).split('/')
		if len(args) == 1:
			firstname = args[0]
			lastname = ' '
		elif len(args) == 2:
			firstname = args[0]
			lastname = args[1]
		await message.client(
			UpdateProfileRequest(first_name=firstname, last_name=lastname))
		await message.edit('Имя изменено успешно!')

	async def setbiocmd(self, message):
		"""—> Изменить био(о себе)"""
		args = utils.get_args_raw(message)
		if not args:
			return await message.edit('Нет аргументов.')
		await message.client(UpdateProfileRequest(about=args))
		await message.edit('Био(о себе) изменено успешно!')

	async def setusercmd(self, message):
		"""—> Изменить свой юзернейм(@)"""
		args = utils.get_args_raw(message)
		if not args:
			return await message.edit('Нет аргументов.')
		try:
			await message.client(UpdateUsernameRequest(args))
			await message.edit('Юзернейм изменен успешно!')
		except UsernameOccupiedError:
			await message.edit('Юзернейм уже занят Попробуйте другой!')


async def check_mediaa(message):
	reply = await message.get_reply_message()
	if not reply:
		return False
	if not reply.file:
		return False
	mime = reply.file.mime_type.split("/")[0].lower()
	if mime != "image":
		return False
	return reply
