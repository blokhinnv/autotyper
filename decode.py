import getpass
from pathlib import Path

qwerty = r"""`qwertyuiop[]asdfghjkl;'zxcvbnm,.~QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>"""
ycuken = "ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"

char_translation_dict = dict(zip(qwerty, ycuken))
assert len(qwerty) == len(ycuken)

ESCAPE_CHAR = "$"


def translate_char(key: str) -> str:
    return "".join(char_translation_dict.get(x, x) for x in key)


def translate_text(text: str) -> str:
    skip_next_translation = False
    chars: list = []
    for idx in range(len(text)):
        c: str = text[idx]
        if c != ESCAPE_CHAR and not skip_next_translation:
            chars.append(translate_char(c))
        elif c != ESCAPE_CHAR and skip_next_translation:
            chars.append(c)
            skip_next_translation = False
        elif c == ESCAPE_CHAR:
            skip_next_translation = True
    return "".join(chars)


if __name__ == "__main__":
    username: str = getpass.getuser()
    postman_path = Path(f"postman/{username}")
    postman_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(postman_path / "in.txt", encoding="utf8") as fp:
        text: str = fp.read()
        translated: str = translate_text(text)
        with open(postman_path / "out.txt", "w", encoding="utf8") as fp:
            fp.write(translated)
        print("package received and translated")
