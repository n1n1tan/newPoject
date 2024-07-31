from control import key_press, SC_DOWN, SC_UP,SC_RIGHT,SC_LEFT, key_down
from queue import Queue
from threading import Thread

q = Queue()


def control_car():
    while func := q.get() is not None:


        # key_down(SC_UP)
        cof = abs(func) // 3200
        cof2 = abs(func) // 5000
        speed = 0.07 - cof2

        if func > 0:
            key_press(SC_UP, interval= speed)
            key_press(SC_RIGHT, interval=cof)
            key_press(SC_LEFT, interval=cof//2)
            # if func > 250:
            #     key_press(SC_DOWN, interval=abs(speed))

        if func < 0:
            key_press(SC_UP, interval= speed)
            key_press(SC_LEFT,interval=cof)
            key_press(SC_RIGHT, interval=abs(cof) // 2)
            # if func < -250:
            #     key_press(SC_DOWN, interval=abs(speed))

th = Thread(target=control_car)