import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize the speech recognizer and the text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Setting the voice to a female one (you can adjust this)

def talk(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens for a voice command, processes it, and returns the command as text."""
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)  # Adjust for background noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'anu' in command:  # Changed 'alexa' to 'anu'
                command = command.replace('anu', '')
                print(command)
            return command
    except sr.UnknownValueError:
        # In case the speech was not recognized
        print("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        # In case there's an issue with the Google API
        talk("Sorry, I couldn't reach the speech recognition service.")
        return ""

def run_anu():
    """Executes commands based on voice input."""
    command = take_command()
    if command:
        print(f"Received command: {command}")
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')
    else:
        print("No valid command received.")

# Continuously run the assistant
while True:
    run_anu()
