#pip instal flask

from flask import Flask, jsonify, request, make_response 

app = Flask(__name__)

business = [
{   "id":1,
    "name":"Nepal house",
    "town":"london",
    "rating": "5",
    "review":[]
},
{    

    "id":2,
    "name":"Nepal Ghar",
    "town":"london",
    "rating": "5",
    "review":[]
},
{
    "id":3,
    "name":"Nepal Villa",
    "town":"london",
    "rating": "5",
    "review":[]
  
}]

@app.route('/',methods=['GET'])
def home():
    return jsonify({"message":"welcome to COM661"})


@app.route('/business', methods=['GET'])
def get_all_business():
    return make_response(jsonify({"Business":business }), 200)

@app.route('/business', methods=['POST'])
def add_business():
    data = request.get_json
    id = business[-1]["id"] = 1
    new_business = {
        "id":id,
        "name": data["name"],
        "town": data["town"],
        "rating": data.get("rating", 0), 
        "review":[]

    }
    businesses.append(new_business)
    return make_response(jsonify(new_business), 201)

if __name__=='__main__':
   app.run(debug=True)

#python app.py   

