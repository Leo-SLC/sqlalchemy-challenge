# Import the dependencies.
from flask import Flask

import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()


# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return f'''
        <h1>Climate App</h1>
        <h4>Check out the following routes:</h4>
        <ul>
            <li>/api/v1.0/precipitation</li>
            <li>/api/v1.0/stations</li>
            <li>/api/v1.0/tobs</li>
            <li>/api/v1.0/[startDate]</li>
            <li>/api/v1.0/[startDate]/[endDate]</li>
        </ul>'''


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    return {date:prcp for date,prcp in session.query(measurement.date, measurement.prcp).filter(measurement.date>="2016-08-23").all()}

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    return {id:loc for id,loc in session.query(station.station, station.name).all()}

@app.route("/api/v1.0/tobs")
def tempsobs():
    session = Session(engine)
    return {date:tobs for date,tobs in session.query(measurement.date, measurement.tobs).filter(((measurement.date>="2016-08-23"))&(measurement.station == "USC00519281")).all()}

@app.route("/api/v1.0/<startDate>")
@app.route("/api/v1.0/<startDate>/<endDate>")
def startend(startDate, endDate="2017-08-23"):
    results = session.query(func.min(measurement.tobs), 
        func.avg(measurement.tobs), 
        func.max(measurement.tobs)).\
        filter((measurement.date>=startDate)&(measurement.date<=endDate)).first()

    print(results)



if __name__ == '__main__':
    app.run(debug=True)