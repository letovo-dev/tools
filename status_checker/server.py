from flask import Flask, jsonify, render_template_string
from logger import get_logger
from check_list import check_list
        
with open("./page.html") as file:
    html_page = file.read()
 
app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template_string(html_page)

@app.route("/data", methods=['GET'])
def return_status():
    return_dict = {}
    for name in check_list:
        check_list[name].check()
        return_dict[name] = check_list[name].state
        
    return jsonify(return_dict)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)