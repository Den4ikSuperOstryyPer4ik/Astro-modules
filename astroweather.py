__version__ = (1, 0, 6)
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/AstroWeather.jpg

import contextlib
import random

import requests

from .. import loader, utils


class AstroWeatherMod(loader.Module):
	"""Модуль для получения информации о погоде в Вашем городе, в красивом формате"""

	strings = {
		"name": "AstroWeather",
		"error": "<emoji document_id=5447644880824181073>⚠️</emoji> <b>Ошибка</b>",
		"api_error": (
			"<emoji document_id=5240241223632954241>🚫</emoji> <b>Вы не указали API ключ</b>!\n"
			"<emoji document_id=5210956306952758910>👀</emoji> <code>Пожалуйста, укажите его в конфиге ниже</code>"
		),
		"search": "{} <b>Поиск информации о погоде в городе</b> <code>{}</code>.."
	}

	async def text(self, temperature: int, veter: int, sky, hum, city, moji):
		"""Generate text"""

		sky = {
			"Clear": "Чистое",
			"Mist": "Туман",
			"Clouds": "Облачно", 
			"Rain": "Дождь", 
			"Snow": "Снег"
		}[sky]
		
		t_emoji = (
			"<emoji document_id=5204204137327111088>🔥</emoji>"
			if temperature > 0
			else "<emoji document_id=5267186302259835638>❄️</emoji>"
		)
		
		v_emoji = (
			"<emoji document_id=5447183459602669338>📉</emoji>"
			if veter >= 15
			else "<emoji document_id=5449683594425410231>🔼</emoji>"
		)


		r_emoji = random.choice([
			"<emoji document_id=5208554136039073738>🌙</emoji>",
			"<emoji document_id=5444932797955317203>🐾</emoji>",
			"<emoji document_id=5458585073060160944>🍀</emoji>",
			"<emoji document_id=5206587423269593472>🌈</emoji>",
			"<emoji document_id=5413390588198265552>💤</emoji>",
			"<emoji document_id=5435981940081566607>🌺</emoji>"
		])
		sity_emoji = random.choice([
			"<emoji document_id=5416117059207572332>⏩</emoji>", 
			"<emoji document_id=5447410659077661506>🌐</emoji>"
		])

		weather = (
			f"{r_emoji} <b>Погода в {city.title()}:</b>\n\n"
			f"{sity_emoji} <b>Город:</b> <code>{city.title()}</code>\n"
			f"{t_emoji} <b>Температура:</b> <code>{temperature}°C</code>\n"
			f"<emoji document_id=5192891734635322759>💦</emoji> <b>Влажность:</b> <code>{hum}%</code>\n"
			f"{v_emoji} <b>Скорость ветра:</b> <code>{veter}м/с</code>\n"
			f"{moji} <b>Небо:</b> <code>{sky}</code>"
		)
		return weather


	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"api_key",
				None,
				lambda: "Api key. Получить можно по туториалу https://t.me/help_code/12",
				validator=loader.validators.Hidden()
			)
		)

	async def get_weather(self, city_id):
		with contextlib.suppress(Exception):
			api_key = self.config["api_key"]
			result = requests.get("http://api.openweathermap.org/data/2.5/weather", params={"q": city_id, "units": "metric", "APPID": api_key})
			result_json = result.json()
			if result_json["cod"] != 200:
				return

			weather = {}
			weather["temp"] = round(result_json["main"]["temp"])
			weather["hum"] = result_json["main"]["humidity"]
			weather["wind_speed"] = result_json["wind"]["speed"]
			weather["sky"] = result_json["weather"][0]["main"]
			if weather["sky"] == "Clouds":
				weather["sky_emoji"] = "<emoji document_id=5391322797123314747>☁️</emoji>"
			if weather["sky"] == "Rain":
				weather["sky_emoji"] = "<emoji document_id=5224681716760715555>🌧️</emoji>"
			if weather["sky"] == "Clear":
				weather["sky_emoji"] = "<emoji document_id=5262761021361104549>☀️</emoji>"
			if weather["sky"] == "Mist":
				weather["sky_emoji"] = "<emoji document_id=5453984836668627018>🌫️</emoji>"
			if weather["sky"] == "Snow":
				weather["sky_emoji"] = "<emoji document_id=5282833267551117457>🌨️</emoji>"

			return weather

	@loader.command()
	async def aw(self, message):
		"""<город> - узнать погоду в указанном городе"""

		search_moji = random.choice([
			"<emoji document_id=5443038326535759644>💬</emoji>",
			"<emoji document_id=5452069934089641166>🔎</emoji>"
		])
		city = utils.get_args_raw(message)
		city = city.title()
		
		getting = await utils.answer(message, self.strings("search").format(search_moji, city))
		
		if self.config["api_key"] is None:
			await utils.answer(getting, self.strings("api_error"))
			msg = await self.client.send_message(message.chat.id, "<b>Открываю конфиг...</b>")
			await self.allmodules.commands["config"](
				await utils.answer(msg, f"{self.get_prefix()}config AstroWeather")
			)
			return
		
		try:
			dict_wea = await self.get_weather(city)
			temp = dict_wea["temp"]
			hum = dict_wea["hum"]
			speed = dict_wea["wind_speed"]
			sky = dict_wea["sky"]
			moji = dict_wea["sky_emoji"]
			text = await self.text(temp, speed, sky, hum, city, moji)
			await utils.answer(getting, text)
		except Exception:
			await utils.answer(getting, self.strings("error"))
