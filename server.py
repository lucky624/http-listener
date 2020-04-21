from flask import Flask, request
from werkzeug.utils import secure_filename
import os, uuid


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data'


@app.route('/', methods=['GET', 'POST', 'PUT'])
def listener():
    data = request.get_data()
    files = request.files

    check_file = False

    try:
        for file in files:
            check_file = True
            file = request.files[file]
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "file_" + uuid.uuid4().hex + '_' + filename))
    except:
        pass

    if data and check_file == False:
        handle = open(os.path.join(app.config['UPLOAD_FOLDER']) + '/' + "output_" + uuid.uuid4().hex, 'wb')
        handle.write(data)
        handle.close()


    return "lucky624"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
