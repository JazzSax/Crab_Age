import htmlContent

class Views():
    def __init__(self):
        pass

    def viewAll(self, allRecords):
        print(htmlContent.viewAll(allRecords))
    def showForm(self):
        print(htmlContent.showForm())
    def showOutput(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        print(htmlContent.showOutput(sex, length, diameter, height, weight, shucked, viscera, shell, age))