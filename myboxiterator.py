class MyBoxIterator:
    def __init__(self,android):
        self.oppo=android

    def __iter__(self):
        return self

    def __next__(self):
        if self.oppo is None:
            raise StopIteration
        else:
            data=self.oppo.data
            self.oppo=self.oppo.next
        return data    
