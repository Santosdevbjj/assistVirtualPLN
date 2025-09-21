import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import platform

# Configuração inicial dos motores de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Define a voz para português do Brasil, se disponível
for voice in voices:
    if "brazil" in voice.id.lower() or "portuguese" in voice.id.lower():
        engine.setProperty('voice', voice.id)
        break

# --- Módulo 1: Transformação de Texto em Áudio (Text-to-Speech) ---
def speak(text):
    """
    Converte um texto em fala e o reproduz.
    Args:
        text (str): O texto a ser falado.
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Erro ao converter texto para fala: {e}")

# --- Módulo 2: Transformação de Fala em Texto (Speech-to-Text) ---
def listen():
    """
    Captura áudio do microfone e o converte em texto.
    Retorna:
        str: O texto reconhecido, ou None em caso de erro.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        # Ajusta para o ruído ambiente antes de ouvir
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Nenhuma fala detectada.")
            return None
        
    try:
        print("Reconhecendo...")
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de fala; {e}")
        return None

# --- Ações Automatizadas ---
def search_wikipedia(query):
    """
    Pesquisa um termo na Wikipedia e resume o resultado.
    Args:
        query (str): O termo a ser pesquisado.
    """
    try:
        wikipedia.set_lang("pt")
        # Define o número de frases para o resumo
        result = wikipedia.summary(query, sentences=2)
        print(f"Wikipedia diz: {result}")
        speak(f"De acordo com a Wikipedia, {result}")
    except wikipedia.exceptions.PageError:
        speak(f"Desculpe, não encontrei nenhuma página na Wikipedia sobre {query}.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Sua pesquisa é muito ampla. Por favor, seja mais específico. Possíveis tópicos são: {e.options[0:3]}")
    except Exception as e:
        speak(f"Ocorreu um erro ao pesquisar na Wikipedia: {e}")

def open_youtube(query=None):
    """
    Abre o YouTube ou pesquisa um vídeo específico.
    Args:
        query (str, opcional): O termo de pesquisa para o YouTube.
    """
    if query:
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        speak(f"Abrindo o YouTube e pesquisando por {query}")
    else:
        url = "https://www.youtube.com"
        speak("Abrindo o YouTube.")
    webbrowser.open(url)

def show_location(query):
    """
    Abre o Google Maps com a pesquisa de um local.
    Args:
        query (str): O local a ser pesquisado.
    """
    url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"
    speak(f"Buscando a localização de {query} no mapa.")
    webbrowser.open(url)
