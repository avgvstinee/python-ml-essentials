
class Book :
    def __init__(self, title,publisher,pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book) :
    def __init__(self, title,publisher,pages,format_):
        super().__init__(title,publisher,pages)
        self.format_ = format_


ebook = Ebook('Learn Python Programming', 'Packt Publishing', 500, 'PDF')
print(ebook.title)
print(ebook.publisher)
print(ebook.pages)
print(ebook.format_)


"""
super( ) used to access and call methods from a parent or sibling class. 
It returns a temporary proxy object that delegates method calls to the correct class in your inheritance hierarchy, 
eliminating the need to hardcode specific parent class names.

"""