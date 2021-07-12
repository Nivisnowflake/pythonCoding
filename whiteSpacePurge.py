#! python3

import os
import re

#Odnajdowanie ścieżki pliku
def findPath(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return result

#Funkcja, ktora wczytuje nazwe pliku, usuwa i tworzy nowy plik
def textStrip():

    fileName = input('Wprowadz nazwe pliku')
    filePath = input(r'Wprowadz dysk, na ktorym sie znajduje plik (np. C:\\)')

    actualFilePath = findPath(fileName, filePath)

    fileOpen = open(actualFilePath, 'r')

    print(actualFilePath)

    pullingRawText = fileOpen.read()

    stripper = re.sub(r'\s+', '', pullingRawText)

    print(stripper)

    fileOpen.close()

    open('plikBezBialychZnakow.txt', 'w')

    fileOpen = open('plikBezBialychZnakow.txt', 'w')

    fileOpen.write(stripper)

    fileOpen.close()

textStrip()

print('kopytko')

c = input('Wcisnij enter aby zakonczyc program.')
