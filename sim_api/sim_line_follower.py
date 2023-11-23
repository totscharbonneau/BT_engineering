import bpy, time, mathutils, bmesh

class SimLineFollower:
    __sensors = None
    __sensorsMesh = tuple(bmesh.new() for i in range(0, 5))
    __trackTree = None
    __references = None
    
    def __init__(self, parent, address=None, references=tuple(int(512) for i in range(0, 5))):
        self.__references = references
        self.__sensors = tuple(parent._objects[f"lineSensor{i}"] for i in range(0, 5))
        trackMesh = bmesh.new()
        trackMesh.from_mesh(parent._objects["line"].data)
        trackMesh.transform(parent._objects["line"].matrix_world) 
        self.__trackTree = mathutils.bvhtree.BVHTree.FromBMesh(trackMesh)
        for i, sensorMesh in enumerate(self.__sensorsMesh):
            sensorMesh.from_mesh(self.__sensors[i].data)
    
    def read_raw(self):
        output = []
        for i in range(5):
            sensorMesh = bmesh.new()
            sensorMesh.from_mesh(self.__sensors[i].data)
            sensorMesh.transform(self.__sensors[i].matrix_world)
            sensorTree = mathutils.bvhtree.BVHTree.FromBMesh(sensorMesh)
            overlap = sensorTree.overlap(self.__trackTree)
            output.append(int(bool(overlap))*1024)
        return output
    
    def read_analog(self, trys=None):
        return self.read_raw()

    def read_digital(self):	
        lt = self.read_analog()
        digital_list = []
        for i in range(0, 5):
            if lt[i] < self.__references[i]:
                digital_list.append(0)
            elif lt[i] > self.__references[i]:
                digital_list.append(1)
            else:
                digital_list.append(-1)
        return digital_list

    def get_average(self, mount):
        if not isinstance(mount, int):
            raise ValueError("Mount must be integer")
        return self.read_analog()

    def found_line_in(self, timeout):
        if isinstance(timeout, int) or isinstance(timeout, float):
            pass
        else:
            raise ValueError("Timeout must be integer or float")
        time_start = time.time()
        time_during = 0
        while time_during < timeout:
            lt_status = self.read_digital()
            result = 0
            if 1 in lt_status:
                return lt_status
            time_now = time.time()
            time_during = time_now - time_start
        return False

    def wait_tile_status(self, status):
        while True:
            lt_status = self.read_digital()
            if lt_status in status:
                break

    def wait_tile_center(self):
        while True:
            lt_status = self.read_digital()
            if lt_status[2] == 1:
                break