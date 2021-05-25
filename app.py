# Fill out missing requirements
from helpers import load_from_gcs
from reco import reco_v2
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
reco_data = load_from_gcs('hiphopclass','data/reco_data.csv','reco_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/recommend',methods=['GET'])
def api_predict():
    track_id = request.args.get("track_id")
    try:
    	popularity_threshold = float(request.args.get("popularity_threshold"))
    except TypeError:
    	popularity_threshold = 1
    try:
    	playlist_len = int(request.args.get("playlist_len"))
    except TypeError:
    	playlist_len = 10

    output = reco_v2(input_track_id=track_id, reco_dat=reco_data, popularity_threshold=popularity_threshold, playlist_len=playlist_len)

    return jsonify(output.to_dict('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)