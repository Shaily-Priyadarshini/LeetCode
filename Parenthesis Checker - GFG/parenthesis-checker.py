
#User function Template for python3
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
        self.__head=self.__head.next
        return

    def top(self):
        if self.__count==0:

            return -1
        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count== 0
       
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        s=Stack()
        for i in x:
            if i=="{" or i=="(" or i=="[":
                s.push(i)
            elif i==")":
                if s.top()!="(":
                    return False
                s.pop()
            elif i=="}":
                if s.top()!="{":
                    return False
                s.pop()
            elif i=="]":
                if s.top()!="[":
                    return False
                s.pop()
        
        return s.isEmpty()
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends