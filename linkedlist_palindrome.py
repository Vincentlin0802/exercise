class Node(object):
    def __init__(self,value = None, next = None):
        self.value = value
        self.next = next


class linked_list(object):
    def __init__(self,mxsize = None):
        self.maxsize = mxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def append(self,arr):
        for i in range(len(arr)):
            value = arr[i]
            node = Node(value)
            tailnode = self.tailnode
            if tailnode is None:
                self.root.next = node
            else:
                self.tailnode.next = node
            self.tailnode = node
            self.length += 1

    def ispalindrome(self,head):
        slow = self.head
        fast = self.head
        while (slow.next != None and fast.next.next != None):  # 找到链表中间的节点
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None
        while (fast != None):  # 反转后半部分的链表
            tmp = fast.next
            fast.next = slow
            slow = fast
            fast = tmp

        tmp = slow
        fast = head
        while (slow != None and fast != None):  # 确认回文的结构
            if (slow.value != fast.value):
                print("False")
            slow = slow.next  # 从左边到中间
            fast = fast.next  # 从右边到中间

        print("True")

if __name__ == '__main__':
    a = [1,2,3,4,5]
    h = 1

l = linked_list()
l.append(a)
linked_list.ispalindrome(a,h)