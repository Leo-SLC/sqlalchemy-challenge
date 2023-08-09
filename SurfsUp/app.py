# Import the dependencies.
from flask import Flask


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return '<h1>Hello world!!!</h1>'

if __name__ == '__main__':
    app.run(debug=True)