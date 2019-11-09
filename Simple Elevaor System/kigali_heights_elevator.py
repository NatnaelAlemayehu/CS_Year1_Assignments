from Kigali_heights_elevator_class import Elevator
import time
import sys

#Test methods and results
# Test 1: if the user inputs their current floor and their destination floor as the same. 
# The elevator comes to the users
# current floor but then the program quits after saying elevator is now going to your destination
# Test 2: the elevator doesn't accept a floor number that is outside of the buildings floor range
# Test 3: the elevator shows its floor in each floor it goeas through and displays the door status when open and closed
# Test 4: the elevator is designed to stop wherever the last user has dropped off. It won't go back to its beginning floor.
# using the elevator status method it updates its current floor each time a user uses it.
# Test 5: the elevator is adjustable to any size of building floor large medium or small. It works very well.


kh_elevator = Elevator(7, -1, 1, "closed")
user_current_floor_input = ""
user_destination_floor_input = ""

def main():
    global user_current_floor_input
    global user_destination_floor_input
    print("\n")
    print("Welcome to Kigali Heights Elevator system.")
    print("The elevator is now", kh_elevator.elevator_door_status, 
          "and is on floor", kh_elevator.current_position)
    user_current_floor_input = input("What floor are you on currently? Press only numbers. \n")
    try:
        user_current_floor_input_int = int(user_current_floor_input)
    except ValueError:
        print("Numbers only allowed.")
        main()
    user_destination_floor_input = input("What floor do you want to go to? Press only numbers. \n")
    try:
        user_destination_floor_input_int = int(user_destination_floor_input)
    except ValueError:
        print("Numbers only allowed.")
        main()    
    # checks if user current and destination floor is within the allowed range of floors for the elevator object
    if user_destination_floor_input_int and user_current_floor_input_int in range(kh_elevator.min_floor, 
                                                                                  kh_elevator.max_floor + 1):        
        #if block when the users is standing on a floor above the elevators position
        if user_current_floor_input_int > kh_elevator.current_position:
            print("elevator is going up!")
            # gives a delay of 1 sec in execuation and thus creates effect of slow movement as an elevator
            time.sleep(1)
            #loop prints each floor number 
            for floors in range(kh_elevator.current_position, user_current_floor_input_int + 1):
                print("Elevator is now on floor", floors)
                time.sleep(1)
                kh_elevator.elevator_position(floors)
                if floors == user_current_floor_input_int:
                    print("Elevator has reached")
                    kh_elevator.open_elevator()
                    time.sleep(2)
                    print("Elevator is now open. Please get in.")
                    time.sleep(2)
                    kh_elevator.close_elevator()
                    print("Elevator is now closed.")
                    time.sleep(1)
            print("Elevator is now going to your destination")
            #if block when the user is standing below the elevator floor position
            if kh_elevator.current_position < user_destination_floor_input_int:
                print("Elevator going up")
                #for loop prints each floor number
                for floors in range(kh_elevator.current_position, user_destination_floor_input_int + 1):                    
                    print("Elevator is now on floor", floors)
                    time.sleep(1)
                    kh_elevator.elevator_position(floors)
                    if floors == user_destination_floor_input_int:
                        print("You have arrived at your destination")
                        kh_elevator.open_elevator()
                        time.sleep(1)
                        print("Thank you for using Kigali Heights Elevator system.")
                        kh_elevator.close_elevator()
                        proceed = input("Input yes if you want to continue using the elevator or" +
                                        " press any other character to exit. \n").lower()
                        if proceed == 'yes':
                            main()
                        else:
                            sys.exit()
            # if block when the elevators position is above the users desitination floor
            elif kh_elevator.current_position > user_destination_floor_input_int:
                print("Elevator going down")
                #for loop prints each floor number
                for floors in range((kh_elevator.current_position - user_destination_floor_input_int) + 1):                    
                    print("Elevator is now on floor", kh_elevator.current_position)
                    time.sleep(1)
                    kh_elevator.elevator_position(kh_elevator.current_position - 1)
                if kh_elevator.current_position + 1 == user_destination_floor_input_int:
                    print("You have arrived at your destination")
                    kh_elevator.open_elevator()
                    time.sleep(1)
                    print("Thank you for using Kigali Heights Elevator system.")
                    kh_elevator.close_elevator()
                    proceed = input("Input yes if you want to continue using the elevator or" + 
                        " press any other character to exit. \n").lower()
                    if proceed == 'yes':
                        main()
                    else:
                        sys.exit()
        # if block when the users position is below the elvators position (floor)
        elif user_current_floor_input_int < kh_elevator.current_position:
            print("elevator is going down!")
            time.sleep(1)
            for floors in range(kh_elevator.current_position - user_current_floor_input_int):
                print("Elevator is now on floor", kh_elevator.current_position)
                time.sleep(1)
                kh_elevator.elevator_position(kh_elevator.current_position - 1)
                if kh_elevator.current_position == user_current_floor_input_int:
                    print("Elevator has reached")
                    kh_elevator.open_elevator()
                    time.sleep(2)
                    print("Elevator is now open. Please get in.")
                    time.sleep(2)
                    kh_elevator.close_elevator()
                    print("Elevator is now closed.")
                    time.sleep(1)
            print("Elevator is now going to your destination")
            #if block when the elevator position is below the user's destiantion floor
            if kh_elevator.current_position < user_destination_floor_input_int:
                print("Elevator going up!")
                for floors in range(kh_elevator.current_position, user_destination_floor_input_int + 1):
                    print("Elevator is now on floor", floors)
                    time.sleep(1)
                    kh_elevator.elevator_position(floors)
                    if floors == user_destination_floor_input_int:
                        print("You have arrived at your destination")
                        kh_elevator.open_elevator()
                        time.sleep(1)
                        print("Thank you for using Kigali Heights Elevator system.")
                        kh_elevator.close_elevator()
                        proceed = input("Input yes if you want to continue using the elevator or" + 
                        " press any other character to exit. \n").lower()
                        if proceed == 'yes':
                            main()
                        else:
                            sys.exit()
            #if block when the users current position is greater than the desitination floor
            elif kh_elevator.current_position > user_destination_floor_input_int:
                print("Elevator going down")
                for floors in range((kh_elevator.current_position - user_destination_floor_input_int) + 1):
                    print("Elevator is now on floor", kh_elevator.current_position)
                    time.sleep(1)
                    kh_elevator.elevator_position(
                        kh_elevator.current_position - 1)
                if kh_elevator.current_position + 1 == user_destination_floor_input_int:
                    print("You have arrived at your destination")
                    kh_elevator.open_elevator()
                    time.sleep(1)
                    print("Thank you for using Kigali Heights Elevator system.")
                    kh_elevator.close_elevator()
                    proceed = input("Input yes if you want to continue using the elevator or" +
                                    " press any other character to exit. \n").lower()
                    if proceed == 'yes':
                        main()
                    else:
                        sys.exit()
            #if block when the users floor is the same as the elevators position
        elif user_current_floor_input_int == kh_elevator.current_position:
            print("Elevator has arrived.")
            print("Elevator is now open. Please get in.")
            time.sleep(2)
            print("Elevator is now closed.")
            if kh_elevator.current_position < user_destination_floor_input_int:
            #for loop prints each floor number
                print("Elevator going up")
                for floors in range(kh_elevator.current_position, user_destination_floor_input_int + 1):                    
                    print("Elevator is now on floor", floors)
                    time.sleep(1)
                    kh_elevator.elevator_position(floors)
                    if floors == user_destination_floor_input_int:
                        print("You have arrived at your destination")
                        kh_elevator.open_elevator()
                        time.sleep(1)
                        print("Thank you for using Kigali Heights Elevator system.")
                        kh_elevator.close_elevator()
                        proceed = input("Input yes if you want to continue using the elevator or" +
                                        " press any other character to exit. \n").lower()
                        if proceed == 'yes':
                            main()
                        else:
                            sys.exit()
            #if block when the elevators position is greater than the user destination floor
            elif kh_elevator.current_position > user_destination_floor_input_int:
                print("Elevator going down")
                #for loop prints each floor number
                for floors in range((kh_elevator.current_position - user_destination_floor_input_int) + 1):                    
                    print("Elevator is now on floor", kh_elevator.current_position)
                    time.sleep(1)
                    kh_elevator.elevator_position(kh_elevator.current_position - 1)
                if kh_elevator.current_position + 1 == user_destination_floor_input_int:
                    print("You have arrived at your destination")
                    kh_elevator.open_elevator()
                    time.sleep(1)
                    print("Thank you for using Kigali Heights Elevator system.")
                    kh_elevator.close_elevator()
                    proceed = input("Input yes if you want to continue using the elevator or" + 
                        " press any other character to exit. \n").lower()
                    if proceed == 'yes':
                        main()
                    else:
                        sys.exit()
    else: 
        print("Floor number is out of range of floors in the building.")
        main()

main()
