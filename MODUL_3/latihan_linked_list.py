class Node(object):
    """ Sebuah simpul di linked list """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # Menambah Simpul di depan
    def tambah(self, new_data):
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node

# Mengunjungi Setiap Simpul dari Depan
def kunjungi(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next
