number=3.14



#list to tuple 

fruits=(
    "apple", "banana", "oranges"
)
print(type(fruits))
#print(fruits[0])
print(fruits)

print('converting tuple to list')
fruits=list(fruits)
print(type(fruits))

fruits[0]="kiwi"

print(fruits)
