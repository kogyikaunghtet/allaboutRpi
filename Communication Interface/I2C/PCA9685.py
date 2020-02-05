import time
import math

class PWM:
    _mode_adr              = 0x00
    _base_adr_low          = 0x08
    _base_adr_high         = 0x09
    _prescale_adr          = 0xFE

    def __init__(self, bus, address = 0x40):
        self.bus = bus
        self.address = address
        self._writeByte(self._mode_adr, 0x00)

    def setFreq(self, freq):
        prescaleValue = 25000000.0
        prescaleValue /= 4096.0
        prescaleValue /= float(freq)
        prescaleValue -= 1.0
        prescale = math.floor(prescaleValue + 0.5)
        oldmode = self._readByte(self._mode_adr)
        if oldmode == None:
            return
        newmode = (oldmode & 0x7F) | 0x10
        self._writeByte(self._mode_adr, newmode)
        self._writeByte(self._prescale_adr, int(math.floor(prescale)))
        self._writeByte(self._mode_adr, oldmode)
        time.sleep(0.005)
        self._writeByte(self._mode_adr, oldmode | 0x80)

    def setDuty(self, channel, duty):
        data = int(duty * 4096 / 100)
        self._writeByte(self._base_adr_low + 4 * channel, data & 0xFF)
        self._writeByte(self._base_adr_high + 4 * channel, data >> 8)

    def _writeByte(self, reg, value):
        try:
            self.bus.write_byte_data(self.address, reg, value)
        except:
            print "Error while writing to I2C device"

    def _readByte(self, reg):
        try:
            result = self.bus.read_byte_data(self.address, reg)
            return result
        except:
            print "Error while reading from I2C device"
            return None
