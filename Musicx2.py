#╔═══╦═══╦═╗░╔╦╗░╔╦══╦╗╔═╗░░╔═══╦╗░╔╦═══╦═══╦═══╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#╚╗╔╗║╔══╣║╚╗║║║░║╠╣╠╣║║╔╝░░║╔═╗║║░║║╔═╗║╔══╣╔═╗║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#░║║║║╚══╣╔╗╚╝║╚═╝║║║║╚╝╝░░░║╚══╣║░║║╚═╝║╚══╣╚═╝║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#░║║║║╔══╣║╚╗║╠══╗║║║║╔╗║░░░╚══╗║║░║║╔══╣╔══╣╔╗╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#╔╝╚╝║╚══╣║░║║║░░║╠╣╠╣║║╚╗░░║╚═╝║╚═╝║║░░║╚══╣║║╚╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#╚═══╩═══╩╝░╚═╝░░╚╩══╩╝╚═╝░░╚═══╩═══╩╝░░╚═══╩╝╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#╔═══╦═══╦════╦═══╦╗░░╔╦╗░░╔╗░░░╔═══╦═══╦═══╦╗░╔╦══╦╗╔═╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#║╔═╗║╔═╗║╔╗╔╗║╔═╗║╚╗╔╝║╚╗╔╝║░░░║╔═╗║╔══╣╔═╗║║░║╠╣╠╣║║╔╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#║║░║║╚══╬╝║║╚╣╚═╝╠╗╚╝╔╩╗╚╝╔╝░░░║╚═╝║╚══╣╚═╝║╚═╝║║║║╚╝╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#║║░║╠══╗║░║║░║╔╗╔╝╚╗╔╝░╚╗╔╝░░░░║╔══╣╔══╣╔╗╔╩══╗║║║║╔╗║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#║╚═╝║╚═╝║░║║░║║║╚╗░║║░░░║║░░░░░║║░░║╚══╣║║╚╗░░║╠╣╠╣║║╚╗░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#╚═══╩═══╝░╚╝░╚╝╚═╝░╚╝░░░╚╝░░░░░╚╝░░╚═══╩╝╚═╝░░╚╩══╩╝╚═╝░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
# requires: requests bs4
# meta developer: @ToXicUse, @Den4ikSuperOstryyPer4ik
# scope: hikka_only
from bs4 import BeautifulSoup
import requests
from telethon.tl.types import Message
from ..utils import rand
from urllib.parse import quote_plus
from .. import loader  # noqa
from .. import utils  # noqa
import re
    @loader.tds
    class Musicx2betaMod(loader.Module):
    """Найти музыку через бота @Den4ikSOPer4ik_music_bot(beta)"""
    async def smx2cmd(self, message):
        """Используй: .smx2 «название», чтобы найти музыку по названию.""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>Нету аргументов.</b>")  
        try:
            await message.edit("<b>Загрузка...</b>") 
            music = await message.client.inline_query('@Den4ikSOPer4ik_music_bot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>Музыка с названием <code>{args}</code> не найдена.</b>")