from .. import loader

class LikeAntTrollMod(loader.Module):
	"""улучшенная версия предыдущего модуля"""
	strings = {"name": "Compliments and Toxicity(beta)"}
	async def likezpmx2cmd(self, message): 
		Комплименты = ["Ты...прекрасная, а еще....", "красивая", "заботливая", "добрая"]
		for i in range(len(Комплименты)): 
			await message.respond(Комплименты[i])