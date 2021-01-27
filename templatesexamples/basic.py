from flask import Flask, render_template
#from flask.ext.images import resized_img_src

app = Flask(__name__)

@app.route('/')
def index():
    #the code looks for a templates folder in the directory
    #it looks for the exact file name to render the template/html.
    return render_template('index.html')
if __name__ == '__main__':
    app.run()

