from control import key_press, SC_DOWN, SC_UP,SC_RIGHT,SC_LEFT, key_down, key_up, SC_INS, SC_DEL
from queue import Queue
from threading import Thread

q = Queue()





def control_car():
    per = 2
    while (func := q.get()) is not None:
        key_down(SC_UP)
        # cof = func / 2000
          # speed = func / 3400
        # print(f'{func} --- {abs(cof):.3}')

        LIMIT2 = 200
        LIMIT1 = 100
        LIMIT3 = 50
        if per > 4:
            key_press(SC_DEL)
            per = 4
        if per < 2:
            key_press(SC_INS)
            per = 2
        if -1*LIMIT2 < func < LIMIT2:
            ...
            key_up(SC_LEFT)
            key_up(SC_RIGHT)
            key_press(SC_INS)
            if per < 3:
                key_press(SC_INS)
                per = 4
        elif func > LIMIT2:
            key_down(SC_RIGHT)
            key_press(SC_DEL)
            if per != 2:
                key_press(SC_DEL)
                per = 2
        elif LIMIT3 < func < LIMIT1:

            # key_press(SC_UP, interval=0.02)
            key_press(SC_LEFT, interval=0.03)
            # key_press(SC_LEFT, interval=abs(cof) / 2)
            # if func > 270:
            #     key_press(SC_DOWN, interval=0.09)
        elif -1*LIMIT1 < func < -1*LIMIT3:
            key_press(SC_RIGHT, interval=0.03)

        elif func < LIMIT2:
            key_down(SC_LEFT)
            if per != 2:
                key_press(SC_DEL)
                per = per - 2
            #key_press(SC_RIGHT, interval=0.05)
            # key_press(SC_UP,interval = 0.06)
            # key_press(SC_LEFT, interval=abs(cof))
            # key_press(SC_RIGHT, interval=abs(cof) / 2)
            # if func < -270:
            #     key_press(SC_DOWN, interval=0.09)
            #     key_press(SC_LEFT, interval=abs(cof) )

th = Thread(target=control_car)