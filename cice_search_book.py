# https://github.com/vgenov-py/t603/blob/master/ex4.md

DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
    {
        "id": "ne_1",
        "title": "Lobo de mar",
        "author": "Jack London",
        "genre": "Narrativa extranjera"
    },
    {
        "id": "np_1",
        "title": "El legado de los huesos",
        "author": "Dolores Redondo",
        "genre": "Narrativa policíaca"
    },
    {
        "id": "dc_1",
        "title": "El error de Descartes",
        "author": "Antonio Damasio",
        "genre": "Divulgación científica"
    },
    {
        "id": "dc_2",
        "title": "El ingenio de los pájaros",
        "author": "Jennifer Ackerman",
        "genre": "Divulgación científica"
    },
    {
        "id": "ne_1",
        "title": "El corazón de las tinieblas",
        "author": "Joseph Conrad",
        "genre": "Narrativa extranjera"
    },
    {
        "id": "dc_5",
        "title": "Metro 2033",
        "author": "Dmitri Glujovski",
        "genre": "Divulgación científica"
    },
    {
        "id": "dc_5",
        "title": "Sidharta",
        "author": "Hermann Hesse",
        "genre": "Narrativa extranjera"
    },
    {
        "id": "el_1",
        "title": "Andres Trapiello",
        "author": "Las armas y las letras",
        "genre": "Narrativa extranjera"
    },
    {
        "id": "aa_1",
        "title": "El poder del ahora",
        "author": "Ekhart Tolle",
        "genre": "Narrativa extranjera"
    },
]

genre = ["Narrativa extranjera", "Divulgación científica", "Narativa policíaca", "Ciencia ficción", "Autoayuda"]


# Verify if exist book , return the index book if exist
def existBook(id_book):
    flag = None
    for key, book in enumerate(DB):
        if book["id"].lower() == id_book.lower():
            flag = key
    return flag


# find books by key,value in the dictionary
def findByKeyValue(key, value):
    respond = []
    for book in DB:
        if book[key].lower() == value.lower():
            respond.append(book)
    return respond

# delete book by ID
def deleteBookById(id):
    msg = "El libro con ID :" + id + " no se encuentra en la Base de Datos!"
    index_book = existBook(id)
    if index_book:
        DB.pop(index_book)
        msg = "El libro ha sido eliminado satisfactoriamente."
    return msg

# update book by ID, key value
def updateBook(id_book, book_title, book_author, book_gender):
    msg = "Fails"
    for key, book in enumerate(DB):
        if book["id"].lower() == id_book.lower():
            DB[key]['title'] = book_title
            DB[key]['author'] = book_author
            DB[key]['genre'] = book_gender
            msg = "El libro ha sido modificado satisfactoriamente."
    return msg

# add new book
def addBook(id_book, book_title, book_author, book_gender):
    msg = "Existe un libro con el mismo ID."
    if not existBook(id_book):
        new_book= {
            "id": id_book,
            "title": book_title,
            "author": book_author,
            "genre": book_gender
        }
        DB.append(new_book)
        msg = "El libro ha sido adicionado satisfactoriamente."
    return msg

# Search Book
def searchBook(selected_option):
    if selected_option == "1":
        id = input("ID: ")
        respond = findByKeyValue("id", id)
        print("Resultado de la Busqueda:", respond)
    if selected_option == "2":
        title = input("Titulo: ")
        respond = findByKeyValue("title", title)
        print("Resultado de la Busqueda:", respond)
    if selected_option == "3":
        autor = input("Autor: ")
        respond = findByKeyValue("autor", autor)
        print("Resultado de la Busqueda:", respond)
    if selected_option == "4":
        print("Seleccione el Genero:")
        # show the gender list to select
        for key, value in enumerate(genre):
            print(key, value)
        gender_option = int(input("genero: "))
        if gender_option >= 0 and gender_option <= len(genre) - 1:
            respond = findByKeyValue("genre", genre[gender_option])
            print("Resultado de la Busqueda:", respond)
        else:
            print("Ha seleccionado una opcion no valida! Pongase los ESPEJUELOS!")

user = "r"
menu = ['1', '2', '3', '4', 'Q', 'q']
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
        elif option_menu == "3":
            print("Modificar Libro".center(50, "-"))
            id_book = input("ID:")
            if existBook(id_book):
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
