from flask import Blueprint, request, jsonify, Flask
from werkzeug.exceptions import BadRequest, NotFound

#Create a Blueprint for laptops
laptops_blueprint = Blueprint('laptops', __name__)

#simulating a database
laptops_db = {}

#Checking if a laptop already exists by laptop_number
def laptop_exists(laptop_number):
    return laptop_number in laptops_db

#Add a Laptop
@laptops_blueprint.route('/laptops/add', methods=['POST'])
def add_laptop():
    try:
        # Parse input JSON data
        data = request.get_json()
        name = data.get('name')
        laptop_number = data.get('laptop_number')
        specifications = data.get('specifications')

        #Check for missing fields
        if not name or not laptop_number or not specifications:
            raise BadRequest("Missing required fields: 'name', 'laptop_number', or 'specifications'.")

        #Check if laptop number is unique
        if laptop_exists(laptop_number):
            raise BadRequest(f"Laptop with laptop_number {laptop_number} already exists.")

        #Add laptop to database
        laptops_db[laptop_number] = {'name': name, 'laptop_number': laptop_number, 'specifications': specifications}
        
        return jsonify({"message": "Laptop added successfully."}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400


#Get All Laptops
@laptops_blueprint.route('/laptops', methods=['GET'])
def get_all_laptops():
    return jsonify(list(laptops_db.values())), 200


#Get a Laptop by Name
@laptops_blueprint.route('/laptops/name/<name>', methods=['GET'])
def get_laptop_by_name(name):
    laptop = next((l for l in laptops_db.values() if l['name'] == name), None)
    
    if laptop:
        return jsonify(laptop), 200
    else:
        raise NotFound(f"Laptop with name '{name}' not found.")


#Get a Laptop by Laptop Number
@laptops_blueprint.route('/laptops/number/<laptop_number>', methods=['GET'])
def get_laptop_by_number(laptop_number):
    laptop = laptops_db.get(laptop_number)

    if laptop:
        return jsonify(laptop), 200
    else:
        raise NotFound(f"Laptop with laptop_number {laptop_number} not found.")


#Update a Laptop by Laptop Number
@laptops_blueprint.route('/laptops/update/<laptop_number>', methods=['PUT'])
def update_laptop(laptop_number):
    if laptop_number not in laptops_db:
        raise NotFound(f"Laptop with laptop_number {laptop_number} not found.")
    
    try:
        #Input JSON data for updates
        data = request.get_json()
        name = data.get('name')
        specifications = data.get('specifications')

        if not name and not specifications:
            raise BadRequest("At least one of 'name' or 'specifications' must be provided.")

        #Update laptop details
        laptop = laptops_db[laptop_number]
        if name:
            laptop['name'] = name
        if specifications:
            laptop['specifications'] = specifications

        return jsonify({"message": "Laptop updated successfully."}), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400


#Delete a Laptop by Laptop Number
@laptops_blueprint.route('/laptops/delete/<laptop_number>', methods=['DELETE'])
def delete_laptop(laptop_number):
    if laptop_number not in laptops_db:
        raise NotFound(f"Laptop with laptop_number {laptop_number} not found.")
    
    #Delete laptop
    del laptops_db[laptop_number]
    return jsonify({"message": "Laptop deleted successfully."}), 200


app = Flask(__name__)

#Register the blueprint
app.register_blueprint(laptops_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
