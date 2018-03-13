class Borrower():
    def __init__(self,n,e,b):
        self.__BorrowerName=n
        self.__EmailAddress=e
        self.__BorrowerID=b
        self.__ItemOnLoan=0

        def GetBorrowerName(self):
            return (self.__BorrowerName)
        def GetEmailAddress(self):
            return (self.__EmailAddress)
        def GetBorrowerID(self):
            return (self.__BorrowerID)
        def GetItemsOnLoan(self):
            return (self.__ItemOnLoan)
        def UpdateItemsOnLoan(self,n):
            self.__ItemsOnLoan += n

        def PrintDeatiles(self):
            print("Borrower:",self.__BorrowerName)
            print("ID:",self.__EmailAddress)
            print("EmailAddress:",self.__BorrowerID)
            print("Items on Loan:",self.__ItemOnLoan)
