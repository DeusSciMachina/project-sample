
import webapp2
import jinja2
import os
from models import Post
from models import Author



the_jinja_env =jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(result_template.render())
class DisplayHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/Show.html')
        self.response.write(result_template.render())
class familyHandler(webapp2.RequestHandler):
        def get(self):
            result_template = the_jinja_env.get_template('templates/about_my_family.html')
            self.response.write(result_template.render())

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/new_post.html')
        self.response.write(result_template.render())
    def post(self):
        theName = self.request.get('name')
        theTitle = self.request.get('title')
        theContent = self.request.get('content')
        theBlogPost = Post(title=theTitle, content=theContent)
        theBlogPost.put()

        the_check_authors = Author.query(Author.username == theName).fetch()
        if len(the_check_authors)>0:
                author = the_check_authors[0]
                author.posts.append(theBlogPost.key)
        else:
                author = Author(username =theName, posts= [theBlogPost.key] )
        author.put()
        theBlogPost=[]
        for theBlogPost_key in author.posts:
            theBlogPost.append(theBlogPost_key.get())


        template_vars = {
        'username': theName,
        'blog_posts': theBlogPost
        }

        print("Received: %s" % (theName))
        var_dict = {
            "line1": theName,
            "line2": theTitle,
            "line3": theContent







        }
        result_template= the_jinja_env.get_template('templates/new_post.html')
        self.response.write(result_template.render(var_dict))




app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/post', BlogHandler),
    ('/Show', DisplayHandler),
    ('/about_my_family',familyHandler)
], debug=True)
