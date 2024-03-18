#! python3

import os
import re

def findPath(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return result

def textStrip():

    fileName = input('Write file name')
    filePath = input(r'Write disk, where file is located (ex. C:\\)')

    actualFilePath = findPath(fileName, filePath)

    fileOpen = open(actualFilePath, 'r')

    print(actualFilePath)

    pullingRawText = fileOpen.read()

    stripper = re.sub(r'\s+', '', pullingRawText)

    print(stripper)

    fileOpen.close()

    open('file_with_no_white_space.txt', 'w')

    fileOpen = open('file_with_no_white_space', 'w')

    fileOpen.write(stripper)

    fileOpen.close()

textStrip()


c = input('Click enter to close the window.')
