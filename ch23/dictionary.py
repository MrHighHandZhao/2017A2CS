#S3C2 Carl Zhao Computer Science Homework

NullPointer = -1

class Node():
    def __init__(self):
        
        self.Data = ""

        self.NPointer = NullPointer

class linkedList():
    def _init_(self):

        self.SPointer = NullPointer

        self.FPointer = 0

        self.record = []

        newNode = None
        
        for i in range(10):

            newNode = Node()

            NewNode.NPointer = i + 1

            self.record.append(NewNode)

        NewNode.NPointer = NullPointer


     def InsertNode(self):

        if FPointer!=NullPointer:

            NewPointer=FPointer

            self.record[NewPointer],Data=NewItem

            FPointer=self.record[FPointer].Pointer

            CPointer= SPointer

            while CPointer!=NullPointer and self.record[CPointer].Data < NewItem:

                PPointer= CPointer

                CPointer=self.record[CPointer].Pointer

            if PPointer= SPointer:

                self.record[NewPointer].Pointer=SPointer

                SPointer=NewPointer

            else:

                self.record[NewPointer].Pointer=self.record[PPointer].Pointer

                self.record[PPointer].Pointer=NewPointer


        


    def FindNode(self):
        

        CPointer=SPointer

        while CPointer!= NullPointer and self.record[CPointer]!= NewItem:

            CPointer!=self.record[CPointer].NPointer

            return CPointe

    def outputNode(self):

        CPointer = self.SPointer

        while CPointer != NullPointer:

            print(self.record[CPointer].Data, end = ",")

            CPointer = self.record[CPointer].NextPointer


    def printList(self):

        for i in range(10):

            print(self.record[i].Data, self.record[i].NPointer)


    def insertNode(self):

        if FPointer != NullPointer:

            NewPointer = FPointer

            self.record[NewPointer].Data = NewItem

            FPointer = self.record[FPointer].NPointer

            PPointer = NullPointer                        


            while (CPointer != NullPointer) and (self.record[CPointer].Data < NewItem):

                PPointer = CPointer

                CPointer = self.record[CPointer].NPointer

            if PPointer == NullPointer:                  

                self.record[NewPointer].NPointer = SPointer

                SPointer = NewPointer

            else:

                self.record[NewPointer].NPointer = self.record[PPointer].NextPointer


                self.record[PPointer].NextPointer = NewPointer

                
            
        



l = linkedList()
l.insertNode(5)
l.insertNode(25)
l.insertNode(15)
l.insertNode(35)
l.printList()                
            
            
            
