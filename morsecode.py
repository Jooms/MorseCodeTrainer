import pygame
import random
import numpy as np
import signal
import pyttsx3

# Initialize Pygame
pygame.init()

# Variables for tone, Morse code, etc.
current_frequency = 700
sample_rate = 44100  
dot_duration = 0.1  
current_wpm = 7  

# Global flag to toggle the display of Morse code
show_morse = True

voice_enabled = False
show_morse = True

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

week_letters = {
    1: 'ETIANM',
    2: 'SURWDK',
    3: 'GOHVFL',
    4: 'PJBXC',
    5: 'YZQ1234567890',
    6: '. , ? /'
}

<<<<<<< HEAD
=======
# Global flag to toggle the display of Morse code

def speak_text(engine, text):
    try:
        engine.say(text.lower())
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"Error speaking text: {e}")
    finally:
        try:
            engine.stop()
        except:
            pass

>>>>>>> 6869bd6 (Add Voice)
# Function to generate tone for given frequency and duration
def generate_tone(frequency, duration, sample_rate=44100):
    num_samples = int(duration * sample_rate)
    t = np.linspace(0, duration, num_samples, endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t) * 32767
    tone = tone.astype(np.int16)
    stereo_tone = np.stack((tone, tone), axis=-1)
    return stereo_tone

# Function to play the morse sound (dot or dash)
def play_morse_sound(symbol, frequency):
    if symbol == '.':
        duration = dot_duration
    elif symbol == '-':
        duration = dot_duration * 3  
    else:
        return  

    sound_array = generate_tone(frequency, duration)
    sound = pygame.sndarray.make_sound(sound_array)
    sound.play()
    pygame.time.delay(int(duration * 1000)) 

# Function to print text in yellow
def print_yellow(text):
    YELLOW = '\033[33m'  
    RESET = '\033[0m'  
    print(f"{YELLOW}{text}{RESET}")

# Function to practice random letters from a specific week
def practice_week_letters_continuously(week_num):
    letters = week_letters[week_num]
    engine = pyttsx3.init()
    while True:
        letter = random.choice(letters)
        if letter == ' ':
            continue
        if show_morse:
            print_yellow(f"Sending: {letter} ({morse_code[letter]})")
        else:
            print_yellow(f"Sending: {letter}")
        for symbol in morse_code[letter]:
            play_morse_sound(symbol, current_frequency)
            pygame.time.delay(int(dot_duration * 1000))  
        pygame.time.delay(int(dot_duration * 3 * 1000))  

        if voice_enabled:
            speak_text(engine,letter)
    engine.stop()

# Function to practice all characters continuously
def practice_all_characters_continuously():
    engine = pyttsx3.init()
    while True:
        letter = random.choice(list(morse_code.keys()))
        if show_morse:
            print_yellow(f"Sending: {letter} ({morse_code[letter]})")
        else:
            print_yellow(f"Sending: {letter}")
        for symbol in morse_code[letter]:
            play_morse_sound(symbol, current_frequency)
            pygame.time.delay(int(dot_duration * 1000))
        pygame.time.delay(int(dot_duration * 3 * 1000))  

        if voice_enabled:
            speak_text(engine,letter)
    engine.stop()

# Function to play user text in morse
def play_user_text_in_morse(user_text):
    for char in user_text.upper():
        if char == ' ':
            print("Space (between words)")
            pygame.time.delay(int(dot_duration * 7 * 1000))  
        elif char in morse_code:
            if show_morse:
                print_yellow(f"Sending: {char} ({morse_code[char]})")
            else:
                print_yellow(f"Sending: {char}")
            for symbol in morse_code[char]:
                play_morse_sound(symbol, current_frequency)
                pygame.time.delay(int(dot_duration * 1000))  
            pygame.time.delay(int(dot_duration * 3 * 1000))  
        else:
            print(f"Skipping unsupported character: {char}")

# Function to print the menu in blue
def print_blue(text):
    BLUE = '\033[34m'  
    RESET = '\033[0m'  
    print(f"{BLUE}{text}{RESET}")

# Function to adjust the tone frequency
def adjust_frequency():
    global current_frequency
    try:
        # Get the desired frequency from the user
        new_frequency = int(input("Enter the new frequency (400-1000 Hz): "))
        if 400 <= new_frequency <= 1000:
            current_frequency = new_frequency
            print(f"Frequency adjusted to {current_frequency} Hz.")
        else:
            print("Invalid frequency. Please enter a value between 400 and 1000 Hz.")
    except ValueError:
        print("Invalid input. Please enter an integer value between 400 and 1000 Hz.")

