from bookshop import *

user = "r"
menu = ['1', '2', '3', '4', '5', 'Q', 'q']
while user.lower() != "q":
    print("Bienvenido al Gestor de Libros".center(50, "-"))
    print("1. Buscar Libro")
    print("2. Adicionar Libro")  # TODO
    print("3. Modificar Libro")
    print("4. Eliminar Libro")
    print("5. Ver Todos los Libros")
    print("Presione la letra Q para salir")
    option_menu = input(":")

    if option_menu in menu:
        if option_menu == "1":
            print("Buscar Libros".center(50, "-"))
            print("1. ID")
            print("2. Titulo")
            print("3. Autor")
            print("4. Genero")
            print("Presione la letra Q para volver al Menu")
            selected_option = input(":")
            if selected_option in menu:
                searchBook(selected_option)
            else:
                print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
        elif option_menu == "2":
            print("Adicionar Libro".center(50, "-"))
            id_book_add = input("ID:")
            if existBook(id_book_add) == -1:
                # TODO menu para add libro
                book_title_add = input("Titulo:")
                book_author_add = input("Autor:")
                book_gender_add = input("Genero:")
                print(addBook(id_book_add, book_title_add, book_author_add, book_gender_add))
            else:
                print("El libro con ID:", id_book_add, "ya se encuentra en la Base de Datos.")
        elif option_menu == "3":
            print("Modificar Libro".center(50, "-"))
            id_book = input("ID:")
            if existBook(id_book) >= 0:
                # TODO menu para modificar libro
                book_title = input("Titulo:")
                book_author = input("Autor:")
                book_gender = input("Genero:")
                print(updateBook(id_book, book_title, book_author, book_gender))
            else:
                print("El libro con ID:", id_book, "no se encuentra en la Base de Datos.")

        elif option_menu == "4":
            print("Eliminar Libro".center(50, "-"))
            id_book = input("ID:")
            print(deleteBookById(id_book.lower()))

        elif option_menu == "5":
            print("Todos los libros", DB)

        elif option_menu == "q":
            print("Hasta la Proxima!!!".center(40, "-"))
            break
    else:
        print("Ha seleccionado una Opcion no valida! USE ESPEJUELOS")
