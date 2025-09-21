## Criando sistema de assistência virtual, utilizando PLN - Processamento de Linguagem Natural.

![bairesDev](https://github.com/user-attachments/assets/5917d3f6-cd14-4f9e-9e36-68a0d71e1aa1)



**Bootcamp BairesDev - Machine Learning Training.**

---

🤖 **Assistente Virtual com PLN**



📖 **Descrição do Projeto**
Este projeto é um sistema de assistência virtual desenvolvido do zero, utilizando Processamento de Linguagem Natural (PLN) para interagir com o usuário por meio de comandos de voz. O assistente é capaz de ouvir, interpretar a fala e responder, além de executar ações automatizadas.

**As principais funcionalidades incluem:**

**Text-to-Speech (TTS):** Conversão de texto para áudio para que o assistente possa "falar".
   
  **Speech-to-Text (STT):** Conversão de áudio do microfone para texto, permitindo a compreensão dos comandos do usuário.
 * Automação: Execução de tarefas como pesquisar na Wikipedia, abrir o YouTube e buscar locais no Google Maps, acionadas por comandos de voz.

💻 **Tecnologias e Bibliotecas Utilizadas**

| Tecnologia/Biblioteca | Descrição |
|---|---|
| Python | Linguagem de programação principal. |
| SpeechRecognition | Para a conversão de fala em texto, utilizando a API de reconhecimento de voz do Google. |
| pyttsx3 | Para a conversão de texto em fala, com suporte a diferentes motores de voz (TTS). |
| PyAudio | Biblioteca de baixo nível para gravação de áudio, necessária para o SpeechRecognition capturar a entrada do microfone. |
| Wikipedia | Para realizar buscas e obter resumos de artigos na Wikipedia. |
| webbrowser | Módulo nativo do Python para abrir URLs e interagir com o navegador web do sistema. |

⚙️ **Requisitos**

**Requisitos de Software**

  - Python 3.8+
  - pip (gerenciador de pacotes do Python)
    
**Requisitos de Hardware**

- Microfone (integrado ou externo) para a funcionalidade de Speech-to-Text.
- Alto-falantes ou fones de ouvido para a funcionalidade de Text-to-Speech.

   
🚀 **Como Rodar o Projeto**

Siga estes passos para configurar e executar o projeto em seu ambiente local.

**1. Clonar o Repositório**
git clone https://github.com/Santosdevbjj/assistVirtualPLN.git
cd assistVirtualPLN

**2. Instalar as Dependências**
É altamente recomendável utilizar um ambiente virtual para isolar as dependências do projeto.

# Cria um ambiente virtual (venv)
python -m venv .venv

# Ativa o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate

# Instala as bibliotecas a partir do arquivo requirements.txt
pip install -r requirements.txt

**Atenção:** A instalação de PyAudio pode requerer a instalação prévia de bibliotecas como portaudio-devel no Linux ou pipwin no Windows. Caso tenha problemas, consulte a documentação da biblioteca.

**3. Executar o Assistente**
Após a instalação das dependências, você pode rodar o assistente virtual.
python src/main.py

O assistente irá começar a ouvir por comandos. Tente dizer algo como:

 * "Pesquisar por inteligência artificial"
 * "Abra o YouTube"
 * "Onde fica a farmácia mais próxima"
 * "Parar"

---
   
📂 **Estrutura do Projeto**
A organização do projeto segue uma estrutura modular para facilitar o desenvolvimento e a manutenção.
assistVirtualPLN/
├── assets/
│   └── audio_input/      # Pasta para armazenar arquivos de áudio de teste.
│
├── notebooks/
│   ├── 01_speech_recognition.ipynb # Notebook de demonstração de Speech-to-Text.
│   └── 02_text_to_speech.ipynb     # Notebook de demonstração de Text-to-Speech.
│
├── src/
│   ├── __init__.py       # Marca 'src' como um pacote Python.
│   ├── core_functions.py # Contém as funções principais do assistente (TTS, STT, ações).
│   └── main.py           # O ponto de entrada principal do programa.
│
├── .gitignore            # Ignora arquivos e pastas que não devem ser versionados.
├── README.md             # Este arquivo.
├── requirements.txt      # Lista de dependências do projeto.
└── setup.py              # Arquivo de configuração para empacotar o projeto.


---

**Descrição dos Arquivos e Pastas**

 - **assets/:** Pasta para armazenar recursos não-código, como áudios para testes.

- **notebooks/:** Contém notebooks Jupyter que podem ser executados no Google Colab, ideais para prototipagem e demonstrações isoladas das funcionalidades de voz.
 
- **src/:** Diretório principal com o código-fonte do assistente.

- **__init__.py:** Essencial para que o Python reconheça src como um pacote, permitindo importações.
   
- **core_functions.py:** O "cérebro" do assistente, onde as funções de conversão de voz e as ações automatizadas estão definidas.
   
- **main.py:** O arquivo que orquestra o fluxo do programa, chamando as funções de core_functions.py com base nos comandos do usuário.
 
 - **.gitignore:** Garante que arquivos de cache, ambientes virtuais e configurações de IDEs não sejam incluídos no controle de versão.

- **requirements.txt:** Lista as bibliotecas Python com suas respectivas versões, garantindo que o ambiente de desenvolvimento seja o mesmo para todos os colaboradores.
 
 - **setup.py:** Transforma o projeto em um pacote Python, permitindo sua instalação via pip.
   
✍️ **Contribuição**
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request para o repositório.


📄 **Licença**
Este projeto está licenciado sob a Licença MIT.


 
