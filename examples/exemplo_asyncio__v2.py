# Exemplo asyncio
from asyncio import (
	all_tasks, create_task, gather, run, sleep 
)
from rich import print
from random import randint

# corrotina assíncrona de teste
async def minha_corrotina(val: int, delay: int = 1):
	print(f'Início da corrotina {val}')
	await sleep(delay)
	print(f'Meio da corrotina {val}')
	await sleep(delay)
	print(f'Fim da corrotina {val}')

	return {'TASK': val, 'tempo': delay}


# Método main para rodar as corrotinas assíncronas
async def main():
	tasks = gather(
		*[minha_corrotina(n, randint(1,8)) for n in range(20)]
	)

	print(f'Fila de TAsKS: {all_tasks()}')

	result = await tasks

	print(f'Fila de TAsKS: {all_tasks()}')
	print(result)


run(main())