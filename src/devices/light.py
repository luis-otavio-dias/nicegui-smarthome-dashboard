import asyncio
import random
from datetime import datetime

from nicegui import ui

from core.decorators import ui_task_handler
from core.exceptions import DeviceConnectionError
from models.schemas import DeviceConfig, DeviceState


class SmartLight:
    def __init__(self, config: DeviceConfig) -> None:
        self.config = config
        self.state = DeviceState()

    @ui_task_handler  # decorator
    async def toggle(self) -> None:
        """Simula ligar/desligar com delay de rede (Async)."""

        # Simula "loading"
        ui.notify(f"Comunicando com {self.config.name}...", type="info")
        await asyncio.sleep(1.5)

        # Erro aleatório para testar a Exception Customizada
        percent_failure = 0.1
        if random.random() < percent_failure:  # 10% de chance de falha
            msg = "O dispositivo não respondeu ao ping."
            raise DeviceConnectionError(msg)

        self.state.is_on = not self.state.is_on
        self.state.last_active = (
            datetime.now().astimezone().strftime("%H:%M:%S")
        )

        status_msg = "LIGADA" if self.state.is_on else "DESLIGADA"
        ui.notify(
            f"{self.config.name} foi {status_msg} com sucesso!",
            type="positive",
        )
