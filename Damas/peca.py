class Peca:
   def __init__(self, color, posicaoX, posicaoY, dama):
      self.color = color #-1 ou 1
      self.posicaoX = posicaoX
      self.posicaoY = posicaoY
      self.dama = False
      
   def opcoes_movimentos(self, tabuleiro):
      opcoes = []
      for x in range(8):
         for y in range(8):
            if tabuleiro[x][y] == tabuleiro[self.posicaoX][self.posicaoY]:
               if not self.dama:
                  #moviemento normal
                  if tabuleiro[x-1][y+self.color] == 0: #frente esquerda
                     opcoes.append(((x-1, y+self.color), False))
                  if tabuleiro[x+1][y+self.color] == 0: #frente direita
                     opcoes.append(((x+1, y+self.color), False))
                  #movimento de caça
                  if tabuleiro[x-1][y+self.color] == self.color * -1 and tabuleiro[x-2][y+self.color*2] == 0: #comer frente esquerda
                     opcoes.append(((x-2, y+self.color*2), True))
                  if tabuleiro[x+1][y+self.color] == self.color * -1 and tabuleiro[x+2][y+self.color*2] == 0: #comer frente direita
                     opcoes.append(((x+2, y+self.color*2), True))
                  if tabuleiro[x+1][y-self.color] == self.color * -1 and tabuleiro[x+2][y-self.color*2] == 0: #comer tras direita
                     opcoes.append(((x+2, y-self.color*2), True))
                  if tabuleiro[x+1][y-self.color] == self.color * -1 and tabuleiro[x+2][y-self.color*2] == 0: #comer tras direita
                     opcoes.append(((x+2, y-self.color*2), True))
               else:
                  #movimento sendo dama

   def movimentar(self, posicaoX, posicaoY):
      self.posicaoX = posicaoX
      self.posicaoY = posicaoY
      if posicaoY == 8 and self.color == -1:
         self.dama = True
      if posicaoY == 0 and self.color == 1:
         self.dama = True               
