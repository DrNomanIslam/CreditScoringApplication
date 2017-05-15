from keras.models import *
from keras.layers import *
import os



def loadModelAndWeight():
	# load json and create model
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'model.json')
	
	json_file = open(file_path, 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights(os.path.join(module_dir, "model.h5"))
	print("Loaded model from disk")

	# evaluate loaded model on test data
	#loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
	return loaded_model