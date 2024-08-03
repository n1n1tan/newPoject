from control import key_press, SC_DOWN, SC_UP,SC_RIGHT,SC_LEFT, key_down, key_up, SC_INS, SC_DEL
from queue import Queue
from threading import Thread

q = Queue()





def control_car():
    per = 4
    while (func := q.get()) is not None:




        LIMIT2 = 200
        LIMIT1 = 100
        LIMIT3 = 50


        if per > 3:
            key_press(SC_DEL, interval=0.1)
            per = 3


        if per < 1:
            key_press(SC_INS, interval=0.1)
            per = 1


        if -1*LIMIT2 < func < LIMIT2:
            key_up(SC_LEFT)
            key_up(SC_RIGHT)
            key_down(SC_UP)
            if per != 3 and per < 4:
                key_press(SC_INS, interval=0.1)
                per = per + 1


        elif func > LIMIT2:
            key_down(SC_RIGHT)
            key_up(SC_UP)
            if per != 1:
                key_press(SC_DEL,interval=0.1)
                per = per - 1


        elif LIMIT3 < func < LIMIT1:
            key_press(SC_LEFT, interval=0.03)


        elif -1*LIMIT1 < func < -1*LIMIT3:
            key_press(SC_RIGHT, interval=0.03)

        elif func < LIMIT2:
            key_down(SC_LEFT)
            key_up(SC_UP)
            if per != 1:
                key_press(SC_DEL,interval=0.1)
                per = per - 1


th = Thread(target=control_car)