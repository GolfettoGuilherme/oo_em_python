#classe pai
class Programa:
    def __init__(self, nome, ano):
        #self.__nome = nome.title() #privado não vai pra classe filha
        self._nome = nome.title() #protegido
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def darLike(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

#classe filha
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano) #chamando metodo da classe pai
        self.duracao = duracao

    def __str__(self): #toString()
        return f'{self._nome} - {self.ano} - {self.duracao} Min - {self._likes} Likes'
    

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano) #chamando metodo da classe pai
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):        
        self.nome = nome
        self._programas = programas

    #"transformou" o seu objeto em iteravel
    def __getitem__(self,item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)



vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("Todo mundo em panico",1999, 100)
demolidor = Serie("demolidor",2016,2) 

tmep.darLike()
demolidor.darLike()
atlanta.darLike()
atlanta.darLike()

filmes_e_series = [vingadores,atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist("Fim de Semana",filmes_e_series)

print(f'tamanho do playlist: {len(playlist_fim_de_semana.listagem)}')

for program in playlist_fim_de_semana:
    print(program)
