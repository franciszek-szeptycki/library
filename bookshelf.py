from dataclasses import dataclass

id_number = 0


@dataclass
class Books:
    title: str
    author: str
    id_number: int

    def __init__(self, title, author, id_of_book):
        self.title = title
        self.author = author
        self.id_number = id_of_book

    def __str__(self):
        return f"id: {self.id_number}    tytuł: \"{self.title}\"    autor: {self.author}"

    def __repr__(self): return f"id: {self.id_number}\ntytuł: \"{self.title}\"\nautor: {self.author}"


# noinspection PyGlobalUndefined
@dataclass
class Bookshelf:
    list_of_books = []
    id_number: int

    @classmethod
    def add_new_books(cls):
        while True:
            print("-" * 45)
            title = input("exit -> aby wyjść / tytuł: ")
            if title == "exit":
                print("wyszedłeś z opcji dodawania pozycji")
                print("-" * 45)
                break
            author = input("exit -> aby wyjść / autor: ")
            if author == "exit":
                print()
                print("wpisz: show -> aby pokazać spis książek")
                print("wpisz: 0 -> aby dodać książkę do zbioru")
                print("wpisz: help -> aby wyświetlić listę komend")
                print("wpisz: exit -> aby zakończyć program")
                print("-" * 45)
                break
            global id_number
            id_number += 1
            cls.list_of_books.append(Books(title, author, id_number))
            print(f"Dodano: {cls.list_of_books[-1]}")

    @classmethod
    def show_books(cls):
        if not cls.list_of_books:
            print("pusto, nic tu nie ma...")
        else:
            print()
            print("Książki w bibliotece: ")
            for a in cls.list_of_books:

                print()
                print(f"{repr(a)}")
        print("-" * 45)
