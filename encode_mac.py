import base64
import time
import zlib

import pyautogui
import pyperclip
from pynput import keyboard
from tqdm import tqdm


def compress_text(text: str) -> str:
    b64 = base64.b64encode(zlib.compress(text.encode(), level=9))
    b64_text = b64.decode()
    print(b64_text)
    return b64_text


def switch_to_english_layout() -> None:
    """Переключает раскладку клавиатуры на английскую (US) на macOS"""
    try:
        # Переключаем раскладку через Cmd+Space (стандартная комбинация на macOS)
        pyautogui.hotkey("ctrl", "space")
        time.sleep(0.3)  # пауза для переключения
        print("Раскладка переключена на английскую")
    except Exception as e:
        print(f"Не удалось переключить раскладку: {e}")


if __name__ == "__main__":
    print("waiting for F10 to be pressed...")
    print("don't forget to copy text into clipboard!")

    # 1. Берем содержимое буфера обмена
    text_to_type = pyperclip.paste()
    compressed_text = compress_text(text_to_type)
    print(
        f"info: original text length: {len(text_to_type)}; compressed text length: {len(compressed_text)}"
    )
    print("Текст из буфера сохранён.")
    print("Нажмите F10 для начала печати...")

    def on_press(key: keyboard.Key | keyboard.KeyCode) -> bool | None:
        try:
            # 2. Ждём нажатия F10
            if key == keyboard.Key.f10:
                print("Печать началась...")
                time.sleep(1.0)  # задержка 1 секунда перед началом печати

                # Переключаем на английскую раскладку
                # switch_to_english_layout()

                # 3. Печатаем символ за символом с прогресс-баром
                for char in tqdm(compressed_text, desc="Печать", unit="симв"):
                    pyautogui.typewrite(char, interval=0.01)
                print("Готово.")
                return False  # останавливаем listener
        except Exception as e:
            print(e)
        return None

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
