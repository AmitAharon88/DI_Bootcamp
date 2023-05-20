class Pagination :
    def __init__(self, items= None, pageSize= 10) :
        self.items = items
        self.pageSize = int(pageSize)
        self.current_page = 1

    
    def createPages(self) :
        sublist = [self.items[i:i+self.pageSize] for i in range(0, len(self.items), self.pageSize)]
        return sublist
        

    def getVisibleItems(self) :
        sublist = self.createPages()
        visiblePage = sublist[self.current_page-1]
        # print(visiblePage)
        return visiblePage
            
    def prevPage(self) :
        sublist = self.createPages()
        visiblePage = self.getVisibleItems()
        if sublist.index(visiblePage) > 0 :
            prevPage_index = sublist.index(visiblePage) - 1
            previousPage = sublist[prevPage_index]
            print(previousPage)
            return previousPage
        else :
            print('You are on the first page. There is no previous page.')
    
    def nextPage(self) :
        sublist = self.createPages()
        visiblePage = self.getVisibleItems()
        if sublist.index(visiblePage) < len(self.items) :
            nextPage_index = sublist.index(visiblePage) + 1
            next_page = sublist[nextPage_index]
            print(next_page)
            return next_page
        else :
            print('You are on the last page. There is no next page.')
    
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
x.nextPage()
x.nextPage()
x.firstPage()
x.lastPage()
x.goToPage(4)