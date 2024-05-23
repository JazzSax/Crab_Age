#import python path
print("Content-Type: text/html")
print()
import cgi
import sys
import os

script_dir = os.path.dirname(os.path.dirname(__file__))


form = cgi.FieldStorage()
all = form.getvalue("ALL")
add = form.getvalue("ADD")

if(all):
    from Functions import view
    view()
if(add):
    from Functions import input
    input()


