from flask import Flask, render_template, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=""
predicted_emotion_img_url=""

@app.route("/")
def home():
    entries = show_entry()
    return render_template("index.html", entries=entries)
    

@app.route("/predict-emotion", methods=["POST"])
def predict_emotion():
    input_text = request.json.get("text")
    if not input_text:
        return jsonify({
            "status": "error",
            "message": "Please enter some text to predict emotion!"
        }), 400
    else:
        predicted_emotion, predicted_emotion_img_url = predict(input_text)                         
        return jsonify({
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emotion_img_url": predicted_emotion_img_url
            },
            "status": "success"
        }), 200
            
#Write the code for API here
@app.route('/save' , methods = ['POST'])
def save():
    date=request.json.get("date")
    product=request.json("product")
    review=request.json.get("rewiew")
    sentiment=request.json.get("sentiment")
   
     # creating a final variable seperated by commas
    data_entry = date + "," + product + "," + review + "," + sentiment

    # open the file in the 'append' mode
    f = open('./static/assets/datafiles/data_entry.csv' , 'a')

    # Log the data in the file
    f.write(data_entry + '\n')

    # return a success message
    return jsonify({'status' : 'success' , 
                    'message' : 'Data Logged'})
                
if __name__ == "__main__":
    app.run(debug=True)

