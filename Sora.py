# -*- coding: utf-8 -*-
from Trie import Trie
from FastSearch import FastSearch
import nltk


class Sora:

    def __init__(self, soraNumber, soraName):
        self.soraNumber = soraNumber
        self.soraName = soraName
        self.__allWordsInSora = Trie()
        self.__allAyat = []
        self.__allWords = []


    def __ARTokenizer(self, sent):
        L = nltk.word_tokenize(sent)
        return L


    def addAya(self, aya):
        allWordsInAya = self.__ARTokenizer(aya)
        self.__allAyat.append(aya)
        self.__addWordsToTrie(allWordsInAya)

    def __addWordsToTrie(self, aya):
        for word in aya:
            if self.__allWordsInSora.search(word) == False:
                self.__allWords.append(word)
            self.__allWordsInSora.add(word)


    def edit_distance(self, s1, s2):
        m = len(s1) + 1
        n = len(s2) + 1

        tbl = {}
        for i in range(m): tbl[i, 0] = i
        for j in range(n): tbl[0, j] = j
        for i in range(1, m):
            for j in range(1, n):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                tbl[i, j] = min(tbl[i, j - 1] + 1, tbl[i - 1, j] + 1, tbl[i - 1, j - 1] + cost)

        return tbl[i, j]



    def search(self, text):
        allMatches = []
        ayaNumber = 1
        for aya in self.__allAyat:
            mySerach = FastSearch()
            idx = mySerach.search(text, aya)
            if idx != -1:
                allMatches.append({ayaNumber: aya})
            ayaNumber += 1
        return allMatches

    def searchInSora(self, text):
        allMatches = self.search(text)
        allWords = self.__ARTokenizer(text)
        wrongIdx = []

        for i in range(len(allWords)):
            if not(self.__allWordsInSora.search(allWords[i])):
                wrongIdx.append(i)
        if len(wrongIdx) == 1:
            for word in self.__allWords:
                if self.edit_distance(word, allWords[wrongIdx[0]]) <= 2:
                    newText = ""
                    for i in range(len(allWords)):
                        if i == wrongIdx[0]:
                            newText = newText + word + " "
                        else:
                            newText = newText + allWords[i] + " "
                    res = self.search(newText.strip())
                    if len(res) >= 1:
                        allMatches.extend(res)
        return allMatches


    def getAllWords(self):
        return self.__allWords

    def getAllAyat(self):
        return self.__allAyat