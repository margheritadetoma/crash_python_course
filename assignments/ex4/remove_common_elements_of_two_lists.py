
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

for element in a[:]:  # Use a[:] to create a copy of the list, so we can modify the original list
    if element in b:
        a.remove(element)
        b.remove(element)


'''
a = [1, 2, 3, 4, 5]
a_copy = a
b = [3, 4, 5, 6, 7]

set_b = set(b)

# Iterate through elements of list a
a = [element for element in a if element not in set_b]

# Update list b to remove common elements
b = [element for element in b if element not in a_copy]
'''

print("List a after removal:", a)
print("List b after removal:", b)

