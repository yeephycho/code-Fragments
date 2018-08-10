import tensorflow as tf
from numpy import random


# Cannot run directly
# Sudo code
# Restore all the variables that the checkpoint has but re-initialize all the variables which the checkpoint doesn't have.

graph = network.build_graph()

key = "batch_normalization"
restore_path = "/path/to/checkpoint/model.ckpt"

all_variables = tf.get_collection_ref(tf.GraphKeys.GLOBAL_VARIABLES)

with tf.Session() as sess:
    sess.run(tf.variables_initializer(all_variables))
    tmp_saver = tf.train.Saver(var_list=[v for v in all_variables if key not in v.name])
    tmp_saver.restore(sess, restore_path)

    sess.run()
