##Reverse a linked list using recursion.

##Example :
##Given 1->2->3->4->5->NULL,

##return 5->4->3->2->1->NULL.

def Reverse_List_Recursion(self, p):
        if p.next is None:
            self.head = p
            return
        self.Reverse_List_Recursion(p.next)
        q = p.next
        q.next = p
        p.next = None
        
    def reverseList(self, p):
        self.head = p
        self.Reverse_List_Recursion(p)
        return self.head
