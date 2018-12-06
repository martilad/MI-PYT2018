def running_sum():
    total = 0
    while True:
        num = (yield total)
        if num:
            total += num

it = running_sum()
print(next(it))  # pro první iteraci nelze použít send() -- nečekáme zatím na yield-u
print(it.send(2))
print(it.send(3))
print(next(it))
print(next(it))


async def demo():
    tasks = []
    for x in some:
        tasks.append(asyncio.ensure_future(add(some, some)))

    for x in tasks:
        print(result : await(x))

    await asyncio.gather(*tasks)