
import webapp2
import jinja2
import os
from Save import SaveState
from Save import Player



the_jinja_env =jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainGamePageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/GamePage.html')
        self.response.write(result_template.render())

class SaveHandler(webapp2.RequestHandler):
    """
    def get(self):
        result_template = the_jinja_env.get_template('templates/new_user.html')
        self.response.write(result_template.render())
    """
    def post(self):
        theName = self.request.get('name')
        theContent = self.request.get('content')
        theSaveGame = SaveState(content=theContent)
        theSaveGame.put()

        the_check_player = Player.query(Player.username == theName).fetch()
        if len(the_check_player)>0:
                player = the_check_player[0]
                player.posts.append(theSaveGame.key)
        else:
                player = Player(username =theName, posts= [theSaveGame.key] )
        player.put()
        theSaveGame=[]
        for theSaveGame_key in player.posts:
            theSaveGame.append(theSaveGame_key.get())


        template_vars = {
        'username': theName,
        'save_game': theSaveGame
        }

        print("Received: %s" % (theName))
        var_dict = {
            "line1": theName,
            "line2": theContent







        }
        result_template= the_jinja_env.get_template('templates/GamePage.html')
        self.response.write(result_template.render(var_dict))




app = webapp2.WSGIApplication([
    ('/', MainGamePageHandler),
    ('/saveState', SaveHandler),

], debug=True)