# Main menu function
def show_menu():
    global transmitting_event, current_wpm, dot_duration, current_frequency, show_morse, voice_enabled
    while True:
        print(f"\nCurrent Frequency: {current_frequency} Hz | Current WPM: {current_wpm}")
        print_blue("\nThis is a Morse Code program by Glenn Maclean WA7SPY.\n")
        print_blue("The methodology for learning the order of characters was\n")
        print_blue("developed by Michael Aretsky N6MQL. Michael died from Covid complications.\n")
        print_blue("He is severely missed by the Ham Radio Morse Code community!\n")
        print_blue("If you spend at least 15 minutes per day with the program in 5 to 6 weeks.\n")
        print_blue("You will have learned Morse Code! Start learning each week's letters in order.\n")
        print_blue("Do not move to the next week letters until you know the previous week's\n")
        print_blue("letters by heart!\n")
        print_blue("Morse Code is an audible language! Turn the dot dash display off as\n")
        print_blue("soon as possible! Once you have learned all the letters (weeks), start\n")
        print_blue("increasing the wpm speed! I highly recommend you get a straigth key and\n")
        print_blue("tone oscillator. Look on ebay or Amazon. Start practice sending characters and replicate the\n")
        print_blue("characters as you have heard them from this program\n")
        print_blue("There will be a time when you get a mental block with the characters. Keep\n")
        print_blue('practicing and work through the mental block and the characters will come to you!\n')
        print_blue("Good luck and Have Fun!")
        print_blue("\nWelcome to the Morse Code Training and Practice Program!\n")
        print_blue("Press Ctrl + C to terminate the sending of letters and quit the program\n")
        print_blue("1. Start continuous random letters from Week 1 (ETIANM)")
        print_blue("2. Start continuous random letters from Week 2 (SURWDK)")
        print_blue("3. Start continuous random letters from Week 3 (GOHVFL)")
        print_blue("4. Start continuous random letters from Week 4 (PJBXC)")
        print_blue("5. Start continuous random letters from Week 5 (YZQ1234567890)")
        print_blue("6. Start continuous random letters from Week 6 (. , ? /)")
        print_blue("7. Start continuous random letters from All Characters (A-Z, 0-9, . , ? /)")
        print_blue("8. Enter custom text to be played in Morse code")  
        print_blue("9. Adjust Tone Frequency 400hz to 1000hz")
        print_blue("10. Set Words Per Minute (5 to 40 wpm)")
        print_blue("11. Toggle Display of Morse Code (dots and dashes)")
        print_blue("12. Toggle Voice")
        print_blue("13. Exit")
        print(f"Dot Dash Display is {'ON' if show_morse else 'OFF'}")
        choice = input("Enter choice (1-13): ")

        if choice == '1':
            practice_week_letters_continuously(1)
        elif choice == '2':
            practice_week_letters_continuously(2)
        elif choice == '3':
            practice_week_letters_continuously(3)
        elif choice == '4':
            practice_week_letters_continuously(4)
        elif choice == '5':
            practice_week_letters_continuously(5)
        elif choice == '6':
            practice_week_letters_continuously(6)
        elif choice == '7':
            practice_all_characters_continuously()
        elif choice == '8':
            user_text = input("Enter your text to be played in Morse code: ")
            play_user_text_in_morse(user_text)  
        elif choice == '9':
            adjust_frequency()
        elif choice == '10':
            current_wpm = int(input("Enter the desired words per minute (WPM): "))
            dot_duration = 60 / (current_wpm * 50)  
            print(f"WPM set to: {current_wpm}")
        elif choice == '11':
            show_morse = not show_morse
            if show_morse:
                print("Morse code display (dots and dashes) is now ON.")
            else:
                print("Morse code display (dots and dashes) is now OFF.")
        elif choice == '12':
            voice_enabled = not voice_enabled
            if voice_enabled:
                print("Voice is now ON.")
            else:
                print("Voice is now OFF.")
        elif choice == '13':
            graceful_exit(None, None)  
        else:
            print("Invalid choice. Please select a valid option.")

# Graceful exit function for handling Ctrl+C
def graceful_exit(signal, frame):
    print("\nProgram interrupted. Exiting...")
    transmitting_event.clear()
    if tts_engine is not None:
        try:
            tts_engine.stop()
        except:
            pass
    pygame.quit()
    exit(0)

signal.signal(signal.SIGINT, graceful_exit)

show_menu()
