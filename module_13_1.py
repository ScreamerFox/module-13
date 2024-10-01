async def start_strongman(name, power):
    balls = 1
    while balls < 5:
        print(f'Силач {name} начал соревнования')
        await asyncio.sleep(balls / power)
        print(f'Силач {name} поднял {balls}')
        balls += 1
    print(f'силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Виктор Блуд', 4))
    task2 = asyncio.create_task(start_strongman('Алексей Столяров', 3))
    task3 = asyncio.create_task(start_strongman('Кирилл Сарычев', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
