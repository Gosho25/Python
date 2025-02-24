class Reader:
    def read(self):
        pass

class TextFile(Reader):
    def read(self):
        return "Четене на текстов файл"

class CSVFile(Reader):

    def read(self):
      return "Четене на CSV файл"
    

text_file = TextFile()
print(text_file.read()) 

csv_file = CSVFile()
print(csv_file.read())