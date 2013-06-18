from .scanner import Scanner

class PatchError(Exception): pass

class Patcher(object):
    def __init__(self):
        self._patches = set()

    def add_patch(self, patch):
        self._patches.add(patch)

    def patch(self, file):
        s = Scanner()
        for p in self._patches:
            s.add_signature(p)

        scanned = list(s.scan(file))

        found_patches = set()
        for offset, patch in scanned:
            if not patch.multi_ok and patch in found_patches:
                raise PatchError('patch %s signature found multiple times' %
                                 patch.name)
            found_patches.add(patch)

        if found_patches != self._patches:
            missing_names = [p.name for p in self._patches-found_patches]
            raise PatchError('some patch signatures not found in file: %s' %
                             ', '.join(missing_names))

        for offset, patch in scanned:
            file.seek(offset)
            patched = patch.patch(file.read(patch.size()))
            file.seek(offset)
            file.write(patched)
