class Book:
    def __init__(self, title, author, description,read=0,id=None):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.read = read
    