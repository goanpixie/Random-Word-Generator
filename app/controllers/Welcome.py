
from system.core.controller import *
import string, random
KEY_LEN=14

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
  
        self.load_model('WelcomeModel')
        self.db = self._app.db
   
    def index(self):  
     

        return self.load_view('index.html')

    def generate(self):
    	print "run this route" 

        if 'counter' in session:
		session['counter']=session['counter']+1
	else:
		session['counter']=0


        a=[random.choice(string.letters+string.digits) for i in range (KEY_LEN)]
        b=("".join(a).upper())
        return self.load_view('index.html',a=a,b=b)






    


        



