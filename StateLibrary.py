import enum


class FixedSymbols(enum.Enum):
    OpenSpace = 'o'  # o == open space
    DoNotCare = 'x'  # x == do not care


start_state = [
    ['B', 'A', 'a', 'D'],
    ['b', 'a', 'a', 'd'],
    ['C', 'F', 'f', 'E'],
    ['c', 'H', 'I', 'e'],
    ['G', None, None, 'J']
]
