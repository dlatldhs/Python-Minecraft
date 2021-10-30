from sys import float_repr_style
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fps_counter.enabled = False #fps 수치 지우는거
window.exit_button.visible = False #빨강색 종료 버튼 

blocks=[
    'dirt.png','assets/coblestone.png','assets/diamond.png','assets/tree.png'
]
block_id = 0

def input(key):
    global block_id

    if key.isdigit():#만약 숫자가 입력이 된다면 
        block_id = int(key)#block_id에 int형으로 숫자를 넣음
        if block_id >= len(blocks):
            block_id = len(blocks)
        print(block_id)


#배경 신 class 세계의 사물
Entity(
    parent=scene,#3d 존재 사실 알림
    model='sphere',#구형 모양 모델 
    texture=load_texture('assets/picture.png'), #texture 정의함 텍스쳐 
    scale=500,#크기
    double_sided=True#구모양인 모델에 텍스쳐를 다 씌운다는 얘기 
    #텍스쳐를 구의 양면에 적용   = * 양 면 * =
)

hand = Entity(
    parent = camera.ui,
    model='tree.png',
    texture=blocks[block_id],
    scale=0.2,
    position=Vec2(0.5,-0.5)
)

#객체 마크에 쓰일 블록하나
class Voxel(Button):
    def __init__(self,position=(0,0,0),texture='assets/tree.png'):
        super().__init__(
            parent=scene,#3D 공간이 있음을 의미함 parent 형의 기본형이 이거임 UI 쓸려면 camera.ui 사용 하셈 
            position=position,#포지션 위치 바닥
            model='cube',#생성되는 ursina 안에 신 class Entity 모델 중 하나 cube 큐브 모양 생성함 모양은..
            origin_y=0.5,
            texture=texture,#텍스쳐
            color=color.color(0,0,random.uniform(0.9,1.0)),#색 랜덤으로
            scale=1.0#크기
        )
    #in class method 첫번째 인자는 항상 거의 대부분 90%정도 self 인자여야함 인스턴스 생성될떄 ㅇㅇ 쳐보셈
    def input(self,key):
        #ursina in hover = mouse pointer 가르킬 경우
        if self.hovered:#마우스를 블록 위에 올린다면
            if key == 'right mouse down':#오른쪽 마우스를 클릭하면 
                Voxel(position=self.position + mouse.normal,texture=blocks[block_id-1])#블록 하나 객체 하나를 생성함
                #새로생성된 블록의 위치는 마우스 포인터에 위치함 normal이 주소임 가상 공간안에서의 주소
            elif key == 'left mouse down':
                destroy(self)#파괴함
        
    
    

#수학에서 3차 처럼 zxy 로 세상을 3d로 나눔 대충 뭔뜻인지 알겠음 ? 일단 가로랑 세로 20길이를 만드는 거임
for z in range(20):
    for x in range(20):
        blok=Voxel(position=(x,0,z))#위에 만들어놓은 블록 객체를 쓴거임 ㅎㅎ

#ursina 함수인데 이렇게하면 플레이어 만들어줌 ㅎ
player = FirstPersonController()#player 를 만듬        


app.run()
