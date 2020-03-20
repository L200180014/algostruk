class node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def cariLinkedList(self, dicari):
        curNode = self
        while curNode is not None:
            if curNode.next is not None:
                if curNode.data != dicari:
                    curNode = curNode.next
                else:
                    print ("Data ", dicari, "ada dalam linked list")
                    break
            elif curNode.next is None:
                print ("Data ", dicari, "tidak ada dalam linked list")
                break

# a = node(12)
# menu = a
# a.next = node(34)
# a = a.next
# a.next = node(10)
# a = a.next
# a.next = node(45)

# menu.cariLinkedList(10)
# menu.cariLinkedList(110)
