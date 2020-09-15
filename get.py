import firebase_admin
import google
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./CredentialFirebase.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'aulaFirestore').document(u'aulaDocument')

try:
    doc = doc_ref.get()
    print(f'Document Data: {doc.to_dict()}')
except google.cloud.exceptions.NotFound:
    print(u'No such data found')