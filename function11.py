def fun():
    s += ' GFG'   # Error: Python thinks s is local
    print(s)

s = "I love GeeksforGeeks"
fun()