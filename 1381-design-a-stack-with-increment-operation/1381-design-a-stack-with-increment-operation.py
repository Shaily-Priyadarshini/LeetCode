class CustomStack:
      

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.a=[]
        self.count=0
        

    def push(self, x: int) -> None:
        if self.count<self.maxSize:
            self.a.append(x)
            self.count+=1
        return
        
        

    def pop(self) -> int:

        if self.count==0:
            return -1
        self.count-=1
        return(self.a.pop())
    def increment(self, k: int, val: int) -> None:
        if self.count<k:
            for i in range(len(self.a)):
                self.a[i]=self.a[i]+val
            return
        for i in range(0,k):
            self.a[i]+=val
        return
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)