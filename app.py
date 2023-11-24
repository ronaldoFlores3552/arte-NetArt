from flask import *
import json
from main import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:   
        image = request.files['image']
        temp = convert_image_to_ascii(image)
        aux = save_ascii_to_image(temp)
        to_json = json.dump({'img_toascii' : temp})
    return render_template('index.html', aux=aux)

if __name__ == '__main__':
    app.run(debug=True)