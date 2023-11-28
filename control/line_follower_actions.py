class LineFollowerActions:
    def RightAhead(self):
        self._targetAngle = 0
        return self._api.lineFollower.read_digital()

    def VeryWeakLeft(self):
        self._targetAngle = -5
        return self._api.lineFollower.read_digital()

    def WeakLeft(self):
        self._targetAngle = -15
        return self._api.lineFollower.read_digital()

    def Left(self):
        self._targetAngle = -25
        return self._api.lineFollower.read_digital()

    def StrongLeft(self):
        self._targetAngle = -35
        return self._api.lineFollower.read_digital()

    def VeryStrongLeft(self):
        self._targetAngle = -45
        return self._api.lineFollower.read_digital()

    def VeryWeakRight(self):
        self._targetAngle = 5
        return self._api.lineFollower.read_digital()

    def WeakRight(self):
        self._targetAngle = 15
        return self._api.lineFollower.read_digital()

    def Right(self):
        self._targetAngle = 25
        return self._api.lineFollower.read_digital()

    def StrongRight(self):
        self._targetAngle = 35
        return self._api.lineFollower.read_digital()

    def VeryStrongRight(self):
        self._targetAngle = 45
        return self._api.lineFollower.read_digital()
