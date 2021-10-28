from sys import float_repr_style
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False #fps 수치 지우는거
window.exit_button.visible = False #빨강색 종료 버튼 

#객체 마크에 쓰일 블록하나
class Voxel(Button):
    def __init__(self,position=(0,0,0),texture='brick'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0,random.uniform(0.9,1.0)),
            scale=1.0
        )

for y in range(20):
    for x in range(20):
        blok=Voxel(position=(x,y,0))

app.run()
