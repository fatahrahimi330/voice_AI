import pyttsx3
import wikipedia

def search_and_speak():
    # Initialize the text-to-speech engine
    voice = pyttsx3.init()

    # Take user input
    query = input("Searching Wikipedia/Google: ")

    # Search Wikipedia for a summary
    result = wikipedia.summary(query, sentences=3)
    print(result)

    # Set the voice to use
    voice.setProperty('rate', 150)  # You can adjust the speech rate as needed

    # Use the selected voice to say the result
    voice.say(result)
    voice.runAndWait()

# Call the function to use it
search_and_speak()
