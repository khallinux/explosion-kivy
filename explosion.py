import random
from random import randint
import pygame
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.uix.floatlayout import FloatLayout


class Explosion(FloatLayout):
    colors = [
        (1, 0, 0),  # Red
        (0, 1, 0),  # Green
        (0, 0, 1),  # Blue
        (1, 1, 0),  # Yellow
        (1, 0, 1),  # Magenta
        (0, 1, 1),  # Cyan
        (1, 0.5, 0),  # Orange
        (0.5, 0, 1),  # Purple
        (0, 1, 0.5),  # Teal
        (1, 0, 0.5),  # Pink
        (0.5, 0.5, 0.5),  # Gray
        (0.5, 0, 0),  # Maroon
        (0, 0.5, 0),  # Olive
        (0, 0, 0.5),  # Navy
        (0.5, 0, 0.5),  # Indigo
        (0.5, 0.5, 0),  # Olive Drab
        (0, 0.5, 0.5),  # Turquoise
    ]
    size_rect = 10
    cent_x = Window.width / 2 - size_rect / 2
    cent_y = Window.height / 2 - size_rect / 2
    print(cent_x, cent_y)
    image = Rectangle(source="star.png")
    def __init__(self,**kwargs):
        super(Explosion,self).__init__(**kwargs)

        with self.canvas:
            for i in range(1000):
                rectangle=Rectangle(pos=(randint(1,800),randint(1,600)),size=(self.size_rect,self.size_rect),texture=self.image.texture)
                self.canvas.add(rectangle)
                Animation(duration=2,pos=(self.cent_x,self.cent_y),size=(0,0)).start(rectangle)

        Clock.schedule_once(self.in_explose,3)


    def in_explose(self,dt):
        for i in range(3):
            Clock.schedule_once(self.on_explose, 2*i)
    def on_explose(self,dt):
        with self.canvas:
            for i in range(1000):
                Color(*random.choice(self.colors))
                rectangle = Rectangle(pos=(self.cent_x,self.cent_y), size=(self.size_rect,self.size_rect),texture=self.image.texture)
                self.canvas.add(rectangle)
                Animation(duration=2, pos=(self.cent_x+randint(-1000, 1000), self.cent_y+randint(-1000, 1000)), size=(0, 0)).start(rectangle)
            self.play_sound("sound/explose.mp3")
    def play_sound(self, filename):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(0.5)
        sound.play()
class ExploseApp(App):
    def build(self):
        return Explosion()
if __name__ == '__main__':
    ExploseApp().run()
