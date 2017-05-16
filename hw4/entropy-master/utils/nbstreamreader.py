# Entropy
# Designed and Developed By Mausam, http://www.cs.washington.edu/homes/mausam
# Modified by Chitesh Tewani

#------------------------------------------------------------#
#                 DO NOT CHANGE ANYTHING IN 	         	 #
#                   THIS FILE                    			 #
#------------------------------------------------------------#

# stolen from: http://eyalarubas.com/python-subproc-nonblock.html
# so that the client DOES not hang infinetely for a bad client.

from threading import Thread
from multiprocessing import Queue

class NonBlockingStreamReader:

    def __init__(self, stream):
        '''
        stream: the stream to read from.
                Usually a process' stdout or stderr.
        '''

        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            '''
            Collect lines from 'stream' and put them in 'quque'.
            '''

            while True:
                line = stream.readline()
                if line:
                    queue.put(line)
                else:
                    return # HOPEFULLY NOTHING ELSE HAPPENS THAT BAD
                    # raise UnexpectedEndOfStream

        self._t = Thread(target = _populateQueue,
                args = (self._s, self._q))
        self._t.daemon = True
        self._t.start() #start collecting lines from the stream

    def readline(self, timeout = None):
        try:
            return self._q.get(block = timeout is not None,
                    timeout = timeout)
        except Empty:
            return None

class UnexpectedEndOfStream(Exception): pass