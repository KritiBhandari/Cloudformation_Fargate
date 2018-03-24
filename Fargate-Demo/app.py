from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome_page():
    #return 'Fargate Container running Python Flask'
     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
