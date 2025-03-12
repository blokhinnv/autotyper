import keyboard
import pyautogui
import pyperclip
from tqdm import tqdm

if __name__ == "__main__":
    print("waiting for F10 to be pressed...")
    keyboard.wait("f10")
    text_to_type = pyperclip.paste()
    for char in tqdm(text_to_type):
        pyautogui.typewrite(char)

    print("Text typed.")
