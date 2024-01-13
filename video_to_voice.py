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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/VideoToVoice.jpg
# requires: moviepy

import os
from pathlib import Path

import moviepy.editor
import telethon

from .. import loader, utils


@loader.tds
class VideoToVoice(loader.Module):
	'''Convert Video to voice'''
	
	strings = {
		"name": "VideoToVoice"
	}
	
	def get_audio(self, path: str) -> str:
		video_file = Path(path)
		
		video = moviepy.editor.VideoFileClip(str(video_file))
		audio = video.audio
		audio.write_audiofile(f"{video_file.stem}.ogg")
		os.remove(path)
		return f"{video_file.stem}.ogg"
	
	def get_duration(self, attributes):
		duration = 0
		for i in attributes:
			if isinstance(i, telethon.tl.types.DocumentAttributeVideo):
				duration = i.duration
				break
		return duration
	
	@loader.command()
	async def convert_to_voice(self, message):
		"""<reply_to_video> -> получить Войс звука видео, либо отправлять команду с прикрепленным видео(оно удалится после отправления сделанного войса), либо отправить команду ответом на видео."""
		msg = await utils.answer(message, "Ожидайте, загрузка...")
		
		reply = await message.get_reply_message()
		
		if message.media is None and reply and reply.media is None or message.media is None and reply is None:
			return await utils.answer(msg, "Кажется вы не ответили командой на видео или не прикрепили видео к сообщению с командой.")
		
		if message.media:
			msg_media = message
		elif reply and reply.media:
			msg_media = await message.get_reply_message()
		else:
			return await utils.answer(msg, "Кажется вы не ответили командой на видео или не прикрепили видео к сообщению с командой.")
		
		
		path = self.get_audio((await msg_media.download_media()))
		
		await self.client.send_file(
			message.chat.id,
			path,
			attributes=[
				telethon.tl.types.DocumentAttributeAudio(
					duration=(self.get_duration(msg_media.media.document.attributes)),
					voice=True,
					title=None,
					performer=None,
					waveform=None
				)
			]
		)
		os.remove(path)

		if msg.out:
			await msg.delete()
