# from flask import Flask , render_template, request
# app = Flask(__name__)

# decorator
# @app.route('/')
# def home():
#     return render_template('home.html')
# @app.route('/about')
# def about():
#     return render_template('about.html')


# @app.route('/profile/<string: name>')
# def profile(name):
#     return "hello" + str(name)


# @app.route('/profile/<int:id>')
# def profile2(id):
#     return " i m siddhi" + str(id)


# client  data bhejta hai usko post request khte hai

# @app.route('/postdata', methods=['POST'])
# def submit():
#     if request.method == "POST":
#       fn =   request.form["firstname"]
#       ln =   request.form["lastname"]
#       print(fn , ln)
#       return "submitted successfully"
#     else:
#         return "something went wrong"

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, Response
# import cv2
# app=Flask(__name__)
# camera= cv2.VideoCapture(0)


# def generate_frame():
#      while True:
#     #      read the camera frame
#       success, frame= camera.read()
#       if not success:
#           break
#       else:
#          ret, buffer= cv2.imencode('.jpg' , frame)
#          frame=buffer.tobytes()

#       yield(b'--frame\r\n'
#             b'content-type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/video',)
# def video():
#     return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')
# if __name__ == "__main__":
#     app.run(debug=False)


from flask import Flask, jsonify, Response, request
from flask_cors import CORS, cross_origin
# from docx import document


from flask import send_file, render_template
import cv2
import base64
app = Flask(__name__)
cors = CORS(app)


products = [
    {
        'name': "siddhi",
        'id': 3,
        'company': "cdac"
    },
    {
        'name': "riddhi",
        'id': 4,
        'company': "cdac-fullstack"
    }]


@app.route('/product')
def get_products():
    return {"products": products}


@app.route('/read_file', methods=['POST'])
def read_file():
    file = request.files['siddhi']
    if file:
        # save the file to a folder
        file.save(file.filename)
        # read the content of the file
        with open(file.filename, 'r') as f:
            content = f.read()
        return jsonify({'message': content})
    else:
        return 'No file uploaded.'


@app.route('/')
def home():
    return render_template('index.html')
    # return '<h1>welcome to flask</h1>'


@app.route('/spaces')
def spaces():
    return render_template('spaces.html')


@app.route('/audio')
def audio():
    return render_template('audio.html')



@app.route('/text')
def text():
    return render_template('text.html')


@app.route('/trans')
def t():
    return render_template('transliteration.html')


@app.route('/ocr')
def ocr_content():
	return render_template('ocr.html')

# @app.route('/convertaudio' , methods=['POST'])
# def audio_convert():
   
@app.route('/MT')
def machine_translation():
	return render_template('MT.html')

@app.route('/s2s')
def speechtotext():
    return render_template('s2s.html')


@app.route('/allproducts', methods=['get'])
@cross_origin()
def getAllProducts():
    return jsonify({"products": products})


@app.route('/reverse', methods=['POST'])
def reverse():
    input_string =request.get_json()
    data = input_string['input_string']
    reversed_string = data[::-1]
    return jsonify({'message':reversed_string})



@app.route('/getImage', methods=['get'])
def getImages():
    img = cv2.imread('bradley.jpg')
    jpg_img = cv2.imencode('.jpg', img)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    data = {"Image": b64_string}
    return jsonify(data)
    # return send_file('bradley.jpg', mimetype='image/jpeg',
    # as_attachment=True)


@app.route('/products', methods=['POST'])
def getProducts():
    jsonData = request.get_json()
    name = jsonData["data1"]
    for product in products:
        if name in product:
            # if products['name']==name:
            return jsonify(product)
        

    return jsonify({'Error': 'Products{} not found'.format(name)})


@app.route('/upload')
def upload_form():
	return render_template('download.html')



@app.route('/download')
def download_file():
	path = "simple.docx"
	return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
