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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/BrawlStats.jpg
# requires: brawlstats

import brawlstats as bs
import requests

from .. import loader, utils


@loader.tds
class BrawlStatsInfo(loader.Module):
	'''Brawl Stars Players/Clubs information :)'''
	
	strings = {
		"name": "BrawlStatsInfo"
	}
	
	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"bs_api_token",
				None,
				doc="Сохраните здесь свой API-Токен BrawlStarsAPI",
				validator=loader.validators.Hidden()
			)
		)
	
	def getip(self):
		ip = requests.get('https://api.myip.com/').json()["ip"]
		return ip
	
	async def client_ready(self, client, db):
		await client.send_message("me", "<b>Модуль был инициализирован.\nВаш IP-Адрес для получения API-Токена BrawlStars: <code>{}</code></b>".format(self.getip()))
		
		try:
			self.bsc = bs.Client(self.config["bs_api_token"]) if self.config["bs_api_token"] else None
		except Exception:
			self.bsc = None
	
	def get_bs_client(self):
		if self.bsc is None:
			self.bsc = bs.Client(self.config["bs_api_token"]) if self.config["bs_api_token"] else None
		return None
	
	@loader.command()
	async def get_my_ip(self, message):
		"""Получить свой IP-Адрес для получения API-Токен BrawlStarsAPI"""
		await utils.answer(message, "<b>Ваш IP-Адрес для получения API-Токена BrawlStars: <code>{}</code></b>".format(self.getip()))
	
	@loader.command()
	async def set_bs_api_token(self, message):
		"""<api_token> - сохранить свой API-Токен в конфиге модуля."""
		await self.allmodules.commands['fconfig'](
			await utils.answer(message, '{}fconfig BrawlStatsInfo bs_api_token {}'.format(self.get_prefix(), utils.get_args_raw(message)))
		)
		self.get_bs_client()
	
	def get_brawlers_names(self, text: str):
		names = {
			'SHELLY': "ШЕЛЛИ",
			'COLT': "КОЛЬТ",
			'BULL': "БУЛЛ",
			'BROCK': 'БРОК',
			'RICO': 'РИКО',
			'SPIKE': 'СПАЙК',
			'BARLEY': 'БАРЛИ', 
			'JESSIE': 'ДЖЕССИ',
			'NITA': "НИТА",
			'DYNAMIKE': 'ДИНАМАЙК', 
			'EL PRIMO': 'ЭЛЬ ПРИМО',
			'MORTIS': 'МОРТИС',
			'CROW': 'ВОРОН',
			'POCO': 'ПОКО',
			'BO': 'БО',
			'PIPER': 'ПАЙПЕР',
			'PAM': 'ПЭМ',
			'TARA': 'ТАРА',
			'DARRYL': 'ДЭРРИЛ',
			'PENNY': 'ПЕННИ',
			'FRANK': 'ФРЭНК',
			'GENE': 'ДЖИН',
			'TICK': 'ТИК',
			'LEON': 'ЛЕОН',
			'ROSA': 'РОЗА', 
			'CARL': 'КАРЛ', 
			'BIBI': 'БИБИ', 
			'8-BIT': '8-БИТ',
			'SANDY': 'СЭНДИ', 
			'BEA': 'БЕА',
			'EMZ': 'ЭМЗ',
			'MR. P': 'МИСТЕР П.', 
			'MAX': 'МАКС',
			'JACKY': 'ДЖЕКИ',
			'GALE': 'ГЭЙЛ',
			'NANI': 'НАНИ',
			'SPROUT': 'СПРАУТ',
			'SURGE': 'ВОЛЬТ',
			'COLETTE': 'КОЛЕТТ',
			'AMBER': 'АМБЕР',
			'LOU': 'ЛУ',
			'BYRON': 'БАЙРОН',
			'EDGAR': 'ЭДГАР',
			'RUFFS': 'ГАВС',
			'STU': 'СТУ',
			'BELLE': 'БЕЛЛЬ',
			'SQUEAK': 'СКУИК',
			'GROM': 'ГРОМ',
			'BUZZ': 'БАЗЗ',
			'GRIFF': 'ГРИФФ',
			'ASH': 'ЭШ',
			'MEG': 'МЭГ',
			'LOLA': 'ЛОЛА',
			'FANG': 'ФЭНГ',
			'EVE': 'ЕВА',
			'JANET': 'ДЖАНЕТ',
			'BONNIE': 'БОННИ',
			'OTIS': 'ОТИС',
			'SAM': 'СЭМ',
			'GUS': 'ГАС',
			'BUSTER': 'БАСТЕР',
			'CHESTER': 'ЧЕСТЕР',
			'GRAY': 'ГРЕЙ',
			'MANDY': 'МЭНДИ',
		}
		text_replaced = text
		for i, o in names.items():
			text_replaced = text_replaced.replace(i, o)
		
		return text_replaced
	
	def get_player_info(self, tag: str, raw: bool = False):
		self.get_bs_client()
		player = self.bsc.get_player(
			tag if not tag.startswith("#") else tag.replace("#", "").replace(" ", "")
		)
		return player if raw else f"<b>Информация об игроке:\nНикнейм: {player.name}\nТег: <code>{player.tag}</code>\nКол-во кубков всего: {player.trophies}\nМакс. кол-во кубков: {player.highest_trophies}\nУровень опыта: {player.exp_level}\nПобед 3x3: {player.x3vs3_victories}\nОдиночных побед: {player.solo_victories}\nПарных побед: {player.duo_victories}\nБравлеров(Бойцов): {len(player.brawlers)}\nТег клуба: <code>{player.club.tag if player.club.tag else 'Отсутствует клуб.'}</code>\nИмя Клуба: {player.club.name if player.club.name else 'Отсутствует клуб.'}</b>"
	
	def get_club_info(self, tag: str, raw: bool = False):
		self.get_bs_client()
		club = self.bsc.get_club(
			tag if not tag.startswith("#") else tag.replace("#", "").replace(" ", "")
		)
		return club if raw else f"<b>Информация о клубе:\nИмя клуба: {club.name}\nТег: <code>{club.tag}</code>\nКол-во кубков всего: {club.trophies}\nМин. необходимое кол-во кубков для входа: {club.required_trophies}\nОписание: {self.get_club_description(club.description)}\nТип клуба: {club.type}\nУчастники:\n{self.get_club_members_info(club)}</b>"
	
	def get_club_members_info(self, club, full: bool = False):
		self.get_bs_client()
		def get_member_role(role: str):
			for i, o in {"vicePresident": "Вице-президент", "president": "Президент", "member": "Участник"}.items():
				role = role.replace(i, o)
			return role
				
		
		return "\n————\n".join(
			[
				f"{i.name}—{get_member_role(i.role)} (<code>{i.tag}</code> | {i.trophies}) " for i in club.get_members()
			] if full else [
				f"{i.name}—{get_member_role(i.role)} (<code>{i.tag}</code>)" for i in club.get_members()
			]
		)
	
	def get_club_description(self, text: str):
		text_replaced = text
		for i in range(15):
			text_replaced = text_replaced.replace(f"c{i}", "code")
		
		return text_replaced
	
	@loader.command()
	async def bs_get_player(self, message):
		"""<#player_tag> <#player_tag2> -> получить информацию об игроке/игроках(теги можно через пробел указывать)"""
		msg = await utils.answer(message, "Собираю информацию, пожалуйста подождите...")
		
		args = utils.get_args_raw(message)
		info = []
		
		self.get_bs_client()
		
		if len(args.split(" ")) != 1:
			for player_tag in args.split(" "):
				info.append(self.get_player_info(player_tag))
			info = "\n———————————\n".join(info)
		else:
			info = self.get_player_info(args)
			
		return await utils.answer(msg, info)
	
	@loader.command()
	async def bs_get_club(self, message):
		"""<#CLUB_TAG> -> получить информацию о клубе по его #ТЕГУ"""
		msg = await utils.answer(message, "Собираю информацию, пожалуйста подождите...")
		
		args = utils.get_args_raw(message)
		info = []
		info = self.get_club_info(args)
			
		return await utils.answer(msg, info)
	
	@loader.command()
	async def bs_get_club_members(self, message):
		"""<#CLUB_TAG> -> получить информацию об участниках клуба по его #ТЕГУ"""
		msg = await utils.answer(message, "Собираю информацию, пожалуйста подождите...")
		
		args = utils.get_args_raw(message)
		info = f"Участники:\n{self.get_club_members_info(self.get_club_info(args, True), True)}"
		
		return await utils.answer(msg, info)
	
	@loader.command()
	async def bs_get_player_brawlers(self, message):
		"""<#player_tag> -> получить информацию о Бравлерах(Бойцах) игрока по его #ТЕГУ"""
		msg = await utils.answer(message, "Собираю информацию, пожалуйста подождите...")
		
		args = utils.get_args_raw(message)
		
		player = self.get_player_info(args, True)
		
		brawlers = []
		for brawler in player.brawlers:
			brawlers.append(f"<b>Имя: {brawler.name}\nКубков на бойце: {brawler.trophies}\nМакс. кол-во кубков на бойце: {brawler.highest_trophies}\nРанг: {brawler.rank}\nСила: {brawler.power}")
		
		info = "\n————————\n".join(brawlers)
		info = self.get_brawlers_names(info)
		
		return await utils.answer(msg, info)
