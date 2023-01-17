#!/usr/bin/python

import daemon

def my_long_script():
    for i in range(1000):
        ffoo = open('some.log', 'a')
        ffoo.write('String no' + str(i))
        ffoo.close()

#with daemon.DaemonContext():
my_long_script()