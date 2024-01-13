__version__ = (1, 6, 0)

# module by:
# █▀ █▄▀ █ █░░ █░░ ▀█
# ▄█ █░█ █ █▄▄ █▄▄ █▄
#        /\_/\
#       ( o.o )
#        > ^ <
# █▀▄▀█ █▀▀ █▀█ █░█░█
# █░▀░█ ██▄ █▄█ ▀▄▀▄▀
#
#                   and                
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/RandomUser.jpg

import logging
import random as r

import grapheme
from telethon.errors import (
    BotGroupsBlockedError,
    ChannelPrivateError,
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    InputUserDeactivatedError,
    UserAdminInvalidError,
    UserAlreadyParticipantError,
    UserBlockedError,
    UserKickedError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    InviteToChannelRequest,
)
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights, Message

from .. import loader
from ..inline.types import InlineCall

logger = logging.getLogger(__name__)

UNMUTE_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    embed_links=False,
)


class RandomUserMod(loader.Module):
    '''choose a random user in chat\nAutors: @AstroModules & @smeowcodes'''

    emoji_list = list(grapheme.graphemes("🤩🥳🤪😜😝😋😘🤯🤠😈🎃😺👀🙊🙈🙉🐵🐸🐣🌝🌚🌜🌛🌙✨⚡️🌟⭐️💫💥☄️❄️☀️🌪🔥☃️☁️💨💧💦🌊🍓🍉🍋🍊🍐🍎🍌🍇🫐🍈🍒🍑🥭🍍🥝"))

    strings = {
        "name": "RandomUser",
        "astro-modules-btn": "🌌 𝑨𝒔𝒕𝒓𝒐 𝑴𝒐𝒅𝒖𝒍𝒆𝒔 ✨",
        "meow-modules-btn": "Meow Modules😽",
        "inline-text": "<b>👥 Click on the button to select a random user in the chat!</b>",
        "rand-user-btn": "🤩 Choose",
        "rand-user-2-btn": "🤯 Choose again",
        "user": "<b>{} The choice fell on {}!\n{}</b>",
        "user-...": "<b>{} The choice fell on {}!\n{}\n\n{}</b>",
        "id": "🆔 ID: <code>{}</code>",
        "id+username": "{} Username: @{}\n🆔 ID: <code>{}</code>",
        "give-adm-btn": "🎩 Give Admin",
        "text-adm": "<b>🎩 Was assigned to the administrator\n👨🏻‍💻 Prefix(rank): «{}»</b>",
        "mute-btn": "🤫 Mute",
        "unmute-btn": "😊 UnMute",
        "ban-btn": "👔 Ban",
        "unban-btn": "😊 UnBan",
        "kick-btn": "👞 Kick",
        "invite-btn": "➕ Add back",
        "prefix-1": "Cool person :)",
        "prefix-2": "Lucky",
        "prefix-3": "⁤ ",
        "prefix-4": "King of Random",
        "prefix-5": "GAY",
        "not_admin": "I`m not an admin here.",
        "no_rights": "I don`t have rights.",
        "user-invited": "🚹 The user has been invited successfully!",
        "user-kicked": "👞 Was kicked out",
        "user-unmuted": "😊 The user unmuted",
        "user-muted": "🤫 Muted",
        "user-banned": "👔 Banned",
        "user-unbanned": "😊 The user unbanned.",
        "invite-error-1": "The user's privacy settings do not allow you to invite him.",
        "invite-error-2": "I don't have a permission.",
        "invite-error-3": "The user is kicked out of the chat, contact the administrators.",
        "invite-error-4": "The bot is blocked in the chat, contact the administrators.",
        "invite-error-5": "The user is blocked in the chat, contact the administrators.",
        "invite-error-6": "The user's account has been deleted.",
        "invite-error-7": "The user is already in the group.",
        "invite-error-8": "You have blocked this user.",
    }

    strings_ru = {
        "_cls_doc": "Выбрать случайного пользователя в чате\nАвторы: @AstroModules & @smeowcodes",
        "inline-text": "<b>👥 Нажмите на кнопку, чтобы выбрать случайного пользователя в чате:</b>",
        "rand-user-btn": "🤩 Выбрать",
        "rand-user-2-btn": "🤯 Выбрать ещё раз",
        "user": "<b>{} Выбор упал на {}!\n{}</b>",
        "user-...": "<b>{} Выбор упал на {}!\n{}\n\n{}</b>",
        "id+username": "{} Имя пользователя: @{}\n🆔 ID: <code>{}</code>",
        "give-adm-btn": "🎩 Назначить на администратора",
        "text-adm": "🎩 Был назначен на администратора\n👨🏻‍💻 Префикс: «{}»",
        "prefix-1": "Крутой :)",
        "prefix-2": "Везучий",
        "prefix-3": "Удачливый",
        "prefix-4": "Король рандома",
        "prefix-5": "Лютейший чел",
        "mute-btn": "🤫 Заткнуть",
        "unmute-btn": "😊 Снять мут",
        "ban-btn": "🚫 Забанить",
        "unban-btn": "💥 Разбанить",
        "kick-btn": "👞 Выгнать",
        "invite-btn": "➕ Добавить обратно",
        "not_admin": "Я здесь не администратор.",
        "no_rights": "🚫 У Вас нет нужных прав",
        "user-invited": "🚹 Пользователь был добавлен обратно!",
        "user-kicked": "👞 Был выгнан",
        "user-unmuted": "🔔 С пользователя был снят мут",
        "user-muted": "🤫 Был заткнут",
        "user-banned": "👔 Был забанен",
        "user-unbanned": "😊 С пользователя был снят бан.",
        "invite-error-1": "Настройки приватности пользователя не позволяют пригласить его.",
        "invite-error-2": "🚫 У Вас нет нужных прав",
        "invite-error-3": "Пользователь кикнут из чата, обратитесь к администраторам.",
        "invite-error-4": "Бот заблокирован в чате, обратитесь к администраторам.",
        "invite-error-5": "Пользователь заблокирован в чате, обратитесь к администраторам.",
        "invite-error-6": "Аккаунт пользователя удалён.",
        "invite-error-7": "Пользователь уже в группе.",
        "invite-error-8": "Вы заблокировали этого пользователя.",
    }

    @loader.command(ru_doc="--> выбрать случайного пользователя в чате | inline-меню с призовыми кнопками")
    async def irandusercmd(self, message: Message):
        "choose a random user in chat | inline menu with prize buttons"
        self.users = [p.id async for p in self.client.iter_participants(message.peer_id)]
        self.chat = await message.get_chat()
        self.chat_id = message.chat_id
        self.message = message
        await self.inline.form(
            text=self.strings("inline-text"),
            reply_markup=[
                [
                    {
                        "text": self.strings("rand-user-btn"),
                        "callback": self.rand_user_inline
                    }
                ]
            ],
            message=message
        )

    async def rand_user_inline(self, call: InlineCall):
        rand_user = r.choice(self.users)
        self.user = await self.client.get_entity(rand_user)
        emoji_list = list(grapheme.graphemes("🤩🥳🤪😜😝😋😘🤯🤠😈🎃😺👀🙊🙈🙉🐵🐸🐣🌝🌚🌜🌛🌙✨⚡️🌟⭐️💫💥☄️❄️☀️🌪🔥☃️☁️💨💧💦🌊🍓🍉🍋🍊🍐🍎🍌🍇🫐🍈🍒🍑🥭🍍🥝"))
        emoji = r.choice(emoji_list)

        if not self.user.username:
            self.link = self.user.first_name
            self.id_or_username = self.strings("id").format(self.user.id)
        else:
            self.link = f"<a href='https://t.me/{self.user.username}'>{self.user.first_name}</a>"
            emoji_list2 = list(grapheme.graphemes("👤👶👧🧒👦👩🧑👨👩‍🦱🧑‍🦱👨‍🦱👩‍🦰🧑‍🦰👨‍🦰👱‍♀👱👱‍♂👩‍🦳🧑‍🦳👨‍🦳👵🧓👴"))
            emoji2 = r.choice(emoji_list2)
            self.id_or_username = self.strings("id+username").format(emoji2, self.user.username, self.user.id)

        await call.edit(
            text=self.strings("user").format(emoji, self.link, self.id_or_username),
            reply_markup=[
                [
                    {
                        "text": self.strings("rand-user-2-btn"),
                        "callback": self.rand_user_inline
                    }
                ],
                [
                    {
                        "text": self.strings("give-adm-btn"),
                        "callback": self.add_to_admins_user
                    }
                ],
                [
                    {
                        "text": self.strings("ban-btn"),
                        "callback": self.ban_user
                    },
                    {
                        "text": self.strings("kick-btn"),
                        "callback": self.kick_user
                    },
                    {
                        "text": self.strings("mute-btn"),
                        "callback": self.mute_user
                    }
                ],
                [
                    {
                        "text": self.strings("astro-modules-btn"),
                        "url": "https://t.me/AstroModules"
                    },
                    {
                        "text": self.strings("meow-modules-btn"),
                        "url": "https://t.me/smeowcodes"
                    }
                ]
            ]
        )

    async def add_to_admins_user(self, call: InlineCall):
        pref1 = self.strings("prefix-1")
        pref2 = self.strings("prefix-2")
        pref3 = self.strings("prefix-3")
        pref4 = self.strings("prefix-4")
        pref5 = self.strings("prefix-5")
        prefs = [pref1, pref2, pref3, pref4, pref5]
        prefix = r.choice(prefs)
        text = self.strings("text-adm").format(prefix)
        emoji = r.choice(self.emoji_list)

        if not self.chat.admin_rights and not self.chat.creator:
            return await call.answer(self.strings("not_admin"), show_alert=True)
        
        try:
            await self.client(
                EditAdminRequest(
                    self.chat_id,
                    self.user.id,
                    ChatAdminRights(
                        add_admins=False,
                        change_info=False,
                        invite_users=self.chat.admin_rights.invite_users,
                        ban_users=False,
                        delete_messages=self.chat.admin_rights.delete_messages,
                        pin_messages=False,
                    ),
                    prefix,
                )
            )
        except ChatAdminRequiredError:
            return await call.answer(self.strings("no_rights"), show_alert=True)
        else:
            await call.answer(text, show_alert=True)
            return await call.edit(
                text=self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
                reply_markup=[
                    [
                        {
                            "text": self.strings("rand-user-2-btn"),
                            "callback": self.rand_user_inline
                        }
                    ]
                ]
            )

    async def mute_user(self, call: InlineCall):
        text = self.strings("user-muted")
        emoji = r.choice(self.emoji_list)
        
        if not self.chat.admin_rights and not self.chat.creator:
            return await call.answer(self.strings("not_admin"), show_alert=True)

        if not self.chat.admin_rights.ban_users:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        try:
            tm = ChatBannedRights(until_date=True, send_messages=True)
            await self.client(EditBannedRequest(
                self.chat_id,
                self.user.id,
                tm
            ))
            await call.answer(text, show_alert=True)
            return await call.edit(
                text=self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
                reply_markup=[
                    [
                        {
                            "text": self.strings("unmute-btn"),
                            "callback": self.unmute_user
                        }
                    ],
                    [
                        {
                            "text": self.strings("rand-user-2-btn"),
                            "callback": self.rand_user_inline
                        }
                    ]
                ]
            )
        except UserAdminInvalidError:
            return await call.answer(self.strings("no_rights"), show_alert=True)

    async def unmute_user(self, call: InlineCall):
        text = self.strings("user-unmuted")
        emoji = r.choice(self.emoji_list)
        if not self.chat.admin_rights and not self.chat.creator:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        if not self.chat.admin_rights.ban_users:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        await self.client(
                EditBannedRequest(self.chat_id, self.user.id, UNMUTE_RIGHTS)
        )
        await call.answer(text, show_alert=True)
        await call.edit(
            self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
            reply_markup=[
                [
                    {
                        "text": self.strings("rand-user-2-btn"),
                        "callback": self.rand_user_inline
                    }
                ]
            ]
        )

    async def ban_user(self, call: InlineCall):
        if not self.chat.admin_rights and not self.chat.creator:
            return await call.answer(self.strings("not_admin"), show_alert=True)

        if not self.chat.admin_rights.ban_users:
            return await call.answer(self.strings("no_rights"), show_alert=True)
        try:
            await self.client(EditBannedRequest(
                self.chat_id,
                self.user.id,
                ChatBannedRights(until_date=None, view_messages=True)
            ))
            text = self.strings("user-banned")
            emoji = r.choice(self.emoji_list)
            await call.answer(text, show_alert=True)
            await call.edit(
                self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
                reply_markup=[
                    [
                        {
                            "text": self.strings("unban-btn"),
                            "callback": self.unban_user
                        }
                    ],
                    [
                        {
                            "text": self.strings("rand-user-2-btn"),
                            "callback": self.rand_user_inline
                        }
                    ]
                ]
            )
        except UserAdminInvalidError:
            return await call.answer(self.strings("no_rights"), show_alert=True)

    async def unban_user(self, call: InlineCall):
        text = self.strings("user-unbanned")
        emoji = r.choice(self.emoji_list)
        if not self.chat.admin_rights and not self.chat.creator:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        if not self.chat.admin_rights.ban_users:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        await self.client(
                EditBannedRequest(
                    self.chat_id,
                    self.user.id,
                    ChatBannedRights(until_date=None, view_messages=False),
                )
            )
        await call.answer(text, show_alert=True)
        await call.edit(
            self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
            reply_markup=[
                [
                    {
                        "text": self.strings("rand-user-2-btn"),
                        "callback": self.rand_user_inline
                    }
                ]
            ]
        )

    async def kick_user(self, call: InlineCall):
        text = self.strings("user-kicked")
        emoji = r.choice(self.emoji_list)

        if not self.chat.admin_rights and not self.chat.creator:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        if not self.chat.admin_rights.ban_users:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        try:
            await self.client.kick_participant(self.chat_id, self.user.id)
        except UserAdminInvalidError:
            return await call.answer(self.strings("no_rights"), show_alert=True)

        await call.answer(text, show_alert=True)
        return await call.edit(
            self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
            reply_markup=[
                [
                    {
                        "text": self.strings("invite-btn"),
                        "callback": self.invite_user
                    }
                ],
                [
                    {
                        "text": self.strings("rand-user-2-btn"),
                        "callback": self.rand_user_inline
                    }
                ]
            ]
        )

    async def invite_user(self, call: InlineCall):
        emoji = r.choice(self.emoji_list)
        try:
            if not self.message.is_channel and self.message.is_group:
                await self.client(
                    AddChatUserRequest(
                        chat_id=self.chat_id, user_id=self.user.id, fwd_limit=1000000
                    )
                )
            else:
                await self.client(
                    InviteToChannelRequest(channel=self.chat_id, users=[self.user.id])
                )
            await call.answer(self.strings("user-invited"), show_alert=True)
            text = self.strings("user-invited")
            return await call.edit(
                text=self.strings("user-...").format(emoji, self.link, self.id_or_username, text),
                reply_markup=[
                    [
                        {
                            "text": self.strings("rand-user-2-btn"),
                            "callback": self.rand_user_inline
                        }
                    ]
                ]
            )

        except UserPrivacyRestrictedError:
            m = self.strings("invite-error-1")
        except UserNotMutualContactError:
            m = self.strings("invite-error-1")
        except ChatAdminRequiredError:
            m = self.strings("invite-error-2")
        except ChatWriteForbiddenError:
            m = self.strings("invite-error-2")
        except ChannelPrivateError:
            m = self.strings("invite-error-2")
        except UserKickedError:
            m = self.strings("invite-error-3")
        except BotGroupsBlockedError:
            m = self.strings("invite-error-4")
        except UserBlockedError:
            m = self.strings("invite-error-5")
        except InputUserDeactivatedError:
            m = self.strings("invite-error-6")
        except UserAlreadyParticipantError:
            m = self.strings("invite-error-7")
        except YouBlockedUserError:
            m = "Вы заблокировали этого пользователя."

        await call.answer(m, show_alert=True)