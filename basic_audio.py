import tensorflow as tf
from tensorflow.contrib.framework.python.ops import audio_ops as contrib_audio
audio_binary = tf.read_file(filename)
desired_channels = 1
wav_decoder = contrib_audio.decode_wav(
    audio_binary,
    desired_channels=desired_channels)
    with tf.Session() as sess:
    sample_rate, audio = sess.run([
        wav_decoder.sample_rate,
        wav_decoder.audio])
        first_sample = audio[0][0] * (1 << 15)
second_sample = audio[1][0] * (1 << 15)
