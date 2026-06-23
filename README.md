# Data Redundancy Removal System

## Problem Statement
Cloud databases often store duplicate data, causing inefficiency and increased storage costs. This project prevents redundant data storage by validating new entries before insertion.

## Solution
The system checks each new data entry using SHA-256 hashing. If the hash already exists, the data is rejected. Only unique and verified data is stored.

## Features
- Duplicate data detection
- Hash-based validation
- Cloud-ready REST APIs
- Lightweight and scalable

## Technologies Used
- Python
- Flask
- SQLite
- SHA-256 Hashing

## How to Run
1. Install dependencies:
   pip install flask

2. Run the application:
   python app.py

3. Test using Postman or browser:
   - POST `/add-data`
   - GET `/view-data`

## Cloud Deployment
This application can be deployed on AWS EC2, Azure App Service, or Google Cloud Run.
