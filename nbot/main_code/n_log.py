#!/usr/bin/python

class N_log(object):

    def __init__(self, name):
        self.name = name
        self.file_name = name+'.log'

    def write(self, message):
        __log = open(self.file_name, 'a')
        __log.write(message+'\r\n')
        __log.close()

    def clear(self):
        open(self.file_name, 'w').close()
