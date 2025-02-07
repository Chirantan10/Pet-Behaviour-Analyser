# import os
# import numpy as np
# import librosa
# import joblib
# from flask import Flask, request, jsonify, send_file
# from gtts import gTTS
# from io import BytesIO
# from flask_cors import CORS
# from pydub import AudioSegment


# app = Flask(__name__)

# CORS(app)

# # Load the pre-trained model
# model_path = 'sound_classification_model.pkl'
# clf = joblib.load(model_path)

# # Define the suggestion dictionary
# suggestions = {
#     'Barking': [
#         "Check if the dog is hungry or thirsty.",
#         "Make sure the dog has enough playtime and exercise.",
#         "Check if there is someone at the door or near your house.",
#         "Try calming the dog by providing some distraction like a toy."
#     ],
#     'Growling': [
#         "The dog may feel threatened or anxious. Ensure a calm environment.",
#         "Avoid approaching the dog too suddenly; let them feel safe.",
#         "Check if the dog is in pain or feeling uncomfortable."
#     ],
#     'Howling': [
#         "The dog may be lonely or anxious. Try giving them attention.",
#         "Provide comfort by spending more time with the dog.",
#         "Consider giving the dog a comfort object like a blanket or toy."
#     ],
#     'Whimpering': [
#         "The dog may be in distress, hungry, or need to go outside.",
#         "Check if the dog has any injuries or is unwell.",
#         "Take the dog out for a bathroom break if needed."
#     ],
#     'Whinning': [
#         "The dog might be feeling anxious or wants attention.",
#         "Provide some physical affection or comfort.",
#         "Ensure the dog is not in pain or discomfort."
#     ]
# }

# @app.route('/')
# def home():
#     return "Server is running"

# # Function to extract features (MFCC)
# # def extract_features(file_path):
# #     try:
# #         # Load the audio file and extract features (MFCCs)
# #         audio, sample_rate = librosa.load(file_path, sr=None)  # sr=None keeps the original sample rate
# #         mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
# #         mfcc_mean = np.mean(mfcc.T, axis=0)  # Calculate the mean of MFCCs across time frames
# #         return mfcc_mean
# #     except Exception as e:
# #         print(f"Error processing {file_path}: {e}")
# #         return None

# def convert_to_wav(input_file, output_file):
#     """Converts any audio format to .wav using pydub."""
#     audio = AudioSegment.from_file(input_file)
#     audio.export(output_file, format='wav')

# def extract_features(file_path):
#     try:
#         # Convert the uploaded audio file to WAV format (if it's not already)
#         temp_wav_path = 'temp_audio_converted.wav'
#         convert_to_wav(file_path, temp_wav_path)
        
#         # Now load the converted .wav file
#         audio, sample_rate = librosa.load(temp_wav_path, sr=None)
#         mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
#         mfcc_mean = np.mean(mfcc.T, axis=0)  # Calculate the mean of MFCCs across time frames
        
#         # Clean up the temporary file
#         os.remove(temp_wav_path)

#         return mfcc_mean
#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")
#         return None

# # Endpoint to process the uploaded audio
# @app.route('/process-audio', methods=['POST'])
# def process_audio():
#     print("POST request received")  
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     # Save the uploaded file
#     uploaded_file = request.files['file']
#     temp_file_path = 'temp_audio.wav'
#     uploaded_file.save(temp_file_path)

#     try:
#         # Extract features from the uploaded file
#         features = extract_features(temp_file_path)
#         if features is None:
#             return jsonify({'error': 'Unable to process the audio file'}), 400

#         # Predict the class
#         predicted_class = clf.predict([features])[0]

#         # Get suggestions for the predicted class
#         class_suggestions = suggestions.get(predicted_class, ["No suggestions available for this class."])
#         suggestion_text = f"The detected sound is '{predicted_class}'. " + " ".join(class_suggestions)

#         # Convert suggestions to audio
#         tts = gTTS(suggestion_text, lang='en')
#         audio_io = BytesIO()
#         tts.write_to_fp(audio_io)
#         audio_io.seek(0)

#         # Clean up the temporary file
#         os.remove(temp_file_path)

