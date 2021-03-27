from flask import  Flask,jsonify,request

app = Flask(__name__)
@app.route('/')
def stanford_page():
    return("""<h1>Hello stanford!</h1>""" ),200

if __name__ == "__main__":
    app.run()