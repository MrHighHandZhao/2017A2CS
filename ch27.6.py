class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0
    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self, b):
        self.__IsRequested = True
        self.__RequestedBy = b
    def PrintDetails(self):
         PrintDetails(self):
         print("Book Details")
         LibraryItem.PrintDetails(self)
         if self.__IsRequested :
            print('Requested by ', self.__RequestedBy)
         else :
            print('no requests')