#         # Send the audio response
#         return send_file(
#             audio_io,
#             mimetype="audio/mpeg",
#             as_attachment=False,
#             download_name="response.mp3"
#         )
#     except Exception as e:
#         print(f"Error processing the audio: {e}")
#         return jsonify({'error': 'An error occurred while processing the audio'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# import os
# import numpy as np
# import librosa
# import joblib
# from flask import Flask, request, jsonify, send_file
# from gtts import gTTS
# from io import BytesIO
# from flask_cors import CORS
# from pydub import AudioSegment

# app = Flask(__name__)
# CORS(app)

# # Load the pre-trained model
# model_path = 'sound_classification_model.pkl'
# clf = joblib.load(model_path)

# # Define the suggestion dictionary
# suggestions = {
#     'Barking': [
#         "Check if the dog is hungry or thirsty.",
#         "Make sure the dog has enough playtime and exercise.",
#         "Check if there is someone at the door or near your house.",
#         "Try calming the dog by providing some distraction like a toy."
#     ],
#     'Growling': [
#         "The dog may feel threatened or anxious. Ensure a calm environment.",
#         "Avoid approaching the dog too suddenly; let them feel safe.",
#         "Check if the dog is in pain or feeling uncomfortable."
#     ],
#     'Howling': [
#         "The dog may be lonely or anxious. Try giving them attention.",
#         "Provide comfort by spending more time with the dog.",
#         "Consider giving the dog a comfort object like a blanket or toy."
#     ],
#     'Whimpering': [
#         "The dog may be in distress, hungry, or need to go outside.",
#         "Check if the dog has any injuries or is unwell.",
#         "Take the dog out for a bathroom break if needed."
#     ],
#     'Whinning': [
#         "The dog might be feeling anxious or wants attention.",
#         "Provide some physical affection or comfort.",
#         "Ensure the dog is not in pain or discomfort."
#     ]
# }

# @app.route('/')
# def home():
#     return "Server is running"

# # Function to extract features (MFCC)
# def extract_features(file_path):
#     try:
#         # Load the audio file and extract features (MFCCs)
#         audio, sample_rate = librosa.load(file_path, sr=None)  # sr=None keeps the original sample rate
#         mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
#         mfcc_mean = np.mean(mfcc.T, axis=0)  # Calculate the mean of MFCCs across time frames
#         return mfcc_mean
#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")
#         return None

# # Function to convert the input audio to .wav format
# def convert_to_wav(input_file, output_file):
#     try:
#         audio = AudioSegment.from_file(input_file)
#         audio.export(output_file, format='wav')
#     except Exception as e:
#         print(f"Error converting {input_file} to WAV: {e}")
#         raise

# # Endpoint to process the uploaded audio
# @app.route('/process-audio', methods=['POST'])
# def process_audio():
#     print("POST request received")  
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     # Save the uploaded file
#     uploaded_file = request.files['file']
#     temp_file_path = 'temp_audio'  # Temporary file without extension
#     uploaded_file.save(temp_file_path)

#     # Convert the uploaded file to .wav format
#     wav_file_path = 'temp_audio.wav'
#     try:
#         convert_to_wav(temp_file_path, wav_file_path)
#     except Exception as e:
#         return jsonify({'error': 'Error converting the audio file to WAV format'}), 400

#     try:
#         # Extract features from the converted .wav file
#         features = extract_features(wav_file_path)
#         if features is None:
#             return jsonify({'error': 'Unable to process the audio file'}), 400

#         # Predict the class
#         predicted_class = clf.predict([features])[0]

#         # Get suggestions for the predicted class
#         class_suggestions = suggestions.get(predicted_class, ["No suggestions available for this class."])
#         suggestion_text = f"The detected sound is '{predicted_class}'. " + " ".join(class_suggestions)

#         # Convert suggestions to audio
#         tts = gTTS(suggestion_text, lang='en')
#         audio_io = BytesIO()
#         tts.write_to_fp(audio_io)
#         audio_io.seek(0)

#         # Clean up the temporary files
#         os.remove(temp_file_path)
#         os.remove(wav_file_path)

