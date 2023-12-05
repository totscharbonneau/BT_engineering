from picar import back_wheels
import time
import picar


picar.setup()
bw = back_wheels.Back_Wheels(db='config')


bw.ready()
bw.backward()

bw.speed = 30
time.sleep(5.35)
bw.stop()


