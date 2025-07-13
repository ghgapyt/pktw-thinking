
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <html>
        <head><title>PKTW THINKING 🤔</title></head>
        <body style="font-family:sans-serif;padding:40px;">
            <h1>Welcome to PKTW THINKING 🤔</h1>
            <p>This is your AI-powered multi-tab assistant powered by Flask.</p>
        </body>
        </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
