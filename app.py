from flask import Flask, render_template, request, send_file
from pypdf import PdfMerger

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/merge', methods=["POST"])
def merge():
    if request.method == 'POST':
        files = request.files.getlist("file")
        merger = PdfMerger()

        for pdf in files:
            merger.append(pdf)

        merger.write("result.pdf")
        merger.close()
    return send_file("result.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)