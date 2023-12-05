1
"""
Variable capteur ---------------------------------------------------------------------------------------------
"""


"""
Constantes ---------------------------------------------------------------------------------------------
"""
DistanceAlerte = 30 # Distance a laquelle on commence a arreter
DistanceArret = 10 # Distance ou on arrete
Distance30cm = 30 #Distance avnt de repartir sur la ligne
DeltaSlow = 0.1 # Variation de l'angle lors de la phase de turn slow
DeltaSlow = 0.5 # Variation de l'angle lors de la phase de turn fast
MaxwaitingTimeTurnSlowly = 10 # Temps avant que turn slow devienne turn fast
MaxwaitingTimePause = 3 # temps de repos en ligne droite avant de recommencer a tourner


"""
La machine a etats ---------------------------------------------------------------------------------------------
"""


class StateMachine:
    def __init__(self, initialState):
        self.currentState = initialState
        self.runAll()
    # Template method:

    def runAll(self):
        test = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        capteurLigne = [0,0,0,0,0]   # capteur 0 gauche, capteur 4 droite
        capteurSonore = 50
        waitingTime = 50
        for testcase in test:
            # Lecture des capteurs
            capteurLigne = testcase
            print(testcase)
            self.currentState = self.currentState.next(capteurLigne, capteurSonore, waitingTime)
            self.currentState.run()
            print(" ")
            # pause
            # increment Waiting time variables


"""
Les etats ---------------------------------------------------------------------------------------------
"""


def allCapteur(input):
    for x in input:
        if x == 0:
            return False
    return True

class State:
    def run(self):
        assert 0, "run not implemented"

    def next(self, capteurLigne, capteurSonore, waitingTime):
        assert 0, "next not implemented"


class TurnSlowlyLeft(State):
    def run(self):
        print("TurnSlowlyLeft")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[1]:
            return State.TurnFastRight ######
        if capteurLigne[2]:
            return State.PauseAfterLeftTurn
        if waitingTime >= MaxwaitingTimeTurnSlowly or capteurLigne[3]:
            return State.TurnFastLeft
        return State.TurnSlowlyLeft


class TurnSlowlyRight(State):
    def run(self):
        print("TurnSlowlyRight")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[3]:
            return State.TurnFastLeft ######
        if capteurLigne[2]:
            return State.PauseAfterRightTurn
        if waitingTime >= MaxwaitingTimeTurnSlowly or capteurLigne[1]:
            return State.TurnFastRight
        return State.TurnSlowlyLeft


class PauseAfterLeftTurn(State):
    def run(self):
        print("PauseAfterLeftTurn")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[3]:
            return State.TurnFastLeft ######
        if not capteurLigne[2]:
            return State.TurnSlowlyRight
        if capteurLigne[1]:
            return State.TurnFastRight
        if waitingTime >= MaxwaitingTimePause:
            return State.TurnSlowlyRight
        return State.PauseAfterLeftTurn


class PauseAfterRightTurn(State):
    def run(self):
        print("PauseAfterRightTurn")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[1]:
            return State.TurnFastRight ######
        if not capteurLigne[2]:
            return State.TurnSlowlyLeft
        if capteurLigne[3]:
            return State.TurnFastLeft
        if waitingTime >= MaxwaitingTimePause:
            return State.TurnSlowlyLeft
        return State.PauseAfterRightTurn


class TurnFastLeft(State):
    def run(self):
        print("TurnFastLeft")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[0]:
            return State.Stop#####
        if capteurLigne[1]:
            return State.TurnSlowlyLeft
        if capteurLigne[2]:
            return State.PauseAfterLeftTurn
        if capteurLigne[3]:
            return State.TurnFastRight
        return State.TurnFastLeft


class TurnFastRight(State):
    def run(self):
        print("TurnFastRight")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[4]:
            return State.Stop#####
        if capteurLigne[3]:
            return State.TurnSlowlyRight
        if capteurLigne[2]:
            return State.PauseAfterRightTurn
        if capteurLigne[1]:
            return State.TurnFastLeft
        return State.TurnFastRight


class Search(State):
    def run(self):
        print("Search")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[0]:
            return State.FoundLineLeftSide
        if capteurLigne[4]:
            return State.FoundLineRightSide
        return State.Search


class FoundLineRightSide(State):
    def run(self):
        print("FoundLineRightSide")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[3]:
            return State.TurnLeftWithInfo
        return State.FoundLineRightSide


class FoundLineLeftSide(State):
    def run(self):
        print("FoundLineLeftSide")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[1]:
            return State.TurnRightWithInfo
        return State.FoundLineLeftSide


class TurnLeftWithInfo(State):
    def run(self):
        print("TurnLeftWithInfo")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[2]:
            return State.PauseAfterRightTurn
        return State.TurnLeftWithInfo


class TurnRightWithInfo(State):
    def run(self):
        print("TurnRightWithInfo")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceAlerte:
            return State.ObstacleDetected
        if capteurLigne[2]:
            return State.PauseAfterLeftTurn
        return State.TurnRightWithInfo


class ObstacleDetected(State):
    def run(self):
        print("ObstacleDetected")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore <= DistanceArret:
            return State.ObstacleStopped
        return State.ObstacleDetected


class ObstacleStopped(State):
    def run(self):
        print("ObstacleStopped")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if waitingTime >= MaxwaitingTimePause:
            return State.ObstacleRecule
        return State.ObstacleStopped


class ObstacleRecule(State):
    def run(self):
        print("ObstacleRecule")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        if allCapteur(capteurLigne):
            return State.Stop
        if capteurSonore >= Distance30cm:
            return State.ObstacleContourne
        return State.ObstacleRecule


class ObstacleContourne(State):
    def run(self):
        print("ObstacleContourne")
        #ici on peut faire la suite de commande dune shot avant de changer d'etat

    def next(self, capteurLigne, capteurSonore, waitingTime):
        return State.Search


class Stop(State):
    def run(self):
        print("Stop")

    def next(self, capteurLigne, capteurSonore, waitingTime):
        return State.Stop


"""
Init---------------------------------------------------------------------------------------------
"""


class Picart(StateMachine):
    def __init__(self):
        # Initial state
        StateMachine.__init__(self, State.Search)


State.TurnSlowlyLeft = TurnSlowlyLeft()
State.TurnSlowlyRight = TurnSlowlyRight()
State.PauseAfterLeftTurn = PauseAfterLeftTurn()
State.PauseAfterRightTurn = PauseAfterRightTurn()
State.TurnFastLeft = TurnFastLeft()
State.TurnFastRight = TurnFastRight()

State.Search = Search()
State.FoundLineRightSide = FoundLineRightSide()
State.FoundLineLeftSide = FoundLineLeftSide()
State.TurnLeftWithInfo = TurnLeftWithInfo()
State.TurnRightWithInfo = TurnRightWithInfo()

State.ObstacleDetected = ObstacleDetected()
State.ObstacleStopped = ObstacleStopped()
State.ObstacleRecule = ObstacleRecule()
State.ObstacleContourne = ObstacleContourne()

State.Stop = Stop()

Picart()