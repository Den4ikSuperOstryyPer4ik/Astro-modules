__version__ = (1, 4, 1)
#                _             __  __           _       _                
#      /\       | |           |  \/  |         | |     | |               
#     /  \   ___| |_ _ __ ___ | \  / | ___   __| |_   _| | ___  ___      
#    / /\ \ / __| __| '__/ _ \| |\/| |/ _ \ / _` | | | | |/ _ \/ __|     
#   / ____ \\__ \ |_| | | (_) | |  | | (_) | (_| | |_| | |  __/\__ \     
#  /_/    \_\___/\__|_|  \___/|_|  |_|\___/ \__,_|\__,_|_|\___||___/     
#                                                                        
#                         © Copyright 2022                               
#                                                                        
#                https://t.me/Den4ikSuperOstryyPer4ik                    
#                              and                                       
#                      https://t.me/ToXicUse                             
#                                                                         
#                 🔒 Licensed under the GNU AGPLv3                       
#             https://www.gnu.org/licenses/agpl-3.0.html                 
#                                                                                                                 
# meta developer: @AstroModules
from .. import loader, utils

import random
from telethon.tl.types import Message, InputMessagesFilterMusic

@loader.tds
class RandomTrackMod(loader.Module):
	"""Получить рандомный трек. 
	Используйте категории чтобы сгенерировать трек на свой вкус."""

	strings = {"name": "RandomTrack"}
  
	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"playlist",
				None,
				doc=lambda: "Введите юзер своего канала с музыкой",
			),
			loader.ConfigValue(
				"fonks",
				"AM_fonks",
				doc=lambda: "Введите юзер своего канала с фонками",
			),
			loader.ConfigValue(
				"remixes",
				"AM_rmx",
				doc=lambda: "Введите юзер своего канала с ремиксами",
			),
			loader.ConfigValue(
				"sad",
				"AM_depressive",
				doc=lambda: "Введите юзер своего канала с грустной музыкой",
			),
			loader.ConfigValue(
				"popular",
				"AM_popular",
				doc=lambda: "Введите юзер своего канала с поп музыкой",
			),
			loader.ConfigValue(
				"hyperpop",
				"hyperpopmusicx_x",
				doc=lambda: "Введите юзер своего канала с хайперпоп музыкой",
			),
			loader.ConfigValue(
				"mems",
				"AM_memss",
				doc=lambda: "Введите юзер своего канала с мемами",
			)
		)

	@loader.command()
	async def rt(self, message: Message):
		"""- сгенерировать трек.

		🫠 Категории:
		  <f> - фонки
		  <r> - ремиксы
		  <m> - мемные звуки
		  <s> - грустная музыка
		  <h> - хайперпоп музыка
		  <p> - популярная музыка
		  <n> - ностальгические треки
		  <my> - треки из вашего плейлиста

		🤫 По желанию, в конфиге, можно указать свои каналы откуда будет отбираться музыка"""

		args = utils.get_args_raw(message)                  
		afonks = self.config['fonks']           
		asad = self.config['sad']               
		ahpop = self.config['hyperpop']         
		armx = self.config['remixes']            
		apop = self.config['popular']
		amems = self.config['mems']             
		aplaylist = self.config['playlist']
		agroup = "shyshomuz"
		nstt = 'AM_NSTL'

		if not args:
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем трек...</b>")
			music = random.choice([msg async for msg in self.client.iter_messages(agroup, limit=1000, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=music)
			if message.out:
				await message.delete()

		if args == "f":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем фонк...</b>")
			fonk = random.choice([msg async for msg in self.client.iter_messages(afonks, limit=100, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=fonk)
			if message.out:
				await message.delete()

		if args == "s":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем грустный трек...</b>")
			depr = random.choice([msg async for msg in self.client.iter_messages(asad, limit=100, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=depr)
			if message.out:
				await message.delete()

		if args == "h":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем хайперпоп...</b>")
			hyper = random.choice([msg async for msg in self.client.iter_messages(ahpop, limit=100, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=hyper)
			if message.out:
				await message.delete()

		if args == "r":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем ремикс...</b>")
			remix = random.choice([msg async for msg in self.client.iter_messages(armx, limit=100, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=remix)
			if message.out:
				await message.delete()

		if args == "m":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем трек...</b>")
			mem = random.choice(await self.client.get_messages(amems, limit=100, reply_to=utils.get_topic(message)))
			await message.respond(file=mem)
			if message.out:
				await message.delete()

		if args == "p":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем трек...</b>")
			pop = random.choice([msg async for msg in self.client.iter_messages(apop, limit=100, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=pop)
			if message.out:
				await message.delete()
				
		if args == "n":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем трек...</b>")
			nst = random.choice([msg async for msg in self.client.iter_messages(nstt, limit=200, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=nst)
			if message.out:
				await message.delete()

		if args == "my":
			await utils.answer(message, "<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем трек с вашего плейлиста...</b>")
			my = random.choice([msg async for msg in self.client.iter_messages(aplaylist, limit=100, filter=InputMessagesFilterMusic, reply_to=utils.get_topic(message))])
			await message.respond(file=my)
			if message.out:
				await message.delete()
				