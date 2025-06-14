def hotel_costs(nights):
    return nights * 140

def plane_ride(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    
def rental_car_cost(days):
    if days>=7:
        return days * 40 - 50
    elif days>=3:
        return days *40 - 20
    else:
        return days * 40
    
def trip_cost(city, days, nights, spending_money):
    return rental_car_cost(days) + hotel_costs(nights) + plane_ride(city) + spending_money

print("Total Cost of trip", trip_cost("Pittsburgh", 3, 2, 200))