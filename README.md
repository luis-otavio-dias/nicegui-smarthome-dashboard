Projeto que simula automação residencial utilizando a biblioteca NiceGUI para a
interface gráfica.

## Instalação

```bash
pip install -r requirements.txt

# uv sync, se estiver usando UV
```

## Uso

```bash
python src/main.py
```

## Funcionalidades

- Controle de dispositivos inteligentes (ex: luzes, termostatos).
- Monitoramento em tempo real do status dos dispositivos.
- Interface amigável para fácil interação com o sistema.

## Estrutura do Projeto

**src**/  
├── **core**/  
│ ├── \_\_init\_\_.py  
│ ├── decorators.py # Decorators  
│ ├── exceptions.py # Exceptions do sistema  
│ └── utils.py # Closures  
├── **models**/  
│ ├── \_\_init\_\_.py  
│ └── schemas.py # Dataclasses  
├── **devices**/  
│ ├── \_\_init\_\_.py  
│ └── light.py # Classes e Async  
└── main.py # Ponto de entrada (NiceGUI)

## Explicação dos Módulos

- **core**: Tratamento de erros, as closures e os decorators que controlam o comportamento da aplicação.

- **models**: Definição das estruturas de dados utilizadas no projeto.

- **devices**: Implementação das classes que representam os dispositivos inteligentes e suas funcionalidades assíncronas.

- **main.py**: Arquivo principal que inicia a aplicação NiceGUI e integra todos os componentes.
