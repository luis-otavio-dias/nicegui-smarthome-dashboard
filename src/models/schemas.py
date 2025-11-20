from dataclasses import dataclass


@dataclass
class DeviceConfig:
    """Define as configurações imutáveis do dispositivo."""
    device_id: str
    name: str
    location: str

@dataclass
class DeviceState:
    """Define o estado mutável do dispositivo."""
    is_on: bool = False
    last_active: str = "Never"
