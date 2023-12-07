import os


def get_value(s):
    return int(''.join(filter(str.isdigit, s)))


def is_subset_possible(subset, max_red, max_green, max_blue):
    r = g = b = 0
    for color in subset.split(','):
        color = color.strip()
        if 'red' in color:
            r += get_value(color)
        elif 'green' in color:
            g += get_value(color)
        elif 'blue' in color:
            b += get_value(color)

    return r <= max_red and g <= max_green and b <= max_blue


def main():
    sum_id = 0
    path = os.path.join(os.getcwd(), 'input/input')
    with open(path) as file:
        text = file.readlines()

    for line in text:
        game_id, subsets = line.split(':')
        game_id = int(game_id.split()[1])  # Extracting the game ID

        game_possible = True
        for subset in subsets.split(';'):
            if not is_subset_possible(subset, 12, 13, 14):
                game_possible = False
                break

        if game_possible:
            sum_id += game_id

    print(sum_id)


if __name__ == "__main__":
    main()
