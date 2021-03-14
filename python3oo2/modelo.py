class Programa:
    def __init__(self, nome, ano ):
        self._nome = nome
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"Nome: {self._nome} - ano: {self.ano} - Likes: {self._likes}"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} - ano: {self.ano} - {self.duracao} min - Likes: {self._likes}"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - ano: {self.ano} - {self.temporadas} Temporadas - Likes: {self._likes}"

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

demolidor.dar_like()
demolidor.dar_like()

tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

print(f"{vingadores.nome} - {vingadores.duracao}: {vingadores.likes}")
print(f"{atlanta.nome} - {atlanta.temporadas}: {atlanta.likes}")

print("---------------------------------------------------")

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
minha_playlist = Playlist("fim de semana", filmes_e_series)

for programa in minha_playlist:
    print(programa)

print(f"Tamanho: {len(minha_playlist)}")

