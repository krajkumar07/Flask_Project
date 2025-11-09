# Flask Contact List Application

A simple Flask web application that allows users to store and manage contact information using MongoDB Atlas as the database.

## Features

- Add new contacts with name and age
- Data validation for required fields
- MongoDB Atlas integration for data storage
- Flash messages for user feedback
- Simple and clean web interface

## Technologies Used

- Python 3.x
- Flask
- MongoDB Atlas
- HTML
- dotenv for environment variables

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/krajkumar07/Flask_Project.git
cd Flask_project
```

2. Install required packages:
```bash
pip install flask pymongo python-dotenv
```

3. Create a `.env` file in the project root and add your MongoDB URI and secret key:
```
MONGO_URI=your_mongodb_uri
SECRET_KEY=your_secret_key
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
Flask_project/
├── app.py           # Main application file
├── templates/       # HTML templates
│   └── index.html  # Main page template
└── .env            # Environment variables
```

## Contributing

Feel free to submit issues and pull requests.

## License

This project is open source and available under the [MIT License](LICENSE).