def ascending(list_of_numbers):
    list_of_numbers.sort()
    return list_of_numbers

list_of_numbers = []
limit = int(input("Enter the limit: "))
for i in range(1, limit + 1):
    list_of_numbers.append(int(input(f'Enter {i}. number: ')))

result = ascending(list_of_numbers)
print(result)
