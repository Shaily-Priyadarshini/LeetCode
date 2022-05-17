#{ 
#Driver Code Starts

 # } Driver Code Ends
def reverse(S):
    s=Stack()
    for i in S:
        s.push(i)
    stri=""
    while s.size()!=0:
        x=s.pop()
        stri+=x

    return stri
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Stack:
    def __init__(self):
        self.__head=None
        self.__count=0

    def push(self, item):
        newnode=Node(item)
        if self.__head is None:
            self.__head=newnode
        else:
            newnode.next = self.__head
            self.__head=newnode
        self.__count += 1
        return

    def pop(self):
        if self.__count==0:

            return -1
        self.__count-=1
        x=self.__head.data
        self.__head=self.__head.next
        return x

    def top(self):
        if self.__count==0:

            return -1
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count== 0

    #Add code here

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
#} Driver Code Ends