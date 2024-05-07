def create_largest_number(number_list):
    # Convert numbers to strings and sort them based on custom comparison
    number_list = sorted(map(str, number_list), key=lambda x: x*3, reverse=True)
    # Concatenate the sorted numbers and return
    return int(''.join(number_list))

number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)
