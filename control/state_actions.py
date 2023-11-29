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
    
    def distanceParcourue(distanceTotal, delta_t, puissanceMoteurInitial):
        vitesse = 0.0029*puissanceMoteurInitial - 0.0245
        distanceTotal += delta_t * vitesse
        return distanceTotal

    ##### ACCELERATION #####
    def accelerationInit():
        # initialisation de l'accélération
        tempsDebut = time.time()
        return tempsDebut

    # POUR PICAR
    def accelerationReel(tempsDebut,puissanceMoteurInitial, puissanceCible, distanceTotal):
        accelerationTerminee = False
        tempsFin = time.time()
        delta_t = tempsFin - tempsDebut
        # gestion de la distance total parcourue
        distanceTotal = distanceParcourue(distanceTotal,delta_t,puissanceMoteurInitial)
        # equation linéaire de la puissance moteur en fonction du temps
        ajustementEquation = (puissanceMoteurInitial - 7.4324)/-208.11      # mise en equation, voir Excel
        puissanceMoteur = 208.11*(delta_t + ajustementEquation) + 7.4324    # mise en equation, voir Excel
        #Gestion de risque sur l'intervalle de puissance des moteurs
        if puissanceMoteur > puissanceCible:
            puissanceMoteur = puissanceCible
            accelerationTerminee = True # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if puissanceMoteur > 100 :
            puissanceMoteur = 100
        if puissanceMoteur < 0 :
            puissanceMoteur = 0
        # il sera possible de fournir le tempsFin et la puissanceMoteur pour combler le tempsDebut et puissanceMoteurInitial de la prochaine itération
        return tempsFin, puissanceMoteur, accelerationTerminee, distanceTotal
    
    # POUR PICAR
    def decelerationReel(tempsDebut,puissanceMoteurInitial,puissanceCible, distanceTotal):
        accelerationTerminee = False
        tempsFin = time.time()
        delta_t = tempsFin - tempsDebut
        # gestion de la distance total parcourue
        distanceTotal = distanceParcourue(distanceTotal,delta_t,puissanceMoteurInitial)
        # equation linéaire de la puissance moteur en fonction du temps
        ajustementEquation = (puissanceMoteurInitial - 100)/-200        # mise en equation, voir Excel
        puissanceMoteur = -200*(delta_t+ajustementEquation) + 100       # mise en equation, voir Excel
        #Gestion de risque sur l'intervalle de puissance des moteurs
        if puissanceMoteur < puissanceCible:
            puissanceMoteur = puissanceCible
            accelerationTerminee = True # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if puissanceMoteur > 100 :
            puissanceMoteur = 100
        if puissanceMoteur < 0 :
            puissanceMoteur = 0
        return tempsFin, puissanceMoteur, accelerationTerminee, distanceTotal
    
    # POUR SIMULATION
    def accelerationSimulation(tempsDebut,vitesseInitial, vitesseCible):
        accelerationTerminee = False
        tempsFin = time.time()
        delta_t = tempsFin - tempsDebut
        ajustementEquation = (vitesseInitial - 0.0041)/-0.5704          # mise en equation, voir Excel
        vitesse = 0.5704*(delta_t + ajustementEquation) + 0.004         # mise en equation, voir Excel
        #Gestion de la vitesse maximal
        if vitesse > vitesseCible:
            vitesse = vitesseCible
            accelerationTerminee = True # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if vitesse < 0:
            vitesse = 0
        return tempsFin, vitesse, accelerationTerminee
    
    # POUR SIMULATION
    def decelerationSimulation(tempsDebut,vitesseInitial, vitesseCible):
        accelerationTerminee = False
        tempsFin = time.time()
        delta_t = tempsFin - tempsDebut
        ajustementEquation = (vitesseInitial - 0.2607)/-0.5704          # mise en equation, voir Excel
        vitesse = -0.5704*(delta_t + ajustementEquation) + 0.2607       # mise en equation, voir Excel
        #Gestion de la vitesse maximal
        if vitesse < vitesseCible:
            vitesse = vitesseCible
            accelerationTerminee = True # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if vitesse < 0:
            vitesse = 0
        return tempsFin, vitesse, accelerationTerminee
    ##### FIN ACCELERATION #####

    ##### VIRAGE #####
    def virage(niveauDeVirage, angleVirageInitial=90, ):
        # niveauDeVirage va de -4 à -1 pour un virage a gauche, de 1 à 4 pour un virage a droite et de 0 pour centrer les roues
        if niveauDeVirage == 0:
            angleVirage = 90
        # virage à droite
        if niveauDeVirage == 1:
            angleVirage = angleVirageInitial + 1
        if niveauDeVirage == 2:
            angleVirage = angleVirageInitial + 3
        if niveauDeVirage == 3:
            angleVirage = angleVirageInitial + 6
        if niveauDeVirage == 4:
            angleVirage = angleVirageInitial + 10 

        # virage à gauche
        if niveauDeVirage == 1:
            angleVirage = angleVirageInitial - 1
        if niveauDeVirage == 2:
            angleVirage = angleVirageInitial - 3
        if niveauDeVirage == 3:
            angleVirage = angleVirageInitial - 6
        if niveauDeVirage == 4:
            angleVirage = angleVirageInitial - 10

        # gestion de l'intervalle maximum de virage
        if  angleVirage > 135:
            angleVirage = 135
        if  angleVirage < 45:
            angleVirage = 45 
             

        return angleVirage
    ##### FIN VIRAGE #####

    def calculDistanceArret(vitesseInitial):
        # permet de calculer à quel distance il faut commencer la deceleration pour atteindre une distance precise
        # a partir de la vitesse maximum selon les équations choisi, il faut 0.45s pour decelerer jusqu'a 0 m/s  
        delta_t = 0.45 - ((vitesseInitial-0.2607)/-0.5704)  # mise en equation, voir Excel
        distanceArret = 0.5*vitesseInitial*delta_t          # equation d'acceleration: x = 1/2(Vx + V0)t
        return distanceArret

