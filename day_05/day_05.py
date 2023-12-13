import os

path = os.path.join(os.getcwd(), 'input/input')
with open(path) as file:
    input_lines = file.readlines()

time = input_lines[0].split(':')[1].strip()
distance = input_lines[1].split(':')[1].strip()

# Convert to lists of integers
time_list = [int(num) for num in time.split()]
distance_list = [int(num) for num in distance.split()]

product = 1

for i, time in enumerate(time_list):
    winning_games = 0
    for milli in range(time):
        run_time = time - milli
        if milli * run_time > distance_list[i]:
            winning_games += 1
        else:
            pass

    product *= winning_games
print(product)
