class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def makeNode(list):
    a = Node(list[0])
    if len(list) > 1:
        b = a
        for i in range(1, len(list)):
            b.next = Node(list[i])
            b = b.next
    return a

def kunjungi(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next

def cari(head, yang_dicari):
    temp = head
    while temp is not None:
        if temp.data == yang_dicari:
            return temp
        temp = temp.next
    return Node(None)


def tambahdepan(head):
    temp = Node('tambah depan', head)
    return temp


def tambahAkhir(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = Node('tambah akhir')
    return head


def tambah(head, posisi):
    """Menambahkan simpul sebelum posisi"""
    temp = head
    while temp is not None:
        if temp.next.data == posisi:
            temp_belakang = temp.next
            temp.next = Node('tambah tengah', temp_belakang)
            return head
        temp = temp.next
    return None


def hapus(head, posisi):
    temp = head
    while temp is not None:
        if temp.next.data == posisi:
            temp_belakang = temp.next.next
            temp.next = temp_belakang
            return head
        temp = temp.next
    return head

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
