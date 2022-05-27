# scope: inline_content
# requires: requests bs4 spotipy
# meta developer: @ToXicUse, @Den4ikSuperOstryyPer4ik

from bs4 import BeautifulSoup

import requests
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InputTextMessageContent,
)
from telethon.tl.types import Message
from telethon.tl.functions.channels import JoinChannelRequest
from ..inline.types import InlineQuery
from ..utils import rand
from urllib.parse import quote_plus
from .. import loader  # noqa
from .. import utils  # noqa
import logging
import re

logger = logging.getLogger(__name__)

api_headers = {
    "User-Agent": "CompuServe Classic/1.22",
    "Accept": "application/json",
    "Host": "api.genius.com",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.82 Safari/537.36"
}
host = "https://api.genius.com"
n = "\n"


def get_lyrics(self, song_url, remove_section_headers=False):
    """Uses BeautifulSoup to scrape song info off of a Genius song URL"""
    page = requests.get(song_url, headers=headers)
    html = BeautifulSoup(page.text.replace("<br/>", "\n"), "html.parser")
    lyrics = "\n".join(
        [
            p.get_text()
            for p in html.find_all("div", attrs={"data-lyrics-container": "true"})
        ]
    )
    # Remove [Verse], [Bridge], etc.
    lyrics = re.sub(r"(\[.*?\])", "</i><b>\g<1></b><i>", lyrics)
    if remove_section_headers:
        lyrics = re.sub(r"(\[.*?\])*", "", lyrics)
        lyrics = re.sub("\n{2}", "\n", lyrics)
    if not lyrics:
        return self.strings['noLyrics']
    return lyrics


def search(q):
    """Search documents hosted on Genius"""
    req = requests.get(
        f"https://api.genius.com/search"
        f"?text_format=plain"
        f"&q={quote_plus(q)}"
        f"&access_token=uhYUr-qrBp5V3o46lA8vcaL1DKXTWVs5SDsb_0CDCIcKxKLwtapqeqkdNu8JnA6w",
        headers=api_headers,
    ).json()

    return [
        {
            "artists": hit["result"]["artist_names"].replace("\u200b", ""),
            "title": hit["result"]["title"].replace("\u200b", ""),
            "pic": hit["result"]["header_image_thumbnail_url"],
            "url": hit["result"]["url"],
            "id": hit["result"]["id"],
        }
        for hit in req["response"]["hits"]
    ]


def add_protocol(x):
    """Add https protocol to link"""
    return f"https:{x}" if x.startswith("//") else x

