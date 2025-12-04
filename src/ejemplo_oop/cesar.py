from collections.abc import Callable

class Cesar:

    def __init__(self, key: int):
        self._key = key % 256

    @property
    def key(self) -> int:
        return self._key
    
    @key.setter
    def key(self, key: int) -> None:
        self._key = key

    def __displace_ascii(self, msg: str, op: Callable[[int,int], int]) -> str:
        ascii_chars = [ord(c) for c in msg]
        def adjust_ascii(c: int) -> int:
            if c > 255:
                c = c % 256
            elif c < 0:
                c = 256 + c
            return c
        ascii_chars_moved = list(map(lambda c: adjust_ascii(op(c, self.key)), ascii_chars))
        new_chars = [chr(c) for c in ascii_chars_moved]
        print(f"{ascii_chars} -> {ascii_chars_moved}")
        return "".join(new_chars)

    def encriptar(self, msg: str) -> str:
        return self.__displace_ascii(msg, lambda a,b: a+b)
    
    def desencriptar(self, msg: str) -> str:
        return self.__displace_ascii(msg, lambda a,b: a-b)
    
if __name__ == "__main__":
    msg = "Una loba en el armario"
    cs = Cesar(200)
    msg_encript = cs.encriptar(msg)
    msg_desencript = cs.desencriptar(msg_encript)

    print(f"Mensaje original: {msg}")
    print(f"Mensaje encriptado: {msg_encript}")
    print(f"Mensaje desencriptado: {msg_desencript}")