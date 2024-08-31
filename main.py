import pygame
import time
pygame.init()

WIDTH = 1000
HEIGHT = 600
TITLE = "space invaders 2p game"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (1000, 600))
r = pygame.image.load("spaceship red.png")
y = pygame.image.load("spaceship yellow.png")
r = pygame.transform.scale(r, (50,50))
y = pygame.transform.scale(y, (50,50))
bullet_y=[]
bullet_r=[]
hp_y = 10
hp_r = 10

  
  
class Spaceship(pygame.sprite.Sprite):
  def __init__(self, x, y, image, angle):
    super().__init__()
    self.image = pygame.transform.rotate(image, angle)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
  def move(self, player, vx, vy):
    self.rect.x = self.rect.x + vx
    self.rect.y = self.rect.y + vy
    if player == "r":
      if self.rect.left < 500:
        self.rect.left = 500
      if self.rect.right > 1000:
        self.rect.right = 1000
    if player == "y":
      if self.rect.right > 500:
        self.rect.right = 500
      if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > 600:
      self.rect.bottom = 600
Spaceship_r = Spaceship(750, 300, r, -90)
Spaceship_y = Spaceship(250, 300, y, 90)
sprite_group = pygame.sprite.Group()
sprite_group.add(Spaceship_r)
sprite_group.add(Spaceship_y)



def handle_bullets():
  global hp_r, hp_y
  for bullet in bullet_y:
    pygame.draw.rect(screen, "yellow", bullet, 0)
    bullet.x = bullet.x + 10
    if Spaceship_r.rect.colliderect(bullet):
      hp_r = hp_r - 1
      bullet_y.remove(bullet)
  for bullet in bullet_r:
    pygame.draw.rect(screen, "red", bullet, 0)
    bullet.x = bullet.x - 10
    if Spaceship_y.rect.colliderect(bullet):
      hp_y = hp_y - 1
      bullet_r.remove(bullet)
border = pygame.Rect((500,0), (10, 600))



run = True

while run:
  screen.blit(bg, (0, 0))
  pygame.draw.rect(screen, "white", border, 0)
  sprite_group.draw(screen)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_CAPSLOCK:
        bullet=pygame.Rect(Spaceship_y.rect.right,Spaceship_y.rect.y + 25, 10, 5 )
        bullet_y.append(bullet)
      if event.key == pygame.K_RSHIFT:
        bullet = pygame.Rect(Spaceship_r.rect.left, Spaceship_r.rect.y + 25, 10, 5)
        bullet_r.append(bullet)

  font = pygame.font.SysFont("Times New Roman/n", 25)
  msg = font.render("Health: " + str(hp_y), True, "White")
  screen.blit(msg, (200, 20))

  font = pygame.font.SysFont("Times New Roman/n", 25)
  msg_2 = font.render("Health: " + str(hp_r), True, "White")
  screen.blit(msg_2, (725, 20))

  if hp_r <= 0:
    font = pygame.font.SysFont("Times New Roman/n", 75)
    end_msg = font.render("Game over! Yellow won!", True, "Yellow")
    screen.blit(end_msg, (250, 325))
    pygame.display.update()
    time.sleep(5)
    run = False
  if hp_y <= 0:
    font = pygame.font.SysFont("Times New Roman/n", 75)
    end_msg = font.render("Game over! Red won!", True, "Red")
    screen.blit(end_msg, (250, 325))
    pygame.display.update()
    time.sleep(5)
    run = False
  handle_bullets()
  
  keys = pygame.key.get_pressed()
  if keys [pygame.K_w]:
    Spaceship_y.move("y", 0, -1)
  if keys [pygame.K_a]:
    Spaceship_y.move("y", -1, 0)
  if keys [pygame.K_d]:
    Spaceship_y.move("y", 1, 0)
  if keys [pygame.K_s]:
    Spaceship_y.move("y", 0, 1)

  if keys [pygame.K_UP]:
    Spaceship_r.move("r", 0, -1)
    
  if keys [pygame.K_LEFT]:
    Spaceship_r.move("r", -1, 0)
  if keys [pygame.K_RIGHT]:
    Spaceship_r.move("r", 1, 0)
  if keys [pygame.K_DOWN]:
    Spaceship_r.move("r", 0, 1)
  pygame.display.update()