from flask import Flask, Response
app = Flask(__name__)
#from app.whitelistDoc import  create_doc_string

@app.route('/')
def home():
    #content = create_doc_string()
    return "Hello world"
    #return Response(content, mimetype='text/plain')