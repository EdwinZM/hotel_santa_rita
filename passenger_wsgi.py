import sys, os
INTERP = os.path.join(os.environ['HOME'], 'santa-rita.interactiva360.com', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


sys.path.append('main')
from main import app as application