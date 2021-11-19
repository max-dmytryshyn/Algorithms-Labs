def calculate_amount_of_paths(corridor, y, x, cells_to_jump, paths_amounts):
    if (y, x) in paths_amounts:
        return paths_amounts[(y, x)]

    result = calculate_amount_of_paths(corridor, y, x - 1, cells_to_jump, paths_amounts)
    cell = corridor[y][x]
    for cell_to_jump in cells_to_jump[cell]:
        if cell_to_jump[1] < x and not (cell_to_jump[0] == y and cell_to_jump[1] == x - 1):
            result += calculate_amount_of_paths(corridor, *cell_to_jump, cells_to_jump, paths_amounts)

    paths_amounts[(y, x)] = result
    return result


def solve_ijones(width, height, corridor):
    cells_to_jump = {}
    for y in range(height):
        for x in range(width):
            cell = corridor[y][x]
            if cell not in cells_to_jump:
                cells_to_jump[cell] = [(y, x)]
            else:
                cells_to_jump[cell].append((y, x))

    paths_amounts = {(i, 0): 1 for i in range(height)}

    if height == 1:
        return calculate_amount_of_paths(corridor, 0, width - 1, cells_to_jump, paths_amounts)

    return calculate_amount_of_paths(corridor, 0, width - 1, cells_to_jump, paths_amounts) \
           + calculate_amount_of_paths(corridor, height - 1, width - 1, cells_to_jump, paths_amounts)


if __name__ == "__main__":
    input_file = open("ijones.in", "r")
    width, height = map(int, input_file.readline().split())
    corridor = [[] for _ in range(width)]
    for y in range(height):
        corridor[y] = input_file.readline()
    input_file.close()

    output_file = open("ijones.out", "w")
    output_file.write(str(solve_ijones(width, height, corridor)))
