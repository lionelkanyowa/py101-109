# 1. Write two distinct ways of reversing the list without mutating the original list

numbers = [1, 2, 3, 4, 5]  # [5, 4, 3, 2, 1]
reversed_num = list(reversed(numbers))
print(reversed_num)

another_reverse = numbers[::-1]
print(another_reverse)

print(numbers)
