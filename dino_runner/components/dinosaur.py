from typing import Self
from pygame.sprite import Sprite
import pygame

from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING
X_POS = 80
Y_POS = 310
JUMP_VELOCITY = 8
class Dinosaur(Sprite):

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.jump_velocity = JUMP_VELOCITY

    def update(self, user_input):

        if self.dino_run:
            self.run()
        
        elif self.dino_jump:
            self.jump()
            
        elif self.dino_duck:
            self.duck()


        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False      
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
            self.dino_run=False
        elif self.dino_duck:
            self.dino_duck=False
            self.dino_run=True        

        if self.step_index >= 10:
            self.step_index = 0
    
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -=0.8
        
        if  self.jump_velocity < -JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_velocity = JUMP_VELOCITY
        print(self.jump_velocity)

    def duck(self):
        self.image=DUCKING
        self.dino_rect.x=X_POS
        self.dino_rect.y=Y_POS+34
        if self.step_index > 5:
            self.image = DUCKING[0]
        else:
            Self.image = DUCKING[0]
        self.step_index +=1


    def run (self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        if self.step_index > 5:
            self.image = RUNNING[1]
        else:
            self.image = RUNNING[0]
        self.step_index +=1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))