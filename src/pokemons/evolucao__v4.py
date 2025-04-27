from asyncio import run
from functools import partial

from aiometer import run_all
from httpx import AsyncClient
from rich import print

from pokes import pokes as pokemons


async def evolucao(poke: str) -> dict:
    """
    Evolução do pokemon assíncrono
    """
    async with AsyncClient(base_url='https://pokeapi.co/api/v2/') as client:
        # request 1
        response = await client.get(f'/pokemon/{poke}')
        id_ = response.json().get('id')
        # prints para observar a ordem de execução
        print(f'... [b][red]{id_}: peguei o id do {poke}')

        # request 2
        response = await client.get(f'/pokemon-species/{id_}')
        evolves = response.json().get('evolution_chain').get('url')
        # prints para observar a ordem de execução
        print(f'... [b][yellow]{id_}: peguei a url da evolução do {poke}')

        # request 3
        response = await client.get(evolves)
        evolution_name = (
            response.json()
            .get('chain')
            .get('evolves_to')[0]
            .get('species')
            .get('name')
        )
        # prints para observar a ordem de execução
        print(f'... [b][green]{id_}: peguei a evolução do {poke}')

        return {'Pokemon': poke, 'Evolution': evolution_name}


async def main() -> None:
    """
    Método main para rodar a busca da evolução do pokemon assíncrono
    """
    # tasks = gather(
    #     *[evolucao(poke) for poke in pokemons]
    # )
    # Utilizando aiometer (nos permite ganhar controle sobre o
    # retorno e o tempo de retorno da API)
    tasks = run_all(
        [partial(evolucao, poke) for poke in pokemons],
        max_at_once=5,
        max_per_second=10,
    )

    result = await tasks
    print(result)


if __name__ == '__main__':
    run(main())
