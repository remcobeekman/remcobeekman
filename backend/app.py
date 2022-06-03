
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://remcopi:janenanita@localhost/flask'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
#ma = Marshmallow(app)

#class Data(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(100))

#    def __init__(self, title):
#        self.title = title

#class DataSchema(ma.Schema):
#    class Meta:
#        fields = ('id','title')

#data_schema = DataSchema()
#data_schemas = DataSchema(many=True)

@app.route('/get', methods = ['GET'])
def get_data():
    #all_data = Data.query.all()
    #results = data_schemas.dump(all_data)
    #return jsonify(results)
    return jsonify({"hallo domme kutsite"})

#@app.route('/add', methods = ['POST'])
#def add_data():
#   title = request.json['title']

#   datas = Data(title)
#   db.session.add(datas)
#   db.session.commit()
3   #return data_schema.jsonify(datas)

if __name__ == "__main__":
    app.run(debug=False)