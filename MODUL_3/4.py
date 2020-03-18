# a
class Node1(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


a = Node1(11)
b = Node1(12)
c = Node1(13)
d = Node1(14)


def cetakDepan():
    a.next = b
    b.next = c
    c.next = d
    print(a.data)
    print(a.next.data)
    print(a.next.next.data)
    print(a.next.next.next.data)


def cetakBelakang():
    d.prev = c
    c.prev = b
    b.prev = a
    print(d.data)
    print(d.prev.data)
    print(d.prev.prev.data)
    print(d.prev.prev.prev.data)


# b
class Node(object):
    def __init__(self, nama, next=None):
        self.data = nama
        self.next = None
        self.prev = None


a = Node(37)
b = Node(38)
c = Node(39)
d = Node(40)


def tambahdepan():
    a.next = b
    b.next = c
    c.next = d
    i = input("Masukan nilai tambahan untuk simpul diawal: ")
    L = Node(i)
    L.next = a
    print(L.data)
    print(L.next.data)
    print(L.next.next.data)
    print(L.next.next.next.data)
    print(L.next.next.next.next.data)


# c
class Node(object):
    def __init__(self, nama, next=None):
        self.data = nama
        self.next = None
        self.prev = None


def tambahAkhir():
    i = input("Masukan nilai tambahan untuk simpul diakhir: ")
    a = Node(37)
    b = Node(38)
    c = Node(39)
    d = Node(40)
    L = Node(i)
    d.prev = c
    c.prev = b
    b.prev = a
    L.prev = d
    print(L.prev.prev.prev.prev.data)
    print(L.prev.prev.prev.data)
    print(L.prev.prev.data)
    print(L.prev.data)
    print(L.data)
