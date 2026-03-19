# Python Chatbot Web UI

A modern, responsive ChatGPT-like web interface for your Python chatbot.

## Features

-   **Backend**: Flask-based API wrapper for the existing `chatbot.py` logic.
-   **Frontend**: Vanilla HTML/CSS/JS (no frameworks) with a sleek dark theme.
-   **Conversation Persistence**: Maintains history during the session (stateless between restarts).
-   **Responsive Design**: Works on mobile and desktop.
-   **Typing Indicator**: Let's users know the bot is thinking.
-   **Auto-scroll**: Automatically scrolls to the latest message.

## Prerequisites

1.  **Ollama**: Ensure Ollama is installed and running with the `llama3` model.
    ```bash
    ollama run llama3
    ```
2.  **Python 3.x**: Ensure Python is installed.

## Setup Instructions

1.  **Install Dependencies**:
    Open your terminal in the project directory and run:
    ```bash
    pip install -r requirment.txt
    ```

2.  **Run the Backend**:
    ```bash
    python app.py
    ```
    The server will start at `http://127.0.0.1:5000`.

3.  **Access the Web UI**:
    Simply open the `index.html` file in your preferred web browser, or navigate to `http://127.0.0.1:5000` in your browser.

## Customization

-   To change the chatbot logic, look for the `chat()` function in `app.py`.
-   To change the UI styles, modify the `<style>` block in `index.html`.

Enjoy your modern chatbot! 🤖
