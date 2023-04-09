from pygame import *
font.init()

class GameSprite(sprite.Sprite):
    def __init__(self,image_name, player_x,player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(image_name), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s]and self.rect.y < 300:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP]and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN]and self.rect.y < 300:
            self.rect.y += self.speed



win_h = 700
win_w = 500
window = display.set_mode((win_h, win_w))
display.set_caption('Пинг-Понг 1000-7...')
clock = time.Clock()
Fps = 65
run = True
Player1 = Player('Plat.png', 10, 150, 100, 200, 5)
Player2 = Player('Plat.png', 630, 150, 100, 200, 5)

WHITE = (190, 220, 235)


while run:
    for e in event.get():
        if e.type == QUIT or e.type == [K_ESCAPE]:
            run = False 

    window.fill(WHITE)
    Player1.update_1()
    Player1.reset()
    Player2.update_2()
    Player2.reset()

    clock.tick(Fps)
    display.update()













































'''from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки :D')
#задай фон сцены
background = transform.scale(image.load('background.png'), (700, 500))
sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
sprite2 = transform.scale(image.load('sprite2.png'), (100,100))
x1 = 50   
y1 = 300
x2 = 590
y2 = 300
speed = 10

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
game = True
clock = time.Clock()
FPS = 65
while game: #основной цикл игры
    window.blit(background,(0, 0))#размещение фона
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():#закрытие игры при нажатии крестика
        if e.type == QUIT or e.type == [K_ESCAPE]:
            game = False #игра должна закрыться 
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed


    clock.tick(FPS)#частота кадров в секунду
    display.update()#обновление кадров игры'''