import os

path = os.path.join(os.getcwd(), 'day_04/input/input')
with open(path) as file:
    input_lines = file.readlines()

sum_count = 0

for line in input_lines:
    game = line.split(':')[1:]
    cards = game[0].split('|')
    elf_cards = [int(num) for num in cards[0].split()]
    winning_cards = [int(num) for num in cards[1].split()]
    count = 0  # Initialize count for each line
    for value in elf_cards:
        if value in winning_cards:
            if count > 1:
                count = 2 * count
            else:
                count += 1  # Increment count when a match is found

    sum_count += count
print(f"Sum = {sum_count}")