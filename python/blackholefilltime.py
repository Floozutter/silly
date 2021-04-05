"""
calculate the time to fill an Industrial Foregoing Black Hole Unit or Tank!
"""

SLOTS = 2_147_483_647

def seconds_from_slots_per_second(slots_per_second: float) -> float:
    return SLOTS / slots_per_second
