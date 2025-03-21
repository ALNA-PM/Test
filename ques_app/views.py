from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

# Establish a MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI
db = client['Question_page']  # Connect to the 'Question_page' database
collection = db['Ques']  # Access the 'Ques' collection

# Dashboard view
def dashboard(request):
    user_data = {'name': 'John Doe', 'role': 'Admin'}  # Example data, you can fetch from the DB
    return render(request, 'dashboard.html', context=user_data)

# Profile view
def profile(request):
    user = request.user  # Get the currently logged-in user
    # Fetch additional user-specific data from the database, if necessary
    return render(request, 'profile.html', {'user': user})

# Report view
def report(request):
    # Fetch reports (if you have a reports collection in your MongoDB or a different model)
    reports = []  # Example, you can query MongoDB for reports if needed
    return render(request, 'report.html', {'reports': reports})

# Questions view
def questions(request):
    # Fetch the first document from the collection (you can adjust this as per your requirements)
    question_document = collection.find_one()  # Assuming you are fetching the first document in the collection

    if question_document:
        # Extract the 'quiz' array which contains all the questions
        questions_data = question_document.get('quiz', [])
    else:
        questions_data = []

    # Pass the fetched questions data to the template
    return render(request, 'questions.html', {'questions': questions_data})