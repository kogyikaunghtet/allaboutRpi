import time
print 'Enter GPIO BCM number:'
gpio = raw_input()
print 'Enter number of blinks you want:'
blinks = raw_input()
f= open ('/sys/class/gpio/export','w')
f.write(str(gpio))
f.close()
path = '/sys/class/gpio/gpio' + gpio + '/direction'
f= open (path,'w')
f.write('out')
f.close()
i=0;
path = '/sys/class/gpio/gpio' + gpio + '/value'
while(i<int(blinks)):
    f= open (path,'w')
    f.write('1')
    f.close()
    time.sleep(0.5)
    f= open (path,'w')
    f.write('0')
    f.close()
    time.sleep(0.5)
    i+=1
f= open ('/sys/class/gpio/unexport','w')
f.write(str(gpio))
f.close()
print 'Good Bye!'

