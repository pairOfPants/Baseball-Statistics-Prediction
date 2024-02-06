class Statistic:
    def __init_(self):
        self.name = "NO_NAME"
        self.value = 0
    def __init__(self,name,value):
        self.name = name
        self.value = value
    def __str__(self):
        return f"{self.name}: {self.value}"
    
