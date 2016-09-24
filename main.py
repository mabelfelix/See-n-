import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import urllib2

jinja_environment = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        signInPageTemplate = jinja_env.get_template('signin.html')

        if GoogleAuth.isSignedIn.get():
            user = GoogleUser.getBasicProfile()
            self.getMain(user)

    def getMain(self):
        MainPageTemplate = jinja_env.get_template('mainpage.html')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
