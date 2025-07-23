def largest_of_three(x: float, y: float, z: float) -> float:
# Return the largest of the three supplied numbers."""
    return max(x, y, z)


# --- display output code ---
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
largest = largest_of_three(*numbers)
print(f"The largest number is {largest}")
