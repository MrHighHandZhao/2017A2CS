#S3C2 Carl Zhao Dictionary

NullPointer=-1
Max=1000
def Hashing(NewItem):
    i=ord(NewItem[1])
    return i

class Node:
    def _init_(self):
        self.Value = Value
        self.key= key

class HashTable:
    def _init_(self):
        self.record=[]
        NewNode= None

        for i in range (1000):
            NewNode=Node()
            self.record.append(NewNode)


    def insert(self,NewItem,Defination):
        i=Hashing(NewItem)
        self.key=[]
        while self.key!=None:
            i=i+1
            if i>=Max-1:
                i=0
        HashTable.record[i].key=NewItem
        HashTable.record[i].value=Defination

    def findRecord(SearchItem):
        i=Hashing(SearchItem)
        while (self.record[i].key!=SearchItem) and (self.record[index].key!=None):
            i=i+1
            if i>Max:
                i=0
            if self.record[i].key!=None:
                print(self.record[i].Value)

l=HashTable()
l.insert("aa","bb")
print(l,findRecord("aa"))
