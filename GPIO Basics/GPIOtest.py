import time
print 'Enter GPIO BCM number:'
gpio = raw_input()
print 'Enter number of blinks you want:'
blinks = raw_input()
file= open ('/sys/class/gpio/export','w')
file.write(str(gpio))
file.close()
path = '/sys/class/gpio/gpio' + gpio + '/direction'
file= open (path,'w')
file.write('out')
file.close()
i=0;
path = '/sys/class/gpio/gpio' + gpio + '/value'
while(i<int(blinks)):
    file= open (path,'w')
    file.write('1')
    file.close()
    time.sleep(0.5)
    file= open (path,'w')
    file.write('0')
    file.close()
    time.sleep(0.5)
    i+=1
file= open ('/sys/class/gpio/unexport','w')
file.write(str(gpio))
file.close()
print 'Good Bye!'

