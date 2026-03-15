import random  # import module to generate random numbers

numbers = []  # create an empty list to store 100 random numbers

# generate numbers using while loop
count = 0  # counter for the loop
while count < 100:
    num = random.randint(0, 1000)  # generate a random number between 0 and 1000
    numbers.append(num)  # add the number to the list
    count += 1  # increment the counter

# manual sorting of the list using bubble sort
n = len(numbers)  # get length of the list
i = 0
while i < n:  # outer loop for passes
    j = 0
    while j < n - i - 1:  # inner loop to compare adjacent elements
        if numbers[j] > numbers[j + 1]:  # if current element is greater than next
            # swap elements using tuple unpacking
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        j += 1
    i += 1

# calculate sum and count of even and odd numbers
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0

for num in numbers:  # iterate through all numbers in the list
    if num % 2 == 0:  # check if the number is even
        even_sum += num  # add to even sum
        even_count += 1  # increment even counter
    elif num % 2 != 0:  # check if the number is odd
        odd_sum += num  # add to odd sum
        odd_count += 1  # increment odd counter
    else:
        continue  # skip any unexpected value (just for demonstration of continue)

# calculate averages
even_avg = even_sum / even_count if even_count != 0 else 0  # average for even numbers
odd_avg = odd_sum / odd_count if odd_count != 0 else 0  # average for odd numbers

# print results
print("Average of even numbers:", even_avg)
print("Average of odd numbers:", odd_avg)