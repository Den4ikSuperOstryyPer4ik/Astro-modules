__version__ = (1, 4, 2)
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/RandomTrack.jpg

import random

from telethon.tl.types import InputMessagesFilterMusic, Message

from .. import loader, utils


@loader.tds
class RandomTrackMod(loader.Module):
	'''Получить рандомный трек. 
	Используйте категории чтобы сгенерировать трек на свой вкус'''

	strings = {"name": "RandomTrack"}
  
	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"playlist",
				None,
				doc=lambda: "Юзер нужного канала с музыкой",
			),
			loader.ConfigValue(
				"fonks",
				"AM_fonks",
				doc=lambda: "Юзер нужного канала с фонками",
			),
			loader.ConfigValue(
				"remixes",
				"AM_rmx",
				doc=lambda: "Юзер нужного канала с ремиксами",
			),
			loader.ConfigValue(
				"sad",
				"AM_depressive",
				doc=lambda: "Юзер нужного канала с грустной музыкой",
			),
			loader.ConfigValue(
				"popular",
				"AM_popular",
				doc=lambda: "Юзер нужного канала с поп музыкой",
			),
			loader.ConfigValue(
				"hyperpop",
				"hyperpopmusicx_x",
				doc=lambda: "Юзер нужного канала с хайперпоп музыкой",
			),
			loader.ConfigValue(
				"mems",
				"AM_memss",
				doc=lambda: "Юзер нужного канала с мемами",
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

		🤫 По желанию, в конфиге, можно указать свои каналы откуда будет отбираться музыка
		"""

		args = utils.get_args_raw(message)
	
		limit = 100
		if not args:
			search_type = "трек"
			search_channel = "shyshomuz"
			limit = 1000
		elif args == "f":
			search_type = "фонк"
			search_channel = self.config['fonks']
		if args == "s":
			search_type = "грустный трек"
			search_channel = self.config['sad']
		if args == "h":
			search_type = "хайпер-поп"
			search_channel = self.config['hyperpop']
		if args == "r":
			search_type = "ремикс"
			search_channel = self.config['remixes']
		if args == "m":
			search_type = "мем"
			search_channel = self.config['mems']
		if args == "p":
			search_type = "трек"
			search_channel = self.config['popular']
		if args == "n":
			search_type = "трек"
			search_channel = "AM_NSTL"
			limit = 200
		if args == "my":
			search_type = "трек с вашего плейлиста"
			search_channel = self.config['playlist']
		
		await utils.answer(message, f"<emoji document_id=5219806684066618617>🫠</emoji> <b>Подбираем {search_type}...</b>")

		media = random.choice([
			msg
			async for msg in self.client.iter_messages(
				search_channel,
				limit=limit,
				filter=InputMessagesFilterMusic if search_type != "мем" else None
			)
		])

		await message.respond(
			file=media,
			reply_to=utils.get_topic(message),
		)

		if message.out:
			await message.delete()
