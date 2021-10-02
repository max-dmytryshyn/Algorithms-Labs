class Hamster:
    def __init__(self, basic_food=0, extra_food=0):
        self.basic_food = basic_food
        self.extra_food = extra_food

    def total_food(self, number_of_neighbours):
        return self.basic_food + self.extra_food * number_of_neighbours


def max_hamsters_amount(hamsters, food_amount):
    used_food_amount = 0
    result = 0

    while result < len(hamsters):
        result += 1
        hamsters.sort(key=lambda hamster: hamster.total_food(result - 1))
        used_food_amount = sum(
            hamster.total_food(result - 1) for hamster in hamsters[:result])
        if used_food_amount > food_amount:
            result -= 1
            break

    return result


if __name__ == "__main__":
    food_amount = int(input())
    total_hamsters_amount = int(input())
    hamsters = []

    for i in range(total_hamsters_amount):
        hamster = (Hamster(*[int(food_need) for food_need in input().split()]))
        if hamster.basic_food <= food_amount:
            hamsters.append(hamster)

    print(max_hamsters_amount(hamsters, food_amount))
