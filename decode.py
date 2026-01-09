import base64
import getpass
import zlib
from pathlib import Path


def decode_text(text: str) -> str:
    return zlib.decompress(base64.b85decode(text)).decode()


if __name__ == "__main__":
    username: str = getpass.getuser()
    postman_path = Path(f"postman/{username}")
    postman_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(postman_path / "in.txt", encoding="utf8") as fp:
        text: str = fp.read()
        decoded: str = decode_text(text)
        with open(postman_path / "out.txt", "w", encoding="utf8") as fp:
            fp.write(decoded)
        print("package received and decoded")
