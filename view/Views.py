import htmlContent

class Views():
    def __init__(self):
        pass

    def viewAll(self):
        print(htmlContent.viewAll())
    def showForm(self):
        print(htmlContent.showForm())
    def showPrediction(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        print(f"<script type='text/javascript'> alert ('show2');</script>")
        print(htmlContent.showPrediction(sex, length, diameter, height, weight, shucked, viscera, shell, age))
     