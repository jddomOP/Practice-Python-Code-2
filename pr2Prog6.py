num = [int(input(f"Enter num {i+1}: ")) for i in range (10)]
result = num[0] - sum(num[1:])
print("Result", result)