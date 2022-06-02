from .. import loader

class LikeAntTrollMod(loader.Module):
	"""улучшенная версия предыдущего модуля"""
	strings = {"name": "Compliments and Toxicity(beta)"}
	Комплименты = ["Ты...прекрасная, а еще....", "красивая", "заботливая", "добрая"]
	async def likezpmx2cmd(self, message): 
		for i in range(len(Комплименты)): 
			await message.respond(Комплименты[i])