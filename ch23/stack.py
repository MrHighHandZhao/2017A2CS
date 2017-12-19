#S3C2 Carl Zhao Stack
class stack:
    def _init_(self):
        self.items=""      

    def putItemIn(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def itemsOut(self):
        del self.items[]

    def order(self):
        return len(self.items)

    def empty(self):
        return self.order()==0

    def top(self):
        return self.items[self.order()-1]

    
