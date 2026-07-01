list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = []

for item in list1:
    merged.append(item)

for item in list2:
    merged.append(item)

print("Merged list:")
print(*merged)