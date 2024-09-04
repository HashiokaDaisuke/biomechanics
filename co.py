class Class1:#慣習的に頭文字は大文字
    """Test class: Class1"""
    def __init__(self, name, birth, mathScore, japaneseScore):
        self.__name = name
        self.__birth = birth
        self.__mathScore = mathScore
        self.__japaneseScore = japaneseScore

        self.__average = self.__averageScore()


    def __averageScore(self):
        return (self.__mathScore + self.__japaneseScore) / 2
    
    def getName(self):
        return self.__name

    def getAverage(self):
        return self.__average
    
def averageAdd(n,people):
    if n == -1:
        return 0
    else:
        return people[n].getAverage() + averageAdd(n - 1,people)