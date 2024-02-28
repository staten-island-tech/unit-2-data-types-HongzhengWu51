books = [ { 
    'Title': "Crime and Punishment",
    'Genre': "Novel",
    'Characters':["Rodion Raskolnikov", "Porfiry Petrovitch", "Sonia Marmeladova"]
}, {
    'Title': "The Great Gatsby",
    'Genre': "Novel",
    'Characters': ["Jay Gatsby", "Mr. Gatz", "Nick Carraway"] 
}, {
    'Title': "Death of a Salesman",
    'Genre': "Plays",
    'Characters': ["Willy Loman", "Biff Loman", "Happy Loman"]
}, {
    'Title': "No Longer Human",
    'Genre': "Novel",
    'Characters': ["Yozo", "Takeichi"]
}]

def get_book(books):
    for book in books():
        if "Crime" in 