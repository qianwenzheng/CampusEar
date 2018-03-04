from subprocess import Popen
p = Popen("script.bat", cwd=r"C:\Users\seanl\Documents\GitHub\CampusEar")
stdout, stderr = p.communicate()