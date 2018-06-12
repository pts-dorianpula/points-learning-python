numbers = [
2,14,144,62,1729,44,101,210,6,12,33,550,1001,11,142,674,37,45,167,764,999,3,66,174,982,112,245,501,63,91
]

# Task 1: count how many numbers are less than 50
counter = 0
for number in numbers:
    if number < 50:
        counter = counter + 1

print(counter)



# Task 2: count how many numbers are greater than 500 and less than 1000
counter = 0
for number in numbers:
    # if number > 500 and number < 1000:
    if 500 < number < 1000:
        counter = counter + 1

print(counter)



# Bonus: count how many numbers are odd
counter = 0
for number in numbers:
    result = float(number) / 2
    if result != int(result):
        # OMG it's odd!
        counter = counter + 1

print(counter)

# Bonus: count how many numbers are odd
counter = 0
for number in numbers:
    result = float(number) / 2
    if ".5" in str(result):
        # OMG it's odd!
        counter = counter + 1

print(counter)


print("###", len([x for x in numbers if x % 2 == 1]))
