import json
import joblib
import numpy as np
#from azureml.core.model import Model
import json
import pickle
#from sklearn.externals import joblib

# Called when the service is loaded
#def init():
#    global model
    # Get the path to the deployed model file and load it
#    model_path = Model.get_model_path('diabetes_model')
#    model = joblib.load(model_path)
#     model = joblib.load('diabetes_model.pkl') 


# Called when a request is received
def model_run(raw_data,model):
    # Get the input data as a numpy array
    data = np.array(json.loads(raw_data)['data'])
    # Get a prediction from the model
    predictions = model.predict(data)
    # Get the corresponding classname for each prediction (0 or 1)
    classnames = ['not-diabetic', 'diabetic']
    predicted_classes = []
    for prediction in predictions:
        predicted_classes.append(classnames[prediction])
    # Return the predictions as JSON
    return json.dumps(predicted_classes)

def model_predict(patient) : 
#load model
   model = joblib.load('diabetes_model.pkl') 
   #x_new = [[2,180,74,24,21,23.9091702,1.488172308,22]]
   x_new = patient
   print ('Patient: {}'.format(x_new[0]))
 # Convert the array to a serializable list in a JSON document
   input_json = json.dumps({"data": x_new})
	# Call the web service, passing the input data (the web service will also accept the data in binary format)
   predictions = model_run(input_json,model)
#y_hat2=.predict(X_test)
# Get the predicted class - it'll be the first (and only) one.
   predicted_classes = json.loads(predictions)
   print(predicted_classes[0])

   return {'Patient': x_new[0], 'Predicted_class': predicted_classes[0]}

if __name__ == "__main__":
    print ("local call ...")
    model_predict()
