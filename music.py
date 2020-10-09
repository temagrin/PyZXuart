from comunication import AY
from macros.notes import NOTES


def renred_pause(buffer, sec):
    for _ in range(int(sec/0.02)):
        buffer.append([])


if __name__ == '__main__':
    ay = AY()
    ay.connect()
    ay.clean()
    buffer = []
    # http://f.rdw.se/AY-3-8910-datasheet.pdf

    oct = 2
    melody = [0, 12, 0, 24, 10, 22, 9, 21]
    start_note = 36
    i = 0
    for it in range(192):
        if it == 32:
            oct = 1
        if it == 64:
            oct = 3
        if it == 96:
            oct = 2
        if it == 128:
            oct = 1
        if it == 160:
            oct = -1

        transponse = melody[i]
        i += 1
        if i >= len(melody):
            i = 0
        for _ in range(1):
            fine, coarse = NOTES[start_note + (oct*12)+transponse]
            frame = []

            frame.extend((0, fine))  # R0 FINE Chanel A
            frame.extend((1, coarse))  # R1 COARSE Chanel A
            frame.extend((7,  0b00111100))  # R7 Enable A
            frame.extend((8,  0b00001111))  # R8 Volume channel A full
            frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A

            buffer.append(frame)

            fine, coarse = NOTES[start_note + 3 + (oct*12)+transponse]
            frame = []
            frame.extend((0, fine))  # R0 FINE Chanel A
            frame.extend((1, coarse))  # R1 COARSE Chanel A
            frame.extend((7, 0b00111110))  # R7 Enable A
            frame.extend((8, 0b00001111))  # R8 Volume channel A full
            frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
            buffer.append(frame)

            fine, coarse = NOTES[start_note + 7 + (oct*12)+transponse]
            frame = []
            frame.extend((0, fine))  # R0 FINE Chanel A
            frame.extend((1, coarse))  # R1 COARSE Chanel A
            frame.extend((7, 0b00111110))  # R7 Enable A
            frame.extend((8, 0b00001111))  # R8 Volume channel A full
            frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
            buffer.append(frame)

        frame = []
        frame.extend((7, 0b00111111))  # R7 Enable A
        frame.extend((8, 0b00000000))  # R8 Volume channel A full
        frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
        buffer.append(frame)

        for _ in range(2):
            fine, coarse = NOTES[start_note + (oct*12)+transponse]
            frame = []

            frame.extend((0, fine))  # R0 FINE Chanel A
            frame.extend((1, coarse))  # R1 COARSE Chanel A
            frame.extend((7, 0b00111110))  # R7 Enable A
            frame.extend((8, 0b00001011))  # R8 Volume channel A full
            frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
            buffer.append(frame)

            fine, coarse = NOTES[start_note + 3 + (oct*12)+transponse]
            frame = []
            frame.extend((0, fine))  # R0 FINE Chanel A
            frame.extend((1, coarse))  # R1 COARSE Chanel A
            frame.extend((7, 0b00111110))  # R7 Enable A
            frame.extend((8, 0b00001011))  # R8 Volume channel A full
            frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
            buffer.append(frame)

            fine, coarse = NOTES[start_note + 7 + (oct*12)+transponse]
            frame = []
            frame.extend((0, fine))  # R0 FINE Chanel A
            frame.extend((1, coarse))  # R1 COARSE Chanel A
            frame.extend((7, 0b00111110))  # R7 Enable A
            frame.extend((8, 0b00001011))  # R8 Volume channel A full
            frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
            buffer.append(frame)

        frame = []
        frame.extend((7, 0b00111111))  # R7 Enable A
        frame.extend((8, 0b00000000))  # R8 Volume channel A full
        frame.extend((10, 0b00001111))  # R10 Amplitude Control Chanel A
        buffer.append(frame)

    ay.play_buffer(buffer)
    ay.clean()
    ay.close_port()
