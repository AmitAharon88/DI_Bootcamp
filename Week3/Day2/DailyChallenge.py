class Pagination :
    def __init__(self, items= None, pageSize= 10) :
        self.items = items
        self.pageSize = (pageSize)
    
    def createPages(self) :
        sublist = [self.items[i:i+self.pageSize] for i in range(0, len(self.items), self.pageSize)]
        return sublist

    def getVisibleItems(self) :
        sublist = self.createPages()
        visiblePage = sublist[self.pageNum]
        print(visiblePage)
        return visiblePage
            
    def prevPage(self) :
        sublist = self.createPages()
        visiblePage = self.getVisibleItems()
        if sublist.index(visiblePage) > 0 :
            prevPage_index = sublist.index(visiblePage) - 1
            print(sublist[prevPage_index])
            return 
        else :
            print('You are on the first page. There is no previous page.')

    
    def nextPage(self) :
        sublist = self.createPages()
        nextPage_index = sublist.index(visiblePage) - 1
        print(sublist[self.pageNum+1])
    
    def firstPage(self) :
        sublist = self.createPages()
        print(sublist[0])
        
    def lastPage(self) :
        sublist = self.createPages()
        print(sublist[-1])
        
    def goToPage(self, pageNum) :
        sublist = self.createPages()
        if pageNum > 0 :
            my_page = sublist[pageNum-1]
        else :
            my_page = sublist[pageNum]
        print(my_page)
        return my_page

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
x = Pagination(alphabetList, 5)

x.getVisibleItems()
x.prevPage()
x.nextPage()
x.firstPage()
x.lastPage()
x.goToPage(4)
