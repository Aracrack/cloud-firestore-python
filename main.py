import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./CredentialFirebase.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

def getData():
    f = open('data.json')
    data = json.load(f)
    return data

response = getData()
nome = response['nome']
faculdade = response['faculdade']
curso = response['curso']
ano = response['ano']

doc_ref = db.collection(u'aulaFirestore').document(u'aulaDocument')
doc_ref.set({
    u'name': nome,
    u'university': faculdade,
    u'course': curso,
    u'year': ano,
})

