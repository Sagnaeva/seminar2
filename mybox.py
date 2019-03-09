from myboxiterator import MyBoxIterator

class Mybox:
    def __init__(self):
        self.iphone=iphone
        self.samsung=samsung
        self.nokia

    def __len__(self):
        return len (self.iphone)

    def add (self,android):
        self.oppo.append (android)

    def remove (self,android):
        assert android in self.oppo
        idx=self.oppo.index(android)
        return self.oppo.pop(idx)

    def __contains__(self,android):
        return android in self.oppo

    def __iter__(self,android):
        return myboxiterator(self.oppo)
