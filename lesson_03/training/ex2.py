from book import Book

library = [Book("Бойцовский клуб", "Чак Паланик"),
           Book("Мастера и Маргарита", "Михаил Булгаков"),
           Book("Анна Каренина", "Лев Толстой")]

for book in library:
    print(f"{book.title} - {book.author}")
