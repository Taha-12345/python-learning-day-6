# Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i

print("Sum:", total)

# Count even numbers from 1 to 100
count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1

print("Even numbers count:", count)
