
class PGS_FILE:
    def __init__(self, filename):
        self._filename = filename

    def next_frame(self):
        with open(self._filename, 'rb') as f:
            frame = []
            # https://documentation.help/AY-3-8910.12-ZX-Spectrum-ru/ay_r9zqf.htm offset 16 = 15 + 1
            readed_byte = f.read(16)  # skip headers bytes
            while readed_byte:
                readed_byte = f.read(1)
                if not readed_byte:
                    break
                first_byte = readed_byte[0]
                if 0xFF == first_byte:
                    if frame:
                        returner_frame = frame[:]
                        frame = []
                        yield returner_frame
                    else:
                        yield []
                else:
                    second_byte = f.read(1)[0]
                    if first_byte == 0xFE:
                        for _ in range(second_byte * 4):
                            yield []
                    else:
                        frame.append(int(first_byte))
                        frame.append(int(second_byte))
        yield frame
