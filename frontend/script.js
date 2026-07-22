const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(message, sender) {

    const div = document.createElement("div");

    div.className = sender === "user"
        ? "user-message"
        : "bot-message";

    // Allow HTML (for clickable links)
    div.innerHTML = message.replace(/\n/g, "<br>");

    // Make all links open in a new tab
    const links = div.querySelectorAll("a");

    links.forEach(link => {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
    });

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

}

async function sendMessage() {

    const message = userInput.value.trim();

    if (!message) return;

    addMessage(message, "user");

    userInput.value = "";

    // Show typing indicator
    addMessage("🤖 Typing...", "bot");

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        // Simulate typing delay
        setTimeout(() => {

            // Remove typing indicator
            if (chatBox.lastChild) {
                chatBox.removeChild(chatBox.lastChild);
            }

            // Show bot response
            addMessage(data.response, "bot");

        }, 1000);

    } catch (error) {

        // Remove typing indicator
        if (chatBox.lastChild) {
            chatBox.removeChild(chatBox.lastChild);
        }

        addMessage("❌ Unable to connect to the server.", "bot");

        console.error(error);

    }

}

// Send button
sendBtn.addEventListener("click", sendMessage);

// Press Enter
userInput.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {
        sendMessage();
    }

});

// Quick Action Buttons
function quickMessage(text) {

    userInput.value = text;

    sendMessage();

}

// Clear Chat
const clearBtn = document.getElementById("clear-chat");

clearBtn.addEventListener("click", () => {

    chatBox.innerHTML = `
        <div class="bot-message">
            👋 Welcome to North Star Support!
            <br><br>

            I can help you with:

            <ul>
                <li>📦 Track an Order</li>
                <li>🔄 Returns & Exchanges</li>
                <li>🚚 Shipping Information</li>
                <li>🎒 Product Recommendations</li>
                <li>👨‍💼 Live Agent</li>
            </ul>

            Type your question below.

        </div>
    `;

});