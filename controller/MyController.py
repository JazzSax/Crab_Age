#!C:\Users\Cliff\AppData\Local\Programs\Python\Python311\python
print("Content-Type: text/html")
print()
import cgi
import sys
import os

script_dir = os.path.dirname(os.path.dirname(__file__))

form = cgi.FieldStorage()
all = form.getvalue("ALL")
add = form.getvalue("ADD")
search = form.getvalue("search")
detail = form.getvalue("searchDetail")
back = form.getvalue("back")

if(all):
    from Functions import view
    view()
if(add):
    from Functions  import input
    input()
if(search):
    from Functions import search
    search(detail)
if(back):
    from Functions import home
    home()


  




