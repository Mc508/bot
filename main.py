import speech_recognition as sr
import webbrowser
import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize recognizer and text-to-speech
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to find and use the search box
def search_with_jarvis(driver):
    time.sleep(2)  # Wait for the page to load
    
    # Possible search box selectors
    search_methods = [
        (By.NAME, "q"),       # Google, Bing, DuckDuckGo
        (By.NAME, "search"),  # Wikipedia, many sites
        (By.ID, "searchbox"), # Generic ID
        (By.CLASS_NAME, "search-box"),  
        (By.TAG_NAME, "input")  # Last resort: first input field
    ]

    search_box = None
    for method, value in search_methods:
        try:
            search_box = driver.find_element(method, value)
            print(f"Found search box using {method}: {value}")
            break
        except:
            continue

    if search_box:
        driver.execute_script("arguments[0].style.border='3px solid red'", search_box)
        print("Search box highlighted!")

        # Ask user what to search
        speak("What do you want to search?")
        with sr.Microphone() as source:
            print("Listening for search query...")
            try:
                audio = recognizer.listen(source)
                query = recognizer.recognize_google(audio)
                print(f"Searching for: {query}")
                
                # Type and search
                search_box.send_keys(query)
                search_box.send_keys(Keys.RETURN)
                speak(f"Searching for {query}")
            except sr.UnknownValueError:
                speak("I could not understand, please try again.")
            except sr.RequestError:
                speak("Network error, please check your internet.")
    else:
        print("No search box found.")
        speak("I couldn't find the search box.")

# Function to process voice commands
def processCommand(command):
    command = command.lower()
    
    if "open google" in command:
        speak("Opening Google")
        driver = webdriver.Chrome()  # Use Edge with webdriver.Edge()
        driver.get("https://www.google.com")
        search_with_jarvis(driver)

    elif "open gpt" in command:
        speak("Opening Chatgpt")
        # webbrowser.open("https://www.chatgpt.com")
        driver = webdriver.Chrome()  # Use Edge with webdriver.Edge()
        driver.get("https://www.chatgpt.com")
        search_with_jarvis(driver)
    
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
        driver = webdriver.Chrome()  # Use Edge with webdriver.Edge()
        driver.get("https://www.google.com")
        search_with_jarvis(driver)
    
    elif "youtube" in command:
        speak("Opening Instagram")
        # webbrowser.open("https://www.youtube.com")
        driver = webdriver.Chrome()  # Use Edge with webdriver.Edge()
        driver.get("https://www.youtube.com")
        search_with_jarvis(driver)

    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
        driver = webdriver.Chrome()  # Use Edge with webdriver.Edge()
        driver.get("https://www.google.com")
        search_with_jarvis(driver)

    elif "open stackoverflow" in command:
        speak("Opening Stack Overflow")
        webbrowser.open("https://www.stackoverflow.com")
        driver = webdriver.Chrome()  # Use Edge with webdriver.Edge()
        driver.get("https://www.google.com")
        search_with_jarvis(driver)

# Main loop to listen for "Jarvis"
if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis' command...")
                audio = recognizer.listen(source)
                word = recognizer.recognize_google(audio)
                print(f"Recognized: {word}")

                if "hello" in word.lower():
                    speak("Hello, how can I help you?")
                
                processCommand(word)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")








# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# recognizer  = sr.Recognizer()
# engine = pyttsx3.init()
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if c.lower() == "open google":
#         speak("Opening google")
#         webbrowser.open("www.google.com")
#         driver = webdriver.Chrome()  # Use webdriver.Edge() for Edge

#         # Open a webpage
#         url = "https://www.google.com"  # Change this to any webpage
#         driver.get(url)

#         time.sleep(2)  # Wait for page to load

#         # Possible ways to locate a search box
#         search_box = None
#         search_methods = [
#             (By.NAME, "q"),       # Google, Bing, DuckDuckGo
#             (By.NAME, "search"),  # Wikipedia, many other sites
#             (By.ID, "searchbox"), # Generic ID
#             (By.CLASS_NAME, "search-box"),  # Some websites use this
#             (By.TAG_NAME, "input")  # Last resort: find first input field
#         ]

#         # Try different methods to find the search box
#         for method, value in search_methods:
#             try:
#                 search_box = driver.find_element(method, value)
#                 print(f"Found search box using {method}: {value}")
#                 break
#             except:
#                 continue

#         # Highlight search box if found
#         if search_box:
#             driver.execute_script("arguments[0].style.border='3px solid red'", search_box)
#             print("Search box highlighted!")
#         else:
#             print("No search box found.")

#         # Keep browser open for 5 seconds before closing
#         time.sleep(5)
#         driver.quit()
#     elif c.lower() == "open youtube":
#         speak("Opening youtube")
#         webbrowser.open("www.youtube.com")
#     elif c.lower() == "open facebook":
#         speak("Opening facebook")
#         webbrowser.open("www.facebook.com")
#     elif c.lower() == "open instagram":
#         speak("Opening instagram")
#         webbrowser.open("www.instagram.com")
#     elif c.lower() == "open twitter":
#         speak("Opening twitter")
#         webbrowser.open("www.twitter.com")
#     elif c.lower() == "open stackoverflow":
#         speak("Opening stackoverflow")

# if __name__ == "__main__":
#     speak("Initializing jarvis")

#     #listen for word jarvis
#     while True:
#         r = sr.Recognizer()

#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source)

#             word = r.recognize_google(audio)
#             print(word)
#             processCommand(word)
#             if word.lower() == "hello":
#                 speak("bolo su kam chhe")
#                 speak("Hello, how can I help you?")
#                 with sr.Microphone() as source:
#                     print("Jarvis Active")
#                     audio = r.listen(source)
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
