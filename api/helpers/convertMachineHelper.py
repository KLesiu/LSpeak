import base64
import io
from typing import BinaryIO


def base64_to_binary_io(base64_string: str) -> BinaryIO:
    # Dekodowanie danych base64
    binary_data = base64.b64decode(base64_string)
    # Tworzenie obiektu BinaryIO z danych binarnych
    binary_io = io.BytesIO(binary_data)
    return binary_io