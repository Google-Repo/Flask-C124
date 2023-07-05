from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
    "data":[
        {
            "contact": "9987644456",
            "Name":"Raju",
            "done":False,
            "id":1
        },
        {
            "contact": "9876543222",
            "Name": "Rahul",
            "done":False,
            "id":2
        }
    ]
}]

@app.route("/")

def hey_buddy():
    return "Hey buddy!"

@app.route("/add-data", methods=["POST"])

def add_contacts():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
        
    contact = {
        'id':contacts[-1]['id']+1, 
        'title':request.json.get('description',""),
        'done':False    
    }
    
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added successfully!"
    })
    
@app.route("/get-data")

def get_contact():
    return jsonify({
        "data":contacts
    })
       
if __name__ == "__main__":
    app.run(debug=True)
    