import time

def estimated_population(population_number, olds):
    year = 2022
    population = 7850000000
    years_later = 0
    while population < population_number:
        olds = olds + 1
        if population_number > 8000000000:
            time.sleep(0.3)
        else:
            time.sleep(1)
        year += 1
        population = population * 1.01
        print("In " + str(year) + ", the world population will be " + str(population) + "and you will be " + str(olds) + " years old.")
    years_later = year - 2022
    print("After " + str(years_later) + " years " + ", the world population will be " + str(population_number))
    

def estimated_year(year_estimated, olds):
    year = 2022
    population = 7850000000
    inhabitants = 0
    while year < year_estimated:
        olds += 1
        if year_estimated > 2035:
            time.sleep(0.3)
        else:
            time.sleep(1)
        year += 1
        population = population * 1.01
        print("In " + str(year) + ", the world population will be " + str(population) + " and you will be " + str(olds) + " years old. ")
    inhabitants = population - 7850000000
    print("There are more people with: " + str(inhabitants))

print("Welcome to estimated population per year.")
print("If you want to know how many people will be on earth based on the chosen year, press 'y'. \nIf you want to find out in which year the population written by you will be, press 'p'")
choose = input()
if choose == 'y':
    yeart = input("Write the year: ")
    old = input("How old are you? ")
    olds = float(old)
    years = float(yeart)
    estimated_year(years, olds)
elif choose == 'p':
    popt = input("Write the population (write only first three numbers if is more than three write four): ")
    old = input("How old are you? ")
    olds = float(old)
    pops = float(popt)
    pop = pops * 10000000
    estimated_population(pop, olds)
    
