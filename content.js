let recognition;
let transcriptElement;

function startTranscription() {
    // Create a transcript element if it doesn't exist
    if (!transcriptElement) {
        transcriptElement = document.createElement('div');
        transcriptElement.style.position = 'absolute';
        transcriptElement.style.bottom = '10px';
        transcriptElement.style.width = '100%';
        transcriptElement.style.textAlign = 'center';
        transcriptElement.style.color = 'white';
        transcriptElement.style.background = 'rgba(0, 0, 0, 0.7)';
        transcriptElement.style.padding = '10px';
        transcriptElement.style.fontSize = '20px';
        document.body.appendChild(transcriptElement);
    }

    // Initialize the Web Speech API
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
            transcript += event.results[i][0].transcript;
        }
        transcriptElement.innerText = transcript;
    };

    recognition.start();
}

function stopTranscription() {
    if (recognition) {
        recognition.stop();
        recognition = null;
    }
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'start') {
        startTranscription();
    } else if (request.action === 'stop') {
        stopTranscription();
    }
});
