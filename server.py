from flask import Flask, request
from werkzeug.utils import secure_filename
import os, uuid


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'


@app.route('/', methods=['GET', 'POST', 'PUT'])
def listener():
    data = request.get_data()
    files = request.files

    if data:
        handle = open(os.path.join(app.config['UPLOAD_FOLDER']) + '/' + "output_" + uuid.uuid4().hex, 'wb')
        handle.write(data)
        handle.close()

    try:
        for file in files:
            file = request.files[file]
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "file_" + uuid.uuid4().hex + '_' + filename))
    except:
        pass

    return "lucky624"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
