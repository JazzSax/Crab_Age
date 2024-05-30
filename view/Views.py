import htmlContent

class Views():
    def __init__(self):
        pass

    def viewAll(self, allRecords):
        print(htmlContent.viewAll(allRecords))
    def showForm(self):

        print(htmlContent.showForm())
    def showOutput(self, res,result, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        print(htmlContent.showOutput(res,result,sex, length, diameter, height, weight, shucked, viscera, shell, age))
    def home(self):
        print(htmlContent.home())
    def search(self, result):
        print(htmlContent.viewAll(result))