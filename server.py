''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detection()
        function. The output returned shows the emotion with its confidence 
        score in addition to the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        text_to_be_displayed = "Invalid text! Please try again!"

    else:
        text_to_be_displayed = "For this statement, the response is "
        text_to_be_displayed += "\'anger\': " + str(anger_score) + ", "
        text_to_be_displayed += "\'disgust\': " + str(disgust_score) + ", "
        text_to_be_displayed += "\'fear\': " + str(fear_score) + ", "
        text_to_be_displayed += "\'joy\': " + str(joy_score) + " and "
        text_to_be_displayed += "\'sadness\': " + str(sadness_score) + ". "
        text_to_be_displayed += "The dominant emotion is " + dominant_emotion + "."
    return text_to_be_displayed
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
