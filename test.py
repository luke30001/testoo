from flask import Flask
  
app = Flask(__name__)
  
  
@app.route('/')
def home():
    return "Welcome to GeeksForGeeks !"
  
  
if __name__ == "__main__":
    website_url = 'testoo.onrender.com'
    app.config['SERVER_NAME'] = website_url
    app.run()
