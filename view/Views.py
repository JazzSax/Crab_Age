import htmlContent

class Views():
    def __init__(self):
        pass

    def viewAll(self):
        print(htmlContent.viewAll())
    def showForm(self):
        print(htmlContent.showForm())
    def showOutput(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        print(htmlContent.showOutput(sex, length, diameter, height, weight, shucked, viscera, shell, age))