#         # Send the audio response
#         return send_file(
#             audio_io,
#             mimetype="audio/mpeg",
#             as_attachment=False,
#             download_name="response.mp3"
#         )
#     except Exception as e:
#         print(f"Error processing the audio: {e}")
#         return jsonify({'error': 'An error occurred while processing the audio'}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')



# import os
# import numpy as np
# import librosa
# import soundfile as sf
# import joblib
# from flask import Flask, request, jsonify, send_file
# from gtts import gTTS
# from io import BytesIO
# from pydub import AudioSegment  # For audio conversion
# from flask_cors import CORS

# app = Flask(__name__)

# CORS(app)

# # Load the pre-trained model
# model_path = 'sound_classification_model.pkl'
# clf = joblib.load(model_path)

# # Define the suggestion dictionary
# suggestions = {
#     'Barking': [
#         "Check if the dog is hungry or thirsty.",
#         "Make sure the dog has enough playtime and exercise.",
#         "Check if there is someone at the door or near your house.",
#         "Try calming the dog by providing some distraction like a toy."
#     ],
#     'Growling': [
#         "The dog may feel threatened or anxious. Ensure a calm environment.",
#         "Avoid approaching the dog too suddenly; let them feel safe.",
#         "Check if the dog is in pain or feeling uncomfortable."
#     ],
#     'Howling': [
#         "The dog may be lonely or anxious. Try giving them attention.",
#         "Provide comfort by spending more time with the dog.",
#         "Consider giving the dog a comfort object like a blanket or toy."
#     ],
#     'Whimpering': [
#         "The dog may be in distress, hungry, or need to go outside.",
#         "Check if the dog has any injuries or is unwell.",
#         "Take the dog out for a bathroom break if needed."
#     ],
#     'Whinning': [
#         "The dog might be feeling anxious or wants attention.",
#         "Provide some physical affection or comfort.",
#         "Ensure the dog is not in pain or discomfort."
#     ]
# }

# # Function to extract features (MFCC)
# def extract_features(file_path):
#     try:
#         # Load the audio file and extract features (MFCCs)
#         audio, sample_rate = librosa.load(file_path, sr=None)  # sr=None keeps the original sample rate
#         mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
#         mfcc_mean = np.mean(mfcc.T, axis=0)  # Calculate the mean of MFCCs across time frames
#         return mfcc_mean
#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")
#         return None

# # Endpoint to process the uploaded audio
# @app.route('/process-audio', methods=['POST'])
# def process_audio():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file provided'}), 400

#     uploaded_file = request.files['file']
#     original_file_path = 'uploaded_audio'
#     temp_file_path = 'temp_audio.wav'

#     # Save the uploaded file
#     uploaded_file.save(original_file_path)

#     try:
#         # Convert input audio to .wav if not already in .wav format
#         try:
#             audio = AudioSegment.from_file(original_file_path)
#             audio.export(temp_file_path, format="wav")
#         except Exception as e:
#             os.remove(original_file_path)
#             return jsonify({'error': f'Error converting audio to WAV format: {e}'}), 400

#         # Extract features from the converted .wav file
#         features = extract_features(temp_file_path)
#         if features is None:
#             os.remove(original_file_path)
#             os.remove(temp_file_path)
#             return jsonify({'error': 'Unable to extract features from the audio file'}), 400

#         # Predict the class
#         predicted_class = clf.predict([features])[0]

#         # Get suggestions for the predicted class
#         class_suggestions = suggestions.get(predicted_class, ["No suggestions available for this class."])
#         suggestion_text = f"The detected sound is '{predicted_class}'. " + " ".join(class_suggestions)

#         # Convert suggestions to audio
#         tts = gTTS(suggestion_text, lang='en')
#         audio_io = BytesIO()
#         tts.write_to_fp(audio_io)
#         audio_io.seek(0)

#         # Clean up temporary files
#         os.remove(original_file_path)
#         os.remove(temp_file_path)

#         # Send the audio response
#         return send_file(
#             audio_io,
#             mimetype="audio/mpeg",
#             as_attachment=False,
#             download_name="response.mp3"
#         )
#     except Exception as e:
#         print(f"Error processing the audio: {e}")
#         os.remove(original_file_path)
#         os.remove(temp_file_path)
#         return jsonify({'error': f'An error occurred: {e}'}), 500

