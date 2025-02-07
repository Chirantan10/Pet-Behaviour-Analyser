// let mediaRecorder;
// let audioChunks = [];

// // Buttons
// const recordBtn = document.getElementById('recordBtn');
// const stopBtn = document.getElementById('stopBtn');
// const playBtn = document.getElementById('playBtn');
// const uploadBtn = document.getElementById('uploadBtn');

// // Status Text
// const statusText = document.getElementById('status');

// let audioBlob;
// let audioURL;

// recordBtn.addEventListener('click', async () => {
//   try {
//     const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
//     mediaRecorder = new MediaRecorder(stream);

//     mediaRecorder.onstart = () => {
//       audioChunks = [];
//       statusText.textContent = 'Recording...';
//       recordBtn.disabled = true;
//       stopBtn.disabled = false;
//       playBtn.disabled = true;
//       uploadBtn.disabled = true;
//     };

//     mediaRecorder.ondataavailable = (event) => {
//       audioChunks.push(event.data);
//     };

//     mediaRecorder.onstop = () => {
//       audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
//       audioURL = URL.createObjectURL(audioBlob);
//       statusText.textContent = 'Recording stopped. You can play or upload the audio.';
//       recordBtn.disabled = false;
//       stopBtn.disabled = true;
//       playBtn.disabled = false;
//       uploadBtn.disabled = false;
//     };

//     mediaRecorder.start();
//   } catch (error) {
//     console.error('Error accessing microphone:', error);
//     statusText.textContent = 'Error accessing microphone. Please check your permissions.';
//   }
// });

// stopBtn.addEventListener('click', () => {
//   mediaRecorder.stop();
// });

// playBtn.addEventListener('click', () => {
//   const audio = new Audio(audioURL);
//   audio.play();
// });

// uploadBtn.addEventListener('click', () => {
//   const formData = new FormData();
//   formData.append('file', audioBlob, 'audio.wav');

//   fetch('http://127.0.0.1:5000/process-audio', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       statusText.textContent = 'Audio uploaded successfully!';
//       console.log('Response:', data);
//     })
//     .catch((error) => {
//       console.error('Error uploading audio:', error);
//       statusText.textContent = 'Failed to upload audio.';
//     });
// });
let mediaRecorder;
let audioChunks = [];

// Buttons
const recordBtn = document.getElementById('recordBtn');
const stopBtn = document.getElementById('stopBtn');
const playBtn = document.getElementById('playBtn');
const uploadBtn = document.getElementById('uploadBtn');

// Status Text
const statusText = document.getElementById('status');

let audioBlob;
let audioURL;

recordBtn.addEventListener('click', async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.onstart = () => {
      audioChunks = [];
      statusText.textContent = 'Recording...';
      recordBtn.disabled = true;
      stopBtn.disabled = false;
      playBtn.disabled = true;
      uploadBtn.disabled = true;
    };

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
      audioURL = URL.createObjectURL(audioBlob);
      statusText.textContent = 'Recording stopped. You can play or upload the audio.';
      recordBtn.disabled = false;
      stopBtn.disabled = true;
      playBtn.disabled = false;
      uploadBtn.disabled = false;
    };

    mediaRecorder.start();
  } catch (error) {
    console.error('Error accessing microphone:', error);
    statusText.textContent = 'Error accessing microphone. Please check your permissions.';
  }
});

stopBtn.addEventListener('click', () => {
  mediaRecorder.stop();
});

playBtn.addEventListener('click', () => {
  const audio = new Audio(audioURL);
  audio.play();
});

// uploadBtn.addEventListener('click', () => {
//   const formData = new FormData();
//   formData.append('file', audioBlob, 'audio.wav');

//   // Ensure the correct endpoint is being hit. Make sure Flask server is running on the right port.
//   fetch('http://127.0.0.1:5000/process-audio', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((response) => {
//       if (response.ok) {
//         return response.blob(); // Expecting an audio file response (mp3)
//       } else {
//         throw new Error('Failed to upload audio');
//       }
//     })
//     .then((audioBlob) => {
//       const audioUrl = URL.createObjectURL(audioBlob);
//       // Play the response audio (the suggestions in voice form)
//       const audio = new Audio(audioUrl);
//       audio.play();
//       statusText.textContent = 'Audio uploaded successfully! Playing the response...';
//     })
//     .catch((error) => {
//       console.error('Error uploading audio:', error);
//       statusText.textContent = 'Failed to upload audio.';
//     });
// });
uploadBtn.addEventListener('click', () => {
  // Check if audioBlob is available before proceeding
  if (!audioBlob) {
    statusText.textContent = 'No audio recorded to upload. Please record an audio first.';
    return;
  }

  const formData = new FormData();
  formData.append('file', audioBlob, 'audio.wav');

  // Ensure the correct endpoint is being hit. Make sure Flask server is running on the right port.
  fetch('http://127.0.0.1:5000/process-audio', {
    method: 'POST',
    body: formData,
  })
    .then((response) => {
      if (response.ok) {
        // Expecting an audio file response (mp3)
        return response.blob();
      } else {
        return response.json().then((data) => {
          throw new Error(data.error || 'Failed to process audio on the server');
        });
      }
    })
    .then((audioBlob) => {
      // Create a URL for the audio blob and play the response
      const audioUrl = URL.createObjectURL(audioBlob);
      const audio = new Audio(audioUrl);
      audio.play();

      statusText.textContent = 'Audio uploaded successfully! Playing the response...';
    })
    .catch((error) => {
      console.error('Error uploading audio:', error);
      statusText.textContent = `Failed to upload audio: ${error.message}`;
    });
});

