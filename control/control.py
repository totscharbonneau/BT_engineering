import bpy

class Control:
    _api = None
    _currentState = "INIT"
    _currentSecondaryState = None
    _distanceTLINE = 0
    _lineFollowerData = None
    _distanceCapteur = -1

    def __init__(self, api):
        self._api = api


    def control(self):
        bpy.context.scene.frame_end = 500
        for i in range(0,500):
            self._lineFollowerData = self._api.lineFollower.read_digital()
            # self._distanceCapteur = self._api.ultrasonicAvoidance.get_distance()
            self.runState()
            self._currentState, self._currentSecondaryState = self.switchState()
            bpy.context.scene.frame_set(i)
            self._api.move()
            if self._currentState == "STOP":
                break
        print("done")
    
    def runState(self):
        match self._currentState:
            case "FOLLOWLINE":
                self._api.backWheels.speed(10)
                match self._lineFollowerData:
                    case [0,0,0,0,0]:
                        None
                    case [1,0,0,0,0]:
                        self._api.frontWheels.wanted_angle += -5
                    case [1,1,0,0,0]:
                        self._api.frontWheels.wanted_angle += -3
                    case [0,1,0,0,0]:
                        self._api.frontWheels.wanted_angle += -1
                    case [0, 1, 1, 0, 0]:
                        self._api.frontWheels.wanted_angle = self._api.frontWheels.wanted_angle*0.75 
                    case [0, 0, 1, 0, 0]:
                        None
                    case [0, 0, 1, 1, 0]:
                        self._api.frontWheels.wanted_angle = self._api.frontWheels.wanted_angle*0.75  
                    case [0, 0, 0, 1, 0]:
                        self._api.frontWheels.wanted_angle += 1
                    case [0, 0, 0, 1, 1]:
                        self._api.frontWheels.wanted_angle += 3
                    case [0, 0, 0, 0, 1]:
                        self._api.frontWheels.wanted_angle += 5
                    case _:
                        print("unexpected line sensor reading")
            case "OBSTACLE":
                match self._currentSecondaryState:
                    case "INIT":
                        None
                    case "APPROCHE":
                        self._api.backWheels.speed(self._api.backWheels.getCurrentSpeed()*(1/(self._distanceCapteur-3))) 
                    case "STOP":
                        self._api.backWheels.stop()
            case "INIT":
                None
                # Add code for the INIT state
            case "STOP":
                None
                # Add code for the STOP state
            case "TEST":
                self._api.backWheels.speed(10)
                if bpy.context.scene.frame_current == 10:
                    self._api.frontWheels.wanted_angle = 15
            case "TLINE":
                match self._currentSecondaryState:
                    case "INIT":
                        self._api.frontWheels.wanted_angle = 0
                        self._api.backWheels.stop()
                        self._api.backWheels.backward()
                        self._distanceTLINE = 0
                    case "BACKING":
                        self._api.backWheels.speed(10)
                        self._distanceTLINE += self._api.backWheels.getCurrentSpeed()*1/100/24
                    case "END":
                        self._api.backWheels.stop()
                        self._distanceTLINE = 0
                    case _:
                        print("Invalid secondary state")
            case _:
                print("Invalid state")

    def switchState(self):
        match self._currentState:
            case "FOLLOWLINE":
                if self._lineFollowerData == [1,1,1,1,1] or self._lineFollowerData == [1,1,1,1,0] or self._lineFollowerData == [0,1,1,1,1]:
                    return "TLINE", "INIT"
                elif self._distanceCapteur != -1:
                    return "OBSTACLE", "INIT"
                else:
                    return self._currentState, None
            case "OBSTACLE":
                match self._currentSecondaryState:
                    case "INIT":
                        return "OBSTACLE" , "APROCHE"
                    case "APPROCHE":
                        if self._distanceCapteur <= 3:
                            return "OBSTACLE", "STOP"
                        else:
                            return "OBSTACLE", "APPROCHE"
                    case "STOP":
                        return "STOP", None
                    case _:
                        print("Invalid secondary state")
            case "INIT":
                if bpy.context.scene.frame_current == 10:
                    return "FOLLOWLINE", None
                else:
                    return self._currentState, None
            case "STOP":
                    return "STOP", None
            case "TEST":
                return self._currentState, None
            case "TLINE":
                match self._currentSecondaryState:
                    case "INIT":
                        return "TLINE", "BACKING"
                    case "BACKING":
                        if self._distanceTLINE <= 0.30:
                            return "TLINE", "BACKING"
                        else:
                            return "TLINE", "END"
                    case "END":
                        return "STOP", None
                    case _:
                        print("Invalid secondary state")
            case _:
                print(self._currentState)
                print("Invalid state")