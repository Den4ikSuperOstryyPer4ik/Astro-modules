__version__ = (1, 3, 1)
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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/TwinkManager.jpg

from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class TwinkManagerMod(loader.Module):
	'''Управление твинками через основной аккаунт.'''

	strings = {
		"name": "Twink-Manager",
		"pref1": "Префикс первого вашего твинка",
		"pref2": "Префикс второго вашего твинка (если имеется)",
		"pref3": "Префикс третьего вашего твинка (если имеется)",
		"all_t": "Выполнять действия также и с вашего основного аккаунта?"
	}

	async def client_ready(self, client, db):
		self._db = db
		self._me = await client.get_me()

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				"prefix_1",
				"!",
				doc=lambda: self.strings("pref1"),
			),
			loader.ConfigValue(
				"prefix_2",
				None,
				doc=lambda: self.strings("pref2"),
			),
			loader.ConfigValue(
				"prefix_3",
				None,
				doc=lambda: self.strings("pref3"),
			),
			loader.ConfigValue(
				'all',
				False,
				doc=lambda: self.strings("all_t"),
				validator=loader.validators.Boolean(),)
		)

	@loader.command()
	async def trestart(self, message: Message):
		"""- перезагрузить аккаунты"""

		restart = 'restart --force'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{restart}')
					await self.allmodules.commands["restart"](
						await utils.answer(m, f"{self.get_prefix()}{restart}")
					)
				else:
					m = await utils.answer(message, f'{p1}{restart}')
					n = await utils.answer(m, f'{p2}{restart}')
					await self.allmodules.commands["restart"](
						await utils.answer(n, f"{self.get_prefix()}{restart}")
					)
			else:
				m = await utils.answer(message, f'{p1}{restart}')
				n = await utils.answer(m, f'{p2}{restart}')
				o = await utils.answer(m, f'{p3}{restart}')
				await self.allmodules.commands["restart"](
					await utils.answer(o, f"{self.get_prefix()}{restart}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{restart}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{restart}')
					n = await utils.answer(m, f'{p2}{restart}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{restart}')
				n = await utils.answer(m, f'{p2}{restart}')
				o = await utils.answer(m, f'{p3}{restart}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	@loader.command()
	async def tping(self, message: Message):
		"""- проверить пинг"""

		ping = 'ping'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{ping}')
					await self.allmodules.commands["ping"](
						await utils.answer(m, f"{self.get_prefix()}{ping}")
					)
				else:
					m = await utils.answer(message, f'{p1}{ping}')
					n = await utils.answer(m, f'{p2}{ping}')
					await self.allmodules.commands["ping"](
						await utils.answer(n, f"{self.get_prefix()}{ping}")
					)
			else:
				m = await utils.answer(message, f'{p1}{ping}')
				n = await utils.answer(m, f'{p2}{ping}')
				o = await utils.answer(m, f'{p3}{ping}')
				await self.allmodules.commands["ping"](
					await utils.answer(o, f"{self.get_prefix()}{ping}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{ping}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{ping}')
					n = await utils.answer(m, f'{p2}{ping}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{ping}')
				n = await utils.answer(m, f'{p2}{ping}')
				o = await utils.answer(m, f'{p3}{ping}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	@loader.command()
	async def tdlmod(self, message: Message):
		""" <name/link> - загрузить модули на аккаунты"""

		args = utils.get_args_raw(message)
		dlmod = 'dlmod'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{dlmod} {args}')
					await self.allmodules.commands["dlmod"](
						await utils.answer(m, f"{self.get_prefix()}{dlmod} {args}")
					)
				else:
					m = await utils.answer(message, f'{p1}{dlmod} {args}')
					n = await utils.answer(m, f'{p2}{dlmod} {args}')
					await self.allmodules.commands["dlmod"](
						await utils.answer(n, f"{self.get_prefix()}{dlmod} {args}")
					)
			else:
				m = await utils.answer(message, f'{p1}{dlmod} {args}')
				n = await utils.answer(m, f'{p2}{dlmod} {args}')
				o = await utils.answer(m, f'{p3}{dlmod} {args}')
				await self.allmodules.commands["dlmod"](
					await utils.answer(o, f"{self.get_prefix()}{dlmod} {args}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{dlmod} {args}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{dlmod} {args}')
					n = await utils.answer(m, f'{p2}{dlmod} {args}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{dlmod} {args}')
				n = await utils.answer(m, f'{p2}{dlmod} {args}')
				o = await utils.answer(m, f'{p3}{dlmod} {args}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	@loader.command()
	async def tterminal(self, message: Message):
		""" <command> - выполнить действие в терминале"""

		args = utils.get_args_raw(message)
		terminal = 'terminal'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{terminal} {args}')
					await self.allmodules.commands["terminal"](
						await utils.answer(m, f"{self.get_prefix()}{terminal} {args}")
					)
				else:
					m = await utils.answer(message, f'{p1}{terminal} {args}')
					n = await utils.answer(m, f'{p2}{terminal} {args}')
					await self.allmodules.commands["terminal"](
						await utils.answer(n, f"{self.get_prefix()}{terminal} {args}")
					)
			else:
				m = await utils.answer(message, f'{p1}{terminal} {args}')
				n = await utils.answer(m, f'{p2}{terminal} {args}')
				o = await utils.answer(m, f'{p3}{terminal} {args}')
				await self.allmodules.commands["terminal"](
					await utils.answer(o, f"{self.get_prefix()}{terminal} {args}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{terminal} {args}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{terminal} {args}')
					n = await utils.answer(m, f'{p2}{terminal} {args}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{terminal} {args}')
				n = await utils.answer(m, f'{p2}{terminal} {args}')
				o = await utils.answer(m, f'{p3}{terminal} {args}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	@loader.command()
	async def tupdate(self, message: Message):
		"""- обновить хикку на аккаунтах"""

		update = 'update --force'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{update}')
					await self.allmodules.commands["update"](
						await utils.answer(m, f"{self.get_prefix()}{update}")
					)
				else:
					m = await utils.answer(message, f'{p1}{update}')
					n = await utils.answer(m, f'{p2}{update}')
					await self.allmodules.commands["update"](
						await utils.answer(n, f"{self.get_prefix()}{update}")
					)
			else:
				m = await utils.answer(message, f'{p1}{update}')
				n = await utils.answer(m, f'{p2}{update}')
				o = await utils.answer(m, f'{p3}{update}')
				await self.allmodules.commands["update"](
					await utils.answer(o, f"{self.get_prefix()}{update}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{update}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{update}')
					n = await utils.answer(m, f'{p2}{update}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{update}')
				n = await utils.answer(m, f'{p2}{update}')
				o = await utils.answer(m, f'{p3}{update}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	@loader.command()
	async def thelp(self, message: Message):
		""" <name/-f>- список модулей либо информация о модуле"""

		args = utils.get_args_raw(message)
		helpp = 'help'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{helpp} {args}')
					await self.allmodules.commands["helpp"](
						await utils.answer(m, f"{self.get_prefix()}{helpp} {args}")
					)
				else:
					m = await utils.answer(message, f'{p1}{helpp} {args}')
					n = await utils.answer(m, f'{p2}{helpp} {args}')
					await self.allmodules.commands["helpp"](
						await utils.answer(n, f"{self.get_prefix()}{helpp} {args}")
					)
			else:
				m = await utils.answer(message, f'{p1}{helpp} {args}')
				n = await utils.answer(m, f'{p2}{helpp} {args}')
				o = await utils.answer(m, f'{p3}{helpp} {args}')
				await self.allmodules.commands["helpp"](
					await utils.answer(o, f"{self.get_prefix()}{helpp} {args}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{helpp} {args}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{helpp} {args}')
					n = await utils.answer(m, f'{p2}{helpp} {args}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{helpp} {args}')
				n = await utils.answer(m, f'{p2}{helpp} {args}')
				o = await utils.answer(m, f'{p3}{helpp} {args}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	@loader.command()
	async def tloadmod(self, message: Message):
		""" <reply> - загрузить файл модуля на аккаунты"""

		ld = 'loadmod'
		p1 = self.config['prefix_1']
		p2 = self.config['prefix_2']
		p3 = self.config['prefix_3']
		full = self.db.get(__name__, "allAcc")

		if full:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")

			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{ld}')
					await self.allmodules.commands["loadmod"](
						await utils.answer(m, f"{self.get_prefix()}{ld}")
					)
				else:
					m = await utils.answer(message, f'{p1}{ld}')
					n = await utils.answer(m, f'{p2}{ld}')
					await self.allmodules.commands["loadmod"](
						await utils.answer(n, f"{self.get_prefix()}{ld}")
					)
			else:
				m = await utils.answer(message, f'{p1}{ld}')
				n = await utils.answer(m, f'{p2}{ld}')
				o = await utils.answer(m, f'{p3}{ld}')
				await self.allmodules.commands["loadmod"](
					await utils.answer(o, f"{self.get_prefix()}{ld}")
				)
		else:
			tp2 = self.db.get(__name__, "prefixN2")
			tp3 = self.db.get(__name__, "prefixN3")
			if not tp3:
				if not tp2:
					m = await utils.answer(message, f'{p1}{ld}')
					await utils.answer(m, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
				else:
					m = await utils.answer(message, f'{p1}{ld}')
					n = await utils.answer(m, f'{p2}{ld}')
					await utils.answer(n, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')
			else:
				m = await utils.answer(message, f'{p1}{ld}')
				n = await utils.answer(m, f'{p2}{ld}')
				o = await utils.answer(m, f'{p3}{ld}')
				await utils.answer(o, '<emoji document_id=5213442551851262055>✔️</emoji> <b>Готово</b>')

	
	@loader.watcher()
	async def watcher(self, message: Message):
		if not self.config['prefix_2']:
			self.db.set(__name__, "prefixN2", False)
		else:
			self.db.set(__name__, "prefixN2", True)

		if not self.config['prefix_3']:
			self.db.set(__name__, "prefixN3", False)
		else:
			self.db.set(__name__, "prefixN3", True)

		if self.config['all']:
			self.db.set(__name__, 'allAcc', True)
		else:
			self.db.set(__name__, 'allAcc', False)
		