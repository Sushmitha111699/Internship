class Library:
    def __init__(self, books):
        self.books = books

    def __contains__(self, item):
        return item in self.books
library = Library(["Python", "Java", "C++", "Data Science"])
print("Python" in library)
print("AI" in library)
