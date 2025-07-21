from ursina import *

app = Ursina()

# Add a player cube
player = Entity(model='cube', color=color.red, position=(0,0,1),size_list=(2,2,2))

# Add the floor
ground = Entity(model='plane', scale=10, color=color.green, collider='box')

camera.position = (0, 0, 20)
camera.rotation_x = 0
camera.look_at((0,0,0))
def update():
    if held_keys['left arrow']:
        player.x -= 0.1
        # print((player.x,player.y,player.z))
        # print(held_keys)
    if held_keys['right arrow']:
        player.x += 0.1
        # print((player.x,player.y,player.z))
        # print(held_keys)
    if held_keys['up arrow']:
        player.z -= 0.1
        # print((player.x,player.y,player.z))
        # print(held_keys)
    if held_keys['down arrow']:
        player.z +=0.1
        # print((player.x,player.y,player.z))
        # print(held_keys)

app.run()
