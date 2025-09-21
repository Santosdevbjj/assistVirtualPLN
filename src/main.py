import re
from core_functions import speak, listen, search_wikipedia, open_youtube, show_location

def main():
    """
    Função principal que gerencia o loop do assistente virtual.
    """
    speak("Olá! Sou seu assistente virtual. Como posso ajudar?")
    while True:
        command = listen()
        if command:
            command = command.lower()
            
            # Condições de saída
            if "parar" in command or "desligar" in command or "sair" in command:
                speak("Até mais!")
                break

            # Ações de pesquisa na Wikipedia
            if "pesquisar" in command or "procure por" in command:
                query = re.search(r'(pesquisar|procure por)(.+)', command)
                if query:
                    search_query = query.group(2).strip()
                    speak(f"Certo, procurando por {search_query} na Wikipedia.")
                    search_wikipedia(search_query)
                else:
                    speak("Por favor, diga o que devo pesquisar.")
            
            # Ações relacionadas ao YouTube
            elif "abrir youtube" in command:
                open_youtube()
            elif "assistir" in command or "ver no youtube" in command:
                query = re.search(r'(assistir|ver no youtube)(.+)', command)
                if query:
                    video_query = query.group(2).strip()
                    open_youtube(video_query)
                else:
                    speak("Por favor, diga o que você quer assistir.")
            
            # Ações de localização no mapa
            elif "onde fica" in command or "me mostre a localização de" in command:
                query = re.search(r'(onde fica|me mostre a localização de)(.+)', command)
                if query:
                    location_query = query.group(2).strip()
                    show_location(location_query)
                else:
                    speak("Por favor, diga qual local você quer encontrar.")

            # Resposta padrão para comandos não reconhecidos
            else:
                speak("Desculpe, não entendi o seu comando. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
