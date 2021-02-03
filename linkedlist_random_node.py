class randNode():
    def __init__(self,val=None):
        self.val = val
        self.rand = None
        self.next = None


def copy_random_list(head):
     cur = head
     while (cur != None):   #复制每个节点
         next = cur.next
         cur.next = randNode(cur.val)
         cur.next.next = next
         cur = next

     cur = head
     while (cur != None):  #设置随机指针
         cur.next.rand = None if cur.rand else cur.rand.next
         cur = cur.next.next

     CopyHead = head.next
     cur = head
     while cur != None:    #拆开
         next = cur.next
         cur.next = next.next
         next.next = None if next.next == None else next.next.next
         cur = cur.next
     return CopyHead
