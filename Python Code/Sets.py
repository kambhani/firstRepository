from functions import exponent

#Demonstrates how to use sets in Python
s = set()
for i in range(5):
    s.add(i)
s.add(0)
print(s)

#For fun: using dictionaries (basically maps)
ages = {"Me": 15, "Mother": 43}
ages["Me"] += 1
ages["Brother"] = 14
print(ages)

#For ultra fun: import function from another file (see top for import statement)
print(exponent(3, 3))





