from flask import Flask, Response
from whitelistDoc import  create_doc_string


app = Flask(__name__)

@app.route("/")
def showWhitelistDoc():
    content = create_doc_string()
    return Response(content, mimetype='text/plain')