@loader.tds
class LyricsMod(loader.Module):
    """Музыка и тексты песен"""

    strings = {
        "name": "Music Module",
        "type_name": "<b>🚫 Please type name of the song</b>",
        "genius": "🎵 Full lyrics on Genius",
        "noSpotify": "<b>🚫 Please install SpotifyNow module and proceed auth</b>\n"
                     "🌃 Install: <code>.dlmod https://mods.hikariatama.ru/spotify.py</code>",
        "notFound": "🚫 No results found",
        "couldn'tFind": "We couldn't find what are you looking for",
        "sauth": "<b>🚫 Execute <code>.sauth</code> before using this action.</b>",
        "SpotifyError": "<b>🚫 Spotify error</b>",
        "noResults": "<b>🚫 No results found for <code>{}</code></b>",
        "noLyrics": "<b>🚫 Couldn't find the lyrics</b>",
        "lyrics": "Lyrics for <b>{}</b> by <b>{}</b>\n<i>{}",
        "loading": "Loading lyrics for <b>{}</b> by <b>{}</b>...\n{}",
    }

    strings_ru = {
        "_cls_doc": "Поиск тексов песен с Genius",
        "_cmd_doc_lyrics": "Получить слова песни",
        "_cmd_doc_slyrics": "Получить слова песни прослушиваемой в Спотифай, "
                            "для работоспособности требуется модуль SpotifyNow",
        "_ihandle_doc_lyrics": "Поиск текста песни",
        "type_name": "<b>🚫 Пожалуйста, введите имя композиции</b>",
        "genius": "🎵 Полный текст на Genius",
        "noSpotify": "<b>🚫 Пожалуйста установи модуль SpotifyNow и пройди авторизацию.</b>\n"
                     "🌃 Установка: <code>.dlmod https://mods.hikariatama.ru/spotify.py</code>",
        "notFound": "🚫 Результаты не найдены",
        "couldn'tFind": "К сожалению мы не нашли, что вы искали",
        "sauth": "<b>🚫 Выполни <code>.sauth</code> перед этим действием.</b>",
        "SpotifyError": "<b>🚫 Ошибка Спотифай</b>",
        "noResults": "<b>🚫 Результаты для <code>{}</code> не найдены</b>",
        "noLyrics": "<b>🚫 Не удалось найти текст</b>",
        "lyrics": "Текст песни <b>{}</b> от <b>{}</b>\n<i>{}",
        "loading": "Загрузка текста песни <b>{}</b> от <b>{}</b>...\n{}"
    }

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
        self.bot_id = (await self.inline.bot.get_me()).id
        try:
            channel = await self.client.get_entity(f"t.me/{self.strings['author']}")
            await client(JoinChannelRequest(channel))
        except Exception:
            logger.info(f"Can't join {self.strings['author']}")
        try:
            post = (await client.get_messages(self.strings["author"], ids=[13]))[0]
            await post.react("❤️")
        except Exception:
            logger.info(f"Can't react to {self.strings['author']}")

    async def lyricscmd(self, message: Message):
        """Get lyrics"""
        text = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not text:
            if reply:
                if (
                        getattr(reply, "media", None)
                        and getattr(reply.media, "document", None)
                        and getattr(reply.media.document, "attributes", None)
                ):
                    text = reply.media.document.attributes[1].file_name.rsplit(".", 1)[0]
                else:
                    try:
                        e = next(entity for entity in reply.entities if type(entity).__name__ == "MessageEntityCode")
                        text = reply.raw_text[e.offset - 1: e.offset + e.length]
                    except Exception:
                        text = reply.raw_text
            else:
                await utils.answer(message, self.strings["type_name"])
                return
        if tracks := search(text):
            track = tracks[0]
        else:
            await utils.answer(message, self.strings["noResults"].format(text))
            return
        await self.inline.form(
            self.strings["lyrics"].format(
                track["title"], track["artists"], get_lyrics(self, track["url"])
            )[:4092] + "</i>",
            reply_markup=[[{"text": self.strings["genius"], "url": track["url"]}]],
            force_me=False,
            message=message,
        )

    async def lyrics_inline_handler(self, query: InlineQuery) -> None:
        """Search song"""
        text = query.args
        if not text:
            return
        tracks = search(text)
        if not tracks:
            await query.answer(
                [
                    InlineQueryResultArticle(
                        id="-1",
                        title=self.strings["notFound"],
                        description=self.strings["couldn'tFind"],
                        thumb_url="https://img.icons8.com/stickers/100/000000/nothing-found.png",
                        input_message_content=InputTextMessageContent(
                            self.strings["noResults"].format(text),
                            parse_mode="HTML",
                        ),
                    )
                ],
                cache_time=0,
            )
            return
        res = [
            InlineQueryResultArticle(
                id=track["id"],
                title=track["title"],
                description=track["artists"],
                thumb_url=add_protocol(track["pic"]),
                input_message_content=InputTextMessageContent(
                    self.strings['loading'].format(track['title'], track['artists'], track['url']),
                    parse_mode="HTML",
                    disable_web_page_preview=True,
                ),
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(self.strings['genius'], url=track["url"])
                ),
            ) for track in tracks[:50]
        ]
        await query.answer(res, cache_time=0)

    async def slyricscmd(self, message: Message):
        """Get lyrics from your current Spotify playback (Needs SpotifyNow module)"""
        check = self.db.get("SpotifyNow", "acs_tkn", "404")
        if check == "404":
            await utils.answer(message, self.strings["noSpotify"])
            return
        elif check is None:
            await utils.answer(message, self.strings["sauth"])
            return
        try:
            sp = spotipy.Spotify(
                auth=self.db.get("SpotifyNow", "acs_tkn")["access_token"]
            )
            current_playback = sp.current_playback()
        except Exception:
            await utils.answer(message, self.strings["SpotifyError"])
            return
        try:
            track = current_playback["item"]["name"]
        except Exception:
            track = None
        try:
            artists = ", ".join([artist["name"] for artist in current_playback["item"]["artists"]])
        except Exception:
            artists = None
        text = f"{artists} {track}"
        if tracks := search(text):
            track = tracks[0]
        else:
            await utils.answer(message, self.strings["noResults"].format(text))
            return
        await self.inline.form(
            self.strings["lyrics"].format(
                track["title"], track["artists"], get_lyrics(self, track["url"])
            )[:4092] + "</i>",
            reply_markup=[[{"text": self.strings["genius"], "url": track["url"]}]],
            force_me=False,
            message=message,
        )

    async def watcher(self, message: Message) -> None:
        if (
                getattr(message, "out", False)
                and getattr(message, "via_bot_id", False)
                and message.via_bot_id == self.bot_id
                and (
                "Loading lyrics for" in getattr(message, "raw_text", "")
                or "Загрузка текста песни" in getattr(message, "raw_text", "")
        )
        ):
            e = message.entities
            track = {
                "title": message.raw_text[e[0].offset:e[0].offset + e[0].length],
                "artists": message.raw_text[e[1].offset:e[1].offset + e[1].length],
                "url": message.raw_text.splitlines()[1]
            }
            await self.inline.form(
                self.strings["lyrics"].format(
                    track["title"], track["artists"], get_lyrics(self, track["url"])
                )[:4092] + "</i>",
                reply_markup=[[{"text": self.strings["genius"], "url": track["url"]}]],
                force_me=False,
                message=message,
            )
        return
        
    async def smcmd(self, message): 
        """Используй: .sm «название» чтобы найти музыку по названию.""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>Нету аргументов.</b>")  
        try: 
            await message.edit("<b>Загрузка...</b>") 
            music = await message.client.inline_query('lybot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>Музыка с названием <code>{args}</code> не найдена.</b>")
    async def smx2cmd(self, message):
        """Используй: .smx2 «название», чтобы найти музыку по названию.""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>Нету аргументов.</b>")  
        try:
            await message.edit("<b>Загрузка...</b>") 
            music = await message.client.inline_query('Den4ikSOPer4ik_music_bot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>Музыка с названием <code>{args}</code> не найдена.</b>")