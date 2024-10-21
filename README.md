# Jarvis - A Simple Voice Assistant

This is a basic voice-controlled assistant, "Jarvis," built with Python. Jarvis can perform tasks like opening websites, playing music from a predefined library, and fetching the latest news headlines using the News API.

### Features

- Voice recognition using the speech_recognition library
- Control to open popular websites (Google, Facebook, YouTube, LinkedIn)
- Play music from a predefined library of songs
- Fetch and read out the latest news headlines

## Technologies Used

- Python: Core language
- SpeechRecognition: For voice command recognition
- Pyttsx3: For text-to-speech functionality
- Webbrowser: To open websites in the default browser
- Requests: To fetch news data from an external API
- Music Library: Simple dictionary of song titles mapped to YouTube URLs

### Usage

- Wake Word: The assistant listens for the wake word "Jarvis." After recognizing "Jarvis," you can issue a command.

- Commands :

    - "Open Google" to open the Google homepage.
    - "Play [song name]" to play a song from the predefined music library.
    - "News" to hear the latest news headlines.

## Example Commands

- "Jarvis, open Google"
- "Jarvis, play Skyfall"
- "Jarvis, what's the news?"

### File Structure

- jarvis.py: The main Python script for running the assistant.
- musicLibrery.py: A simple Python file containing a dictionary of song titles and their corresponding YouTube URLs.

## Future Improvements

- Add support for more commands and interactions
- Improve the music library by integrating an external music API
- Implement a more advanced wake word detection system