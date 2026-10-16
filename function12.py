s = "Python is great!"

def fun():
    global s
    s += " GFG"   
    print(s)
    s = "Look for GeeksforGeeks Python Section"  
    print(s)

fun()
print(s)