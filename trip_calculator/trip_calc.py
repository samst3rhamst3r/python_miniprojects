
def get_user_input(msg, cast_type):
    while True:
        try:
            user_input = cast_type(input(msg))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")
            continue

km_to_drive = get_user_input("Please input number of kilometers to drive: ", float)
ltrs_per_km = get_user_input("What is the ltr/km usage of your car? ", float)
price_per_ltr = get_user_input("What is the current price per liter of fuel? ", float)

trip_cost = km_to_drive * ltrs_per_km * price_per_ltr

print(f"The cost of your trip will be ${trip_cost:.2f}")