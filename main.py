from box_class import mybox, myboxiterator

cls=mybox()

mbi=myboxiterator(1)
cls.add(mbi)
mbi=myboxiterator(2)
cls.add(mbi)
mbi=myboxiterator(3)
cls.add(mbi)
cls.remove(2)

for data in cls:
    print(data)
