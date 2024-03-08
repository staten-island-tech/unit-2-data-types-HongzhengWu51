
#the code for characters in book[characters] creates a loop that goes through the book that when through a loop to find all of the characters.
#Remember when making the loop that what I am finding has to correspond with which category it's in.
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
    for book in books:
        if 'Rodion Raskolnikov' in book['characters']:
            print(book['title'], book['genre'])
            for characters in book['characters']:
                print(characters)
get_book(books)
