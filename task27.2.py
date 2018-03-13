import datetime
class LibraryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author__Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate=datatime.date.today()

    def GetTitle(self):
        return(self.__Title)
    def Borrowing(self):
        self.__OnLoan=True
        self.__DueDate=self.__DueDate+datetime,timedelta(weeks=3)
    def Returning(self):
        self.OnLoan=False
    def PrintDeatiles(self):
        print(self.Title,';',self.__Author__Artist,';',end='')
        print(self.__ItemID,';',self.__OnLoan,';',self.__DueDate)
class Book(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__IsRequested=False
        self.__RequestedBy=0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self):
        self.__IsRequested=True
class CD(LibraryItem):
    def __init__(self,t,a,i):
        LibraryItem.__init__(self,t,a,i)
        self.__Genre=""
    def GetGenre(self):
        return(self.Genre)
    def SetGenre(self,g):
        self.Genre=g

def main():
    ThisBook=Book("The Legend of ChuLiuXiang","GuLong",7777)
    ThisCD=CD("Hey Jude","Beatles",8888)
    ThisBook.PrintDeatiles
    ThisCD.PrintDeatiles
