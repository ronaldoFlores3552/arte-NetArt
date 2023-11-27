from flask import *
import json
from main import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:   
        print('post')
        
        image = request.files['image']
        temp = convert_image_to_ascii(image)
        save_ascii_to_image(temp)
        to_img = url_for('static', filename='ascii_art2.png')
        print(to_img)
        return render_template('index.html', to_img=to_img)

if __name__ == '__main__':
    app.run(debug=True)