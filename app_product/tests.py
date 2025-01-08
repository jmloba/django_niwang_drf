from datetime import datetime

class Messageconvert():
  def __init__(self, email,name, created=None):


    self.email  = email
    self.name = name    
    self.created = created or datetime.now()
    

