class LineFollowerActions:
    def RightAhead(self):
        self._targetAngle = 90
        return self._api.lineFollower.read_digital()

    def VeryWeakLeft(self):
        self._targetAngle = 85
        return self._api.lineFollower.read_digital()

    def WeakLeft(self):
        self._targetAngle = 75
        return self._api.lineFollower.read_digital()

    def Left(self):
        self._targetAngle = 65
        return self._api.lineFollower.read_digital()

    def StrongLeft(self):
        self._targetAngle = 55
        return self._api.lineFollower.read_digital()

    def VeryStrongLeft(self):
        self._targetAngle = 45
        return self._api.lineFollower.read_digital()

    def VeryWeakRight(self):
        self._targetAngle = 95
        return self._api.lineFollower.read_digital()

    def WeakRight(self):
        self._targetAngle = 105
        return self._api.lineFollower.read_digital()

    def Right(self):
        self._targetAngle = 115
        return self._api.lineFollower.read_digital()

    def StrongRight(self):
        self._targetAngle = 125
        return self._api.lineFollower.read_digital()

    def VeryStrongRight(self):
        self._targetAngle = 135
        return self._api.lineFollower.read_digital()
