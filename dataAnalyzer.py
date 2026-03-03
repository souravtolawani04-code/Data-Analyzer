print("Data Analyzer")
print("-------------")

numbers = []

count = int(input("How many numbers you want to enter: "))

for i in range(count):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\nTotal:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

print("Thank You❤️")