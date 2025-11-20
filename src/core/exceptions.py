class SmartHomeError(Exception):
    """Classe base para exceções do projeto."""

class DeviceConnectionError(SmartHomeError):
    """Erro disparado quando o dispositivo falha ao conectar."""
