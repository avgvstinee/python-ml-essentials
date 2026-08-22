from dataclasses import dataclass

@dataclass
class Book :
    title: str
    author: str
    year: int


b = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', year=1925)
print(b)  # Output: Book(title='The Great Gatsby', author='F. Scott Fitzgerald', year=1925)