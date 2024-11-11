import random

def dataAdquisicion():
    p_sistolica = random.uniform(60, 90)
    p_diastolica = random.uniform(110,130)
    return {
        "p_sistolica": p_sistolica,
        "p_diastolica": p_diastolica
    }
