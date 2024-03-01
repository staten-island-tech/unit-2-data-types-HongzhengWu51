Search= (input("Search fir a genre"))

books = [ {'Title': "Crime and Punishment",
    'genre': "psycological Novel",
    'characters':["Rodion Raskolnikov", "Porfiry Petrovitch", "Sonia Marmeladova"],
}, {'title': "The Great Gatsby",
    'genre': "Tragedy",
    'characters': ["Jay Gatsby", "Mr. Gatz", "Nick Carraway"], 
}, {'title': "Death of a Salesman",
    'genre': "Plays",
    'characters': ["Willy Loman", "Biff Loman", "Happy Loman"],
}, {'title': "No Longer Human",
    'genre': "Novel",
    'characters': ["Yozo", "Takeichi"],
}]
def get_book(books):
    for book in books():
        if 'Rodion Raskolnikov' in book ['characters']:
            print(book['genre'], book['title'])
get_book(books)