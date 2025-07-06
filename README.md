# Morse Code Trainer

Created by: WA7SPY

---

## About

This program helps you learn Morse code interactively!

You can:

- Practice letters in weekly groups
- Send random words and sentences built from each week's letters
- Send random call signs, numbers, and punctuation
- Enter your own text to send in Morse code
- Adjust tone frequency and speed (WPM)
- Use Flash Card Mode to display large letters as they are sent
- Toggle dot-dash display for reference

Morse code is an **audible language**—be sure to turn off the visual dot-dash display as soon as you can.

**Practice at least 15 minutes per day.**  
Do not move to the next week’s letters until you can copy the current week’s letters confidently.

When you have memorized all letters, numbers, and punctuation, you can practice with mixed random selections.

**GOOD LUCK—ENJOY LEARNING!**

---

## Revision History

**v2.0 – July 5, 2025**
- Refactored menu structure with submenus
- Added Ctrl+C handling to stop sending and return to the main menu
- Added random numbers and punctuation practice
- Added week-specific random words and sentences
- Improved settings handling
- Added clean exit option (menu option 9)

---

## Requirements

- Python 3
- [pygame](https://www.pygame.org/)
- numpy

---

## Installation

Follow the steps below for your platform.

---

### Windows

1. Install Python 3 from [python.org](https://www.python.org/).
2. Open **Command Prompt**.
3. Install dependencies:

    ```sh
    pip install pygame numpy
    ```

4. (Optional) Create a virtual environment:

    ```sh
    python -m venv pyEnv
    pyEnv\Scripts\activate
    ```

---

### macOS and Linux

1. Make sure Python 3 is installed:

    ```sh
    python3 --version
    ```

2. Install dependencies:

    ```sh
    pip3 install pygame numpy
    ```

3. (Optional) Create a virtual environment:

    ```sh
    python3 -m venv pyEnv
    source pyEnv/bin/activate
    ```

---

## Running the Program

Navigate to the folder containing `morsecode.py`.

**Windows:**

```sh
python morsecode.py
```

**macOS and Linux:**

```sh
python3 morsecode.py
```

---

## Example Screen Output

```
Morse Code Trainer - Main Menu
1. Practice Week Letters
2. Random Word
3. Random Sentence
4. Random Call Sign
5. Random Numbers (0123456789)
6. Random Punctuation (.,?/)
7. Enter Custom Text
8. Settings
9. Exit
Display: ON | Flash: OFF | WPM: 10 | Frequency: 700Hz
Choice:
```

While sending, the program will display:

```
Sending: E (.)
```

---

## Using the Program

**Main Menu Options:**
- **1. Practice Week Letters:** Sends letters from a specific week's group randomly.
- **2. Random Word:** Sends 3 randomly selected words.
- **3. Random Sentence:** Sends a randomly selected sentence.
- **4. Random Call Sign:** Sends a randomly selected ham call sign.
- **5. Random Numbers:** Sends numbers randomly.
- **6. Random Punctuation:** Sends punctuation marks randomly.
- **7. Enter Custom Text:** You type anything, and it will send it back in Morse code.
- **8. Settings:** Adjust frequency, WPM, display options, and flash card mode.
- **9. Exit:** Close the program.

---

## Exiting the Program

- **To stop sending and return to the main menu:**  
  Press **Ctrl+C**
- **To exit completely:**  
  Select **menu option 9**

---

