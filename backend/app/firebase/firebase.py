from firebase_admin import credentials, firestore
import firebase_admin

cred = credentials.Certificate('mercury-2ed09-firebase-adminsdk-qktzh-9d56af016f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

