# Desenvolva sua classe Recipiente aqui.
class Recipiente:
    def __init__(self, tamanho):
        self.tamanho = 0 if tamanho < 0 else tamanho
        self.conteudo = 0
        self.limpo = True

    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        return False
    
    def lavar(self):
        self.esvaziar()
        self.limpo = True

    def esta_limpo(self):
        return self.limpo
    
    def estado(self):
        if self.limpo:
            return "limpo"
        return "sujo"

    def sujar(self):
        self.limpo = False
    
    def __repr__(self) -> str:
        return "Um recipiente %s não especificado" % (self.estado())

    def __str__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"    