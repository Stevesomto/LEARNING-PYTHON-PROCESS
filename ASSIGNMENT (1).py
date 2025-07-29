# import stage

import math
from typing import Tuple

def triangle_area(a: float, b: float, c: float) -> float:
#Return the area of a triangle using Heron's formula."""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle.")
    s = (a + b + c) / 2  # semi‑perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


# --- driver code ---
if __name__ == "__main__":
    sides: Tuple[float, float, float] = tuple(
        float(input(f"Enter length of side {i+1}: ")) for i in range(3)
    )
    area = triangle_area(*sides)
    print(f"The area of the triangle is {area:.2f} square units.")
