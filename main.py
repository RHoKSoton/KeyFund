import cgi
import datetime
import urllib
import webapp2
import json
import httplib 
from google.appengine.ext import db
from google.appengine.api import users

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MainPage(webapp2.RequestHandler):
    def get(self):
#        guestbook_name=self.request.get('guestbook_name')
#        greetings_query = Greeting.all().ancestor(
#            guestbook_key(guestbook_name)).order('-date')
#        greetings = greetings_query.fetch(10)

        template_values = {
#            'greetings': greetings,
#            'url': url,
#            'url_linktext': url_linktext,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class GetData(webapp2.RequestHandler):
    def get(self):
        # Process data
        sex = self.request.get("sex")
        # Get postcode from data set
        json_response = ""
        for data in Data.datas:
            

            postcode = data["Postcode"]
            
            # You have post code now. 
            
            # TODO
            
            #...
            
            #Pretend that you have geo info back
            data['lat'] = 51.501009611553926 + float(data['KeyFundStage'])
            data['long'] = -0.141587067110009 + float(data['KeyFundStage'])
            #TODO send back JSON
        # convert postcode to geographical information
        
#        "GroupProjectID": "0001",
#        "GroupProjectMemberID": "10001",
#        "GROUPID": "200",
#        "KeyFundStage": "1",
#        "Gender": "Male",
#        "Postcode": "SO17 2HQ"
#        "lat": ""
#        "long" ""
        
        
        # Send response back to client
        self.response.write(json_response)
        
class Data:
    datas = [{
             "GroupProjectID": "0001",
             "GroupProjectMemberID": "10001",
             "GROUPID": "200",
             "KeyFundStage": "1",
             "Gender": "Male",
             "Postcode": "SO17 2HQ"
    }, {
        "GroupProjectID": "0002",
        "GroupProjectMemberID": "10001",
        "GROUPID": "201",
        "KeyFundStage": "3",
        "Gender": "Female",
        "Postcode": "SO17 2LB"
    }, {
        "GroupProjectID": "0003",
        "GroupProjectMemberID": "10001",
        "GROUPID": "202",
        "KeyFundStage": "4",
        "Gender": "Male",
        "Postcode": "SO15 2DB"
    }]
    
    
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/getData', GetData)],
                              debug=True)
