from google.appengine.ext import ndb



class SaveState(ndb.Model):
    name = ndb.StringProperty()
    content = ndb.TextProperty()
class Player(ndb.Model):
    username = ndb.StringProperty()
    posts = ndb.KeyProperty(kind = "Post", repeated = True)
