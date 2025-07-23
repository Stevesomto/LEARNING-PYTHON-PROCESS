# LIST COMPRRHENSION PROVIDES A SIMPLE AND CONCISE WAY TO CREATE AND MANIPULATE LIST USING A SINGLE LINE OF CODE. THEY ARE READY AND FASTER THAN TRADITIONAL LOOP
# []   [expression for item in iterable if condition]

squares = [x ** 2 for x in range(20)]
print(squares)


names = ["Alice", "Stephen", "Somto"]
short_names = [name for name in names if len(name) < 6]
print (short_names)
