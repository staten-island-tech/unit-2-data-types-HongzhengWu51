#search= (input("Search for a genre:"))

books = [ {
    'title': "Crime and Punishment",
    'genre': "psycological novel",
    'characters':["Rodion Raskolnikov", "Porfiry Petrovitch", "Sonia Marmeladova"]
}, {
    'title': "The Great Gatsby",
    'genre': "tragedy",
    'characters': ["Jay Gatsby", "Mr. Gatz", "Nick Carraway"]
}, {
    'title': "Death of a Salesman",
    'genre': "plays",
    'characters': ["Willy Loman", "Biff Loman", "Happy Loman"]
}, {
    'title': "No Longer Human",
    'genre': "novel",
    'characters': ["Yozo", "Takeichi"]
}]


def get_book(books):
    for book in books():
        if "psycological novel" in book['genre']:
            print(book['title'], book['characters'])
get_book(books)

#if search == (input("psycologcal novel")):
   # print(books['title'], books['genre'])