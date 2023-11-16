with open("control/line_follower_state_machine.py") as f:
    code = f.read()
    exec(code)

class StateActions:
    lineFollowerState = RightAhead([0,0,1,0,0])

    def __init__(self):
        lineFollowerState = RightAhead([0,0,1,0,0])

    def lineFollowerAction(self):
        print(self._stateActions.lineFollowerState)
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
        self._api.backWheels.forward()
        self._api.backWheels.speed(10)
        distance = self._api.ultrasonicAvoidance.get_distance()
        print(distance)
        if(distance < 13):
            obstacle = True
        else:
            obstacle = False
        if(self._stateActions.lineFollowerState == None):
            finalT = True
        else:
            finalT = False
        print(obstacle, finalT)
        return obstacle, finalT

    def stopAction(self):
        self._api.backWheels.forward()
        self._api.backWheels.speed(5)
        if(self._api.ultrasonicAvoidance.less_than(10.5) == 1):
            self._api.backWheels.speed(0)
            stopped = True
        else:
            stopped = False
        return stopped

    def backwardAction(self):
        self._api.backWheels.backward()
        self._api.backWheels.speed(8)
        if(self._api.ultrasonicAvoidance.less_than(25) == 0):
            self._api.backWheels.speed(0)
            done = True
        else:
            done = False
        return done

    def goAroundAction(self):
        self._api.backWheels.forward()
        self._api.backWheels.speed(8)
        for i in range(30):
            bpy.context.scene.frame_set(bpy.context.scene.frame_current+1)
            self._api.move()
            self._api.frontWheels.__wanted_angle += -3
        for i in range(60):
            bpy.context.scene.frame_set(bpy.context.scene.frame_current+1)
            self._api.move()
            self._api.frontWheels.__wanted_angle += 3
        while(self._api.lineFollower.read_digital() != [0,0,1,0,0]):
            bpy.context.scene.frame_set(bpy.context.scene.frame_current+1)
            self._api.move()
        done = True
        return done
        
    def tStop(self):
        self._api.backWheels.forward()
        self._api.backWheels.speed(0)
        stopped = True
        test = True
        return stopped, test

    def finalBackward(self):
        self._api.backWheels.backward()
        self._api.backWheels.speed(8)
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
        if(self._stateActions.lineFollowerState == None):
            self._api.backWheels.speed(0)
            done = True
        else:
            done = False
        return done

    def finalStop(self):
        self._api.backWheels.forward()
        self._api.backWheels.speed(0)
        stopped = True
        return stopped