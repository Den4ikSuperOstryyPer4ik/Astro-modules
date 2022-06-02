from .. import loader

class LikeAntTrollMod(loader.Module):
	"""улучшенная версия предыдущего модуля"""
	strings = {"name": "Compliments and Toxicity(beta)"}
	Комплименты = ["Ты...прекрасная, а еще....", "красивая", "заботливая", "добрая"]
	for i in range(len(Комплименты)): 
		await message.respond(Комплименты[i])