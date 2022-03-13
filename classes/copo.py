# Desenvolva sua classe Copo aqui.
from classes.recipiente import Recipiente


class Copo(Recipiente):
    def __init__(self, tamanho):
        super().__init__(tamanho)

    def encher(self, bebida="água"):
        if not self.limpo:
            return "Não se pode encher um copo sujo"
        self.sujar()
        self.conteudo = self.tamanho
        self.bebida = bebida
    
    def beber(self, quantidade):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.esvaziar()
        self.limpo = True

    def __repr__(self) -> str:
        if(self.conteudo == 0):
            return "Um copo vazio de %sml" % (float(self.tamanho))
        return "Um copo de %sml contendo %sml de %s" % (float(self.tamanho), float(self.conteudo), self.bebida)

    def __str__(self) -> str:
        if(self.conteudo == 0):
            return f"Um copo vazio de {float(self.tamanho)}ml"
        return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"
    