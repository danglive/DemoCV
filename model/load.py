# imports
import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# opening and store file in a variable
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout

from tensorflow.keras import backend as K
import tensorflow.compat.v1 as tf



# Reload the model from the 2 files we saved
with open('model.json') as json_file:
    json_config = json_file.read()
new_model = keras.models.model_from_json(json_config)
new_model.load_weights('model2.h5')
print("Loaded Model from disk")

# compile and evaluate loaded model

new_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
#graph = tf.get_default_graph()
new_model.summary()
print (new_model)
print(new_model.outputs)
print(new_model.inputs)


###ye5dem

def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    """
    Freezes the state of a session into a pruned computation graph.

    Creates a new computation graph where variable nodes are replaced by
    constants taking their current value in the session. The new graph will be
    pruned so subgraphs that are not necessary to compute the requested
    outputs are removed.
    @param session The TensorFlow session to be frozen.
    @param keep_var_names A list of variable names that should not be frozen,
                          or None to freeze all the variables in the graph.
    @param output_names Names of the relevant graph outputs.
    @param clear_devices Remove the device directives from the graph for better portability.
    @return The frozen graph definition.
    """
    from tensorflow.python.framework.graph_util import convert_variables_to_constants
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        # Graph -> GraphDef ProtoBuf
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = convert_variables_to_constants(session, input_graph_def,
                                                      output_names, freeze_var_names)
        return frozen_graph


from keras import backend as K
import tensorflow as tf
tf.compat.v1.Session()
frozen_graph = freeze_session(K.get_session(),
                              output_names=[out.op.name for out in new_model.outputs])
                              

tf.train.write_graph(frozen_graph, "new_model", "tf_model.pb", as_text=False)


