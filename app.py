from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['flask_db']
collection = db['user_data']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not name or not age:
            flash('Name and Age are required fields.', 'error')
            return render_template('index.html')  
        try:
            age_int = int(age)
            collection.insert_one({'name': name, 'age': age_int})
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')
            return render_template('index.html')  
    return render_template('index.html')  

@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)
