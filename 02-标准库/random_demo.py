import random

r = random.Random()
print(r.random()) # [0, 1)
print(r.randint(100, 200))
print(r.randrange(100, 200, 10))

