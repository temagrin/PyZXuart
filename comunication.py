import serial
from serial.tools import list_ports


class AY:
    def __init__(self):
        self._port = None

    def connect(self):
        port_name = None
        if self._port:
            self.close_port()
        ports = self._get_ports()
        if len(ports) == 0:
            print("Not found com-ports")
            exit(0)
        if len(ports) == 1:
            port_name = ports[0]
        if len(ports) > 1:
            print("Select emulator port in list")
            for i, port_name in enumerate(ports):
                print(f"  {i} :: {port_name}")
            while 1:
                number_port = input(f"Choice number from 0 to {len(ports) - 1} or 'e' to exit")
                if number_port == "e":
                    exit(0)
                if number_port not in range(len(ports)):
                    continue
                try:
                    port_name = ports[int(number_port)]
                except:
                    continue
        if not port_name:
            exit(0)

        print(f"Connect to {port_name.device}")
        self._port = serial.Serial()
        self._port.baudrate = 57600
        self._port.bytesize = serial.EIGHTBITS
        self._port.stopbits = serial.STOPBITS_ONE
        self._port.parity = serial.PARITY_NONE
        self._port.port = port_name.device
        try:
            self._port.open()
        except:
            print(f"com-port {port_name} not opened, check system")
            exit(0)

    def close_port(self):
        if self._port.is_open:
            self._port.close()

    def _get_ports(self):
        return list_ports.comports()

    def clean(self):
        for i in range(16):
            self.wr(i, 0)

    def wr(self, reqister: int, data: int):
        self._port.write(bytes([reqister, data]))

    def play_macros(self, macros):
        for r, d in macros:
            self.wr(r, d)
