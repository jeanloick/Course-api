import json
import firebase_admin
from firebase_admin import credentials
import pyrebase 

from dotenv import dotenv_values

config = dotenv_values('.env')

# Initialize Firebase Admin with the service account information
cred = credentials.Certificate(json.loads(config['FIREBASE_SERVICE_ACCOUNT_KEY']))
firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(json.loads(config['FIREBASE_CONFIG']))
db = firebase.database()
authRecipe = firebase.auth()