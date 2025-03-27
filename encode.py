import base64
import zlib

import keyboard
import pyautogui
import pyperclip
from tqdm import tqdm


def compress_text(text: str) -> str:
    b64 = base64.b64encode(zlib.compress(text.encode(), level=9))
    b64_text = b64.decode()
    return b64_text


if __name__ == "__main__":
    print("waiting for F10 to be pressed...")
    print("don't forget to copy text into clipboard!")
    keyboard.wait("f10")
    text_to_type = pyperclip.paste()
    compressed_text = compress_text(text_to_type)
    print(
        f"info: original text length: {len(text_to_type)}; compressed text length: {len(compressed_text)}"
    )
    for char in tqdm(compressed_text):
        pyautogui.typewrite(char)

    print("Text typed.")
