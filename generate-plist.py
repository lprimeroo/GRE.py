import plistlib
import getpass

username = getpass.getuser()

d = {   'Label':'com.'+username+'.gre',
	'Program':'/Users/'+username+'/gre.py',
	'StartInterval':30,
	'RunAtLoad':True,
	'StandardErrorPath':'tmp/com.'+username+'.gre.err',
	'StandardOutPath':'/tmp/com.'+username+'.gre.out',		 
      }

output_file = open('com.'+username+'.gre.plist','w+')
plistlib.writePlist(d, output_file)
