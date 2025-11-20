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

## Organização do Projeto  
  * Classes Organizadas em Pacotes:  
      Estrutura do projeto compostas por classes cuidadosamente distribuídas em módulos e submódulos, facilitando a navegação e manutenção do código.
  
  * Recursos Intermediários:
    * **Decorators**: Para adicionar funcionalidades às classes e métodos de maneira modular.
    * **Closures**: Para manter o estado interno de funções.
    * **Estruturas Assíncronas (async/await)**: Para lidar com operações que podem ser executadas de forma concorrente.
    * **Tratamento Estruturado de Exceções**: Para garantir que o sistema seja robusto e trate erros de forma adequada.
    * **Dataclasses**: Para simplificar a criação de classes que armazenam dados, tornando o código mais claro e fácil de entender.


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
├── **devices**/  # Classes e Async 
│ ├── \_\_init\_\_.py  
│ └── light.py  
│ └── voice_assistant.py 
└── main.py # Ponto de entrada (NiceGUI)

## Explicação dos Módulos

- **core**: Tratamento de erros, as closures e os decorators que controlam o comportamento da aplicação.

- **models**: Definição das estruturas de dados utilizadas no projeto.

- **devices**: Implementação das classes que representam os dispositivos inteligentes e suas funcionalidades assíncronas.

- **main.py**: Arquivo principal que inicia a aplicação NiceGUI e integra todos os componentes.
