from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# OS
import logging
import math
import os

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Deep Learning Framework
import tensorflow as tf

# Utils
from caption_generator import CaptionGenerator
from model import ShowAndTellModel
from vocabulary import Vocabulary

# Define a flask app
app = Flask(__name__)

# Feed params to model
model_path = "models/show-and-tell.pb"
vocab_file = "data/word_counts.txt"
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


# Loading Input Image
def _load_filenames(input_files):
    filenames = []
    for file_pattern in input_files.split(","):
        filenames.extend(tf.gfile.Glob(file_pattern))
    logger.info("Running caption generation on %d files matching %s",
                len(filenames), input_files)
    return filenames

# Loading Model, Vocubulary dict and a Input Image
model = ShowAndTellModel(model_path)
vocab = Vocabulary(vocab_file)
print('Model loaded. Check http://localhost:5000/')

# Inferencing Functions
def inference(model, vocab, filenames):
    generator = CaptionGenerator(model, vocab)
    sentences = []
    for filename in filenames:
        with tf.gfile.GFile(filename, "rb") as f:
            image = f.read()
        captions = generator.beam_search(image)
        print("Captions for image %s:" % os.path.basename(filename))
        for i, caption in enumerate(captions):
            # Ignore begin and end tokens <S> and </S>.
            sentence = [vocab.id_to_token(w) for w in caption.sentence[1:-1]]
            sentence = " ".join(sentence)
            sentences.append(" %d - %s (%f)" % (i, sentence, math.exp(caption.logprob)))
            print("  %d) %s (%f)" % (i, sentences[i], math.exp(caption.logprob)))

    return "<br>".join(sentences)


# Flask Route 
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def upload():

    global model, vocab

    if request.method == 'POST':
        # Get the file from post reqest
        f = request.files['file']

        # Save the file to ./Uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'image', secure_filename(f.filename))
        f.save(file_path)
        filenames = _load_filenames(file_path)

        print("basepath : %s" %basepath)
        print("file_path : %s" %file_path)
        print("secure_filename: %s" %secure_filename(f.filename))

        # Write 

        # Make predictions
        predictions = inference(model, vocab, filenames)
        print(jsonify({"predictions" : predictions}))
        return jsonify(predictions)
    return None

if __name__ == "__main__":

    #Serve the app with gevent
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
