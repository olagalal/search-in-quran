import pandas as pd
from Sora import Sora
class SearchInQuran:
    __souaName = [""]
    def __makeReady(self):
        self.__quran.columns = ['sura_no', 'aya_no', 'text']
        self.__quran['sura_no'] = pd.to_numeric(self.__quran['sura_no'], downcast='integer')
        self.__quran['aya_no'] = pd.to_numeric(self.__quran['aya_no'], downcast='integer')
        fo = open("souar.txt", "r")
        all = fo.readlines()
        for i in range(len(all)):
            self.__souaName.append(all[i].strip())
        fo.close()

    def __addAllSouar(self):
        for i in range(1, 115):
            temp = Sora(i, self.__souaName[i])
            all = self.__quran[self.__quran['sura_no'] == i].text.tolist()
            for aya in all:
                temp.addAya(aya)
            self.__allSouar.append(temp)


    def __init__(self):
        self.__allSouar = [Sora(0, "")]
        self.__quran = pd.read_csv('quran-simple-clean.txt', sep="|", header=None)
        self.__makeReady()
        self.__addAllSouar()

    def searchInAllSouar(self, text):
        allFounds = []
        for i in range(1, 115):
            temp = self.__allSouar[i]
            found = temp.searchInSora(text)
            if len(found) > 0:
                allFounds.append((temp.soraNumber, temp.soraName, found))
        return allFounds

    def viewAllAyatInSora(self, index):
        return self.__allSouar[index].getAllAyat()

    def viewAllWordstInSora(self, index):
        return self.__allSouar[index].getAllWords()



