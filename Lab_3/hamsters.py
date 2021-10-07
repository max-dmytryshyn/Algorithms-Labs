class Hamster:
    def __init__(self, basic_food=0, extra_food=0):
        self.basic_food = basic_food
        self.extra_food = extra_food

    def total_food(self, number_of_neighbours):
        return self.basic_food + self.extra_food * number_of_neighbours


def delete_useless_hamsters(hamsters, food_amount):
    new_hamsters = []
    for hamster in hamsters:
        if hamster.basic_food <= food_amount:
            new_hamsters.append(hamster)
    hamsters[:] = new_hamsters


def find_hamsters_amount(possible_amounts, hamsters, food_amount):
    if len(possible_amounts) == 0:
        return 0

    if len(possible_amounts) == 1:
        return possible_amounts[0]

    current_amount = possible_amounts[len(possible_amounts) // 2]
    hamsters.sort(key=lambda hamster: hamster.total_food(current_amount - 1))
    if sum(hamster.total_food(current_amount - 1) for hamster in hamsters[:current_amount]) > food_amount:
        return find_hamsters_amount(possible_amounts[:len(possible_amounts) // 2], hamsters, food_amount)
    else:
        return find_hamsters_amount(possible_amounts[len(possible_amounts) // 2:], hamsters, food_amount)


def max_hamsters_amount(hamsters, food_amount):
    delete_useless_hamsters(hamsters, food_amount)
    return find_hamsters_amount([i + 1 for i in range(len(hamsters))], hamsters, food_amount)


if __name__ == "__main__":
    food_amount = int(input())
    total_hamsters_amount = int(input())
    hamsters = []

    for i in range(total_hamsters_amount):
        hamsters.append(Hamster(*[int(food_need) for food_need in input().split()]))

    print(max_hamsters_amount(hamsters, food_amount))
