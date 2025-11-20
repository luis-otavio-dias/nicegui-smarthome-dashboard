import functools
from collections.abc import Awaitable, Callable
from typing import Any

from nicegui import ui

from core.exceptions import SmartHomeError


def ui_task_handler(
    func: Callable[..., Awaitable[Any]]
) -> Callable[..., Awaitable[Any]]:
    """
    DECORATOR:
    Envolve funções async. Mostra uma notificação de início,
    trata exceções customizadas e notifica o sucesso ou erro na UI.
    """
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await func(*args, **kwargs)

        except SmartHomeError as e:
            ui.notify(f"Erro de Negócio: {e}", type="warning")

        except Exception as e:
            ui.notify(f"Erro Crítico: {e!s}", type="negative")

    return wrapper
