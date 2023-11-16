from dataclasses import dataclass

with open("control/state_actions.py") as f:
    code = f.read()
    exec(code)

@dataclass
class FollowLine:
    obstacle: bool
    finalT: bool

@dataclass
class Stop:
    stopped: bool

@dataclass
class Backward:
    done: bool

@dataclass
class GoAround:
    done: bool

@dataclass
class TStop:
    stopped: bool
    isTest: bool

@dataclass
class FinalBackward:
    done: bool

@dataclass
class FinalStop:
    stopped: bool

State = FollowLine | Stop | Backward | GoAround | TStop | FinalBackward | FinalStop

EXIT = None

class StateMachine:
    _api = None
    _stateMachine = None

    def __init__(self, api):
        self._api = api
        self._stateActions = StateActions()

    def doStateAction(self, state : State):
        match state:
            case FollowLine(obstacle, finalT):
                match (obstacle, finalT):
                    case (False, False):
                        nextObstacle, nextFinalT = StateActions.lineFollowerAction(self)
                        return FollowLine(nextObstacle, nextFinalT)
                    case (True, False):
                        nextStopped = StateActions.stopAction(self)
                        return Stop(nextStopped)
                    case ((True | False), True):
                        nextStopped, nextIsTest = StateActions.tStop(self)
                        return TStop(nextStopped, nextIsTest)
            case Stop(stopped):
                match stopped:
                    case False:
                        nextStopped = StateActions.stopAction(self)
                        return Stop(nextStopped)
                    case True:
                        nextDone = StateActions.backwardAction(self)
                        return Backward(nextDone)
            case Backward(done):
                match done:
                    case False:
                        nextDone = StateActions.backwardAction(self)
                        return Backward(nextDone)
                    case True:
                        nextDone = StateActions.goAroundAction(self)
                        return GoAround(nextDone)
            case GoAround(done):
                match done:
                    case False:
                        nextDone = StateActions.goAroundAction(self)
                        return GoAround(nextDone)
                    case True:
                        nextObstacle, nextFinalT = StateActions.lineFollowerAction(self)
                        return FollowLine(nextObstacle, nextFinalT)
            case TStop(stopped, isTest):
                match (stopped, isTest):
                    case (False, (True | False)):
                        nextStopped, nextIsTest = StateActions.tStop(self)
                        return TStop(nextStopped, nextIsTest)
                    case (True, False):
                        return EXIT
                    case (True, True):
                        nextDone = StateActions.finalBackward(self)
                        return FinalBackward(nextDone)
            case FinalBackward(done):
                match (done):
                    case False:
                        nextDone = StateActions.finalBackward(self)
                        return FinalBackward(nextDone)
                    case True:
                        nextStopped = StateActions.finalStop(self)
                        return FinalStop(nextStopped)
            case FinalStop(stopped):
                match stopped:
                    case False:
                        nextStopped = StateActions.finalStop(self)
                        return FinalStop(nextStopped)
                    case True:
                        return EXIT

    def loopStateMachine(self):
        me = self
        stateobj = FollowLine(False, False)
        for i in range(250):
            stateobj = StateMachine.doStateAction(self=me, state=stateobj)
            bpy.context.scene.frame_set(i)
            self._api.move() 