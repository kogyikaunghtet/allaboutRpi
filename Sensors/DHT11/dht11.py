import time
import RPi.GPIO as GPIO
class DHT11Result:
  ERR_NO_ERROR = 0
  ERR_MISSING_DATA = 1
  ERR_CRC = 2
  error_code = ERR_NO_ERROR
  temperature = -1
  humidity = -1
  def __init__(self, error_code, temperature, humidity):
    self.error_code = error_code
    self.temperature = temperature
    self.humidity = humidity
  def is_valid(self):
    return self.error_code == DHT11Result.ERR_NO_ERROR
class DHT11:
  __pin = 0
  def __init__(self, pin):
    self.__pin = pin
  def read(self):
    GPIO.setup(self.__pin, GPIO.OUT)
    self.__send_and_sleep(GPIO.HIGH, 0.05)
    self.__send_and_sleep(GPIO.LOW, 0.02)
    GPIO.setup(self.__pin, GPIO.IN, GPIO.PUD_UP)
    data = self.__collect_input()
    pull_up_lengths = self.__parse_data_pull_up_lengths(data)
    if len(pull_up_lengths) != 40:
      return DHT11Result(DHT11Result.ERR_MISSING_DATA, 0, 0)
    bits = self.__calculate_bits(pull_up_lengths)
    the_bytes = self.__bits_to_bytes(bits)
    checksum = self.__calculate_checksum(the_bytes)
    if the_bytes[4] != checksum:
      return DHT11Result(DHT11Result.ERR_CRC, 0, 0)
    return DHT11Result(DHT11Result.ERR_NO_ERROR, the_bytes[2], the_bytes[0])

  def __send_and_sleep(self, output, sleep):
    GPIO.output(self.__pin, output)
    time.sleep(sleep)
  def __collect_input(self):
    unchanged_count = 0
    max_unchanged_count = 100
    last = -1
    data = []
    while True:
      current = GPIO.input(self.__pin)
      data.append(current)
      if last != current:
        unchanged_count = 0
	last = current
      else:
	unchanged_count += 1
	if unchanged_count > max_unchanged_count:
	  break
    return data
  def __parse_data_pull_up_lengths(self, data):
    STATE_INIT_PULL_DOWN = 1
    STATE_INIT_PULL_UP = 2
    STATE_DATA_FIRST_PULL_DOWN = 3
    STATE_DATA_PULL_UP = 4
    STATE_DATA_PULL_DOWN = 5
    state = STATE_INIT_PULL_DOWN
    lengths = []
    current_length = 0
    for i in range(len(data)):
      current = data[i]
      current_length += 1
      if state == STATE_INIT_PULL_DOWN:
        if current == GPIO.LOW:
	  state = STATE_INIT_PULL_UP
	  continue
	else:
	  continue
      if state == STATE_INIT_PULL_UP:
        if current == GPIO.HIGH:
	  state = STATE_DATA_FIRST_PULL_DOWN
	  continue
	else:
	  continue
      if state == STATE_DATA_FIRST_PULL_DOWN:
        if current == GPIO.LOW:
	  state = STATE_DATA_PULL_UP
	  continue
	else:
	  continue
      if state == STATE_DATA_PULL_UP:
        if current == GPIO.HIGH:
	  current_length = 0
	  state = STATE_DATA_PULL_DOWN
	  continue
	else:
	  continue
      if state == STATE_DATA_PULL_DOWN:
        if current == GPIO.LOW:
	  lengths.append(current_length)
	  state = STATE_DATA_PULL_UP
	  continue
	else:
	  continue
    return lengths
  def __calculate_bits(self, pull_up_lengths):
    shortest_pull_up = 1000
    longest_pull_up = 0
    for i in range(0, len(pull_up_lengths)):
      length = pull_up_lengths[i]
      if length < shortest_pull_up:
        shortest_pull_up = length
      if length > longest_pull_up:
	longest_pull_up = length
    halfway = shortest_pull_up + (longest_pull_up - shortest_pull_up) / 2
    bits = []
    for i in range(0, len(pull_up_lengths)):
      bit = False
      if pull_up_lengths[i] > halfway:
        bit = True
      bits.append(bit)
    return bits
  def __bits_to_bytes(self, bits):
    the_bytes = []
    byte = 0
    for i in range(0, len(bits)):
      byte = byte << 1
      if (bits[i]):
        byte = byte | 1
      else:
	byte = byte | 0
      if ((i + 1) % 8 == 0):
	the_bytes.append(byte)
	byte = 0
    return the_bytes
  def __calculate_checksum(self, the_bytes):
    return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255
