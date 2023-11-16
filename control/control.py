import bpy

class Control:
    _api = None
    _currentState = "INIT"
    _lineFollowerData = None

    def __init__(self, api):
        self._api = api


    def control(self):
        for i in range(0,250):
            self._lineFollowerData = self._api.lineFollower.read_digital()
            self.runState()
            self._currentState = self.switchState()
            bpy.context.scene.frame_set(i)
            self._api.move()
    
    def runState(self):
        match self._currentState:
            case "FOLLOWLINE":
                self._api.backWheels.speed(10)
                match self._lineFollowerData:
                    case [0,0,0,0,0]:
                        None
                    case [1,0,0,0,0]:
                        self._api.frontWheels.__wanted_angle += -5
                    case [1,1,0,0,0]:
                        self._api.frontWheels.__wanted_angle += -3
                    case [0,1,0,0,0]:
                        self._api.frontWheels.__wanted_angle += -1
                    case [0, 1, 1, 0, 0]:
                        self._api.frontWheels.__wanted_angle = self._api.frontWheels.__wanted_angle*0.75 
                    case [0, 0, 1, 0, 0]:
                        None
                    case [0, 0, 1, 1, 0]:
                        self._api.frontWheels.__wanted_angle = self._api.frontWheels.__wanted_angle*0.75  
                    case [0, 0, 0, 1, 0]:
                        self._api.frontWheels.__wanted_angle += 1
                    case [0, 0, 0, 1, 1]:
                        self._api.frontWheels.__wanted_angle += 3
                    case [0, 0, 0, 0, 1]:
                        self._api.frontWheels.__wanted_angle += 5
                    case _:
                        print("unexpected line sensor reading")
            case "OBSTACLE":
                print("State = OBSTACLE")
                # Add code for the OBSTACLE state
            case "INIT":
                None
                # Add code for the INIT state
            case "STOP":
                print("State = STOP")
                # Add code for the STOP state
            case "TEST":
                self._api.backWheels.speed(10)
                if bpy.context.scene.frame_current == 10:
                    self._api.frontWheels.__wanted_angle = 15

            case _:
                print("Invalid state")

    def switchState(self):
        match self._currentState:
            case "FOLLOWLINE":
                return self._currentState
            case "OBSTACLE":
                print("State = OBSTACLE")
                # Add code for the OBSTACLE state
            case "INIT":
                if bpy.context.scene.frame_current == 10:
                    return "FOLLOWLINE"
                else:
                    return self._currentState
            case "STOP":
                None
                # Add code for the STOP state
            case "TEST":
                return self._currentState
            case _:
                print(self._currentState)
                print("Invalid state")