def sum_of_range(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        total_sum += num
    return total_sum
start_num = int(input("Enter the starting point of the range: "))
end_num = int(input("Enter the last point of the range: "))
result = sum_of_range(start_num, end_num)
print("The sum of numbers from", start_num, "to", end_num, "is:", result)
