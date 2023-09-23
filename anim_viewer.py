from pico2d import *
open_canvas()

character = load_image('sonic3.png')

stand_index = [0,51,101,147,196,270]
running_index = [-3,55,115,170, 170]
def stand(frame, x):
    character.clip_draw(173 + stand_index[frame], 345, 45, 100, x, 90)

def running(frame, x):
    character.clip_draw(250 + running_index[frame] + 5, 85, 50, 80, x, 90)

def Backdumbling(frame, x):
    character.clip_draw(11 + running_index[frame], 0, 55, 80, x, 90)


x = 0
frame = 0
back = False
while True:
    clear_canvas()
    if x < 700 and back == False:
        running(frame, x)
        x += 5

    elif x == 700 and back == False:
        back = True
        stand(frame, x)

    elif x >= 50 and back == True:
        Backdumbling(frame, x)
        x -= 5
        if x <= 50:
            back = False

    frame = frame + 1
    if frame >= 5:
        frame = 0
    update_canvas()
    delay(0.01)
    get_events()
    pass


close_canvas()