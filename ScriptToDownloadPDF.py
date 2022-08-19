import urllib.request

def download(tutorialName):
    url = 'https://bugs.python.org/file47781/Tutorial_EDIT.pdf' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    downloadLocation = r'C:\Users\admin\main\newfolder\make'

    pdf = urllib.request.urlopen(url)
    saveFile = open(downloadLocation + tutorialName +  '.pdf', 'wb')  # because pdf is a binary file
    saveFile.write(pdf.read())
    saveFile.close()
    print('Downloaded!')

if __name__ == '__main__':
    tutorialName = input('Name of the tutorial pdf to be downloaded: ')
    download(tutorialName)