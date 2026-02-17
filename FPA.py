print("=========== FUNCTION POINT ANALYSIS ===========")

print("\nWeight Table:")
print("-------------------------------------------------")
print("Type   | Low | Average | High")
print("-------------------------------------------------")
print("EI     |  3  |    4    |  6")
print("EO     |  4  |    5    |  7")
print("EQ     |  3  |    4    |  6")
print("ILF    |  7  |   10    | 15")
print("EIF    |  5  |    7    | 10")
print("-------------------------------------------------")

weights = {
    "EI": {"low": 3, "average": 4, "high": 6},
    "EO": {"low": 4, "average": 5, "high": 7},
    "EQ": {"low": 3, "average": 4, "high": 6},
    "ILF": {"low": 7, "average": 10, "high": 15},
    "EIF": {"low": 5, "average": 7, "high": 10}
}

ufp = 0

for component in weights:
    print(f"\nEnter details for {component}")
    count = int(input("Count: "))
    level = input("Complexity (low/average/high): ").lower()
    ufp += count * weights[component][level]

print("\nUnadjusted Function Points (UFP):", ufp)

print("\nRate the following 14 General System Characteristics (0 to 5)")

total_gsc = 0
for i in range(1, 15):
    rating = int(input(f"GSC {i}: "))
    total_gsc += rating

caf = 0.65 + (0.01 * total_gsc)

print("\nComplexity Adjustment Factor (CAF):", round(caf, 2))

fp = ufp * caf

print("\nFinal Function Points (FP):", round(fp, 2))

print("\n============= DONE =============")
