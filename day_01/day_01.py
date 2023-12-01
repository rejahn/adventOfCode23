with open('./input/input') as file:
    text = file.readlines()

calibrated_numbers = []
for line in text:
    num = ''.join(c for c in line if c.isdigit())
    
    if len(num) == 1:
        num = num * 2
    elif len(num) > 2:
        num = num[0] + num[-1]
    
    calibrated_numbers.append(int(num))

answer = sum(calibrated_numbers)

print("Sum: ", answer)
