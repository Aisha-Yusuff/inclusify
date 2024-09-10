let recognition;
let transcriptElement;

function startTranscription() {
  // Create a transcript element if it doesn't exist

  // Initialize the Web Speech API
  recognition = new webkitSpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;

  recognition.onresult = (event) => {
    let transcript = "";
    for (let i = event.resultIndex; i < event.results.length; i++) {
      transcript += event.results[i][0].transcript;
    }
    transcriptElement = transcript;
  };

  console.log(transcriptElement, "transcriptElement");

  recognition.start();
}

function stopTranscription() {
  if (recognition) {
    recognition.stop();
    recognition = null;
  }
  window.find(transcriptElement);
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "start") {
    startTranscription();
  } else if (request.action === "stop") {
    stopTranscription();
  }
});
