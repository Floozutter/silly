"""
calculate the time to fill an Industrial Foregoing Black Hole Unit or Tank!
"""

SLOTS = 2_147_483_647

def proportion(slots_filled: int) -> float:
    # https://english.stackexchange.com/questions/275734
    return slots_filled / SLOTS

def seconds(slots_per_second: float) -> float:
    return SLOTS / slots_per_second
