def get_input(prompt, input_type=str):
    try:
        return input_type(input(prompt))
    except ValueError:
        print("Invalid input. Please try again.")
        return get_input(prompt, input_type)

def handle_flight():
    print("Okay you're flying.")
    flight_class = input("Please indicate if you will be booking First class, Economy or Business: ").lower()
    luggage = get_input("Please enter your total luggage weight in Kilograms: ", int)
    flyingwhere = input("Will you be flying locally or internationally? ").lower()

    if flyingwhere == "internationally":
        print("I'd recommend flying with Qantas.")
    elif flyingwhere == "locally":
        print("I'd recommend flying with American Airlines.")

    if flight_class == "first class":
        print("There is no additional charge for luggage.")
    elif flight_class == "economy" and luggage >= 50:
        print("There will be a $40.00 surcharge for weights over 50 kg.")
    elif flight_class == "business" and luggage >= 50:
        print("There is a flat rate of $30.00 surcharge for business class.")

def handle_drive():
    print("Okay, a road trip then.")
    drivingwhere = input("Will you be traveling locally or across country? ").lower()
    if drivingwhere == "locally":
        print("Avis is having some great deals on their local rentals.")
    else:
        print("Hertz has great cross country packages.")

def handle_beach():
    print("I'd say head to Florida!")
    beach_type = input("Do you want popular or remote beaches? ").lower()
    if beach_type == "remote":
        print("Remote beaches are great for couples!")
    elif beach_type == "popular":
        print("Popular beaches are great for friends and family!")
    else:
        print("There are other beaches that you are welcome to explore.")

def handle_city():
    print("I'd recommend visiting Santa Fe. It's a great drive through the mountains.")
    stay_type = input("Would you prefer a Hotel or a Casino Resort? ").lower()
    if stay_type == "hotel":
        print("The La Fonda is really nice this time of year.")
    elif stay_type in ("casino resort", "casino", "resort"):
        print("Buffalo Thunder Casino and Resort is just up the road.")
    else:
        print("Maybe an Airbnb is a better option for you.")

def handle_adventure():
    adventure_type = input("Do you like Rafting or visiting the Pueblos? ").lower()
    if adventure_type == "rafting":
        print("The Rio Grande White Water Rafting Company is a good place to check out.")
    elif adventure_type == "pueblos":
        print("I'd recommend starting with the Tewa Pueblo outside of Santa Fe.")
    else:
        print("Maybe the Albuquerque Cultural Center will spark some ideas.")

def main():
    print("Welcome to Justin's Travel Center")
    enter = get_input("Press 1 to begin or 2 to quit: ", int)

    while enter == 1:
        destination = input("Do you have a place in mind which you would like to visit? Yes or No: ").lower()
        if destination == "yes":
            travel = input("Will you be flying or driving? ").lower()
            if travel == "flying":
                handle_flight()
            elif travel == "driving":
                handle_drive()
            else:
                print("Maybe a cruise or train ride is what you have in mind.")
        elif destination == "no":
            trip_type = input("Okay, what sounds best? Beach/City or Adventure: ").lower()
            if trip_type == "beach":
                handle_beach()
            elif trip_type == "city":
                handle_city()
            elif trip_type == "adventure":
                handle_adventure()
            else:
                print("Perhaps a staycation is a better idea for you.")
        enter = get_input("Press 1 to start again or 2 to quit: ", int)

    print("Thank you for using Justin's Travel Center! Safe travels! ✈️🚗")

if __name__ == "__main__":
    main()
