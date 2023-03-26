from flask import Flask, render_template, request
import openai
import os
import requests

app = Flask(__name__)

#import library
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


#Home Page
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')


@app.route('/lang_selection', methods=['POST'])
def lang_selection():
    print("hello")
    if request.method == 'POST':
        #text = request.form['comp_select']
        #print(text)
        #print("=================================")
        select = request.form.get('comp_select')
        lang = str(select)
        print("=================================")
        #return(lang) # just to see what select is
        return render_template('record.html', lang=lang)

@app.route('/speech_to_text/<lang>', methods=['POST'])
def speech_to_text(lang):
    print(lang)
    print("testing======================")
    with sr.Microphone() as source:
        print('Say Something for 6 seconds')
        audio_text = r.listen(source,timeout=6)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            #au = r.adjust_for_ambient_noise(audio_text, duration = 1)
            #print(audio_text)
            text = r.recognize_google(audio_text, language = lang)
            print(text)
            
            # Set up API endpoint and API key
            api_url = 'https://api.openai.com/v1/images/generations'
            api_key = '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'

            # Set up request parameters
            prompt = text
            model = 'image-alpha-001'
            num_images = 1
            size = '512x512'
            response_format = 'url'

            # Set up request headers
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            }

            # Set up request body
            data = {
                'model': model,
                'prompt': prompt,
                'num_images': num_images,
                'size': size,
                'response_format': response_format
            }

            # Make the request
            response = requests.post(api_url, headers=headers, json=data)

            # Parse the response
            if response.status_code == 200:
                result = response.json()['data'][0]['url']
                print(f'Generated image: {result}')
            else:
                print(f'Request failed with status code {response.status_code}: {response.text}')   
    
        except:
            print('Sorry.. run again...')
            test = "Try Again"
    
    return render_template('image.html', text=text, result=result)



@app.route('/text_to_img/<text>', methods=['GET', 'POST'])
def text_to_img(text):
    images = []
    text_new = text
    #text = "A 3D representation of a blue tennis ball on a green grass"
    res = create_img_from_text(text_new)
    if len(res) > 0:
        for img in res:
            images.append(img['url'])
    print(images)
    print("=======================================")
    
    return render_template('home.html')

if __name__ == "__main__":
    app.secret_key='12345'
    app.run(host='0.0.0.0', port=5000, debug=True) 