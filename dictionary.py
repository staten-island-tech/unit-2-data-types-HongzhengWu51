pick_genre= (input("Search for a genre:"))

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
   for genre in books():
        if genre in books['genre'] == pick_genre:
         print(books['title'], books['characters'])
get_book(books)

