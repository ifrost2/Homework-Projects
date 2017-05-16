# Entropy
# Designed and Developed By Mausam, http://www.cs.washington.edu/homes/mausam
# Modified by Chitesh Tewani

#------------------------------------------------------------#
#                 DO NOT CHANGE ANYTHING IN 	         	 #
#                   THIS FILE                    			 #
#------------------------------------------------------------#

# humanSocket.py
# this is a module which emulates a human user as a client connected to socket :p

# import os, sys
# sys.path.insert(0, os.path.realpath('../utils/'))
# from nbstreamreader import NonBlockingStreamReader as NBSR

import json

TEXTCONV = {'A': 'R', 'B': 'C', 'C': 'G','D':'B', 'E':'Y', '-':'-'}
class HumanSocket:
	def __init__(self):
		pass

	# this is actually the recv :D weird but true!
	def send(self, msg):
		if (len(msg) <= 0):
			return

		dct = json.loads(msg)

		# if 'payload' in dct and 'ORDER' not in dct['payload'] and 'CHAOS' not in dct['payload']:
		# 	for a in TEXTCONV:
		# 		dct['payload'] = dct['payload'].replace(a, TEXTCONV[a])

		if (dct['purpose'] == 'reset'):
			self.reset = 0
			pass

		elif (dct['purpose'] == 'kill'):
			pass

		elif (dct['purpose'] == 'update'):
			#print "here"
			print 'server$ %s'%dct['payload'][:-2].strip().replace('\n', '\nserver$ ')
			#print "all printed"
			#a = dct['payload']
			print 'Color picked %s'%TEXTCONV[dct['payload'][-2]]
			#print TEXTCONV[a]
			inp = raw_input('Your Move$ ')
			self.nextInp = inp+'\n'

		elif (dct['purpose'] == 'update_only'):
			print 'server$ %s'%dct['payload'].strip().replace('\n', '\nserver$ ')

	# this is actually the send method!! - weird but true :D
	def recv(self, sz):
		if (self.nextInp):
			move = self.nextInp
			self.nextInp == None
			return json.dumps({'payload': move, 'status':True})
		else:
			print 'Error $ Something bad happened'

	def proveYourSelf():
		return 'human'

	def close(self):
		pass
