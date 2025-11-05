

class Book:
    def __init__(self,title,author,content):
        self.title=title
        self.author=author
        self.content=content

    def save_to_file(self,filename):
        with open(f'{filename}.txt', "a") as f:
            f.write(f'{self.title},{self.author},{self.content}')



class Save:
    def __init__(self,filename,item:Book):
        with open(f'{filename}.txt', "a") as f:
            f.write(f'{item.title},{item.author},{item.content}')