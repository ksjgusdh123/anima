from pico2d import *
open_canvas()

character = load_image('sonic3.png')

stand_index = [0,51,101,147,196,270]
running_index = [-3,55,115,170, 170]
jump_index_x = [0, 80, 0, 0, 0]
jump_index_y = [150, 150, 245, 245, 245]

def stand(frame, x, y):
    character.clip_draw(173 + stand_index[frame], 345, 45, 100, x, y)

def running(frame, x, y):
    character.clip_draw(250 + running_index[frame] + 5, 85, 50, 80, x, y)

def Backdumbling(frame, x, y):
    character.clip_draw(11 + running_index[frame], 0, 55, 80, x, y)

def jump(frame, x, y):
    character.clip_draw(20 + jump_index_x[frame], jump_index_y[frame], 65, 105, x, y)


x = 50
frame = 0
y = 90
back = False
jumpping = False
while True:
    clear_canvas()
    if x == 50 and y <= 500:
       jump(frame, x, y)
       y+=20
       jumpping = True
       if(y >= 500):
           jumpping = False

    elif x < 700 and back == False:
        running(frame, x, y)

        x += 5

    elif x == 700 and back == False:
        back = True
        stand(frame, x, y)

    elif x >= 50 and back == True:
        Backdumbling(frame, x, y)
        x -= 5
        if x <= 50:
            back = False

    frame = frame + 1
    if frame >= 5:
        if(jumpping):
            frame = 2
        else:
            frame = 0
    update_canvas()
    delay(0.05)
    get_events()
    pass


close_canvas()