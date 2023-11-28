with open("sim_api/sim_api.py") as f:
    code = f.read()
    exec(code)

with open("control/state_machine.py") as f:
    code = f.read()
    exec(code)

SIMULATION = True
RESET = True
NUMBEROFCYCLES = 500

if(SIMULATION):
    api = SimAPI(RESET, NUMBEROFCYCLES)

stateMachine = StateMachine(api)
stateMachine.loopStateMachine()