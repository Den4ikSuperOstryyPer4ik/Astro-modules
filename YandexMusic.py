__version__ = (1, 1, 1)
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

class YaMusicMod(loader.Module):
	'''Поиск музыки через музыкального бота от Яндекса'''

	strings = {
		"name": "YandexMusic",
		"na": "😅 <b>А что искать то?</b>",
		"searching": "<b>Поиск...</b>",
	}
	
	async def ymcmd(self, message):
		"""- найти трек по названию"""
		args = utils.get_args_raw(message) 
		r = await message.get_reply_message() 
		bot = '@music_yandex_bot'
		if not args: 
			return await message.edit(self.strings("na"))  
		try: 
			await message.edit(self.strings("searching")) 
			music = await message.client.inline_query(bot, args) 
			await message.delete() 
			try:
				await message.client.send_file(message.to_id, music[1].result.document, caption="<b>🎧 Возможно, это тот трек, который вы искали</b>", reply_to=utils.get_topic(message) if r else None)  
			except:
				await message.client.send_file(message.to_id, music[3].result.document, caption="<b>🎧 Возможно, это тот трек, который вы искали</b>", reply_to=utils.get_topic(message) if r else None) 
		except: return await message.client.send_message(message.chat_id, f"<b>😔 Нам не удалось найти трек с названием <code>{args}</code><b>")
