from datetime import datetime
from time import sleep

from comunication import AY

if __name__ == '__main__':
    print('Parse file')
    # f = open("Nemesis The Warlock.psg", "rb") # Glitched(((
    f = open("D.J.Serg - SoundStorm (2001) (Millennium 1901, 2).psg", "rb")  # Normal)))
    frames = []
    frame = []
    is_header = True
    byte = f.read(1)
    while byte:
        byte = f.read(1)
        if not byte:
            break
        if '\t' == byte[0]:
            continue
        if '\r' == byte[0]:
            continue

        if 0xFF == byte[0]:
            # start frame
            is_header = False
            if frame:
                frames.append(frame)
            frame = []
            continue
        elif 0xFE == byte[0]:
            try:
                byte = int(f.read(1)[0])
                for _ in range(byte*4):
                    frames.append(None)
            except:
                print("WTH???", byte[0])
            continue
        elif not is_header:
            try:
                frame.append(int(byte[0]))
            except:
                print("WTH???", byte[0])

    print('Start melody')
    ay = AY()
    ay.connect()

    # По идее надо частоту фреймов с заголовка файла вытянуть.
    # оно там 5 или 6 байтом должно идти. но у хардкоженого трека это 50Гц
    co = 0
    for f in frames:
        start_time = datetime.now()
        print("Frame", hex(co))
        co += 1
        if f:
            for i in range(int(len(f)/2)):
                ay.wr(f[i*2], f[i*2+1])
                print(hex(f[i*2]), '<-', hex(f[i*2+1]))
        else:
            print("skip frame")
        end_time = datetime.now()
        # делаем задержку в 1/50 секунды учитывая время сколько была отправка данных.
        sleep_time = 0.02 - ((end_time-start_time).microseconds*0.000001)
        print("to next frame est:", sleep_time)
        sleep(sleep_time)
        print()
