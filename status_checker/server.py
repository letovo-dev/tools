from flask import Flask, jsonify, render_template_string, render_template
from logger import get_logger
from check_list import check_list
import os
        
current_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        
# with open(os.path.join(current_file_path, "page.html")) as file:
#     html_page = file.read()
 
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('page.html')

@app.route("/data", methods=['GET'])
def return_status():
    return_dict = {}
    for name in check_list:
        check_list[name].check()
        return_dict[name] = check_list[name].state
        
    return jsonify(return_dict)

@app.route("/logs", methods=['GET'])
def return_logs():
    try:
        latest_log_file = max([os.path.join(current_file_path, "logs", f) for f in os.listdir(os.path.join(current_file_path, "logs"))], key=os.path.getctime)
    except ValueError:
        return render_template('logs.html', logs=[{'text': 'No logs yet', 'level': 'info'}])
    logs = []
    with open(latest_log_file, 'r') as file:
        for line in file:
            if "ERROR" in line:
                logs.append({'text': line, 'level': 'error'})
            elif "WARNING" in line:
                logs.append({'text': line, 'level': 'warning'})
            else:
                logs.append({'text': line, 'level': 'info'})
    return render_template('logs.html', logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)