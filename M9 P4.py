#Greg Brewer
#6/10/23
#Problem 4 create awhile loop that initializes  counter

counter = 0
tens = []

while counter <= 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print("List of numbers divisible by 10:", tens)
