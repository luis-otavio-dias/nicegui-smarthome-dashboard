from nicegui import ui

from core.utils import create_voltage_sensor
from devices.light import SmartLight
from devices.voice_assistant import VoiceAssistant
from models.schemas import DeviceConfig

smart_light_config = DeviceConfig(
    device_id="L01", name="Luz da Sala", location="Sala de Estar"
)
smart_light = SmartLight(smart_light_config)

voice_assistant_config = DeviceConfig(
    device_id="VA01", name="Assistente de Voz", location="Sala de Estar"
)
voice_assistant = VoiceAssistant(voice_assistant_config)

voltage_sensor = create_voltage_sensor()


def create_voice_assistant_card(dark_mode: ui.dark_mode) -> None:
    """Cria o card do assistente de voz."""
    with ui.card().classes("w-96"):
        ui.markdown(f"### {voice_assistant.config.name} 🗣")
        ui.label(f"Local: {voice_assistant.config.location}").classes(
            "text-gray-500"
        )
        ui.separator()
        ui.label("Status: Pronto").classes("text-lg font-bold q-my-md")

        async def process_voice_command() -> None:
            spinner_va.set_visibility(True)
            command = await voice_assistant.listen()

            if command:
                if "luz" in command.lower():
                    await voice_assistant.respond(
                        "Entendido. Alterando a luz."
                    )
                    await smart_light.toggle()

                    if smart_light.state.is_on:
                        dark_mode.disable()
                    else:
                        dark_mode.enable()

                    ui.notify(
                        "Comando executado com sucesso!", type="positive"
                    )
                else:
                    await voice_assistant.respond(
                        "Desculpe, não entendi o comando."
                    )
            spinner_va.set_visibility(False)

        with ui.row().classes("items-center"):
            ui.button(
                "Ouvir Comando", on_click=process_voice_command, icon="mic"
            )
            ui.label("Comando: Alterar luz").classes("text-gray-500")
            spinner_va = ui.spinner(size="lg").props("color=secondary")
            spinner_va.set_visibility(False)


def create_smart_light_card(dark_mode: ui.dark_mode) -> None:
    """Cria o card da luz inteligente."""
    with ui.card().classes("w-96"):
        ui.markdown(f"### {smart_light.config.name} 💡")
        ui.label(f"Local: {smart_light.config.location}").classes(
            "text-gray-500"
        )

        ui.separator()

        last_active_label = ui.label(
            f"Última atividade: {smart_light.state.last_active}"
        ).classes("text-gray-500")

        ui.separator()

        status_label = ui.label("Status: DESCONHECIDO").classes(
            "text-lg font-bold q-my-md"
        )

        def update_ui() -> None:
            is_on = smart_light.state.is_on
            color = "text-green-500" if is_on else "text-red-500"
            text = "LIGADO" if is_on else "DESLIGADO"
            status_label.text = f"Status: {text}"
            status_label.classes(replace=color)

            last_active_label.text = (
                f"Última atividade: {smart_light.state.last_active}"
            )

            if is_on:
                dark_mode.disable()
            else:
                dark_mode.enable()

        async def on_click() -> None:
            spinner.set_visibility(True)
            await smart_light.toggle()
            update_ui()
            spinner.set_visibility(False)

        with ui.row().classes("items-center"):
            ui.button("Alternar Energia", on_click=on_click)
            spinner = ui.spinner(size="lg").props("color=primary")
            spinner.set_visibility(False)

        update_ui()


def create_voltage_monitor_card() -> None:
    """Cria o card do monitor de voltagem."""
    with ui.card().classes("w-96 q-mt-md"):
        ui.markdown("### ⚡ Monitor de Voltagem")
        voltage_label = ui.label("Carregando...")
        ui.timer(1.0, lambda: voltage_label.set_text(f"{voltage_sensor()} V"))


@ui.page("/")
def main_page() -> None:
    """Página principal da aplicação NiceGUI."""
    ui.colors(primary="#5898d4", secondary="#26a69a")
    dark = ui.dark_mode(value=True)

    with ui.header().classes("items-center justify-between"):
        ui.label("Smart Home Dashboard").classes("text-xl font-bold")

    with ui.column().classes("w-full items-center q-pa-md"):
        create_voice_assistant_card(dark)
        create_smart_light_card(dark)
        create_voltage_monitor_card()


ui.run(title="SmartHome", language="pt-BR")
