class LibraryItem:
        def __init__(self,t,a,i):
            self.__Title=t
            self.__Author_Artist = a
            self.__ItemID = i
            self.__OnLoan = False
            self.__DueDate = datetime.date.today()
            self.__BorrowerID = 0


        def Borrowing(self, b):
                self.__OnLoan = True
                self.__DueDate = self.__DueDate +datetime.timedelta(weeks=3）
                self.__BorrowerID = b

        def PrintDetails(self):
                print(self.__Title, ' ; ',self.__Author_Artist, ' ; ', end='')
                print(self.__ItemID, ' ; ', self.__OnLoan)
                print(self.__DueDate, ' ; Borrower: ',self.__BorrowerID)

        def main():
                ThisBook = Book("Counter Strike", "Gabe", 1234)
                ThisBook.PrintDetails()
                NewBorrower = Borrower("Ken Su", "KenIsStupid@163.com", 123)
                ThisBook.Borrowing(123)
                NewBorrower.UpdateItemsOnLoan(1)
                ThisBook.PrintDetails()
                NewBorrower.PrintDetails()
