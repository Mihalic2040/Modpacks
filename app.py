from flask import Flask, render_template, Blueprint, jsonify, request
import os
from werkzeug.utils import secure_filename

from src.jsonparser import parse
from src.modpackdata import get_modpack_data

app = Flask(__name__, template_folder='src/templates', static_folder='src/public')


modpacks_static = Blueprint('modpacks_static', __name__, static_folder='./modpacks', static_url_path='/modpacks/static')
app.register_blueprint(modpacks_static)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/modpacks')
def modpacks():
    
    return render_template('modpacks.html', modpacks=parse())

@app.route('/modpacks/list')
def modpacks_list():
    return parse()

@app.route('/modpacks/<name>')
def modpack_page(name):
    # Load modpack data based on the name parameter

    modpack_data = get_modpack_data(name=name)
    # Render the modpack template with the modpack data
    if modpack_data == None:
        return "Modpack not exist"
    return render_template('modpack.html', modpack_data=modpack_data)

@app.route('/upload')
def upload():
    return render_template('upload.html')



if __name__ == '__main__':
    app.run(debug=True)
