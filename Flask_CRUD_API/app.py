from flask import Flask
from laptops_blueprint import laptops_blueprint

# Initialize the Flask application
app = Flask(__name__)

# Register the laptops blueprint with the base URL '/laptops'
app.register_blueprint(laptops_blueprint, url_prefix='/laptops')

# Run the application on localhost:5000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
