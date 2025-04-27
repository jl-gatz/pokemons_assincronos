# Exemplo asyncio
from asyncio import sleep, create_task, all_tasks, run
from rich import print

async def minha_corrotina(val: int, delay: int = 1):
	print(f'Início da corrotina {val}')
	await sleep(delay)
	print(f'Meio da corrotina {val}')
	await sleep(delay)
	print(f'Fim da corrotina {val}')

async def main():
	task1 = create_task(minha_corrotina(1, 10))
	task2 = create_task(minha_corrotina(2))
	task3 = create_task(minha_corrotina(3))
	task4 = create_task(minha_corrotina(4))

	print(f'Tarefas pendentes antes de await: {all_tasks()}')

	await task1

	print(f'Tarefas pendentes após await 1: {all_tasks()}')

	await task2

	print(f'Tarefas pendentes após await 2: {all_tasks()}')


run(main())