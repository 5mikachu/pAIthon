document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const fileInput = document.getElementById('file-input').files[0]; // Get the file

    if (userInput.trim() === '' && !fileInput) return;

    const formData = new FormData();
    formData.append('message', userInput);

    if (fileInput) {
        formData.append('file', fileInput);

        const fileNameDisplay = `<em>📄 - ${fileInput.name}</em>`;
        addMessageToChat(fileNameDisplay, 'user-message');
    }

    if (userInput.trim() !== '') {
        addMessageToChat(userInput, 'user-message');
    }

    fetch('/get_response', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const aiResponse = data.response;
        addMessageToChat(aiResponse, 'ai-message');
    });

    document.getElementById('user-input').value = '';
    document.getElementById('file-input').value = '';
}

function addMessageToChat(message, className) {
    const chatContainer = document.getElementById('chat-container');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', className);
    messageDiv.innerHTML = message.replace(/\n/g, '<br />');
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}
