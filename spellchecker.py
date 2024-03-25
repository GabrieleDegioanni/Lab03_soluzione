import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multiDic = md.MultiDictionary()
        # self._multiDic.printDic("italian")

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()

        print("------------------------------")
        print("Using contains")
        t1 = time.time()
        parole = self._multiDic.searchWord(words,language)
        for parola in parole:
            if not parola.corretta:
                print(parola)
        t2 = time.time()
        print("Time elapsed " + str(t2-t1))
        print("------------------------------")
        print("Using Linear search")
        t1 = time.time()
        parole = self._multiDic.searchWordLinear(words,language)
        for parola in parole:
            if not parola.corretta:
                print(parola)
        t2 = time.time()
        print("Time elapsed " + str(t2-t1))
        print("------------------------------")
        print("Using Dichotomic search")
        t1 = time.time()
        parole = self._multiDic.searchWordDichotomic(words,language)
        for parola in parole:
            if not parola.corretta:
                print(parola)
        t2 = time.time()
        print("Time elapsed " + str(t2-t1))

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text