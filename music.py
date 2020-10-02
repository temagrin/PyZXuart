from time import sleep
from macros import drums, synth
from comunication import AY


def chponk(ay):
    t1 = 0x1A
    t2 = 1
    ay.wr(6, 0)
    ay.wr(7, 0xF8)
    ay.wr(1, t2)
    i = 255
    for _ in range(25):
        v = int(i / 16)
        j = (int(i / 12) % 2)
        ay.wr(8, v)
        z = int(t1 - (j * 30))
        if z < 0:
            z = 255 + z
        ay.wr(0, z)
        sleep(0.012)
        i -= 10


if __name__ == '__main__':
    ay = AY()
    ay.connect()

    for _ in range(4):
        for _ in range(4):
            sleep(0.12)
            ay.play_macros(synth.SHORT_BASS_1)
        chponk(ay)

    ay.play_macros(drums.SNARE)
    sleep(0.2)
    ay.play_macros(drums.SNARE)
    sleep(0.6)

    for _ in range(4):
        ay.play_macros(drums.SNARE)
        sleep(0.2)
        for _ in range(2):
            ay.play_macros(drums.BD)
            sleep(0.24)
            for _ in range(3):
                ay.play_macros(synth.SHORT_BASS_1)
                sleep(0.12)
            chponk(ay)


    ay.close_port()
