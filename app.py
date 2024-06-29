from flask import Flask, request, render_template
from downloader import handle_link

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    quality = request.form['quality']
    result = handle_link(url, quality)
    return result

if __name__ == "__main__":
    app.run(debug=True)
