from flask import Flask,render_template,request,redirect,url_for
from processor import GenerateDescription

app = Flask(__name__)

generator = GenerateDescription()

@app.route("/")

def home():
    return render_template("index.html")
    
@app.route("/predict", methods=['POST','GET'])
def predict():
    if request.method == "POST":
        try:
            image = request.files.get("file")
            caption = generator.generate(image)
            caption = caption.strip("start")
            caption = caption.strip("end")
            caption = caption.strip()
            caption = caption.capitalize()
            caption += "."

        except:
            return "Something Unexpected Happened.. Try again!"
        
        return caption
        
    else:
        return render_template('index.html')
        
@app.errorhandler(404)
def error(e):
    return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)