with open("sim_api/sim_api.py") as f:
    code = f.read()
    exec(code)

SIMULATION = True
RESET = True

if(SIMULATION):
    api = SimAPI(RESET)

api