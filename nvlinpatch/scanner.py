class Scanner(object):
    def __init__(self):
        self._signatures = set()

    def add_signature(self, sig):
        self._signatures.add(sig)

    def scan(self, file):
        size = 1024
        buf = ''
        offset = 0
        file.seek(0)
        while True:
            data = file.read(size)
            if data == '': break
            buf += data
            if len(buf) > size*2:
                offset += len(buf) - size*2
                buf = buf[-size*2:]
            for sig in self._signatures:
                found = sig.find(buf)
                if found != -1 and found < size:
                    yield (found+offset, sig)
