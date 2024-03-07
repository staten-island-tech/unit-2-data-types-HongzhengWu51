x = ["a", "b", ]

def pan(y):
    for i in x:
        if i not in x:
            if i not in y:
                return False
    return True
