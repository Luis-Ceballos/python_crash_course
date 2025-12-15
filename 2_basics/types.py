text = "Hello"  # This is a string -> str
number = 100  # This is a integer -> int
decimal = 2.4  # This is a float -> float
complex_number = 8j  # This is a complex number -> complex

# Sequence types
drivers = ["Lando", "Lewis", "George"]  # This is a list type -> list[type]

grid_place_number = (
    "P1",
    "P2",
    "P3",
)  # This is a tuple type -> tuple[type, type, type]

numbers = range(1, 1000)  # This is a range type -> range

driver_one = {
    "Mercedes": "George",
    "Mclaren": "Lando",
    "Ferrari": "Lewis",
}  # This is a dictionary type -> dict[type, type]

unique_numbers = {
    1,
    2,
    2,
    3,
    3,
    3,
    4,
}  # This is a set that makes sure there are no duplicates -> set[type]
# print(unique_numbers) -> prints 1, 2, 3, 4

is_on = True  # This is a boolean type -> bool
is_off = False

is_empty = (
    None  # This tells python that the varibale has nothing assigned to it -> None
)
hello = None
# print(type(hello)) -> <class 'NoneType'>

"""
Examples
"""

# Tuple example
teams: tuple[str, str, str] = ("Mercedes", "Mclaren", "Ferrari")
# print(teams[0]) -> Mercedes

# Dictionary example
team_points: dict[str, int] = {"Mercedes": 690, "Ferrari": 645, "Red Bull": 586}
