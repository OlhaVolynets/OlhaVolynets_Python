
def zero_fuel(distance, milles_per_gallon, car_gallons):
    calc_milles = car_gallons * milles_per_gallon
    if calc_milles >= distance:
        return True
    else:
        return False

print(zero_fuel(50, 25, 2))