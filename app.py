######Note the Kevin and Brian ######
#I wasn't able to finish the assaignment, spent about 3.5 hours trying to figure it out,b ut got stuck adn wanted to spend the time working on my project. My plan was to import the csv using pandas into a pd.DataFrame, which I did succeed at. This allowed me to look at the data and the dtypes which helped me construct my model. The model only has three attributes, Startime Endtime and Duration, because I think that's all I needed for the analysis. I created an empty database in ElephantSQL and my plan was to use the model to import the file into the database, but that's the point I got stuck.  I thought probably I was supposed to iterate thru each record in the pd.DataFrame and add it to the model, using Flask Shell.  But, I can't get Flask shell to run. Flask will run, but not Flask Shell. Keep getting "Error: Could not import "app". I googled error and it said to make sure to set FLASK_APP=myappname, which I did. I googled for a while, tried to make sure I had all the elements I need in my flask app, but apparently I'm missing something or did something wrong.   *\_O_/*     <---that's me throwing my hands in the air, although it kind of looks like i'm throwing explosives, which would be an overstatment of my frustrations with the project. Now i'm gonna go work on my website some more. See you Friday morning! Thanks for ten weeks of fun times! I can't believe its almost over!  Despite all the things I still can't do and things I still don't know, I did learn a TON in this course, and I hope to just never stop learning!"
#
################################################


from flask import Flask, jsonify, request
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

FLASK_APP='/app.py'

# initialize  Flask application
app= Flask(__name__)

if __name__ == '__main__':
  app.run

#read csv
x = 'DivvyChallenge.csv'
def get_data(x):
    d = pd.read_csv(x)
    print(type(d))
    print(d.dtypes)
    return d

get_data(x)

#define Db
db = SQLAlchemy()


#model
class Divvy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.String(20))
    stoptime = db.Column(db.String(20))
    trip_duration = db.Column(db.Integer)

   
    def __init__(self, starttime, stoptime, trip_duration):
        self.starttime = starttime
        self.stoptime = stoptime
        self.trip_duration= trip_duration
        db.session.add(self)
        db.session.commit()


#db info
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 


#route
@app.route("/divvy<starttime><endtime>", methods=["POST"])
def search_divvy():
    if request.method=='POST':
        result = Divvy.query.all()
        return jsonify(result.to_dict())
        




@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Divvy': Divvy}