import random
from collections.abc import Callable


def create_voltage_sensor() -> Callable[[], float]:
    """
    CLOSURE:
    Retorna uma função que simula a leitura de voltagem.
    A função interna mantém o estado da última leitura para evitar
    pulos bruscos de valor.
    """
    current_voltage = 110.0  # Estado inicial
    def get_reading() -> float:
        nonlocal current_voltage

        fluctuation = random.uniform(-0.5, 0.5)
        current_voltage += fluctuation
        return round(current_voltage, 2)

    return get_reading
