from flask import Flask, render_template, request
import modelt
import json 

app = Flask(__name__)

@app.route('/')
def root_page():
    return render_template('sample.html')

# pickle 파일 실행
@app.route('/run_model')
def run_model():
    #res_data = request.get_json()
    patient = request.args.get('patient')

    if patient is None or patient == "":
        patient = [[2,180,74,24,21,23.9091702,1.488172308,22]]
    else :
        patient = eval(patient)

    print('Patient Arg:0 {}'.format(patient))
    result = modelt.model_predict(patient)

    return json.dumps(result)    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
