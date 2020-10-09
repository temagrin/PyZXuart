F_CLOCK_AY = 1750000
A4 = 440.0


def render_notes():
    notes = {}
    for note in range(128):
        f_note = (A4 / 32) * (2 ** ((note - 9) / 12))
        tp = int(F_CLOCK_AY/(f_note * 16))
        # coarse = tp >> 8
        coarse, fine = divmod(tp, 256)
        if coarse < 15:
            notes.update({note: (fine, coarse)})
        else:
            notes.update({note: (255, 15)})
    return notes


NOTES = render_notes()
