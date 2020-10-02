from datetime import datetime
from time import sleep

from comunication import AY
from tools import PGS_FILE


def play_pgs(ay, pgs):
    co = 0
    for f in pgs.next_frame():
        start_time = datetime.now()
        print("Frame", hex(co))
        co += 1
        if f:
            for i in range(int(len(f) / 2)):
                ay.wr(f[i * 2], f[i * 2 + 1])
                sleep(0.00001)
                print(hex(f[i * 2]), '<-', hex(f[i * 2 + 1]))
        else:
            print("  empty  ")
        end_time = datetime.now()
        # делаем задержку в 1/50 секунды учитывая время сколько была отправка данных.
        sleep_time = 0.02 - ((end_time - start_time).microseconds * 0.000001)
        print("to next frame est:", sleep_time)
        sleep(sleep_time)
        print()


if __name__ == '__main__':
    pgs = PGS_FILE("Nemesis The Warlock.psg")
    # pgs = PGS_FILE("D.J.Serg - SoundStorm (2001) (Millennium 1901, 2).psg")
    ay = AY()
    ay.connect()
    ay.clean()

    try:
        play_pgs(ay, pgs)
    except KeyboardInterrupt:
        print("Stop by user")

    ay.clean()
    ay.close_port()
