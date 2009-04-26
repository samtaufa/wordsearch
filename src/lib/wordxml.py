import zipfile, re

class wordxml:
    def __init__(self):
        pass
    def readDocx(self, docx):
      inarc = zipfile.ZipFile(docx,'r')
      names = inarc.namelist()
      dict = {}
      for name in names:
        dict[name] = inarc.read(name)
      inarc.close
      #~ print dict.keys()  
      return dict

    def readDocumentFromDocx(self, docx):
      arc = zipfile.ZipFile(docx,'r')
      s = arc.read('word/document.xml')
      f = open('document.xml','w')
      f.write(s)
      f.close()
      return s

    def updateDocumentInDocx(self, docx,doc):
      dict = readDocx(docx)
      archive = zipfile.ZipFile(docx,'w')
      for name in dict.keys():
        if (name == 'word/document.xml'):
          dict[name] = doc
        archive.writestr(name,dict[name])
      archive.close()

    def tagDocx(self, docx,tags):
      dict = readDocx(docx)
      archive = zipfile.ZipFile(docx,'w')
      for name in dict.keys():
        if (name == 'docProps/core.xml'):
          dict[name] = re.sub('<cp:keywords>(.*)</cp:keywords>','<cp:keywords>%s</cp:keywords>' % 
            tags, dict[name])
        archive.writestr(name,dict[name])
      archive.close()
