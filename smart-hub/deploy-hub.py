from ConfigParser import SafeConfigParser
import os
import subprocess
import sys

def excute_remote_script(host, path_to_script, arg) :
    print "Connecting to " + host + "."
    result = subprocess.check_output("ssh -q " + host + "exit", shell=True)

    if result == "0" :
        print "Successfully connected to " + host + "."
    	os.system("ssh " + host + "'bash -s' < " + path_to_script + arg)
		
    else :
        print "Failed to connect to $host (Error code: " + result + ")."

def excute_script(path_to_script, arg) :
    os.system(path_to_script + arg)


#Main
parser = SafeConfigParser()
parser.read('/Users/jared/Repository/deployment/scripts/config.ini')

if len(sys.argv) >= 1 :
	deployment=sys.argv[1]
	arg=' '.join(sys.argv[2:])

	if parser.has_section(deployment) :
		host=parser.get(deployment, 'host')
		path_to_script=parser.get(deployment, 'path_to_script')
		if host == "smart-hub" :
			excute_script(path_to_script, arg)
		else :
			excute_remote_script(host, path_to_script, arg)
	else :
		print "Could not find " + deployment+ "."

else :
	print "Must be only one arg, try [deploy $deployment_name]."