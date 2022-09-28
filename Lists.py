#How to make a list and print it
cars = ['Suzuki', 'Honda', 'Mitsubishi', 'Mazda', 'Nissan', 'Toyota']
print(cars)
#How to append one more car brand to the list.
#You can append only one item at a time to a list
cars.append('Kia') 
print(cars)
cars.append('Morris Garage')
print(cars)
#How to sort the car brands in alphabetical order
cars.sort()
print(cars)
#How to sort the car brands in revers alphabetical order
cars.sort(reverse=True)
print(cars)
#How to print specific cars based on their indices
print(cars[3])
print(cars[-2])
