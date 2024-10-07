# Imports
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    # Performs emotion detection over Flask channel

    # Retrieve the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass text to the emotion_detector function and get required format
    result = emotion_detector(text_to_analyze)

    if result['anger'] is None:
        return "Invalid text! Please try again!"
    else:
        dominant_emotion = result['dominant_emotion']
        del result['dominant_emotion']

        return f"For the given statement, the system response is {result}.\
        The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
