from app import app
#from app.whitelistDoc import  create_doc_string
from flask import Response

@app.route('/')
def home():
    #content = create_doc_string()
    return "Hello world"
    #return Response(content, mimetype='text/plain')