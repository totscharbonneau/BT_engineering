with open("control/line_follower_state_machine.py") as f:
    code = f.read()
    exec(code)

class StateActions:
    lineFollowerState = RightAhead([0,0,1,0,0])
    goAroundState = ['TURN_LEFT', 0]
    

    def __init__(self):
        lineFollowerState = RightAhead([0,0,1,0,0])

    def lineFollowerAction(self):
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
        self._api.backWheels.forward()
        self._targetSpeed = 50
        distance = self._api.ultrasonicAvoidance.get_distance()
        if((distance < 20) & (distance >= 0)):
            obstacle = True
        else:
            obstacle = False
        if(self._stateActions.lineFollowerState == None):
            finalT = True
        else:
            finalT = False
        return obstacle, finalT

    def stopAction(self):
        self._api.backWheels.forward()
        self._targetSpeed = 25
        if(self._api.ultrasonicAvoidance.less_than(10.5) == 1):
            self._targetSpeed = 0
            stopped = True
        else:
            stopped = False
        return stopped

    def backwardAction(self):
        self._api.backWheels.backward()
        distance = self._api.ultrasonicAvoidance.get_distance()
        done = False
        if(distance < 20):
            self._targetSpeed = 50
        elif(distance < 25):
            self._targetSpeed = 25
        else:
            done = True
        return done

    def goAroundAction(self):
        self._api.backWheels.forward()
        self._targetSpeed = 80
        done = False
        if(self._stateActions.goAroundState[0] == 'TURN_LEFT'):
            self._targetAngle = 65
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 30):
                self._stateActions.goAroundState[0] = 'RIGHT_AHEAD'
                self._stateActions.goAroundState[1] = 0
        elif(self._stateActions.goAroundState[0] == 'RIGHT_AHEAD'):
            self._targetAngle = 90
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 70):
                self._stateActions.goAroundState[0] = 'TURN_RIGHT'
                self._stateActions.goAroundState[1] = 0
        elif(self._stateActions.goAroundState[0] == 'TURN_RIGHT'):
            self._targetAngle = 105
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 60):
                self._stateActions.goAroundState[0] = 'TURN_LEFT'
                self._stateActions.goAroundState[1] = 0
                done = True
        return done
        
    def tStop(self):
        self._api.backWheels.forward()
        self._targetSpeed = 0
        stopped = True
        test = TEST
        return stopped, test

    def finalBackward(self):
        self._api.backWheels.backward()
        self._targetSpeed = 30
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
        if(self._stateActions.lineFollowerState == None):
            done = True
        else:
            done = False
        return done

    def finalStop(self):
        self._api.backWheels.forward()
        self._targetSpeed = 0
        stopped = True
        return stopped