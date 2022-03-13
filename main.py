from classes.copo import Copo
from classes.recipiente import Recipiente


if __name__ == "__main__":
      #  r = Recipiente(100)
      #  print(r.esta_limpo())
      #  print(r.estado())
      #  r.sujar()
      #  print(r.esta_limpo())
      #  r.lavar()
      #  print(r.esta_limpo())
    c =  Copo(300)
    print(c)
    c.encher("café")
    print(c.bebida)
    print(repr(c))
    c.beber(30)
    print(repr(c))
    c.lavar()
    print(c.esta_limpo())