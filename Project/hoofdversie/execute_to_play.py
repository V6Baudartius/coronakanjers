import os, sys
if getattr(sys,'frozen',False):
    os.chdir(sys._MEIPASS)

import Ragnarok.main
print('import succesful')

import cProfile
#cProfile.run('Ragnarok.main.execute()')
Ragnarok.main.execute()


