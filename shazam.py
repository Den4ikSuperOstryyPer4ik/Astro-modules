__version__ = (1, 0, 0)
#   
#    @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
#   @@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
#   @@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
#   !@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
#   @!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
#   !!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
#   !!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
#   :!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
#   ::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
#    :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/AstroShazam.png
# The code snippet is adapted from VoiceMod code by D4n1l3k300
# requires: ShazamAPI

import io
from ShazamAPI import Shazam
from .. import loader, utils

@loader.tds
class ShazamMod(loader.Module):
    """Use <reply to voice> to search for a song using audio."""

    strings = {
        "name": 'Shazam',
        "Downloading": "<emoji document_id=5443127283898405358>📥</emoji> <b>Downloading...</b>",
        "Searching": "<emoji document_id=5447410659077661506>🔎</emoji> <b>Searching...</b>",
        "no_reply": "<emoji document_id=5294339927318739359>🎙</emoji> <b>Please reply to an audio message.</b>",
        "not_found": "<emoji document_id=5210952531676504517>🚫</emoji> <b>Song not found.</b>",
        "track_info": (
            "<emoji document_id=5325547803936572038>✨</emoji> <b>Song found</b>\n"
            '<emoji document_id=5460795800101594035>📝</emoji> <b>Name</b> "<code>{}</code>"'
        )
    }

    strings_ru = {
        "Downloading": "<emoji document_id=5443127283898405358>📥</emoji> <b>Загрузка..</b>",
        "Searching": "<emoji document_id=5447410659077661506>🔎</emoji> <b>Поиск..</b>",
        "no_reply": "<emoji document_id=5294339927318739359>🎙</emoji> <b>Oтветьте на аудио сообщение</b>",
        "not_found": "<emoji document_id=5210952531676504517>🚫</emoji> <b>Не удалось найти песню</b>",
        "track_info": (
            "<emoji document_id=5325547803936572038>✨</emoji> <b>Песня найдена</b>\n"
            '<emoji document_id=5460795800101594035>📝</emoji> <b>Название:</b> "<code>{}</code>"'
        )
    }

    async def fetch_audio(self, message):
        reply = await message.get_reply_message()
        if reply and reply.file and reply.file.mime_type.startswith("audio"):
            await utils.answer(message, self.strings['Downloading'])
            audio_data = io.BytesIO(await reply.download_media(bytes))
            await utils.answer(message, self.strings['Searching'])
            return audio_data, reply
        await utils.answer(message, self.strings['no_reply'])
        return None, None

    @loader.command(ru_doc='<reply to audio> - распознать трек')
    async def sh(self, message):
        """<reply to audio> - recognize track"""
        audio_data, reply = await self.fetch_audio(message)
        if not audio_data:
            return

        try:
            shazam = Shazam(audio_data.read())
            recog = next(shazam.recognizeSong())[1]["track"]
            await self.client.send_file(
                message.peer_id,
                file=recog["images"]["background"],
                caption=self.strings['track_info'].format(recog["share"]["subject"]),
                reply_to=reply.id,
            )
            await message.delete()
        except Exception:
            await utils.answer(message, self.strings['not_found'])
