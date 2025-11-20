import asyncio
import random

from nicegui import ui

from core.decorators import ui_task_handler
from core.exceptions import DeviceConnectionError
from models.schemas import DeviceConfig, DeviceState


class VoiceAssistant:
    def __init__(self, config: DeviceConfig) -> None:
        self.config = config
        self.state = DeviceState()

    @ui_task_handler  # decorator
    async def listen(self) -> str:
        """Simula ouvir um comando de voz (Async)."""
        await asyncio.sleep(1)

        # Erro aleatório para testar a Exception Customizada
        percent_failure = 0.3
        if random.random() < percent_failure:  # 30% de chance de falha
            msg = "O dispositivo não respondeu ao ping."
            raise DeviceConnectionError(msg)

        return "alterar luz"

    async def respond(self, message: str) -> None:
        """Simula responder ao usuário (Async)."""
        await asyncio.sleep(0.5)
        ui.notify(f"{self.config.name} diz: {message}", type="info")
