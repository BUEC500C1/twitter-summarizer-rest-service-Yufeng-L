from flask import Flask, render_template, request, send_file
from flask_restful import reqparse, Api, Resource
import os
import tweets2image
import image2video
import queue_Sys
import zipfile

app = Flask(__name__)

@app.route('/') #creates the flask html route
def root():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    user1 = request.form['user1']  # getting usernames
    # user2 = request.form['user2']
    # user3 = request.form['user3']
 
    tweet_keyword = []
    if user1 != "":
        tweet_keyword.append(user1)
    # if user2 != "":
    #     tweet_keyword.append(user2)
    # if user3 != "":
    #     tweet_keyword.append(user3)

    queue_Sys.handler(tweet_keyword,3)
    
    zipFolder = zipfile.ZipFile('videos.zip', 'w', zipfile.ZIP_DEFLATED)
    for item in tweet_keyword : 
        name = item + '.avi'
        zipFolder.write(name)

    zipFolder.close()
    return send_file('videos.zip', mimetype='zip',attachment_filename='videos.zip',as_attachment=True)

if __name__ == '__main__':
	app.run(host = '127.0.0.0',port=80,debug=True)
