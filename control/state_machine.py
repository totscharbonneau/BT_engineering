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
    _targetAngle = 0
    _targetSpeed = 0

    def __init__(self, api):
        self._api = api
        self._stateActions = StateActions()

    # VERIFIER POUR LES KEYBOARD INTERUPT
    # MECANISME DE VERIFICATION DE FICHIER POUR INTERUPT
    # ALGO DES ETATS ET DES CHOIX DE PROCHAIN ETAT 
    def doStateAction(self, state : State): # ETAT ET SOUS-ETAT 
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

    # INITIAL 
    def loopStateMachine(self):
        stateobj = FollowLine(False, False)
        for i in range(NUMBEROFCYCLES):
            print([i, stateobj]) # debug
            stateobj = StateMachine.doStateAction(self=self, state=stateobj) # passe l'état actuel et retourne l'état future
            self.adjustAngle()  # angle cible
            self.adjustSpeed()  # vitesse cible
            self._api.move() # Pour blender
            self._api.cycleAction(i) # Pour blender
    
    def adjustAngle(self):
        realAngle = self._api.frontWheels.getRealAngle()
        if(self._targetAngle > realAngle+5):
            self._api.frontWheels.wanted_angle += 3
            if(self._targetSpeed > 15):
                self._targetSpeed = 15
        elif(self._targetAngle < realAngle-5):
            self._api.frontWheels.wanted_angle -= 3
            if(self._targetSpeed > 15):
                self._targetSpeed = 15
        else:
            self._api.frontWheels.wanted_angle = self._targetAngle
            if(self._targetSpeed > 15):
                self._targetSpeed = 15

    # TROUVER EN MILI SEC LA DUREE DE CHAQUE CYCLE 
    # LIBRAIRIE PYTHON IMPORT TIME 
    def adjustSpeed(self): # AJOUTER L'ACCELERATION ICI 
        realSpeed = self._api.backWheels.getCurrentSpeed()
        if(self._targetSpeed > realSpeed):
            self._api.backWheels.speed(realSpeed+1) # RATE A LEQUEL LA VITESSE CHANGE 
        elif(self._targetSpeed < realSpeed):
            self._api.backWheels.speed(realSpeed-2)