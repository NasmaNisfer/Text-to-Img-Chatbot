#from chatbot import chatbot
from img2img import img2,img1
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/image', methods = ['GET','POST'])
def hello():
    hello.file = request.files['image']
    if hello.file.filename!="":
       hello.file.save("static/input/"+hello.file.filename)

    #print(type(hello.file))
    return '', 204

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
    if hello.file.filename=="":
       im = img1(userText)
    else:
       im = img2(userText,"static/input/"+hello.file.filename)
    return  '<img src='+im+'  width=150 style="border-radius: 10px;">'

if __name__ == "__main__":
    app.run()
