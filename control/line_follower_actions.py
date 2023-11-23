class LineFollowerActions:
    def RightAhead(self):
        return self._api.lineFollower.read_digital()

    def VeryWeakLeft(self):
        self._api.frontWheels.wanted_angle += -1
        return self._api.lineFollower.read_digital()

    def WeakLeft(self):
        self._api.frontWheels.wanted_angle += -2
        return self._api.lineFollower.read_digital()

    def Left(self):
        self._api.frontWheels.wanted_angle += -3
        return self._api.lineFollower.read_digital()

    def StrongLeft(self):
        self._api.frontWheels.wanted_angle += -4
        return self._api.lineFollower.read_digital()

    def VeryStrongLeft(self):
        self._api.frontWheels.wanted_angle += -5
        return self._api.lineFollower.read_digital()

    def VeryWeakRight(self):
        self._api.frontWheels.wanted_angle += 1
        return self._api.lineFollower.read_digital()

    def WeakRight(self):
        self._api.frontWheels.wanted_angle += 2
        return self._api.lineFollower.read_digital()

    def Right(self):
        self._api.frontWheels.wanted_angle += 3
        return self._api.lineFollower.read_digital()

    def StrongRight(self):
        self._api.frontWheels.wanted_angle += 4
        return self._api.lineFollower.read_digital()

    def VeryStrongRight(self):
        self._api.frontWheels.wanted_angle += 5
        return self._api.lineFollower.read_digital()
