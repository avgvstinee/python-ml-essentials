
class Book :
    def __init__(self,title,publisher,pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class EBook(Book):
    def __init__(self,title,publisher,pages,format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_
        
    
""""
Three of the input parameters for Book are duplicated in Ebook. 
This is quite bad practice because we now have two sets of instructions that are doing the same thing. 
Moreover, any change in the signature of Book.__init__() will not be reflected in Ebook. 
We know that Ebook Is-A Book, and therefore we probably want changes to be reflected in the child classes.

”"""
