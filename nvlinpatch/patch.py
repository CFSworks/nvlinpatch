class Patch(object):
    def __init__(self, name, from_sig, to_sig, multi_ok=False):
        self.name = name
        self._from_sig = from_sig
        self._to_sig = to_sig
        self.multi_ok = multi_ok

    def size(self):
        return self._from_sig.size()

    def match(self, input):
        return self._from_sig.match(input)

    def find(self, input, start=0):
        return self._from_sig.find(input, start)

    def patch(self, input):
        assert self.match(input)
        return self._to_sig.patch(input)
