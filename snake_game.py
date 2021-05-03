import pygame
import random

# Variaveis Iniciais
azul = (169, 215, 81)
laranja = (211, 102, 72)
vermelha = (255, 0 , 0)

dimensoes = (500,500) #tupla

d=20
x=dimensoes[0]/2 - d/2
y=dimensoes[1]/2 - d/2

#            [  0  ,   1  ] 
#             [0,1]  [0,1]
snake_body = [[x,y]]

delta_x = d
delta_y = 0

x_food = round(random.randrange(0, dimensoes[0] - d) / d) * d
y_food = round(random.randrange(0, dimensoes[1] - d) / d) * d

tela = pygame.display.set_mode((dimensoes))
tela.fill(azul)
clock = pygame.time.Clock() 


def desenha_cobra(snake_body):
  tela.fill(azul)
  for i in snake_body:
    pygame.draw.rect(tela, laranja, [i[0],i[1],d,d], 10)



def mover_cobra(dx, dy, snake):

  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: #qualquer tecla é pressionada (keydown)
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        if delta_x != d:
          dx = -d
          dy = 0

      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        if delta_x != -d:
          dx = +d
          dy = 0

      elif event.key == pygame.K_UP or event.key == pygame.K_w:
        if delta_y != +d:
          dx = 0
          dy = -d

      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        if delta_y != -d:
          dx = 0
          dy = +d

  # if snake[-1][0] == dimensoes[0] or snake[-1][0] < 0 and \
  #    snake[-1][1] == dimensoes[1] or snake[-1][1] < 0:
  #   x_novo = snake[-1][0] + dx
  #   y_novo = snake[-1][1] + dy
  # else:

  x_novo = snake[-1][0] + dx
  y_novo = snake[-1][1] + dy

  snake.append([x_novo,y_novo])
  del snake[0]

  return dx, dy, snake


def verifica_comida(dx, dy, x_comida, y_comida, snake):
  head = snake[-1]

  x_novo = head[0] + dx
  y_novo = head[1] + dy

  if head[0] == x_comida and head[1] == y_comida:
    snake.append([x_novo, y_novo])
    x_comida = round(random.randrange(0, dimensoes[0] - d) / d) * d
    y_comida = round(random.randrange(0, dimensoes[1] - d) / d) * d

  pygame.draw.rect(tela, vermelha, [x_comida, y_comida,d,d] ,10)

  return x_comida, y_comida, snake

def verifica_parede(snake):
  head = snake[-1]

  if head[0] == dimensoes[0] or head[0] < 0 and \
     head[1] == dimensoes[1] or head[1] < 0:
     raise Exception

def verifica_mordeu_rabo(snake):
  head = snake[-1]
  body = snake.copy()

  del body[-1]
  for x,y in body:
    if head[0] == x and head[1] == y:
      raise Exception



while True:
  pygame.display.update()

  delta_x, delta_y, snake_body = mover_cobra(delta_x, delta_y, snake_body)

  verifica_mordeu_rabo(snake_body)
  verifica_parede(snake_body)

  desenha_cobra(snake_body)
  x_food, y_food, snake_body = \
    verifica_comida(delta_x, delta_y, x_food, y_food, snake_body)

  clock.tick(10)
