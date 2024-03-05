def pal(x):
    y = x.reverse()
    if y == x:

#def pal(x):
 #   y = x[::-1]
  #  if y == x:
        
#This reverses string 
        #for i in x:
       # y = i + y
def pal(x):
    y = ""
    for i in x:
        y = i + y
    if y == x:
        return True
    else:
        return False