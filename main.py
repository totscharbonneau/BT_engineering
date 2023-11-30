SIMULATION = True
RESET = True
NUMBEROFCYCLES = 500

with open("control/state_machine.py") as f:
    code = f.read()
    exec(code)

if(SIMULATION):
    with open("sim_api/sim_api.py") as f:
        code = f.read()
        exec(code)
    api = SimAPI(RESET, NUMBEROFCYCLES)
else:
    with open("sim_api/real_api.py") as f:
        code = f.read()
        exec(code)
    api = RealAPI()

stateMachine = StateMachine(api)
stateMachine.loopStateMachine()