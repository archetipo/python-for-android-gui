#!/usr/bin/python
#-*- coding:utf-8 -*-


import os, sys, re, StringIO
import fcntl, termios, struct
import threading

class ThLogCat( threading.Thread ):
	def __init__( self,parent):

		self.TAGTYPE_WIDTH = 3
		self.TAG_WIDTH = 20
		self.PROCESS_WIDTH = 8 # 8 or -1

		self.KNOWN_TAGS = {
			"dalvikvm": '[color=#1F1ABD][b]Dalvikvm[/b][/color]',
			"Process": '[color=#1F1ABD][b]Process[/b][/color]',
			"ActivityManager": '[color=#85E3EF][b]ActivityManager[/b][/color]',
			"ActivityThread": '[color=#85E3EF][b]ActivityThread[/b][/color]',
		}
		self.TAGTYPES = {
			"V": "[color=#000000][b]V[/b][/color] - " ,
			"D": "[color=#11119A][b]D[/b][/color] - " ,
			"I": "[color=#1A9804][b]I[/b][/color] - ",
			"W": "[color=#DB7900][b]W[/b][/color] - " ,
			"E": "[color=#CF140B][b]E[/b][/color] - " ,
		}
		self.retag = re.compile("^([A-Z])/([^\(]+)\(([^\)]+)\): (.*)$")
		self.parent=parent
		self.dataactive=False
		self.alive = False
		self.adb_args = ' '
		self.adbpath=self.parent.adbpath
		print self.adbpath
		threading.Thread.__init__ ( self )

	def run ( self ):
		# if someone is piping in to us, use stdin as input.  if not, invoke adb logcat
		if os.isatty(sys.stdin.fileno()):
			input = os.popen("%s/adb  %s logcat" % (self.adbpath,self.adb_args))
		else:
			input = sys.stdin

		while (self.alive):
			try:
				line = input.readline()
			except KeyboardInterrupt:
				break

			match = self.retag.match(line)
			if not match is None:
				tagtype, tag, owner, message = match.groups()
				if tag in self.KNOWN_TAGS and tagtype in self.TAGTYPES[tagtype]:
					lineout='%s Type: [b]%s[/b] - Proc:[b]%s[/b] - msg: [b]%s[/b]' % (self.TAGTYPES[tagtype],self.KNOWN_TAGS[tag],owner,message)
				elif tagtype in self.TAGTYPES[tagtype]:
					lineout='%s Type: [color=#9E4509][b]%s[/b][/color] - Proc:[b]%s[/b] - msg: [b]%s[/b]' % (self.TAGTYPES[tagtype],tag,owner,message)
				else:
					lineout='[color=#28520B][b]V[/b][/color] - Type: [color=#9E4509][b]%s[/b][/color] - Proc:[b]%s[/b] - msg: [b]%s[/b]' % (tagtype,tag,owner,message)
				line=lineout
			print line
			self.parent.line='%s. \n'% line
			self.dataactive=True
			if len(line) == 0:
				self.dataactive=False
				break

#--------------------------------------- The End
#~ class Obj():
	#~ def inizia(self):
		#~ self.drivectrl=ThLogCat(self)
		#~ self.drivectrl.start()
#~
#~ o=Obj()
#~ o.inizia()
