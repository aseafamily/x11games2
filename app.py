from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def read_index():
    html_content = ""
    # Check if index.html exists in the current directory
    if os.path.exists("index.html"):
        with open("index.html", "r") as f:
            html_content = f.read()
    else:
        # Fallback content if index.html is not found
        html_content = "<html><body><h1>index.html not found</h1></body></html>"
    return html_content

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 