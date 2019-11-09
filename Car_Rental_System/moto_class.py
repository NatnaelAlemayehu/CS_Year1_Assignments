import sys
from vehicle_class import Vehicle
import car_class
import mainapplication


class Moto(Vehicle):
    def __init__(self, moto_model, year_of_realease, acquisition_year, money_generated, plate_number, rent_times, motohelmet):
        super().__init__(moto_model, year_of_realease, acquisition_year,
                         money_generated, plate_number, rent_times)
        self.motohelmet = motohelmet

    def carbonemissionmoto(self):
        return str((int(self.acquisition_year) - int(self.year_of_realease))*10000*2*9) + " gram of co2 realeased"


moto1 = Moto("Camry", "2016", "2018", "0",  "A345678",  "0", "2")
moto2 = Moto("Chevrolet",  "2015",
             "2016",  "0",  "A434578",  "0", "3")
moto3 = Moto("Charger",  "2015",  "2019",  "0",  "A343455",  "0", "4")
moto4 = Moto("CR-V",  "2017",  "2017",  "0",  "A567890",  "0", "5")
moto5 = Moto("Volkswagen",  "2016",
             "2018",  "5600",  "A389054",  "0", "6")

moto_list = [moto1, moto2, moto3, moto4, moto5]
added_moto = []
number_of_moto_on_list = 5
new_moto_list_starting_point = 0
omondi_input = ""

def listmoto():
    moto_number = 1
    # iterate through each car object to print its model attribute with for loop
    for moto_item in moto_list:
        print("moto", str(moto_number), moto_item.model)
        moto_number = moto_number + 1
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()


def addmoto():
    global new_moto_list_starting_point
    global number_of_moto_on_list
    model = input("what is your moto model? \n")
    year_of_release = input(
        "what is the release year of the moto? \n").lower()
    acquisition_year = input("what year did you acquire it? \n").lower()
    plate_number = input(
        "What is the plate number of this moto? \n").lower()
    rent_times = input('''If you have rented this car before, how many times 
            have you rented it so far? (If you haven't rented it type in 0) \n''').lower()
    money_generated = input(
        "How much money have you made from the moto yet? (If you haven't started earning type in 0) \n").lower()
    number_of_moto_on_list = number_of_moto_on_list + 1
    helmet_number = input(
        "How many helmets does the moto have").lower()

    # create car instance / object name dynamically by concatenation
    new_moto_name = "moto" + str(number_of_moto_on_list)
    added_moto.append(new_moto_name)
    added_moto[new_moto_list_starting_point] = Moto(
        model, year_of_release, acquisition_year, plate_number, rent_times, money_generated, helmet_number)
    moto_list.append(added_moto[new_moto_list_starting_point])
    new_moto_list_starting_point += 1
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()


def removemoto():
    moto_number = 1
    # iterate through each car object to print its model attribute with for loop
    for moto_item in moto_list:
        print("Press", str(moto_number), "to remove", moto_item.model)
        moto_number = moto_number + 1
    moto_to_remove = input("Which car do you want to remove?\n")
    try:
        moto_to_remove_int = int(moto_to_remove)
    except ValueError:
        print("Integer only allowed")
        mainapplication.menu()
        # validates if the users input for car number is within the available range of cars
    if moto_to_remove_int in range(1, number_of_moto_on_list + 1):
            # del deletes the selected item
        moto_list.remove(moto_list[moto_to_remove_int - 1])
    else:
        print("Invalid selection")
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()


def renttimesmoto():

    view_or_update_selection = input('''Type in 1 to view how many times you have rented your moto\n Type 2 to 
        update the number of times that it has been in business\n''')
    if view_or_update_selection == "1":
        moto_number = 1
        for moto_item in moto_list:
            print("car", str(moto_number), "-", moto_item.model,
                  "has been rented", moto_item.rent_times, "times.")
            moto_number = moto_number + 1
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()
    elif view_or_update_selection == "2":
        moto_number = 1
        for moto_item in moto_list:
            print("press", str(moto_number),
                  "to update rent times for", moto_item.model)
            moto_number = moto_number + 1
        moto_selection_to_update = input(
            "Select the moto you want to update:\n")
        try:
            moto_selection_to_update = int(moto_selection_to_update)
        except ValueError:
            print("Integer only allowed")
        mainapplication.menu()
        moto_to_update_rent_times = int(moto_selection_to_update) - 1
        rent_times = input("how many times have you rented this moto \n")
        moto_list[moto_to_update_rent_times].rent_times = rent_times
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()


def revenuemoto():
    userchoice = input("If you want to see your revenue please type in 1 if you want to update" +
                       "\nIf you want to update revenue from a moto press 2 \n")
    if userchoice == "1":
        for moto_item in moto_list:
            print("You have rented your", moto_item.model, moto_item.rent_times,
                  "times", "and generated revenue of USD", moto_item.money_generated)
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()
    elif userchoice == "2":
        moto_number = 1
        # iterate through each car object to print its model attribute with for loop
        for moto_item in moto_list:
            print("moto", str(moto_number), moto_item.model)
            moto_number = moto_number + 1
        motonumber = input(
            "type in the number for the moto you want to make updates\n")
        revenuegenerated = input("How much is the revenue \n")
        try:
            motonumber_int = int(motonumber)
            revenuegenerated = int(revenuegenerated)
        except ValueError:
            print("number only allowed")
        moto_list[motonumber_int - 1].revenue_from_moto(revenuegenerated)
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()


def motohelemet():
    userchoice = input("If you want to see your moto helmets please type in 1" +
                       "\nIf you want to update the number of moto helmet type in 2 \n")
    if userchoice == "1":
        moto_number = 1
        # iterate through each car object to print its model attribute with for loop
        for moto_item in moto_list:
            print(moto_item.model, "has",
                  moto_item.motohelmet, "helmet/s")
            moto_number = moto_number + 1
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()

    elif userchoice == "2":
        moto_number = 1
        # iterate through each car object to print its model attribute with for loop
        for moto_item in moto_list:
            print("press", moto_number, "to update",
                  moto_item.model, "helemt number")
            moto_number = moto_number + 1
        motonumber = input(
            "type in the number for the moto you want to make updates\n")
        helemtnumber = input("How many helemts does this moto have ?\n")
        try:
            motonumber_int = int(motonumber)
            helemtnumber = int(helemtnumber)
        except ValueError:
            print("number only allowed")
        moto_list[motonumber_int - 1].motohelmet = helemtnumber
        proceed = input("Do you want to do another operation?" +
                        " If so type in yes if not type in any character \n").lower()
        if proceed == 'yes':
            mainapplication.menu()
        else:
            sys.exit()


def carbonfootprintmoto():
    moto_number = 1
    # iterate through each car object to print its model attribute with for loop
    for moto_item in moto_list:
        print(moto_item.model, "has a carbon foot print of",
              moto_item.carbonemissionmoto())
        moto_number = moto_number + 1
    proceed = input("Do you want to do another operation?" +
                    " If so type in yes if not type in any character \n").lower()
    if proceed == 'yes':
        mainapplication.menu()
    else:
        sys.exit()
