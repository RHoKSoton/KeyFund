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

        if (sex == "both"):
            self.response.write(Data.datas)
        elif (sex == "male"):
            self.response.write("[")
            male_count = 0
            for data in Data.datas:
                
                if (data["Gender"] == "0"):
                    if (male_count != 0):
                        self.response.write(",")
                    self.response.write(data)
                    male_count = male_count + 1
            self.response.write("]")
        elif (sex == "female"):
            self.response.write("[")
            female_count = 0
            for data in Data.datas:
                
                if (data["Gender"] == "1"):
                    if (female_count != 0):
                        self.response.write(",")
                    self.response.write(data)
                    female_count = female_count + 1
            self.response.write("]")
       
            
            # You have post code now. 
            
            # TODO
            
            #...
            
            #Pretend that you have geo info back
            
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
        
class Data:
    datas = [{
             "GroupProjectID": "0001",
             "GroupProjectMemberID": "10001",
             "GROUPID": "200",
             "KeyFundStage": "1",
             "Gender": "1",
             "Postcode": "SO17 2HQ",
             "lat" : "51.9241468414",
             "long" : "-1939086340051"
    }, {
        "GroupProjectID": "0002",
        "GroupProjectMemberID": "10001",
        "GROUPID": "201",
        "KeyFundStage": "3",
        "Gender": "0",
        "Postcode": "SO17 2LB",
        "lat" : "50.9241468414",
        "long" : "-1.39086340051"
    }, {
        "GroupProjectID": "0003",
        "GroupProjectMemberID": "10001",
        "GROUPID": "202",
        "KeyFundStage": "4",
        "Gender": "1",
        "Postcode": "SO15 2DB",
        "lat" : "49.9241468414",
        "long" : "-0.39086340051"
    }]
    
    
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/getData', GetData)],
                              debug=True)
