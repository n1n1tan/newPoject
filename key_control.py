from control import key_press, SC_DOWN, SC_UP,SC_RIGHT,SC_LEFT, key_down
from queue import Queue
from threading import Thread

q = Queue()


def control_car():
    while (func := q.get()) is not None:
        cof = func / 2000
        # speed = func / 3400
        print(func,abs(cof))
        if func > 0:
            key_press(SC_UP, interval=0.06)
            key_press(SC_RIGHT, interval=abs(cof))
            key_press(SC_LEFT, interval=abs(cof) / 2)
            if func > 270:
                key_press(SC_DOWN, interval=0.09)
        else:
            key_press(SC_UP,interval = 0.06)
            key_press(SC_LEFT, interval=abs(cof))
            key_press(SC_RIGHT, interval=abs(cof) / 2)
            if func < -270:
                key_press(SC_DOWN, interval=0.09)
                key_press(SC_LEFT, interval=abs(cof) )

th = Thread(target=control_car)