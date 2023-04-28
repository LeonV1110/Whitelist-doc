from flask import Flask, Response
app = Flask(__name__)
from whitelistDoc import  create_doc_string

@app.route('/')
def home():
    return "Hallo"
    #content = create_doc_string()
    #return Response(content, mimetype='text/plain')