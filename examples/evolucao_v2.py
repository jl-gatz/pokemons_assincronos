from httpx import Client

pokemons = ['caterpie', 'bulbasaur', 'charmander', 'squirtle', 'pikachu', 'raichu']

def evolucao(poke: str):
	with Client(base_url='https://pokeapi.co/api/v2/') as client:
		print(f'Entrada: {poke}')
		# request 1
		response = client.get(f'/pokemon/{poke}')
		id_ = response.json().get('id')

		# request 2
		response = client.get(f'/pokemon-species/{id_}')
		evolves = (
			response
			.json()
			.get('evolution_chain')
			.get('url')
		)

		# request 3
		response = client.get(evolves)
		evolution_name = (
			response
			.json()
			.get('chain')
			.get('evolves_to')[0]
			.get('species')
			.get('name')
		)

		print(f'SAÍDA: O {poke} evolui ---> {evolution_name}')


for poke in pokemons:
	evolucao(poke)