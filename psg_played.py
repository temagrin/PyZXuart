from comunication import AY
from tools import PGS_FILE


if __name__ == '__main__':
    # pgs = PGS_FILE("Nemesis The Warlock.psg")
    # pgs = PGS_FILE("nq - Ppk (2002).psg")
    pgs = PGS_FILE("D.J.Serg - SoundStorm (2001) (Millennium 1901, 2).psg")
    ay = AY()
    ay.connect()
    ay.clean()
    buffer = [frame for frame in pgs.next_frame()]
    try:
        ay.play_buffer(buffer, loop_play=False)
    except KeyboardInterrupt:
        print("Stop by user")
    ay.clean()
    ay.close_port()
