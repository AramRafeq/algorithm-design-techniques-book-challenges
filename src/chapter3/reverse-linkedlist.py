# this code is not correct
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next = next
def printList(head):
    print(head.data)
    if head.next == None:
        return
    return printList(head.next)

def reverseList(head):
    if head.next == None: 
        return head
    nextnext = head.next.next
    head.next = nextnext
    head = head.next
  
    return reverseList(head)
head = Node(3)
n2 = Node(2)
head.next = n2
n3 = Node(1)
n2.next = n3

printList(head)
printList(reverseList(head))
