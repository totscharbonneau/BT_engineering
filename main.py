SIMULATION = True
RESET = True
NUMBEROFCYCLES = 500
TEST = False

with open("control/state_machine.py") as f:
    code = f.read()
    exec(code)

if(SIMULATION):
    with open("sim_api/sim_api.py") as f:
        code = f.read()
        exec(code)
    api = SimAPI(RESET, NUMBEROFCYCLES)
else:
    from real_api.real_api import *
    api = RealAPI()

stateMachine = StateMachine(api)
stateMachine.loopStateMachine()