# import library ursina
from ursina import *
import math 

#update rotasi,ukuran,perputaran, posisi
def update():
    global t
    t = t + 0.02 #0.02 adalah kecepatan putaran
    angle = math.pi*40/180

    radius_1 = 2 #radius = urutan - 2 jarak dengan matahari
    mercury.x = math.cos(t)*radius_1
    mercury.z = math.sin(t)*radius_1

    radius_2 = 2.5
    venus.x = math.cos(t+angle*2)*radius_2
    venus.z = math.sin(t+angle*2)*radius_2
    
    radius_3 = 3
    earth.x = math.cos(t+angle*3)*radius_3
    earth.z = math.sin(t+angle*3)*radius_3

    radius_4 = 3.2
    mars.x = math.cos(t+angle*4)*radius_4
    mars.z = math.sin(t+angle*4)*radius_4
    
    radius_5 = 3.7
    jupiter.x = math.cos(t+angle*4.5)*radius_5
    jupiter.z = math.sin(t+angle*4.5)*radius_5
    
    radius_6 = 4.7
    saturnus.x = math.cos(t+angle*5)*radius_6
    saturnus.z = math.sin(t+angle*5)*radius_6
    
    radius_7 = 5.5
    uranus.x = math.cos(t+angle*5.5)*radius_7
    uranus.z = math.sin(t+angle*5.5)*radius_7
    
    radius_8 = 6
    saturnus.x = math.cos(t+angle*6.5)*radius_8
    saturnus.z = math.sin(t+angle*6.5)*radius_8
    


    #rotation sun
    sun.rotation_y += time.dt*20
    earth.rotation_y += time.dt*50


# load backround dll
class Sky(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere', #load model
            texture = 'textures/star.jpg', #load background
            present = scene, #load gaya tampilan
            scale = 150, #size backround
            double_sided = True # supaya bisa dilihat segala arah view 
        )

# initial app
app = Ursina()
bg = Sky()
EditorCamera()

#load image sun & planet
sun = Entity(model = "sphere", texture = "textures/sun.jpg" , scale = 3)
mercury = Entity(model = 'obj/Mercury 1K.obj', texture = "textures/mercury.png" , scale = 1)
venus = Entity(model = 'sphere', texture = "textures/venus.jpg" , scale = 0.8)
earth = Entity(model = 'sphere', texture = "textures/earth.jpg" , scale = 0.9)
mars = Entity(model = 'obj/Mars 2k.obj', texture = "textures/mars.png" , scale = 0.1)
jupiter = Entity(model = 'sphere', texture = "textures/jupiter.jpg" , scale = 1.4)
saturnus = Entity(model = 'sphere', texture = "textures/saturn.jpg" , scale = 1.1)
uranus = Entity(model = 'sphere', texture = "textures/uranus.jpg" , scale = 1)
neptunus = Entity(model = 'sphere', texture = "textures/neptun.jpg" , scale = 1.05)



t = -math.pi

# run app
app.run()