__version__ = (1, 0, 0)

import json
import random
import string
import logging
import asyncio
import aiohttp
from .. import loader, utils
from yandex_music import ClientAsync
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.channels import EditAdminRequest

# https://github.com/FozerG/YandexMusicRPC/blob/main/main.py#L133
async def get_current_track(client, token):
    device_info = {"app_name": "Chrome","type": 1,}

    ws_proto = {
        "Ynison-Device-Id": "".join([random.choice(string.ascii_lowercase) for _ in range(16)]),
        "Ynison-Device-Info": json.dumps(device_info),
    }

    timeout = aiohttp.ClientTimeout(total=15, connect=10)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.ws_connect(
                url="wss://ynison.music.yandex.ru/redirector.YnisonRedirectService/GetRedirectToYnison",
                headers={
                    "Sec-WebSocket-Protocol": f"Bearer, v2, {json.dumps(ws_proto)}",
                    "Origin": "http://music.yandex.ru",
                    "Authorization": f"OAuth {token}",
                },
                timeout=10,
            ) as ws:
                recv = await ws.receive()
                data = json.loads(recv.data)

            if "redirect_ticket" not in data or "host" not in data:
                print(f"Invalid response structure: {data}")
                return {"success": False}

            new_ws_proto = ws_proto.copy()
            new_ws_proto["Ynison-Redirect-Ticket"] = data["redirect_ticket"]

            to_send = {
                "update_full_state": {
                    "player_state": {
                        "player_queue": {
                            "current_playable_index": -1,
                            "entity_id": "",
                            "entity_type": "VARIOUS",
                            "playable_list": [],
                            "options": {"repeat_mode": "NONE"},
                            "entity_context": "BASED_ON_ENTITY_BY_DEFAULT",
                            "version": {
                                "device_id": ws_proto["Ynison-Device-Id"],
                                "version": 9021243204784341000,
                                "timestamp_ms": 0,
                            },
                            "from_optional": "",
                        },
                        "status": {
                            "duration_ms": 0,
                            "paused": True,
                            "playback_speed": 1,
                            "progress_ms": 0,
                            "version": {
                                "device_id": ws_proto["Ynison-Device-Id"],
                                "version": 8321822175199937000,
                                "timestamp_ms": 0,
                            },
                        },
                    },
                    "device": {
                        "capabilities": {
                            "can_be_player": True,
                            "can_be_remote_controller": False,
                            "volume_granularity": 16,
                        },
                        "info": {
                            "device_id": ws_proto["Ynison-Device-Id"],
                            "type": "WEB",
                            "title": "Chrome Browser",
                            "app_name": "Chrome",
                        },
                        "volume_info": {"volume": 0},
                        "is_shadow": True,
                    },
                    "is_currently_active": False,
                },
                "rid": "ac281c26-a047-4419-ad00-e4fbfda1cba3",
                "player_action_timestamp_ms": 0,
                "activity_interception_type": "DO_NOT_INTERCEPT_BY_DEFAULT",
            }

            async with session.ws_connect(
                url=f"wss://{data['host']}/ynison_state.YnisonStateService/PutYnisonState",
                headers={
                    "Sec-WebSocket-Protocol": f"Bearer, v2, {json.dumps(new_ws_proto)}",
                    "Origin": "http://music.yandex.ru",
                    "Authorization": f"OAuth {token}",
                },
                timeout=10,
                method="GET",
            ) as ws:
                await ws.send_str(json.dumps(to_send))
                recv = await asyncio.wait_for(ws.receive(), timeout=10)
                ynison = json.loads(recv.data)
                track_index = ynison["player_state"]["player_queue"]["current_playable_index"]
                if track_index == -1:
                    print("No track is currently playing.")
                    return {"success": False}

                track = ynison["player_state"]["player_queue"]["playable_list"][track_index]

            await session.close()
            info = await client.tracks_download_info(track["playable_id"], True)
            track = await client.tracks(track["playable_id"])
            res = {
                "paused": ynison["player_state"]["status"]["paused"],
                "duration_ms": ynison["player_state"]["status"]["duration_ms"],
                "progress_ms": ynison["player_state"]["status"]["progress_ms"],
                "entity_id": ynison["player_state"]["player_queue"]["entity_id"],
                "repeat_mode": ynison["player_state"]["player_queue"]["options"]["repeat_mode"],
                "entity_type": ynison["player_state"]["player_queue"]["entity_type"],
                "track": track,
                "info": info,
                "success": True,
            }
            return res

    except Exception as e:
        print(f"Failed to get current track: {str(e)}")
        return {"success": False}


