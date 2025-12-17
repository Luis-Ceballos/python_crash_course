drivers: list[str] = ["Lewis", "Lando", "Max", "Carlos"]

print(drivers)  # Will return -> Lewis, Lando, Max, Carlos
print(len(drivers))  # Will return 4

print(drivers[0])  # Will return 'Lewis'
print(drivers[-1])  # A negative index will start from the end -> 'Carlos'
print(drivers[0:2])  # Returns a range -> Lewis, Lando, Max

print("Max" in drivers)  # Will return True
