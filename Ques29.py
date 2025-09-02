# 29.	Population Growth: Calculate town population growth over 10 years.
initial_population = int(input("Enter initial population: "))
growth_rate = float(input("Enter the growth rate: "))

print("\nyear\tPopulation")

population = initial_population
for year in range(1, 11):
    population += population * (growth_rate/100)
    print(f"{year}\t{int(population)}")