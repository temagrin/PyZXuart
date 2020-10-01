from time import sleep
from macros import drums
from comunication import AY

if __name__ == '__main__':
    ay = AY()
    ay.connect()

    #B___S_____B_S___
    for _ in range(3):
        ay.play_macros(drums.BD)
        sleep(0.3)
        ay.play_macros(drums.SNARE)
        sleep(0.45)
        ay.play_macros(drums.BD)
        sleep(0.15)
        ay.play_macros(drums.SNARE)
        sleep(0.3)

    ay.close_port()
