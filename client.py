from flask import Flask, jsonify, request
import main

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    image=request.json['sound']
    main.decode_audio(image,'demo.wav')
    text=main.sp_to_txt('demo.wav')
    return jsonify(text)

if __name__=='__main__':
    app.run()
