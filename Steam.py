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
#                                         https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta banner: 
# meta developer: @AstroModules
# required: steampy
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/AstroSteamNow.png
# Part of the module taken from WakaTime by @hikariatama: 38, 158, 208, 324 lines

import time
import logging
import datetime 
import requests
import asyncio

from steampy.client import SteamClient
from .. import loader, utils
from ..inline.types import InlineCall
from telethon.errors.rpcerrorlist import MessageNotModifiedError

logger = logging.getLogger(__name__)

@loader.tds
class Steam(loader.Module):
    '''Get now played game'''

    strings = {
        'name': 'SteamNow',

        '_api_key': "Enter your SteamAPI Key. You can get it by following this tutorial:\n\nhttps://t.me/help_code/20", # Tutorial link
        '_account_id': "Enter your Steam Account ID. More details in the tutorial: \n\nhttps://t.me/help_code/21", # Tutorial link

        'no_api_key_or_id': (
            '<b>❌ You did not specify your API_KEY or ACCOUNT_ID in the config.</b>\n'
            '<b>🚨 Correct this for further module operation</b>'
        ),

        'noGame': "<b>❌ The game is not running or you do not have access</b>",

        'steamNow': (
            '💻 <b>At the moment you are playing:</b>\n\n'
            '🎮 <b>Title:</b> <code>{}</code>\n'
            '🆔 <b>Game ID: {}</b>'
        ),
        'lite_gameInfo': (
            '🎮 <b>Game information:</b>\n\n'
            '<b>Title: </b>{}\n'
            '<b>Price: {}</b>\n'
            '<b>Description:</b>\n- <i>{}</i>'
        ),
        'steamMe': (
            '<b>🎮 Your account:</b>\n\n'
            '<b>Name: </b><i>{}</i> (<i>{}</i>)\n'
            '<b>Online: </b><code>{}</code>\n'
            '<b>Created: </b><code>{}</code>\n'
            '<b>Recent games:</b>\n<i>   • {}</i>'
        ),
        'gameNotFound': '<b>🆔 There is no game with such an identifier, try again</b>',

        "state": "🙂 <b>Steam widgets: {}</b>\n{}",
        "error": "<b>Steam error</b>\n\n{}",
        "tutorial": (
            "ℹ️ <b>To enable the widget, send this text to any chat:"
            " </b><code>{STEAMNOW}</code>"
        ),
        "configuring": "🙂 <b>Steam widget will be ready soon...</b>",
    }


    strings_ru = {

        '_api_key': "Введите ваш SteamAPI Key. Получить его можно по туториалу:\n\n", # Линк на тутор
        '_account_id': "Введите ваш Steam Account ID. Подробнее в туториале: \n\n", # Линк на тутор

        'no_api_key_or_id': (
            '<b>❌ Вы не указали ваш API_KEY или ACCOUNT_ID в конфиге.</b>\n'
            '<b>🚨 Исправьте это для дальнейшей работы модуля</b>'
        ),

        'noGame': "<b>❌ Игра не запущена, или у вас нет доступа</b>",

        'steamNow': (
            '💻 <b>В данный момент вы играете:</b>\n\n'
            '🎮 <b>Название:</b> <code>{}</code>\n'
            '🆔 <b>ID Игры: {}</b>'
        ),
        'lite_gameInfo': (
            '🎮 <b>Информация об игре:</b>\n\n'
            '<b>Название: </b>{}\n'
            '<b>Цена: {}</b>\n'
            '<b>Описание:</b>\n- <i>{}</i>'
        ),
        'steamMe': (
            '<b>🎮 Ваш аккаунт:</b>\n\n'
            '<b>Имя: </b><i>{}</i> (<i>{}</i>)\n'
            '<b>В сети: </b><code>{}</code>\n'
            '<b>Создан: </b><code>{}</code>\n'
            '<b>Последние игры:</b>\n<i>   • {}</i>'
        ),
        'gameNotFound': '<b>🆔 Игры с таким идентификатором нет, попробуйте снова</b>',

        "state": "🙂 <b>Steam виджеты: {}</b>\n{}",
        "error": "<b>Steam error</b>\n\n{}",
        "tutorial": (
            "ℹ️ <b>Для включения виджета отправьте данный текст в любой чат:"
            " </b><code>{STEAMNOW}</code>"
        ),
        "configuring": "🙂 <b>Steam виджет скоро будет готов...</b>",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                'API_KEY', 
                None, 
                doc=lambda: self.strings('_api_key'),
                validator=loader.validators.Hidden(),
            ),
            loader.ConfigValue(
                'ACCOUNT_ID', 
                None, 
                doc=lambda: self.strings('_account_id')
            ),
            loader.ConfigValue(
                "update_interval",
                300,
                lambda: "Messages update interval. Not recommended < 300 seconds",
                validator=loader.validators.Integer(minimum=60),
            ),
        )

    async def client_ready(self, client, db):
        self.db.set(
            "Steam", 
            "widgets", 
            list(map(tuple, self.db.get("Steam","widgets", [])))
        )

        self._task = asyncio.ensure_future(self._parse())


    async def steam_requests(self, request, gameId: bool = None):
        '''Function for requests to SteamAPI'''

        api_key = self.config['API_KEY']
        account_id = self.config['ACCOUNT_ID']

        steam_client = SteamClient(api_key)

        if request == 'SteamNow':
            if not api_key or not account_id:
                return('TokenError', None)

            data = {'key': api_key, 'steamids': account_id}

            response = steam_client.api_call('GET', 'ISteamUser', 'GetPlayerSummaries', 'v2', data).json()['response']   

            try:
                gameId = response['players'][0]['gameid']
                gameName = response['players'][0]['gameextrainfo']

                text = self.strings('steamNow').format(gameName, gameId)

            except:
                text, gameId = self.strings('noGame'), None

            return text, gameId #, photo

        elif request == 'profileInfo':
            if not api_key or not account_id:
                return('TokenError', None, None, None, None, None)

            url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}'
            url2 = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={}&steamid={}&format=json'
            response = requests.get(url.format(self.config['API_KEY'], self.config['ACCOUNT_ID'])).json()['response']['players'][0]

            recentGameInfo = requests.get(url2.format(self.config['API_KEY'], self.config['ACCOUNT_ID'])).json()['response']['games']
            games = []
            for game in recentGameInfo:
                games.append(f'{game["name"]}: {game["playtime_2weeks"]}м. ({game["playtime_forever"]}м.)')

            recentGames = '\n   • '.join(games)
            return(
                response['avatarfull'], # Profile photo
                response['personaname'], # Name: 'ˢˡ ToxUniҨue,
                response['realname'], # Realname: Tox.
                datetime.datetime.fromtimestamp(response['lastlogoff']).isoformat().replace('T', ' '), # Последний раз в сети
                datetime.datetime.fromtimestamp(response['timecreated']).isoformat().replace('T', ' '), # Дата создания аккаунта
                recentGames
            )

        elif request == 'GameInfo':
            if not api_key or not account_id:
                return('TokenError', None)

            url = f"http://store.steampowered.com/api/appdetails?appids={gameId}"
            response = requests.get(url)
            data = response.json()
            game_data = data[str(gameId)]['data']
            capsule_image = game_data.get('header_image', None)
            name = game_data.get('name', None)
            short_description = game_data.get('short_description', None)
            price_overview = game_data.get('price_overview', None)
            
            if price_overview:
                initial_formatted_price = price_overview.get('initial_formatted', None)
                final_formatted_price = price_overview.get('final_formatted', None)
            else:
                initial_formatted_price = None
                final_formatted_price = None
            
            final_price = f'{initial_formatted_price}' if initial_formatted_price == final_formatted_price else f'{final_formatted_price} (<u>{initial_formatted_price}</u>)' 

            text = self.strings('lite_gameInfo').format(name, final_price, short_description)
            return capsule_image, text


    async def game_info_i(
        self, 
        call: InlineCall, 
        gameId: int, 
        message
    ):
        _, text = await self.steam_requests('GameInfo', gameId)

        if _ == 'TokenError':
            return await call.edit(text=self.strings('no_api_key_or_id'))

        await call.edit(text=text)
  

    async def _parse(self, do_not_loop: bool = False):
        while True:
            if self.config["API_KEY"] == None or self.db.get("Steam", "state") == False:
                await asyncio.sleep(5)
                continue

            for widget in self.db.get("Steam", "widgets", []):
                now, _ = await self.steam_requests('SteamNow')

                if now == 'TokenError':
                    await self._client.edit_message(*widget[:2], self.strings('no_api_key_or_id'))

                elif now == self.strings('noGame'):
                    self.db.set('steam', 'inGame', None)
                    await self._client.edit_message(*widget[:2], self.strings('noGame'))

                

                else:
                    in_game_time = self.db.get('steam', 'inGame')
                    if in_game_time is None:
                        self.db.set('steam', 'inGame', time.time())
                        game_time_minutes = 0
                    else:
                        game_time = time.time() - in_game_time
                        game_time_minutes = round(game_time / 60)

                    try:
                        await self._client.edit_message(*widget[:2], now + f'\n\n<b>🕓 В игре: {game_time_minutes} минут.</b>')
                    except:
                        return


            await asyncio.sleep(int(self.config["update_interval"]))

    @loader.command(
        ru_doc=' - получить, во что я сейчас играю'
    )
    async def steamnow(self, message):
        """- get what I'm playing at"""

        text, gameid = await self.steam_requests('SteamNow')

        if text == self.strings('noGame'):
            return await utils.answer(message, text)

        elif text == 'TokenError':
            return await utils.answer(message, self.strings('no_api_key_or_id'))

        capsule_image, _ = await self.steam_requests('GameInfo', gameid)

        await self.inline.form(
            message=message,
            photo=capsule_image,
            text=text,
            reply_markup=[
                {
                    'text': 'Информация об игре',
                    'callback': self.game_info_i,
                    'args': (gameid, message,),
                }
            ]
        )

    @loader.command(
        ru_doc='- открыть аккаунт Steam'
    )
    async def sme(self, message):
        '''- my steam account'''

        photo, fullName, name, date1, date2, games = await self.steam_requests('profileInfo')

        if photo == 'TokenError':
            await utils.answer(message, self.strings('no_api_key_or_id'))

        await utils.answer_file(
            message,
            photo,
            caption=self.strings('steamMe').format(
                fullName, name, date1, date2, games
            )
        )
    
    @loader.command(
        ru_doc='<id> - получить инфо об игре'
    )
    async def game(self, message):
        '''<id> - get game info'''

        args = utils.get_args_raw(message)

        try:
            capsule_image, text = await self.steam_requests('GameInfo', args)

            if capsule_image == 'TokenError':
                await utils.answer(message, self.strings('no_api_key_or_id'))


            await utils.answer_file(message, capsule_image, text)
        except:
            await utils.answer(message, self.strings('gameNotFound'))

    @loader.command(
        ru_doc='- вкл/выкл виджеты SteamNow'
    )
    async def steamtoggle(self, message):
        """ - toggle widgets updates"""

        state = self.db.get('Steam', 'state')
        state = True if state == False else False
        self.db.set('Steam', 'state', state)

        await utils.answer(
            message,
            self.strings("state").format(
                "on" if state else "off", self.strings("tutorial") if state else ""
            ),
        )

    @loader.watcher()
    async def watcher(self, message):
        if (
            self.db.get('Steam', 'state')
            and (await self.client.get_messages(self.db.get('Steam', 'widgets')[0][0], ids=self.db.get('Steam', 'widgets')[0][1])).message == '❌ Вы не во что не играете'
        ):
            now, _ = await self.steam_requests('SteamNow')

            if now == self.strings('noGame') or now == 'TokenError':
                return

            await self._parse(do_not_loop=True)

        try:
            if "{STEAMNOW}" not in getattr(message, "text", "") or not message.out:
                return

            chat_id = utils.get_chat_id(message)
            message_id = message.id

            self.db.set(
                "Steam",
                "widgets",
                self.db.get('steam', "widgets", []) + [(chat_id, message_id, message.text)],
            )

            await utils.answer(message, self.strings("configuring"))
            await self._parse(do_not_loop=True)
        except Exception as e:
            logger.exception("Can't send widget")
            await utils.answer(message, self.strings("error").format(e))
