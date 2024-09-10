let isTranscribing = false;

document.getElementById('toggleTranscript').addEventListener('click', () => {
    isTranscribing = !isTranscribing;
    
    if (isTranscribing) {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, { action: 'start' });
        });
        document.getElementById('toggleTranscript').innerText = 'Stop Transcript';
    } else {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            chrome.tabs.sendMessage(tabs[0].id, { action: 'stop' });
        });
        document.getElementById('toggleTranscript').innerText = 'Show Transcript';
    }
});
