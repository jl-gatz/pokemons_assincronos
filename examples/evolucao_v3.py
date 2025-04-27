from httpx import AsyncClient
from random import randint
from rich import print
from asyncio import (
	all_tasks, create_task, gather, run, sleep
)

from pokes import pokes as pokemons


async def evolucao(poke: str, delay: int = 1):
	'''
	Evolução do pokemon assíncrono
	'''
	async with AsyncClient(base_url='https://pokeapi.co/api/v2/') as client:
		# request 1
		response = await client.get(f'/pokemon/{poke}')
		id_ = response.json().get('id')
		# prints para observar a ordem de execução
		print(f'... [b][red]{id_}: peguei o id do {poke}')

		# request 2
		response = await client.get(f'/pokemon-species/{id_}')
		evolves = (
			response
			.json()
			.get('evolution_chain')
			.get('url')
		)
		# prints para observar a ordem de execução
		print(f'... [b][yellow]{id_}: peguei a url da evolução do {poke}')

		# request 3
		response = await client.get(evolves)
		evolution_name = (
			response
			.json()
			.get('chain')
			.get('evolves_to')[0]
			.get('species')
			.get('name')
		)
		# prints para observar a ordem de execução
		print(f'... [b][green]{id_}: peguei a evolução do {poke}')

		return {'Pokemon': poke, 'Evolution': evolution_name, 'delay': delay}


async def main():
	'''
	Método main para rodar a busca da evolução do pokemon assíncrono
	'''
	tasks = gather(
		*[evolucao(poke, randint(1,8)) for poke in pokemons]
	)

	result = await tasks
	print(result)


if __name__ == '__main__':
	run(main())