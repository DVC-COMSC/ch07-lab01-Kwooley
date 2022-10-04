
# ******************************
# Make your Code
# ******************************
numbers = [0] * 5

for i in range(5):
	numbers[i] = int(input())
	if i == 0 or min > numbers[i]:
		min = numbers[i]
	if i == 0 or max < numbers[i]:
		max = numbers[i]
total = sum(numbers) - min - max
print (total)