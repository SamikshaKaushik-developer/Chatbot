document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function createMessage(message, isUser) {
        const messageContainer = document.createElement('div');
        messageContainer.classList.add('flex');
        messageContainer.classList.add(isUser ? 'justify-end' : 'justify-start');

        const messageBubble = document.createElement('div');
        messageBubble.classList.add('p-3', 'rounded-lg', 'max-w-xs');
        messageBubble.classList.add(isUser ? 'bg-blue-500' : 'bg-gray-200');
        messageBubble.classList.add(isUser ? 'text-white' : 'text-gray-800');
        
        messageBubble.textContent = message;
        messageContainer.appendChild(messageBubble);
        chatBox.appendChild(messageContainer);
        
        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function handleSendMessage() {
        const message = userInput.value.trim();
        if (message) {
            // Display user message
            createMessage(message, true);
            userInput.value = '';

            // Simulate bot response after a short delay
            setTimeout(() => {
                const botResponse = "I'm a simple bot. You said: '" + message + "'";
                createMessage(botResponse, false);
            }, 1000);
        }
    }

    sendButton.addEventListener('click', handleSendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            handleSendMessage();
        }
    });
});