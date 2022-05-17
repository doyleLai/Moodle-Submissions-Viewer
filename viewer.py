from ast import arg
from multiprocessing.spawn import _main
from pydoc import render_doc
import sys
import flask
import json
from flask import send_from_directory
from flask import jsonify, request, render_template
import string
from os import listdir
from os.path import isfile, join, isdir, exists

def main(folder_path:str, port:int):
    binding_data = {
        "path": folder_path,
        "entries": []
    }

    dirs = [f for f in listdir(folder_path) if isdir(join(folder_path, f))]
    for dir in dirs:
        binding_data["entries"].append(
            {
                "std_name": dir.split("_")[0],
                "dir": dir
            }
        )

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def index():
            return render_template("index.html", data = binding_data)

    @app.route('/view/<path:path>')
    def view(path):
        return render_template("view.html", data = path)

    @app.route('/submission/<path:path>')
    def send_report(path):
        if exists(f'{folder_path}/{path}/onlinetext.html'):
            # if onlinetext.html exists
            return send_from_directory(folder_path,f'{path}/onlinetext.html')
        else:
            # else, list files in the folder
            filenames = listdir(f'{folder_path}/{path}')
            return render_template("files.html", data = {"filenames":filenames, "path":path} )

    @app.route('/file/<path:path>')
    def file(path):
        if exists(f'{folder_path}/{path}'):
            return send_from_directory(folder_path,f'{path}')
        else:
            return None

    app.run(port = port)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        print(f'{sys.argv[0]}: Path of the submissions folder and port number should be given.')
        print(f'Suggested port number >=5000')
