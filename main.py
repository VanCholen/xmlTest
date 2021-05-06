from flask import Flask, render_template

app=Flask(__name__)
 
@app.route('/')
def hello_flask():
    return render_template('/views/index.html')
 
if __name__=='__main__':
    app.debug=True
    app.run(host='127.0.0.1',port=5000)