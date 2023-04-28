from flask import Flask, Response
app = Flask(__name__)
from whitelistDoc import  create_doc_string

@app.route('/')
def home():
    
    try: 
        content = create_doc_string()
    except Exception:
        return "There has been an error, go bother Leon"
    return Response(content, mimetype='text/plain')