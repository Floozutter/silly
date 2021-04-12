"""
labels the grid positions for 80 cows
"""

from itertools import count

if __name__ == "__main__":
    counter = count()
    cowgrid = "\n".join(
        " ".join(
            f"{next(counter):02x}" if (i, j) != (4, 4) else "##"
            for j in range(9)
        )
        for i in range(9)
    )
    print(cowgrid)
