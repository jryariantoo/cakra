import os
from flask import Flask, request, render_template, redirect, url_for
import requests
import PyPDF2

app = Flask(__name__)
UPLOAD_FOLDER = 'Documents'
API_KEY = '9eb9f656-d9e1-4aa9-9cf5-5b83b758df3c'
API_URL = 'https://saas.cakra.ai/genv2/llms'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_document(filepath):
    with open(filepath, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        content = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            content += page.extract_text()
    return content

def generate_questions(document_content):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        "model_name": "brain-v2",
        "messages": [
            {
                "role": "system",
                "content": "Your Chatbot AI Assistant"
            },
            {
                "role": "user",
                "content": f"Bayangkan Anda seorang guru, dan harus memberikan 5 pertanyaan berbentuk pilihan ganda untuk diberikan kepada siswa Anda. Pertanyaan-pertanyaan tersebut berdasarkan {document_content}, jadi Anda harus membaca dokumen tersebut sebelum membuat pertanyaan. Setiap pertanyaan memiliki 4 pilihan ganda, yang terdiri dari 3 pilihan salah dan 1 pilihan benar. Selalu tunjukkan pilihan yang benar, gunakan bahasa Indonesia, dan hanya buat 5 pertanyaan."
            }
        ],
        "max_new_tokens": 1250,  
        "do_sample": False,
        "temperature": 0.7,
        "top_k": 50,
        "top_p": 1.0
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data and len(response_data['choices']) > 0:
            return response_data['choices'][0]['content']
        else:
            print("No choices found in the response.")
            return None
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            content = extract_document(filepath)
            questions = generate_questions(content)
            return render_template('index.html', questions=questions)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
