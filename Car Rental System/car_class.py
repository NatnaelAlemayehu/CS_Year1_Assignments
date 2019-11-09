import sys
from vehicle_class import Vehicle
import moto_class
import mainapplication


class Car(Vehicle):
    def __init__(self, model, year_of_realease, acquisition_year, money_generated, plate_number, rent_times):
        super().__init__(model, year_of_realease, acquisition_year,
                         money_generated, plate_number, rent_times)

    def carbonemissioncar(self):
        return str((int(self.acquisition_year) - int(self.year_of_realease))*12000*15*9) + " gram of co2 realsed"


car1 = Car("Toyota Camry", "2016", "2018", "0",  "A345678",  "0")
car2 = Car("Chevrolet Camaro",  "2015",
           "2016",  "0",  "A434578",  "0")
car3 = Car("Dodge Charger",  "2015",  "2019",  "0",  "A343455",  "0")
car4 = Car("Honda CR-V",  "2017",  "2017",  "0",  "A567890",  "0")
car5 = Car("Volkswagen Beetle",  "2016",
           "2018",  "5600",  "A389054",  "0")

car_list = [car1, car2, car3, car4, car5]
added_car = []
number_of_car_on_list = 5
new_car_list_starting_point = 0
omondi_input = ""



def listcar():
    car_number = 1
    # iterate through each car object to print its model attribute with for loop
    for car_item in car_list:
        print("car", str(car_number), car_item.model)
        car_number = car_number + 1
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()


def addcar():
    global new_car_list_starting_point
    global number_of_car_on_list
    model = input("what is your car model? \n")
    year_of_release = input(
        "what is the release year of the car? \n").lower()
    acquisition_year = input("what year did you acquire it? \n").lower()
    plate_number = input(
        "What is the plate number of this car? \n").lower()
    rent_times = input('''If you have rented this car before, how many times 
            have you rented it so far? (If you haven't rented it type in 0) \n''').lower()
    money_generated = input(
        "How much money have you made from the car yet? (If you haven't started earning type in 0) \n").lower()
    number_of_car_on_list = number_of_car_on_list + 1
    try:
        year_of_release = int(year_of_release)
        acquisition_year = int(acquisition_year)
        rent_times = int(rent_times)
        money_generated = int(money_generated)
    except ValueError:
        print("numbers only allowed \n")
        
    # create car instance / object name dynamically by concatenation
    new_car_name = "car" + str(number_of_car_on_list)
    added_car.append(new_car_name)
    added_car[new_car_list_starting_point] = Car(
        model, year_of_release, acquisition_year, plate_number, rent_times, money_generated)
    car_list.append(added_car[new_car_list_starting_point])
    new_car_list_starting_point += 1
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()


def removecar():
    car_number = 1
    # iterate through each car object to print its model attribute with for loop
    for car_item in car_list:
        print("Press", str(car_number), "to remove", car_item.model)
        car_number = car_number + 1
    car_to_remove = input("Which car do you want to remove?\n")
    try:
        car_to_remove_int = int(car_to_remove)
    except ValueError:
        print("Integer only allowed")
        mainapplication.menu()
        # validates if the users input for car number is within the available range of cars
    if car_to_remove_int in range(1, number_of_car_on_list + 1):
            # del deletes the selected item
        car_list.remove(car_list[car_to_remove_int - 1])
    else:
        print("Invalid selection")
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()


def renttimescar():

    view_or_update_selection = input('''Type in 1 to view how many times you have rented your cars\n Type 2 to 
        update the number of times that it has been in business\n''')
    if view_or_update_selection == "1":
        car_number = 1
        for car_item in car_list:
            print("car", str(car_number), "-", car_item.model,
                  "has been rented", car_item.rent_times, "times.")
            car_number = car_number + 1
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()
    elif view_or_update_selection == "2":
        car_number = 1
        for car_item in car_list:
            print("press", str(car_number),
                  "to update rent times for", car_item.model)
            car_number = car_number + 1
        car_selection_to_update = input(
            "Select the car you want to update:\n")
        try:
            car_selection_to_update = int(car_selection_to_update)
        except ValueError:
            print("Integer only allowed")
        mainapplication.menu()
        car_to_update_rent_times = int(car_selection_to_update) - 1
        rent_times = input("how many times have you rented this car \n")
        car_list[car_to_update_rent_times].rent_times = rent_times
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()


def revenuecar():
    userchoice = input("If you want to see your revenue please type in 1 if you want to update" +
                       "\nIf you want to update revenue from a car press 2 \n")
    if userchoice == "1":
        for car_item in car_list:
            print("You have rented your", car_item.model, car_item.rent_times,
                  "times", "and generated revenue of USD", car_item.money_generated)
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()
    elif userchoice == "2":
        car_number = 1
        # iterate through each car object to print its model attribute with for loop
        for car_item in car_list:
            print("car", str(car_number), car_item.model)
            car_number = car_number + 1
        carnumber = input(
            "type in the number for the car you want to make updates\n")
        revenuegenerated = input("How much is the revenue \n")
        try:
            carnumber_int = int(carnumber)
            revenuegenerated = int(revenuegenerated)
        except ValueError:
            print("number only allowed")
        car_list[carnumber_int - 1].money_generated = revenuegenerated
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()


def carbonfootprintcar():
    car_number = 1
    # iterate through each car object to print its model attribute with for loop
    for car_item in car_list:
        print(car_item.model, "has emitted", car_item.carbonemissioncar(), "while operating for",
              str(int(car_item.acquisition_year) - int(car_item.year_of_realease)), "years")
        car_number = car_number + 1
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()
