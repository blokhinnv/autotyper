import keyboard
import pyautogui
import pyperclip
from tqdm import tqdm

qwerty = r"""`qwertyuiop[]asdfghjkl;'zxcvbnm,.~QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""
ycuken = "ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"


assert len(set(qwerty)) == len(qwerty)
assert len(set(ycuken)) == len(ycuken)

assert len(qwerty) == len(ycuken)
# join as keys and values
tr = dict(zip(ycuken, qwerty))

ESCAPE_CHAR = "$"


def translate(key: str) -> str:
    """Returns qwerty key or the given key itself if no mapping found"""
    return "".join(map(lambda x: tr.get(x, x), key))


def escape_char(c: str) -> str:
    return f"{ESCAPE_CHAR}{c}"


def escape_eng_chars(s: str) -> str:
    r = []
    for c in s:
        if c in ycuken:
            r.append(translate(c))
        elif c == "\n":
            r.append(c)
        else:
            r.append(escape_char(c))
    return "".join(r)


if __name__ == "__main__":
    print("waiting for caps lock to be pressed...")
    keyboard.wait("f10")
    text_to_type = pyperclip.paste()
    # Simulate typing each character of the text
    text_to_type = escape_eng_chars(text_to_type)
    for char in tqdm(text_to_type):
        char = translate(char)
        pyautogui.typewrite(char)

    # keyboard.press("ctrl+s")
    print("Text typed.")
