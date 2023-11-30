from flask import *
import json
from to_ascii import *
from main import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:        
        image = request.files['image']
        temp = convert_image_to_ascii(image) ## temp es la lista donde cada valor es una linea 
        #print(temp)
        return jsonify({'ascii_lines': temp})


if __name__ == '__main__':
    app.run(debug=True)