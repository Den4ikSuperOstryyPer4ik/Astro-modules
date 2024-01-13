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
# meta banner: https://raw.githubusercontent.com/Den4ikSuperOstryyPer4ik/Astro-modules/main/Banners/MindTalk.jpg

import requests

from .. import loader, utils


class MindTalkMod(loader.Module):
	'''Your little psychologist Based on MindTalk by Hikamoru'''

	strings = {
		'name': 'MindTalk',
		'args_error': '<emoji document_id=5273793379300289907>❗️</emoji> <b>Missing or invalid arguments!</b>',
		'successful_login': '<emoji document_id=5206607081334906820>✔️</emoji> <b>Login completed successfully. Token saved in config</b>',
		'not_token': '<emoji document_id=5210952531676504517>❌</emoji>  <b>Missing access token. Please login using the <code>{}login</code> command</b>',
		'wait': '<emoji document_id=5310192647313301616>☕️</emoji> <b>Waiting answer from a psychologist...</b>',
		'login_error': (
			'<emoji document_id=5210952531676504517>❌</emoji> '
			'<b>Login failed. You may have entered the wrong password or you are not registered. '
			'Try again, or go through the authorization again using <a href="https://t.me/hikpsybot?start=register">this link.</a></b>'
		),
		'answer': (
			'<emoji document_id=5818995853544656277>👩‍💻</emoji> '
			'<b>Your question:</b> {}\n\n'
			'<emoji document_id=5431602426354344379>👩‍⚕️</emoji> '
			'<b>Answer from psychologist:</b> {}'
		),
		'history_cleared': '<emoji document_id=5818967120213445821>🛡</emoji> <b>Your history has been successfully cleared</b>'
	}

	def __init__(self):
		self.config = loader.ModuleConfig(
			loader.ConfigValue(
				'token',
				None,
				lambda: 'Your access token. Displayed automatically!',
				validator=loader.validators.Hidden()
			)
		)
		self.url = 'https://ps.hikamoru.uz'

	async def get_token(self, login, password):
		params = {
			'username': login,
			'password': password
		}
		if (
			await utils.run_sync(
				requests.post,
				self.url + '/api/authenticate',
				params=params
			)
		).json()['result']:
			token = (
				await utils.run_sync(
					requests.post,
					self.url + '/api/createUserToken',
					params=params
				)
			).json()['result']
			self.config['token'] = token
			return True
		else:
			return False

	@loader.command()
	async def login(self, message):
		'''<login> <password> - log in and save token'''

		args = utils.get_args_raw(message)
		if not args or not args.split()[1]:
			return await utils.answer(message, self.strings('args_error'))

		login, password = args.split()
		gen = await self.get_token(login, password)

		return await utils.answer(
			message,
			self.strings(
				'login_error'
				if not gen
				else 'successful_login'
			)
		)

	@loader.command()
	async def ask(self, message):
		'''<message> - ask a psychologist a question'''

		args = utils.get_args_raw(message)
		if not args:
			return await utils.answer(message, self.strings('args_error'))

		if not self.config['token']:
			return await utils.answer(
				message,
				self.strings('not_token').format(self.get_prefix())
			)

		params = {
			'userMessage': args,
			'TOKEN': self.config['token']
		}
		msg = await utils.answer(message, self.strings('wait'))
		response = (requests.post(self.url + '/api/chat', params=params)).json()
		text = response['result']

		await utils.answer(msg, self.strings('answer').format(args, text))

	@loader.command()
	async def mtclear(self, message):
		'''- clear MindTalk history'''

		if not self.config['token']:
			return await utils.answer(
				message,
				self.strings('not_token').format(self.get_prefix())
			)

		params = {'TOKEN': self.config['token']}
		await utils.run_sync(
			requests.post,
			self.url + '/api/clear_chat_history',
			params=params
		)
		
		await utils.answer(message, self.strings('history_cleared'))
