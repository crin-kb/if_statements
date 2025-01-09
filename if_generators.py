numbers = [1,2,3,4,5]
even_gen = (num for num in numbers if num % 2 == 0)
for even in even_gen:
    print(even)