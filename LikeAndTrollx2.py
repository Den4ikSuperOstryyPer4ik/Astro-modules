from .. import loader

class LikeAntTrollMod(loader.Module):
	"""улучшенная версия предыдущего модуля"""
	strings = {"name": "Compliments and Toxicity(beta)"}
	async def likezpmx2cmd(self, message): 
		Комплименты = [ ["Ты...прекрасная, а еще....", ] ["красивая", "заботливая", "добрая"] ]
		await message.edit("Ты......")
		await sleep(1)
		await message.edit("Ты...прекрасная...")
		await sleep(1)
		await message.edit("Ты...прекрасная, а еще....")
		for i in range(len(Комплименты)): 
			await message.respond(Комплименты[i])