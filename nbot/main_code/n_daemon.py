#!/usr/bin/python

import daemon

def my_long_script():
    for i in range(100000):
        ffoo = open('some.log', 'a')
        ffoo.write('String no' + str(i) + '\n')
        ffoo.close()

with daemon.DaemonContext():
    my_long_script()
