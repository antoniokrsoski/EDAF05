import hashlib as h
# implement dict class from scratch

class Dictionary():

    def __init__(self):
        self.size = 0

    def hash(self, value: str):
        m = h.sha256()
        m.update(value.encode('utf-8'))
        return m.hexdigest()
    


if __name__ == "__main__":
    d = Dictionary()
    print(d.hash("test"))

    
