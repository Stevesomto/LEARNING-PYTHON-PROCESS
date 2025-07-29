# SET 

A = {1, 2, 6, 7, 8, 10, 12}
B = {3, 6, 10, 1, 15, 17, 18}

intersection = A & B
union = A | B
are_disjoint = A.isdisjoint(B)  # True if the sets share no elements

print(f"6(i) Intersection: {intersection}")
print(f"6(ii) Union: {union}")
print(f"6(iii) Disjoint? {'Yes' if are_disjoint else 'No'}")
