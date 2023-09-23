from pico2d import *
open_canvas()

character = load_image('sonic3.png')

stand_index = [0,51,101,147,196,270]
running_index = [-3,55,115,170]
def stand(frame):
    if frame >= 5:
        frame = 0
    character.clip_draw(173 + stand_index[frame], 345, 45, 100, 400, 90)
    pass

def runnig(frame):

    character.clip_draw(250 + running_index[frame] + 5, 85, 50, 80, 400, 90)

    pass

x = 0
frame = 0

while True:
    clear_canvas()
    #stand(frame)
    runnig(frame)
    update_canvas()
    delay(0.05)
    get_events()
    frame = frame + 1
    if frame >= 4:
        frame = 0
    pass


close_canvas()