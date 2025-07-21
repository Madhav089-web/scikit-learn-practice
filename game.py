from ursina import *

app = Ursina("game-testing",icon="charizard.png")

# Add a player cube
player = Entity(model='cube',  position=(0,0,1),size_list=(5,5,5), texture='brick')
sphere = Entity(
    model='sphere',
    # color=color.azure,
    scale=2,
    position=(0, 0, -1),
    collider='sphere',
  
    
)
# sphere_group = Entity()

# # Create 3 spheres under the same group
# for i in range(3):
#     s = Entity(
#         model='sphere',
#         color=color.random_color(),
#         scale=1,
#         position=(0, 0, i*2),
#         parent=sphere_group
#     )

# Add the floor
ground = Entity(model='plane', scale=10, color=color.green, collider='box',position=(0,0,0))

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
