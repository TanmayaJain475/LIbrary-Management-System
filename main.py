class Library:
    def __init__(self , listofbooks):
        self.books = listofbooks
        
    def displayAvailablebooks(self):
        print("books Present In this library are: ")
        for book in self.books:
            print(" *" + book)
    def borrowbook(self, bookName):
        if bookName in self.books:
            print(f"You Have been issued {bookName}. Please keep it safe and return in within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry this book is either not available or has been issued please wait until the book is available")
            return False
    def returnbook(self, bookName):
        self.books.append(bookName)
        print("Thanks For returning this book!! Hope You Enjoy It Lot")
    def donatebook(self, bookName):
        self.books.append(bookName)
        print("Thanks for donating this book to the library!!! Have A great day Ahead!")
class Student:
    def requestbook(self):
        self.book = input("Enter The Name of The book you want to borrow: ")
        return self.book
    def returnbook(self):
        self.book = input("Enter The Name of The book you want to return: ")
        return self.book
    def donatebook(self):
        self.book = input("Enter The name of the book you want to donate: ")
        return self.book
if __name__ == '__main__':
    CentralLibrary = Library(["The Golden Compass. by Philip Pullman",
                              "Don Quixote. by Miguel de Cervantes",
                              "The Satanic Verses. by Salman Rushdie",
                              "The Lord of the Rings. by J.R.R. Tolkien",
                              "The Shadow of the Wind. by Carlos Ruiz Zafon",
                              "Ulysses. by James Joyce",
                              "Song of Solomon. by Toni Morrison",
                              "War and Peace. by Leo Tolstoy", ])
    student = Student()
    # CentralLibrary.displayAvailablebooks()
    while (True):
        welcomemsg = '''\n    =====Welcome To The Central Library========
        please choose an option:
        1. list of books
        2. request a book 
        3. return a book
        4. donate a book
        5. exit the library
        '''
        print(welcomemsg)
        a = int(input("Enter A Choice: "))
        if a == 1:
            CentralLibrary.displayAvailablebooks()
        elif a ==2:
            CentralLibrary.borrowbook(student.requestbook())
        elif a == 3:
            CentralLibrary.returnbook(student.returnbook())
        elif a == 4:
            CentralLibrary.donatebook(student.donatebook())
        elif a == 5:
            print("Thanks For Choosing central library.have a great day ahead")
            exit() 
        else:
            print("Invalid choice!! ")