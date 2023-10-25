import firebase_admin
from firebase_admin import credentials
from configs.firebase_config import firebaseConfig
import pyrebase

if not firebase_admin._apps:
    cred = credentials.Certificate("configs/masterchief-recipe-api-firebase-adminsdk-kl4dr-94934182e6.json")
    firebase_admin.initialize_app(cred)
    
#cred = credentials.Certificate("path/to/serviceAccountKey.json")
#firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
authRecipe = firebase.auth()