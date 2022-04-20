class Llnode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Llist:
    def __init__(self):
        self.head = None
    def print(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
    def insert_at_beginning(self, val):
        newnode = Llnode(val)
        newnode.next = self.head
        self.head = newnode
    def insert_at_end(self, val):
        newnode = Llnode(val)
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode
    def insert_middle(self, val, prev):
        newnode = Llnode(val)
        newnode.next = prev.next
        prev.next = newnode
    def remove(self, val):
        curr = self.head
        if curr.val == val:
            self.head = curr.next
            curr = None
        curr = curr.next
        prev = self.head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            prev = curr
            curr = curr.next



days = Llist()
days.head = Llnode("Mon")
e2 = Llnode("Tues")
e3 = Llnode("Wed")
days.head.next = e2
e2.next = e3

days.insert_at_beginning("Sun")

days.insert_at_end("Thurs")

days.insert_middle("AHHHH", days.head.next.next)

days.remove("AHHHH")
days.remove("Wed")
days.remove("Tues")
days.remove("Thurs")
days.print()
