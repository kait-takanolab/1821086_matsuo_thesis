import subprocess

#subprocess.call('home/pi/tools/nginxrestart.sh');
#subprocess.call('sudo stop nginx');

subprocess.run(['/home/pi/tools/nginxrestart.sh'])

