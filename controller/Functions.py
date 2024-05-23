import sys
import os
script_dir = os.path.dirname(os.path.dirname(__file__))


def view():
    sys.path.append(script_dir + "/view/")
    from Views import Views
    view = Views()
    view.viewAll()

def input():
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showForm()

