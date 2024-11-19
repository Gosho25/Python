#class Book:
#    def __init__(self, title, genre, price, year):
#        self.title = title
#        self.genre = genre
#        self.price = price
#        self.year = year

#    def discount(self):
#        if 2017 <= self.year <= 2021:
#            self.price -= self.price*0.05  
#        elif self.year < 2017:
#            self.price -= self.price*0.10
#        else:
#            print("No discount") 


#    def delete_books(book_list, genre, price):
#        return [book for book in book_list if not (book.genre == genre and book.price == price)]


#    def average_price(book_list, year):
#        prices = list(filter(lambda book: book.year > year, book_list))
#        return sum(book.price for book in prices) / len(prices) if prices else 0.0

#print("-------------------------------------------")
#book1 = Book("Снежанка", "приказка", 12.90, 2001)
#book2 = Book("Java", "информативна", 18.90, 1999)
#book3 = Book("Куджо", "приказка", 22.00, 2017)
#book4 = Book("Das Auto", "роман", 14.00, 2024)
#book5 = Book("Снежни братя", "роман", 9.00, 2001)
#book6 = Book("Кери", "роман", 17.00, 2015)

#books = [book1, book2, book3, book4, book5, book6]


#for book in books:
#    book.discount()
#print("-------------------------------------------")
#books = Book.delete_books(books, "роман", 14.00)

#avg_price = Book.average_price(books, 2020)
#for book in books:
#    print(f"{book.title}, {book.genre}, {book.price:.2f}, {book.year}")
#    print('=================================')

#print(f"Avr. price after 2020: {avg_price:.2f}")
