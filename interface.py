from bookshelf import Bookshelf


def print_commends():
    print("wpisz: show -> aby pokazać spis książek")
    print("wpisz: add -> aby dodać książkę do zbioru")
    print("wpisz: help -> aby wyświetlić listę komend")
    print("wpisz: exit -> aby zakończyć program")
    print("-" * 45)


print("Witam!")
print_commends()

while True:
    answer = input()
    if answer == "show":
        Bookshelf.show_books()
    elif answer == "add":
        Bookshelf.add_new_books()
    elif answer == "help":
        print_commends()
    elif answer == "exit":
        break
    else:
        print("spróbuj ponownie")