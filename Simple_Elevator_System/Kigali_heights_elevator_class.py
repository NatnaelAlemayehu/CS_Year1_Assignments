class Elevator:
    def __init__(self, max_floor, min_floor, current_position, elevator_door_status):
        self.max_floor = int(max_floor)
        self.min_floor = int(min_floor)
        self.current_position = int(current_position)
        self.elevator_door_status = elevator_door_status
       
    #method to change elevator door status when opened
    def open_elevator(self):
        self.elevator_door_status = "opened"
        return self.elevator_door_status
    #method to change elevator door status when closed
    def close_elevator(self):
        self.elevator_door_status = "closed"
        return self.elevator_door_status
    #method to update elevator current floor position value when going either up or down
    def elevator_position(self, elevator_position):
        self.current_position = int(elevator_position)

