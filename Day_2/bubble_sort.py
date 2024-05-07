def bubble_sort(num_list):
    n = len(num_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

num_list = [89, 43, 99, 55, 87, 67]

bubble_sort(num_list)

print("Sorted list:", num_list)
