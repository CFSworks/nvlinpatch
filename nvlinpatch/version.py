from .signature import Signature

class Version(Signature):
    def __init__(self, ver, sig):
        super(Version, self).__init__(sig._data, sig._mask)
        self.ver = ver
        self._patches = []

    def add_patch(self, patch):
        self._patches.append(patch)