# if __name__ == '__main__':
#     app.run(debug=True ,  host='0.0.0.0')

import os
import numpy as np
import librosa
import joblib
from flask import Flask, request, jsonify, send_file
from gtts import gTTS
from io import BytesIO
from flask_cors import CORS
from pydub import AudioSegment

app = Flask(__name__)
CORS(app)

AudioSegment.converter = "C:/ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = "C:/ffmpeg/bin/ffprobe.exe"

# Load the pre-trained model
model_path = 'sound_classification_model.pkl'
clf = joblib.load(model_path)

# Define the suggestion dictionary
suggestions = {
    'Barking': [
        "Check if the dog is hungry or thirsty.",
        "Make sure the dog has enough playtime and exercise.",
        "Check if there is someone at the door or near your house.",
        "Try calming the dog by providing some distraction like a toy."
    ],
    'Growling': [
        "The dog may feel threatened or anxious. Ensure a calm environment.",
        "Avoid approaching the dog too suddenly; let them feel safe.",
        "Check if the dog is in pain or feeling uncomfortable."
    ],
    'Howling': [
        "The dog may be lonely or anxious. Try giving them attention.",
        "Provide comfort by spending more time with the dog.",
        "Consider giving the dog a comfort object like a blanket or toy."
    ],
    'Whimpering': [
        "The dog may be in distress, hungry, or need to go outside.",
        "Check if the dog has any injuries or is unwell.",
        "Take the dog out for a bathroom break if needed."
    ],
    'Whinning': [
        "The dog might be feeling anxious or wants attention.",
        "Provide some physical affection or comfort.",
        "Ensure the dog is not in pain or discomfort."
    ]
}

@app.route('/')
def home():
    return "Server is running"

# Function to convert the audio file to WAV using pydub
def convert_to_wav(input_file, output_file):
    try:
        audio = AudioSegment.from_file(input_file)
        audio.export(output_file, format='wav')
        return output_file
    except Exception as e:
        print(f"Error converting {input_file} to WAV: {e}")
        return False

# Function to extract features (MFCC)
def extract_features(file_path):
    try:
        # Load the audio file and extract features (MFCCs)
        audio, sample_rate = librosa.load(file_path, sr=None)  # sr=None keeps the original sample rate
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
        mfcc_mean = np.mean(mfcc.T, axis=0)  # Calculate the mean of MFCCs across time frames
        return mfcc_mean
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

# Endpoint to process the uploaded audio
@app.route('/process-audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    # Save the uploaded file
    uploaded_file = request.files['file']
    temp_file_path = 'temp_audio'

    # Save the file with its original format
    uploaded_file.save(temp_file_path)

    # Convert the uploaded audio to WAV format
    wav_file_path = 'temp_audio.wav'
    if not convert_to_wav(temp_file_path, wav_file_path):
        return jsonify({'error': 'Error converting the audio file to WAV format'}), 400

    try:
        # Extract features from the converted WAV file
        features = extract_features(wav_file_path)
        if features is None:
            return jsonify({'error': 'Unable to process the audio file'}), 400

        # Predict the class
        predicted_class = clf.predict([features])[0]

        # Get suggestions for the predicted class
        class_suggestions = suggestions.get(predicted_class, ["No suggestions available for this class."])
        suggestion_text = f"The detected sound is '{predicted_class}'. " + " ".join(class_suggestions)

        # Convert suggestions to audio
        tts = gTTS(suggestion_text, lang='en')
        audio_io = BytesIO()
        tts.write_to_fp(audio_io)
        audio_io.seek(0)

        # Clean up the temporary files
        os.remove(temp_file_path)
        os.remove(wav_file_path)

        # Send the audio response
        return send_file(
            audio_io,
            mimetype="audio",
            as_attachment=False,
            download_name="response.mp3"
        )
    except Exception as e:
        print(f"Error processing the audio: {e}")
        return jsonify({'error': 'An error occurred while processing the audio'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


