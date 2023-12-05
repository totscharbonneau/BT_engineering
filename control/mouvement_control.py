with open("control/line_follower_state_machine.py") as f:
    code = f.read()
    exec(code)

import time # Confirmer ou placer le import

class MouvementControl:
    # DECLARATION DES VARIABLES DE CONTROLE
    tempsDerniereAction = 0
    tempsNouvelleAction = 0
    delta_t = 0

    puissanceMoteurPiCar = 0 # speed() 
    puissanceCible = 0
    vitesse = 0

    distanceParcourue = 0       # sera mise en jour en fonction des déplacements effectués
    deplacementTotal = 0        # garde en mémoire le déplacement total du parcours
    distanceArret = 0

    niveauDeVirage = 0
    angleRoue = 90

    acceleration = "null"
    deceleration = "null"
    reculer = "null"
    
    def ajusterVitesse(self, puissanceMoteurCible):
        #acceleration
        self.puissanceCible = puissanceMoteurCible
        if self.puissanceMoteurPiCar < puissanceMoteurCible and (self.acceleration == "null" or self.acceleration == "termine"):
            self.accelerationInit(self)
        elif self.puissanceMoteurPiCar < puissanceMoteurCible and self.acceleration == "en_cours":
            self.accelerationReel(self)
        #deceleration
        elif self.puissanceMoteurPiCar > puissanceMoteurCible and (self.deceleration == "null" or self.acceleration == "termine"):
            self.decelerationInit(self)
        elif self.puissanceMoteurPiCar > puissanceMoteurCible and self.deceleration == "en_cours":
            self.decelerationReel(self)
        return self.puissanceMoteurPiCar

    def ajusterAngle(self, angleCible):  
        deltaAngle = angleCible - self.angleRoue
        if deltaAngle > 0:
            if deltaAngle <= 10:
                self.niveauDeVirage = 1
            elif deltaAngle <= 20:
                self.niveauDeVirage = 2
            elif deltaAngle <= 40:
                self.niveauDeVirage = 3
            else:
                self.niveauDeVirage = 4
        
        if deltaAngle < 0:
            if deltaAngle >= -10:
                self.niveauDeVirage = -1
            elif deltaAngle >= -20:
                self.niveauDeVirage = -2
            elif deltaAngle >= -40:
                self.niveauDeVirage = -3
            else:
                self.niveauDeVirage = -4
        self.virage()
        return self.angleRoue

    def reculerDistantce(self, puissanceMoteurCible, distance): 
        if self.reculer == "null":
            self.puissanceCible = puissanceMoteurCible
            self.reculerDistanceInit()
        if self.reculer == "en_cours":
            if self.distanceParcourue < distance - self.distanceArret:
                puissanceMoteurPiCar = self.ajusterVitesse(self.puissanceCible)
            else: 
                puissanceMoteurPiCar = self.ajusterVitesse(0)
                if self.distanceParcourue >= distance or self.puissanceMoteurPiCar <= 0:
                    self.reculer == "null"
        return puissanceMoteurPiCar
    
    def reculerDistanceInit(self):
        self.acceleration = "null"
        self.deceleration = "null"
        self.reculer = "en_cours"
        self.calculDistanceArret()
        self.distanceParcourue = 0
        return
        

    ##### DEPLACEMENT #####
    def calculDistanceParcourue(self):
        self.vitesse = 0.0029*self.puissanceMoteurInitial - 0.0245
        self.distanceParcourue += self.delta_t * self.vitesse
        self.deplacementTotal += self.delta_t * self.vitesse
        return

    ##### ACCELERATION #####
    def accelerationInit(self):
        self.acceleration = "en_cours"
        self.tempsDerniereAction = time.time()
        return
    
    def decelerationInit(self):
        self.deceleration = "en_cours"
        self.tempsDerniereAction = time.time()
        return

    # POUR PICAR
    def accelerationReel(self):
        self.tempsNouvelleAction = time.time()
        self.delta_t = self.tempsNouvelleAction - self.tempsDerniereAction
        # gestion de la distance total parcourue
        self.distanceParcourue = self.calculDistanceParcourue(self)
        # equation linéaire de la puissance moteur en fonction du temps
        ajustementEquation = (self.puissanceMoteurPiCar - 7.4324)/-208.11      # mise en equation, voir Excel
        puissanceMoteur = 208.11*(self.delta_t + ajustementEquation) + 7.4324    # mise en equation, voir Excel
        #Gestion de risque sur l'intervalle de puissance des moteurs
        if puissanceMoteur > self.puissanceCible:
            puissanceMoteur = self.puissanceCible
            self.acceleration = "termine" # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if puissanceMoteur > 100 :
            puissanceMoteur = 100
        if puissanceMoteur < 0 :
            puissanceMoteur = 0
        self.puissanceMoteurPiCar = puissanceMoteur
        return
    
    # POUR PICAR
    def decelerationReel(self):
        self.tempsNouvelleAction = time.time()
        self.delta_t = self.tempsNouvelleAction - self.tempsDerniereAction
        # gestion de la distance total parcourue
        self.distanceParcourue = self.calculDistanceParcourue(self)
        # equation linéaire de la puissance moteur en fonction du temps
        ajustementEquation = (self.puissanceMoteurPiCar - 100)/-200        # mise en equation, voir Excel
        puissanceMoteur = -200*(self.delta_t+ajustementEquation) + 100       # mise en equation, voir Excel
        #Gestion de risque sur l'intervalle de puissance des moteurs
        if puissanceMoteur < self.puissanceCible:
            puissanceMoteur = self.puissanceCible
            self.deceleration = "temine" # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if puissanceMoteur > 100 :
            puissanceMoteur = 100
        if puissanceMoteur < 0 :
            puissanceMoteur = 0
        self.puissanceMoteurPiCar = puissanceMoteur
        return
    
    # POUR SIMULATION
    def accelerationSimulation(self):
        self.tempsNouvelleAction = time.time()
        self.delta_t = self.tempsNouvelleAction - self.tempsDerniereAction
        ajustementEquation = (self.vitesse - 0.0041)/-0.5704          # mise en equation, voir Excel
        vitesse = 0.5704*(self.delta_t + ajustementEquation) + 0.004         # mise en equation, voir Excel
        #Gestion de la vitesse maximal
        if vitesse > self.vitesseCible:
            vitesse = self.vitesseCible
            self.acceleration = "null" # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if vitesse < 0:
            vitesse = 0
        self.vitesse = vitesse
        return
    
    # POUR SIMULATION
    def decelerationSimulation(self):
        self.tempsNouvelleAction = time.time()
        self.delta_t = self.tempsNouvelleAction - self.tempsDerniereAction
        ajustementEquation = (self.vitesse - 0.2607)/-0.5704          # mise en equation, voir Excel
        vitesse = -0.5704*(self.delta_t + ajustementEquation) + 0.2607       # mise en equation, voir Excel
        #Gestion de la vitesse maximal
        if vitesse < self.vitesseCible:
            vitesse = self.vitesseCible
            self.deceleration = "null" # la puissance cible est atteinte, on peut mettre fin à l'accélération
        if vitesse < 0:
            vitesse = 0
        self.vitesse = vitesse
        return
    ##### FIN ACCELERATION #####

    ##### VIRAGE #####
    def virage(self):
        # niveauDeVirage va de -4 à -1 pour un virage a gauche, de 1 à 4 pour un virage a droite et de 0 pour centrer les roues
        angleVirage = self.angleRoue
        if self.niveauDeVirage == 0:
            angleVirage = 90
        # virage à droite
        if self.niveauDeVirage == 1:
            angleVirage += 1
        if self.niveauDeVirage == 2:
            angleVirage += 3
        if self.niveauDeVirage == 3:
            angleVirage += 6
        if self.niveauDeVirage == 4:
            angleVirage += 10 

        # virage à gauche
        if self.niveauDeVirage == -1:
            angleVirage -= 1
        if self.niveauDeVirage == -2:
            angleVirage -=  3
        if self.niveauDeVirage == -3:
            angleVirage -= 6
        if self.niveauDeVirage == -4:
            angleVirage -= 10

        # gestion de l'intervalle maximum de virage
        if  angleVirage > 135:
            angleVirage = 135
        if  angleVirage < 45:
            angleVirage = 45 

        self.angleRoue = angleVirage
        return   
    ##### FIN VIRAGE #####

    def calculDistanceArret(self):
        # permet de calculer à quel distance il faut commencer la deceleration pour atteindre une distance precise
        # a partir de la vitesse maximum selon les équations choisi, il faut 0.45s pour decelerer jusqu'a 0 m/s
        self.vitesse = 0.0029*self.puissanceCible - 0.0245
        delta_t = 0.45 - ((self.vitesse-0.2607)/-0.5704)  # mise en equation, voir Excel
        self.distanceArret = 0.5*self.vitesse*delta_t     # equation d'acceleration: x = 1/2(Vx + V0)t
        return
