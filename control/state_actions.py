with open("control/line_follower_state_machine.py") as f:
    code = f.read()
    exec(code)

import time # Confirmer ou placer le import

# POUR CHAQUE ETAT DECRIT LES ACTIONS A PRENDRE 
class StateActions:
    lineFollowerState = RightAhead([0,0,1,0,0])
    goAroundState = ['TURN_LEFT', 0]
    vitesseMax = 0.2 # déterminer la vitesse maximum du véhicule, v=0.05 permet une décélération sécuritaire sur 1.5cm 

    def __init__(self):
        lineFollowerState = RightAhead([0,0,1,0,0])


    def lineFollowerAction(self):
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState) # Un deuxieme etat dans cet etat pour decrire si il doit aller a gauche fort faible a droite fort failbe ....
        self._api.backWheels.forward()
        self._targetSpeed = 20
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
        self._targetSpeed = 5
        if(self._api.ultrasonicAvoidance.less_than(10.5) == 1):
            #self._api.backWheels.speed(0)
            stopped = True
        else:
            stopped = False
        return stopped

    def backwardAction(self):
        self._api.backWheels.backward()
        distance = self._api.ultrasonicAvoidance.get_distance()
        done = False
        if(distance < 20):
            self._targetSpeed = 20
        elif(distance < 25):
            self._targetSpeed = 5
        else:
            #self._api.backWheels.speed(0)
            done = True
        return done

    def goAroundAction(self):
        self._api.backWheels.forward()
        self._targetSpeed = 25
        done = False
        if(self._stateActions.goAroundState[0] == 'TURN_LEFT'):
            self._targetAngle = -25
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 30):
                self._stateActions.goAroundState[0] = 'RIGHT_AHEAD'
                self._stateActions.goAroundState[1] = 0
        elif(self._stateActions.goAroundState[0] == 'RIGHT_AHEAD'):
            self._targetAngle = 0
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 70):
                self._stateActions.goAroundState[0] = 'TURN_RIGHT'
                self._stateActions.goAroundState[1] = 0
        elif(self._stateActions.goAroundState[0] == 'TURN_RIGHT'):
            self._targetAngle = 15
            self._stateActions.goAroundState[1] += 1
            if(self._stateActions.goAroundState[1] == 60):
                self._stateActions.goAroundState[0] = 'TURN_LEFT'
                self._stateActions.goAroundState[1] = 0
                done = True
        return done
        
    def tStop(self):
        self._api.backWheels.forward()
        #self._api.backWheels.speed(0)
        stopped = True
        test = True
        return stopped, test

    def finalBackward(self):
        self._api.backWheels.backward()
        self._targetSpeed = 10
        self._stateActions.lineFollowerState = doLineFollowerStateAction(self, lineFollowerState=self._stateActions.lineFollowerState)
        if(self._stateActions.lineFollowerState == None):
            #self._api.backWheels.speed(0)
            done = True
        else:
            done = False
        return done

    def finalStop(self):
        self._api.backWheels.forward()
        #self._api.backWheels.speed(0)
        stopped = True
        return stopped
    
    def accelerationInit():
        # initialisation de l'accélération
        tempsDebut = time.time()
        return tempsDebut

    def acceleration(tempsDebut):
        # il faut faire accelerationInit() en premier pour obtenir le tempsDebut
        # déterminer la nouvelle vitesse
        tempsFin = time.time()
        delta_t = tempsFin - tempsDebut
        vitesse = 0.5704*delta_t + 0.0041 # équation de la vitesse en fonction du temps pour une accélération inférieur à 0.65m/s^2
        puissanceMoteur = (vitesse+0.0245)/0.0029 # équation de la puissance des moteurs
        return vitesse, puissanceMoteur

    def deceleration(tempsDebut,vitesseInitial):
        # il faut faire accelerationInit() en premier pour obtenir le tempsDebut
        # déterminer la nouvelle vitesse
        tempsFin = time.time()
        delta_t = tempsFin - tempsDebut
        ajustementEquation = (vitesseInitial - 0.2607)/0.5704
        vitesse = -0.5704*(delta_t+ajustementEquation) + 0.2607 # équation de la vitesse en fonction du temps pour une décélération supérieur à -0.65m/s^2
        puissanceMoteur = (vitesse+0.0245)/0.0029 # équation de la puissance des moteurs
        return vitesse, puissanceMoteur

