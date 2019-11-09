import moto_class
import car_class 
import sys

omondi_input_start = ""

# Test 1: After a user has remove all available cars, if he/she continues to remove a car it 
# throws out an error saying "invalid literal for int() with base 10: 'ty'"

# Test 2: when adding a car user can input a number only as the name of the car and 
# car write a string when asked for the realase year

# Test 3: User can add or remove any car successfully without error except as mentioned on test 1 

# Test 4: User sees all the cars availabl in the list for each service he calls. 
# So of there are lots of cars, it won't look good

# Test 5: since user can inputs the rent times and the revenue made if a user rent 0 times but 
# adds revenue

# Test 6: User can get number of helmerts for the motos and also can get the 
# carbon emission of each moto or car

#The Algorithm
#I used a combination of list and dictionary to store car / moto instances as this would allow me to iterate
#or perform other operations quite easily. Moto and car have different list and dictionary so that it is 
#quite easy to manage the list as it grows and perform various tasks on it.

def menu():
    global omondi_input_start
    omondi_input_start = input('''Press 1 to access your moto information.
Press 2 to access your cars information \n''')
    if omondi_input_start == "1":
        omondi_input_moto_info = input('''press 1 to get a list of your motos 
press 2 to add a new moto
press 3 to remove a moto
press 4 to update or view the number of times you have rented your motos
press 5 to find or update the money you made from each moto
press 6 to see or update the number of helemets for your moto
press 7 to get the carbon foot print of each moto
press q to quit \n''')
        if omondi_input_moto_info == "1":
        #calls listcar method from Omondi_function.py
            moto_class.listmoto()
        elif omondi_input_moto_info == "2":
            #calls addcars method from Omondi_function.py
            moto_class.addmoto()
        elif omondi_input_moto_info == "3":
            #calls removecar method from Omondi_function.py
            moto_class.removemoto()
        elif omondi_input_moto_info == "4":
            #calls renttimes method from Omondi_function.py
            moto_class.renttimesmoto()
        elif omondi_input_moto_info == "5":
            #calls revenue method from Omondi_function.py
            moto_class.revenuemoto()
        elif omondi_input_moto_info == "6":
            moto_class.motohelemet()
        elif omondi_input_moto_info == "7":
            moto_class.carbonfootprintmoto()
        else:
            sys.exit()

    elif omondi_input_start == "2":
        omondi_input_car_info = input('''press 1 to get a list of your cars 
press 2 to add a new car 
press 3 to remove a car
press 4 to update or view the number of times you have rented your cars 
press 5 to find or update the money you made from each car
press 6 to get the carbon emission of your cars
press any other key to exit to quit \n''')
        if omondi_input_car_info == "1":
        #calls listcar method from Omondi_function.py
            car_class.listcar()
        elif omondi_input_car_info == "2":
            #calls addcars method from Omondi_function.py
            car_class.addcar()
        elif omondi_input_car_info == "3":
            #calls removecar method from Omondi_function.py
            car_class.removecar()
        elif omondi_input_car_info == "4":
            #calls renttimes method from Omondi_function.py
            car_class.renttimescar()
        elif omondi_input_car_info == "5":
            #calls revenue method from Omondi_function.py
            car_class.revenuecar()
        elif omondi_input_car_info == "6":
            car_class.carbonfootprintcar()           
        else:
            sys.exit()


if __name__ == "__main__":
    print(" ---------------------------------------------- ")
    print("| Welcome Omondi. What do you want to do today?|")
    print(" ---------------------------------------------- ")
    menu()

