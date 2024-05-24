#!/Python37/python
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
    #print("<script type='text/javascript'> alert ('aaaa');</script>")
    from Functions import view
    view()
if(add):
    from Functions import input
    input()



