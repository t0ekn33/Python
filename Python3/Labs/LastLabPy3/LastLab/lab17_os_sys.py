"""lab17_os_sys.py

This program shows the basic usage of several features in the
sys, os, platform and getpass modules.  You may need to change the values of the
ds and di variables to get a meaningful result.
"""

import os, sys
import platform
import getpass
import multiprocessing

print('Number of CPUs -', multiprocessing.cpu_count())
print('User name is', getpass.getuser())
env = platform.uname()  # save the platform description info (os and chip)
print('sys.version type is', type(sys.version))
print('Python version is {0}'.format(sys.version[0:6]))
print('Execution Platform is {0} {1} \nProcessor {2}'.format(
    env[0], env[3], env[5])) # print OS version and CPU chip
# print(env)
print(sys.stdin, '\n', sys.stdout)

#ds = '/home/student/pydata/words.txt'
#di = '/home/student/pydata'
ds = 'c:/pydata/words.txt'
di = 'c:/pydata'

print(sys.argv)
print(os.getcwd())
print(os.path.exists(ds), os.path.isdir(di), os.path.isfile(ds))
print(os.path.isdir(ds), os.path.isfile(di))
print(os.path.basename(ds), os.path.dirname(ds))
print('\nsys.path type is', type(sys.path))
print('\nEntries in the current path:')
for item in sys.path:
    print(item)
sys.exit()  #terminates the program
print('Did we get this far?')
