
import random
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= 1000 and 1 <= max <= 1000):
        return[]
    if min > max:
        return[]
    if quantity > ( max - min + 1) or quantity <= 0:
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers = random.randint(min, max)
        numbers.add(number)
        return sorted(numbers)
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(lottery_numbers)
    

    <body>
    <h1> Homework 3-4 </h1>
<body>
