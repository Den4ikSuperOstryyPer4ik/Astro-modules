#     ___  ___  ___  ___                    
#    |   \/ __|/ _ \| _ \                   
#    | |) \__ \ (_) |  _/                   
#    |___/|___/\___/|_|   
#                  _    
#     __ _ _ _  __| |                       
#    / _` | ' \/ _` |                       
#    \__,_|_||_\__,_|                       
#     _____                      _ _  _ _   
#    |_   _|____ ___  _ __ _ _ _| | |(_) |__
#      | |/ _ \ \ / || / _` | '_|_  _| | / /
#      |_|\___/_\_\\_, \__,_|_|   |_||_|_\_\
#                  |__/                     
#
#                 © Copyright 2022
#
#      https://t.me/Den4ikSuperOstryyPer4ik
#                      and
#             https://t.me/ToXicUse
#
#       🔒 Licensed under the GNU AGPLv3
#    https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
# meta pic: https://0x0.st/o18O.jpg
# meta banner: https://0x0.st/o1AM.jpg 
# scope: hikka_only

from .. import loader, utils
from telethon.tl.types import Message
import asyncio

@loader.tds
class iOSAppsForAndroid(loader.Module):
	"""
	🇷🇺 iOS приложения на Android, или же 
	проще говоря Android приложения с интерфейсом, как на iOS
	🇺🇸 iOS Applications for Android, or more simply,
	Android applications with an interface like on iOS
	"""

	strings = {
		"name": "iOSappsForAndroid",
		"apps-list": "<b>The list of applications in the module at the moment:\nApplication name --> command</b>\n<i>1) iCall --> .iCallApp \n2) iLauncher --> .iLauncherApp \n3) iLock --> .iLockApp \n4) iSwiftKeyboard --> .iSwiftApp \n5) iWhatsApp --> .iWhatsApp \n6)iNotes --> .iNotesApp \n7) iMessages --> .iMessagesApp \n8) iContacts --> .iContactsApp \n9) iPhotos --> .iPhotosApp \n10) iCalculator --> .iCalculator\n<b>All applications are taken from the channel @progi95 & @IbreymMods</b></i>",
		"support_chat_btn": "🎩 Support Chat 🎓",
		"more_modules_btn": "🌌 More Modules ✨",
		"wait": "🕑Waiting...",
		"isto4nik_apps": "Channel Apps",
		"isto4nik_apps2": "Channel Apps 2",
		"iCalculator_text": "<b>ICalculator Pro is an ios—style calculator for your android, with ios design, with calculator history and with other settings.\n♦️ Ibreym Mods (https://t.me/IbreymMods).\nMods: the full version is open, without ads.\nIbreym Mods. (<a href='https://telegra.ph/Kalkulyator-v-stile-ios-16-na-lyuboj-android-07-12 '>screenshots</a></b>",
		"iCall_text": "🔥<b>iCall Pro</b> — <i>a dialer in the style of iOS on Android with a beautiful iPhone design and various functions, such as changing the contact wallpaper, etc.<i>\n<b>🔑Mods: PRO version.\n \n \n🔑Description of the modification:</b>\n<i>— Update: 2.4.4. \n— The full version has been purchased. \n— All functions are open. \n— All templates are available. \n— Advertising is disabled. \n— Removed excess. \n is a working mod.</i></b>",
		"iLauncher_text1": "<b>🔥Ios 16 Launcher is an application with which you can turn your android desktop into an iPhone. Changes icons, style, screen recording on ios. \n🔑Mods: PRO version.</b>",
		"iLauncher_text2": "<b>🚀Description of the modification: \nModder: Ibreym. \n— Removed the advertising completely. \n— The application is completely in Russian, so it will not be so difficult to configure it. ✅To activate, you need to issue all the necessary permissions, and then click on the 'make default launcher' button.</b>",
		"iLock_text": "<i><b>🚀iLock — ios-style screen lock, with the coolest style, translated into Russian, removed ads, you can put your background, password and more. Throw screenshots in the comments.\n🔑Mods: PRO version. \n🔘Mods from Ibreym: \n— Removed the ad.\n— Translated into Russian to make it more understandable for you to configure.\n— And also translated the inscriptions on the lock screen to make it look better.Set up following the instructions, everything is easy and simple. The screen works cool, and it looks.</b></i>",
		"iSwiftKey_text1": "<b>😍The newest iPhone keyboard for your android. And now attention: - ios themes, ios 16 emoticons, there are any languages, including Russian, there is a t9 (hint, correction of words), the ability to change the size, and most importantly - the iPhone sound when typing.\n😍Run to watch:</b>",
		"iSwiftKey_text2": "<b>🌚iOS—style keyboard for any android with iOS 16 and emoticons: \n— Dark and white iOS theme.\n- Supports Russian and other languages. \n— there is a T9 hint, correction of words. \n— you can adjust the size of the keyboard for yourself. \n— there is an iPhone typing sound.\n🎥All this needs to be configured, and for this, watch the video review on the button above</b>",
		"iWhatsApp_text1": "<b>♻️Ibreym-WhatsApp is the best whatsapp mod from the developer Ibreym. It's two in one! - WhatsApp+ features, and the design is apple where you can spend time with a buzz!\n🔺Developer: Stefano (Mb Mods)\n🎥Video review:</b>",
		"iWhatsApp_text2": "<b><i>MBWhatsapp.\nNew: 9.30.b2.\nWhat's new?\n Corrected:\n- Running the app on some devices\n🔷 Improved the ability to confirm the status of the media before sending (MB preferencias/Home screen /🙅🏼Status -> Confirm before sending the status).Added the ability to disable notifications from those who blocked you.\n🛑 Fixed:\n🔺 Probably fixed forced closure for Android -8 (please report it if it's still happening).\n🔺 Minor fixes in default themes.\n🔺 Fixed: default wallpaper.Fixed: The status did not stop when opening the download dialog box.\n🔺 Fixed: copy the title in the status.\n🔺 Fixed: hide the quicklist.\n🔺 Fixed: hide searchview.\n🔺 Fixed: hiding a string of archived chats.\n🔺 Fixed: changing the size of rows.Fixed: changing the size of emoticons.\n🔺 Fixed: changing the size of stickers.Fixed: disabling large emoticons. (❤️)\n🔺 Fixed: some emoticons (🫢,🤭)</i></b>.",
		"iNotes_text": "<b>iNotes Pro — ios-style notes for your android with ios design and themes, with the ability to set a password when logging in, and with other various functions and features!\nMods: the full version is open, without ads.\nIbreym Mods. (<a href='https://telegra.ph/Zametki-v-stile-ios-16-na-lyuboj-android-07-11'>screenshots</a>)</b>",
		"iPhotos_text": "<b>iPhotos is a very beautiful iOS—style gallery for your android, with a beautiful iPhone design, two themes, with a basket, with albums and other various settings.\nMods: the full version is open, without ads.\nIbreym Mods. (<a href='https://telegra.ph/Galereya-v-stile-ios-16-na-lyuboj-android-07-10 '>screenshots</a>)</b>",
		"iMessages_text": "<b>iMessages — ios-style messages for your android, with built-in iOS themes in black and light colors, with a beautiful design, and various settings!\nThe full version is open for subscribers, where there are no ads and pro functions are available.\nIbreym Mods.</b>",
		"iContacts_text": "<b>iContacts Ios — iOS-style contacts for your android with a dark and light iPhone theme, design, and other functions like an iPhone.\nMods: the full version is open, without ads.\nIbreym Mods.</b>",
	}

	strings_ru = {
		"apps-list": "<b>Список приложений в модуле на данный момент:\nНазвание приложения --> команда</b> \n<i>1) iCall --> .iCallApp \n2) iLauncher --> .iLauncherApp \n3) iLock --> .iLockApp \n4) iSwiftKeyboard --> .iSwiftApp \n5) iWhatsApp --> .iWhatsApp \n6)iNotes --> .iNotesApp \n7) iMessages --> .iMessagesApp \n8) iContacts --> iContactsApp \n9) iPhotos --> iPhotosApp \n10) iCalculator --> .iCalculatorApp\n<b>Все приложения взяты из канала @progi95 & @IbreymMods</b></i>",
		"support_chat_btn": "🎩 Чат поддержки 🎓",
		"more_modules_btn": "🌌 Больше Модулей ✨",
		"wait": "🕑Ожидайте...",
		"isto4nik_apps": "Канал приложений",
		"isto4nik_apps2": "Канал приложений 2",
		"iCalculator_text": "<b>iCalculator Pro — калькулятор в стиле ios на ваш андроид, с ios дизайном, с историей калькулятора и с другими настройками.\n♦️ Ibreym Mods (https://t.me/IbreymMods).\nМоды: открыта полная версия, без рекламы.\nIbreym Mods. (<a href='https://telegra.ph/Kalkulyator-v-stile-ios-16-na-lyuboj-android-07-12'>скрины</a></b>",
		"iCall_text": "🔥<b>iCall Pro</b> — <i>звонилка в стиле iOS на Android с красивым, айфоновским дизайном и различными функциями, например смена обоев контакта и т.д.<i>\n<b>🔑Моды: PRO версия.\n \n \n🔑Описание модификации:</b>\n<i>— Обнова: 2.4.4. \n— Куплена полная версия. \n— Открыты все функции. \n— Доступны все шаблоны. \n— Отключена реклама. \n— Удалено лишнее. \n— Мод рабочий.</i>",
		"iLauncher_text1": "<b>🔥Ios 16 Launcher  — приложение с помощью которого вы можете превратить свой рабочий стол андроида в айфон. Меняет иконки, стиль, запись экрана на ios. \n🔑Моды: PRO версия.</b>",
		"iLauncher_text2": "<b>🚀Описание модификации: \nМоддер: Ibreym. \n— Убрали полностью рекламу. \n— Приложение полностью на русском языке, поэтому настроить его будет не так сложно. \n ✅Для активации нужно выдать все необходимые разрешения, а потом нажать на кнопку «make default launcher».</b>",
		"iLock_text": "<i><b>🚀iLock — блокировка экрана в стиле ios, с крутейшим стилем., перевел на русским язык, удалил рекламу, можно поставить свой фон, пароль и не только. Скрины кидайте в комментариях.\n🔑Моды: PRO версия. \n🔘Моды от Ibreym: \n— Удалил рекламу.\n— Перевел на русский язык, чтобы вам было более понятно настроить.\n— А также перевел надписи на экране блокировки, чтобы выглядело лучше.\nНастраивайте следуя инструкциям, все легко и просто. Экран круто работает, и выглядит.</b></i>",
		"iSwiftKey_text1": "<b>😍Новейшая айфоновская клавиатура на ваш андроид. А теперь внимание: - темы ios, смайлы ios 16, есть любые языки, в том числе русский, есть т9(подсказка, исправление слов), возможность менять размер, и самое главное - айфоновский звук при печатании.\n😍Беги смотреть:</b>",
		"iSwiftKey_text2": "<b>🌚Клавиатура в стиле ios на любой андроид со смайлами ios 16 и: \n— темная и белая тема ios.\n— поддерживает русский и другие языки. \n— есть Т9 подсказка, исправление слов. \n— можно подстроить под себя размер клавиатуры. \n— есть айфоновский звук печатания.\n🎥Всё это нужно настроить, а для этого смотрите видеообзор по кнопке выше</b>",
		"iWhatsApp_text1": "<b>♻️Ibreym-WhatsApp — самый лучший мод на whatsapp от разработчика Ibreym. Это два в одном! - функции whatsApp +, а дизайн - apple где можно с кайфом проводить время!\n🔺Developer: Stefano (Mb Mods)\n🎥Видеообзор:</b>",
		"iWhatsApp_text2": "<b><i>MBWhatsapp.\nОбнова: 9.30.b2.\nЧто нового?\nИсправлено:\n- Запуск приложения на некоторых устройствах\n🔷 Улучшена возможность подтверждения перед отправкой статуса носителя (MB preferencias/Главный экран /🙅🏼Статус -> Подтвердить перед отправкой статуса).\n🔷 Добавлена возможность отключения уведомлений от тех , кто вас заблокировал.\n🛑 Исправлено:\n🔺 Вероятно, исправлено принудительное закрытие для Android -8 (сообщите об этом, если это все еще происходит).\n🔺 Незначительные исправления в темах по умолчанию.\n🔺 Исправлено: обои по умолчанию.\n🔺 Исправлено: статус не останавливался при открытии диалогового окна загрузки.\n🔺 Исправлено: копировать заголовок в статусе.\n🔺 Исправлено: скрыть быстрый список.\n🔺 Исправлено: скрыть searchview.\n🔺 Исправлено: скрытие строки архивированных чатов.\n🔺 Исправлено: изменение размера строк.\n🔺 Исправлено: изменение размера смайликов.\n🔺 Исправлено: изменение размера наклеек.\n🔺 Исправлено: отключение больших смайликов. (❤️)\n🔺 Исправлено: некоторые смайлики (🫢,🤭)</i></b>.",
		"iNotes_text": "<b>iNotes Pro — заметки в стиле ios на ваш андроид с дизайном и темами ios, с возможностью поставить пароль при входе, и с другими различными функциями и возможностями!\nМоды: открыта полная версия, без рекламы.\nIbreym Mods. (<a href='https://telegra.ph/Zametki-v-stile-ios-16-na-lyuboj-android-07-11'>скрины</a>)</b>",
		"iPhotos_text": "<b>iPhotos — очень красивая галерея в стиле ios на ваш андроид, с красивым айфоновским дизайном, двумя темами, с корзиной, с альбомами и другими различными настройками.\nМоды: открыта полная версия, без рекламы.\nIbreym Mods. (<a href='https://telegra.ph/Galereya-v-stile-ios-16-na-lyuboj-android-07-10'>скрины</a>)</b>",
		"iMessages_text": "<b>iMessages — сообщения в стиле ios на ваш андроид, со встроенными ios темами черного и светлого цвета, с красивым дизайном, и различными настройками!\nОткрыта полная версия для подписчиков, где нет рекламы и доступны pro функции.\nIbreym Mods.</b>",
		"iContacts_text": "<b>iContacts Ios — контакты в стиле ios на ваш андроид с темной и светлой айфоновской темой, дизайном, и другими функциями как у айфона.\nМоды: открыта полная версия, без рекламы.\nIbreym Mods.</b>",
	}

	async def iAppsListcmd(self, message):
		"""-->List iOS Apps for Android"""
		await self.inline.form(
			self.strings("apps-list"),
			reply_markup=[
				[{"text": self.strings("support_chat_btn"), "url": "https://t.me/AstroModulesChat"}],
				[{"text": self.strings("more_modules_btn"), "url": "https://t.me/AstroModules"}],
				[{"text": self.strings("isto4nik_apps"), "url": "https://t.me/progi95"}],
				[{"text": self.strings("isto4nik_apps2"), "url": "https://t.me/IbreymMods"}],
				[{"text": "🚫 Закрыть | 🚫 Close", "action": "close"}],
			],
			message=message,
		)

	async def iCallAppcmd(self, message: Message):
		""" --> iCall"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/progi95/3806"
		await message.respond(self.strings("iCall_text"), file=file)

	async def iLauncherAppcmd(self, message: Message):
		""" --> iLauncher"""
		await self.inline.form(
			self.strings("iLauncher_text1"),
			message=message,
			reply_markup=[
				[{"text": "🎥Видеообзор", "url": "https://youtu.be/D3IjVjuy9kI"}],
			],
			photo="https://0x0.st/o1Pe.jpg"
		)
		await asyncio.sleep(1)
		file = "https://t.me/progi95/3801"
		await message.respond(self.strings("iLauncher_text2"), file=file)

	async def iLockAppcmd(self, message: Message):
		""" -->iLock"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/progi95/3796"
		await message.respond(self.strings("iLock_text"), file=file)

	async def iSwiftAppcmd(self, message: Message):
		""" --> iSwiftKeyboard"""
		await self.inline.form(
			self.strings("iSwiftKey_text1"),
			message=message,
			reply_markup=[
				[{"text": "🎥Видеообзор", "url": "https://youtu.be/n0aFenC3cz0"}],
			],
			photo="https://0x0.st/o1ZH.jpg"
		)
		await asyncio.sleep(1)
		file = "https://t.me/progi95/3754"
		await message.respond(self.strings("iSwiftKey_text2"), file=file)

	async def iWhatsAppcmd(self, message: Message):
		""" --> iWhatsApp"""
		await self.inline.form(
			self.strings("iWhatsApp_text1"),
			message=message,
			reply_markup=[
				[{"text": "🎥Видеообзор", "url": "https://youtu.be/rlFNpG2BRB0"}],
			],
			photo="https://0x0.st/o1Zm.jpg"
		)
		await asyncio.sleep(1)
		file = "https://t.me/progi95/3757"
		await message.respond(self.strings("iWhatsApp_text2"), file=file)

	async def iNotesAppcmd(self, message: Message):
		""" --> iNotes"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/IbreymMods/576"
		await message.respond(self.strings("iNotes_text"), file=file)

	async def iPhotosAppcmd(self, message: Message):
		""" --> iPhotos"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/IbreymMods/574"
		await message.respond(self.strings("iPhotos_text"), file=file)

	async def iContactsAppcmd(self, message: Message):
		""" --> iContacts"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/IbreymMods/573"
		await message.respond(self.strings("iContacts_text"), file=file)

	async def iMessagesAppcmd(self, message: Message):
		""" --> iMessages"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/IbreymMods/572"
		await message.respond(self.strings("iMessages_text"), file=file)

	async def iCalculatorAppcmd(self, message: Message):
		""" --> iCalculator"""
		await utils.answer(self.strings("wait"))
		await asyncio.sleep(1)
		file = "https://t.me/IbreymMods/577"
		await message.respond(self.strings("iCalculator_text"), file=file)