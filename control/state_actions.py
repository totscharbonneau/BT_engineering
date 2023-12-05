with open("control/line_follower_state_machine.py") as f:
    code = f.read()
    exec(code)

class StateActions:
    lineFollowerState = RightAhead([0,0,1,0,0])
    lastLineFollowerState = RightAhead([0,0,1,0,0])
    lineFollowerSubState = ['NORMAL', 0]
    goAroundState = ['TURN_LEFT', 0]
    finalbackwardState = ['SKIP_T', 0]
    tStopState = ['SKIP_T', 0]
    finalStopState = ['SKIP_T', 0]
    

    def __init__(self):
        lineFollowerState = RightAhead([0,0,1,0,0])

    def lineFollowerAction(self, isFirst=False):
        if(isFirst):
            self._stateActions.lineFollowerSubState[1] = 0
        self._stateActions.lastLineFollowerState = self._stateActions.lineFollowerState
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
        if((self._stateActions.lastLineFollowerState != self._stateActions.lineFollowerState) & self._stateActions.lastLineFollowerState = VeryStrongRight):
            self._stateActions.lineFollowerSubState = ['TURN_RIGHT', 0]
        elif((self._stateActions.lastLineFollowerState != self._stateActions.lineFollowerState) & self._stateActions.lastLineFollowerState = VeryStrongLeft):
            self._stateActions.lineFollowerSubState = ['TURN_LEFT', 0]
        if(self._stateActions.lineFollowerSubState[0] == 'TURN_LEFT'):
            self._targetAngle = 45
            if(self._stateActions.lineFollowerSubState[1] = 20 | self._stateActions.lineFollowerState = RightAhead):
                self._stateActions.lineFollowerSubState[0] = 'NORMAL'
                self._stateActions.lineFollowerSubState[1] = 0 
            self._stateActions.lineFollowerSubState[1] += 1
        elif(self._stateActions.lineFollowerSubState[0] == 'TURN_RIGHT'):
            self._targetAngle = 135
            if(self._stateActions.lineFollowerSubState[1] = 20 | self._stateActions.lineFollowerState = RightAhead):
                self._stateActions.lineFollowerSubState[0] = 'NORMAL'
                self._stateActions.lineFollowerSubState[1] = 0 
            self._stateActions.lineFollowerSubState[1] += 1
        distance = self._api.ultrasonicAvoidance.get_distance()
        if((distance < 20) & (distance >= 0)):
            obstacle = True
        else:
            obstacle = False
        if(self._stateActions.lineFollowerState == None):
            self._stateActions.lineFollowerState = RightAhead([0,0,1,0,0])
            finalT = True
        else:
            finalT = False
        return obstacle, finalT

    def stopAction(self):
        self._forward = True
        self._targetSpeed = 25
        if(self._api.ultrasonicAvoidance.less_than(10.5) == 1):
            self._targetSpeed = 0
            stopped = True
        else:
            stopped = False
        return stopped

    def backwardAction(self):
        self._backward = True
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
        self._forward = True
        self._targetSpeed = 60
        done = False
        if(self._stateActions.goAroundState[0] == 'TURN_LEFT'):
            self._targetAngle = 65 # 65
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 67):
                self._stateActions.goAroundState[0] = 'RIGHT_AHEAD'
                self._stateActions.goAroundState[1] = 0
        elif(self._stateActions.goAroundState[0] == 'RIGHT_AHEAD'):
            self._targetAngle = 90 #90
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 50): #50
                self._stateActions.goAroundState[0] = 'TURN_RIGHT'
                self._stateActions.goAroundState[1] = 0
        elif(self._stateActions.goAroundState[0] == 'TURN_RIGHT'):
            self._targetAngle = 115 #115
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 5):
                self._stateActions.goAroundState[0] = 'TURN_LEFT'
                self._stateActions.goAroundState[1] = 0
                done = True
        return done
        
    def tStop(self):
        #print((self._stateActions.tStopState, self._stateActions.lineFollowerState))
        if(TEST):
            self._targetSpeed = 45
            if(self._stateActions.tStopState[0] == 'SKIP_T'):
                stopped = False
                self._stateActions.tStopState[1] += 1
                if(self._stateActions.tStopState[1] == 30):
                    self._stateActions.tStopState[0] = 'SEARCH_T'
                    self._stateActions.tStopState[1] = 0
            elif(self._stateActions.tStopState[0] == 'SEARCH_T'):
                self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
                if(self._stateActions.lineFollowerState == None):
                    self._stateActions.lineFollowerState = RightAhead([0,0,1,0,0])
                    stopped = True
                    self._forward = True
                    self._targetSpeed = 0
                    self._stateActions.tStopState[0] = 'SKIP_T'
                    self._stateActions.tStopState[1] = 0
                else:
                    stopped = False
        else:
            self._forward = True
            self._targetSpeed = 0
            self._targetAngle = 90
            stopped = True
        return stopped, TEST

    def finalBackward(self):
        #print((self._stateActions.finalbackwardState, self._stateActions.lineFollowerState))
        self._backward = True
        if(self._stateActions.finalbackwardState[0] == 'SKIP_T'):
            done = False
            self._stateActions.finalbackwardState[1] += 1
            if(self._stateActions.finalbackwardState[1] == 30):
                self._stateActions.finalbackwardState[0] = 'SEARCH_T'
                self._stateActions.finalbackwardState[1] = 0
        elif(self._stateActions.finalbackwardState[0] == 'SEARCH_T'):
            self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
            if(self._stateActions.lineFollowerState == None):
                self._stateActions.lineFollowerState = RightAhead([0,0,1,0,0])
                done = True
                self._stateActions.finalbackwardState[0] = 'SKIP_T'
                self._stateActions.finalbackwardState[1] = 0
            else:
                done = False
        self._targetSpeed = 30
        self._targetAngle = 90
        return done

    def finalStop(self):
        #print((self._stateActions.finalStopState, self._stateActions.lineFollowerState))
        self._forward = True
        self._targetSpeed = 45
        stopped = False
        if(self._stateActions.finalStopState[0] == 'SKIP_T'):
            self._stateActions.finalStopState[1] += 1
            if(self._stateActions.finalStopState[1] == 30):
                self._stateActions.finalStopState[0] = 'SEARCH_T'
                self._stateActions.finalStopState[1] = 0
        elif(self._stateActions.finalStopState[0] == 'SEARCH_T'):
            self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
            if(self._stateActions.lineFollowerState == None):
                self._stateActions.lineFollowerState = RightAhead([0,0,1,0,0])
                self._stateActions.finalStopState[0] = 'SKIP_T2'
                self._stateActions.finalStopState[1] = 0
        elif(self._stateActions.finalStopState[0] == 'SKIP_T2'):
            self._stateActions.finalStopState[1] += 1
            if(self._stateActions.finalStopState[1] == 30):
                self._stateActions.finalStopState[0] = 'FINAL_LINE'
                self._stateActions.finalStopState[1] = 0
        elif(self._stateActions.finalStopState[0] == 'FINAL_LINE'):
            self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
            if(self._stateActions.lineFollowerState == None):
                self._stateActions.lineFollowerState = RightAhead([0,0,1,0,0])
                stopped = True
                self._stateActions.finalStopState[0] = 'SKIP_T'
                self._stateActions.finalStopState[1] = 0
        self._targetAngle = 90
        return stopped

    def goBehind(self):
            self._backward = True
            self._targetSpeed = 35
            done = False
            if(done == False):
                self._targetAngle = 0
                self._stateActions.goAroundState[1] += 1
                if(self._stateActions.goAroundState[1] == 150):
                    self._targetSpeed = 0
                    self._stateActions.goAroundState[1] = 0
                    done = True
            return done