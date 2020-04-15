# odd number detection without any conditional statements

arr = [23, 12, 45, 36, 67, 79]
even = 0
odd = 0
even_odd = ["Even", "Odd"]
for a in arr:
    print(even_odd[a&1])
