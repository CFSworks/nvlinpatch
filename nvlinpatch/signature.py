class Signature(object):
    def __init__(self, data, mask):
        self._data = data
        self._mask = mask
        self._size = len(self._data)
        assert len(self._mask) == self._size

    def size(self):
        return self._size

    def match(self, input):
        if len(input) != self._size: return False
        if self._mask == '\xff'*self._size: return input == self._data
        for i,x in enumerate(input):
            if ord(self._data[i]) != ord(x)&ord(self._mask[i]):
                return False
        return True

    def find(self, input, start=0):
        if self._mask == '\xff'*self._size: return input.find(self._data, start)
        for offset in range(start, len(input)-self._size+1):
            if self.match(input[offset:offset+self._size]):
                return offset
        return -1

    def patch(self, input):
        out = ''
        for i,d,m in zip(input, self._data, self._mask):
            out += chr(ord(i)&(0xFF^ord(m)) | ord(d)&ord(m))
        out += input[self.size():]
        return out

def sig_raw(s):
    return Signature(s, '\xff'*len(s))

def sig_hex(s):
    s = s.replace(' ','')
    hex_data = ''
    hex_mask = ''
    for c in s:
        if c == '?':
            hex_data += '0'
            hex_mask += '0'
        else:
            hex_data += c
            hex_mask += 'F'
    return Signature(hex_data.decode('hex'), hex_mask.decode('hex'))