class YmLive(loader.Module):
    '''Модуль для демонстрации играющей песни в Яндекс.Музыке'''

    strings = {
        "name": "YandexMusicLive",
        
        "_text_token": "Токен аккаунта Яндекс Музыки",
        "_text_id": "ID канала, который будет использоваться для показа треков...",

        "on/off": "YandexMusicLive теперь {}",
        'channel_id_error': "В конфиге не указан ID канала. Исправь это!",

        "_from_bot_channel_error": (
            "Не найден ID канала в конфиге. Пожалуйста исправь это для "
            "дальнейшего использования модуля..."
        ),
        'token_from_YmNow': (
            "У вас установлен модуль YmNow и в его конфиге я нашел токен. "
            "Для вашего удобства токен автоматически выставлен в конфиг. "
            "Приятного использования :)"
        ),
        "tutor": (
            "🎉 Добро пожаловать в модуль YandexMusicLive!\n"
            "Вы успешно загрузили модуль, который позволяет отображать играющую музыку "
            "из Яндекс.Музыки прямо в названии вашего канала!\n\n"
            "🌟 Чтобы модуль начал работать, выполните следующие шаги:\n"
            "1) <b>Создайте канал:</b> Cоздайте новый канал, в котором будет "
            "отображаться играющий сейчас трек, и закрепите этот канал в своем профиле.\n\n"
            "2) <b>Настройка токена Яндекс.Музыки:</b> Перейдите в <code>{}config YandexMusicLive</code>"
            " -> YandexMusicToken и вставьте ваш токен Яндекс.Музыки. <a href='{}'>(Туториал на получение токена)</a>\n\n"
            "3) <b>Настройка ID канала:</b> Перейдите в <code>{}config YandexMusicLive</code> -> channel_id"
            " и вставьте ID вашего канала. \n  Если вы не знаете, как получить ID канала - Напишите в канал"
            " сообщение с текстом <code>{}e m.chat.id</code> и вставьте в конфиг то, что вам выдаст ЮзерБот\n\n"
            "4) <b>Переустановите модуль</b> После выполнения всех настроек переустановите модуль, чтобы завершить процесс настройки."
        )
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "YandexMusicToken", 
                None, 
                lambda: self.strings["_text_token"], 
                validator=loader.validators.Hidden()
            ),
            loader.ConfigValue(
                "channel_id",
                None,
                lambda: self.strings["_text_id"],
                validator=loader.validators.TelegramID()
            ),
        )

    async def client_ready(self, client, db):
        """Инициализация клиента и базы данных"""
        self.client = client
        self.db = db

    async def on_dlmod(self):
        """Действия при загрузке модуля"""
        if self.get("new_") != False:
            await self.inline.bot.send_message(
                self.client._tg_id, 
                self.strings("tutor").format(
                    self.get_prefix(), 
                    "https://github.com/MarshalX/yandex-music-api/discussions/513#discussioncomment-2729781",
                    self.get_prefix(),
                    self.get_prefix()
                )
            )
            self.set("new_", False)

        if self.config["YandexMusicToken"] and self.config["YandexMusicToken"].startswith("y0_"):
            await self.add_bot_to_channel(self.config["channel_id"])

    async def add_bot_to_channel(self, channel_id):
        """Добавление бота в канал и выдача прав администратора"""
        try:
            await self._client(
                EditAdminRequest(
                    channel=int(channel_id),
                    user_id=self.inline.bot_username,
                    admin_rights=ChatAdminRights(change_info=True),
                    rank="YandexMusicLiveBot"
                )
            )
            self.set("ymlive_bot_added", True)
        except Exception as e:
            logging.error(f"Не удалось выдать боту права в канале: {e}")

    async def get_current_track(self, token):
        """Получение информации о текущем треке из Яндекс.Музыки"""
        try:
            client = ClientAsync(token)
            await client.init()
            respond = await get_current_track(client, token)
            track = respond.get("track")
            if not track:
                return None
            return {
                "title": track[0]["title"], 
                "artists": [artist["name"] for artist in track[0]["artists"]], 
                "duration_ms": int(track[0]["duration_ms"])
            }
        except Exception as e:
            logging.error(f"Ошибка при получении трека: {e}")
            return None

    async def update_channel_title(self, channel_id, track_name):
        """Обновление названия канала, если оно отличается от текущего трека"""
        try:
            channel_info = await self.client.get_fullchannel(channel_id)
            current_title = channel_info.chats[0].title.split(' - ')[0]
            new_title = track_name.split(' - ')[0]
            if current_title != new_title:
                await self.inline.bot.set_chat_title(int(f'-100{channel_id}'), track_name)
                messages = await self._client.get_messages(channel_id, limit=1)
                if messages and messages[0].action:
                    await messages[0].delete()
        except Exception as e:
            logging.error(f"Ошибка при изменении названия канала: {e}")

    @loader.command(ru_doc="- включить/выключить YaLive")
    async def yalive(self, message):
        """Включение или выключение автоматического обновления названия канала"""
        if not self.config["channel_id"]:
            await utils.answer(message, self.strings["channel_id_error"])
            return

        if not self.get("ymlive_bot_added"):
            await self.add_bot_to_channel(self.config["channel_id"])

        autochannel_status = self.get("autochannel", False)
        self.set("autochannel", not autochannel_status)
        status_text = "enabled" if not autochannel_status else "disabled"
        await utils.answer(message, self.strings["on/off"].format(status_text))

    @loader.loop(interval=30, autostart=True)
    async def autochannel_loop(self):
        """Цикл для автоматического обновления названия канала каждые 30 секунд"""
        if not self.get("autochannel"):
            return
        if not self.config["channel_id"]:
            await self.inline.bot.send_message(self.client._tg_id, self.strings["_from_bot_channel_error"])
            self.set("autochannel", False)
            return
        try:
            track_info = await self.get_current_track(self.config["YandexMusicToken"])
            if track_info:
                artists = ", ".join(track_info["artists"])
                track_name = f"{track_info['title']} - {utils.escape_html(artists)}"
                await self.update_channel_title(self.config["channel_id"], track_name)
        except Exception as e:
            logging.error(f"Ошибка в autochannel_loop: {e}")
