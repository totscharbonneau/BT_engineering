SIMULATION = False
RESET = True
NUMBEROFCYCLES = 500
TEST = True

with open("control/state_machine.py") as f:
    code = f.read()
    exec(code)

if(SIMULATION):
    with open("sim_api/sim_api.py") as f:
        code = f.read()
        exec(code)
    api = SimAPI(RESET, NUMBEROFCYCLES)
else:
    import real_api.real_api
    api = RealAPI()

stateMachine = StateMachine(api)
stateMachine.loopStateMachine()