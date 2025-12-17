drivers: list[str] = ["Lewis", "Lando", "Max", "Carlos"]

print(drivers)  # Will return -> Lewis, Lando, Max, Carlos
print(len(drivers))  # Will return 4

print(drivers[0])  # Will return 'Lewis'
print(drivers[-1])  # A negative index will start from the end -> 'Carlos'
print(drivers[0:2])  # Returns a range -> Lewis, Lando, Max

print("Max" in drivers)  # Will return True

drivers[0] = "Checo" # This will replace value at index 0 with new value -> 'Checo'
print(drivers[0])

drivers.insert(4, '!!!') # Will insert '!!!' at the 4th inded
print(drivers)
drivers.append('Valteri') # Append adds the value to the end of the list

drivers.pop(4) # Removes the value at the 4th index
print(drivers)

reserve_drivers: list[str] = ['Oscar', 'Charles', 'kimmi']
drivers.extend(reserve_drivers) # Will return a concatinated list
print(drivers)