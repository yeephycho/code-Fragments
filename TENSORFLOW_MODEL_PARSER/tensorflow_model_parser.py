import tensorflow as tf
import numpy as np

sess = tf.Session()
saver = tf.train.import_meta_graph('densenet.ckpt-38465.meta')
saver.restore(sess, 'densenet.ckpt-38465')

for var in tf.global_variables():
    print var.name, sess.run(var)
