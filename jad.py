import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Initialize the conversation
def start_conversation():
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt='Hi\nJad:',
        temperature=0.7,
        max_tokens=50,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Generate a response given user input
def generate_response(user_input):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'User: {user_input}\nJAD:',
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

class ChatbotWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Chatbot")
        self.setFixedSize(600, 600)  # Set a fixed window size
        self.setup_ui()
        
        # Start the conversation and display the initial response
        self.add_message(start_conversation(), is_user=False)

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        # Create a scrollable text area for the conversation
        self.conversation_text = QtWidgets.QTextEdit()
        self.conversation_text.setReadOnly(True)
        self.conversation_text.setFont(QtGui.QFont("Arial", 12))
        self.layout.addWidget(self.conversation_text)

        # Create an input field for user messages
        self.user_input = QtWidgets.QLineEdit()
        self.user_input.setFont(QtGui.QFont("Arial", 12))
        self.user_input.returnPressed.connect(self.handle_user_input)
        self.layout.addWidget(self.user_input)

        # Create a send button
        self.send_button = QtWidgets.QPushButton("Send")
        self.send_button.setFont(QtGui.QFont("Arial", 12))
        self.send_button.clicked.connect(self.handle_user_input)
        self.layout.addWidget(self.send_button)

        # Set the background and text colors
        self.setStyleSheet("background-color: #F0F0F0;")
        self.conversation_text.setStyleSheet("background-color: white; color: black;")
        self.user_input.setStyleSheet("background-color: white; color: black;")
        self.send_button.setStyleSheet("background-color: #4287f5; color: white;")

    def handle_user_input(self):
        user_message = self.user_input.text()
        if user_message.lower() == 'quit':
            QtWidgets.QApplication.quit()
        else:
            # Add the user message to the conversation
            self.add_message(user_message, is_user=True)
            
            # Generate a response from the chatbot
            response = generate_response(user_message)
            
            # Add the chatbot response to the conversation
            self.add_message(response, is_user=False)
            
            # Clear the user input field
            self.user_input.clear()

    def add_message(self, message, is_user=True):
        if is_user:
            self.conversation_text.append("<b>User:</b> " + message)
        else:
            self.conversation_text.append("<b>AI:</b> " + message)
        
        # Scroll to the bottom of the text area
        self.conversation_text.verticalScrollBar().setValue(self.conversation_text.verticalScrollBar().maximum())

        # Clear the formatting for the new line
        self.conversation_text.setCurrentCharFormat(QtGui.QTextCharFormat())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ChatbotWindow()
    
    # Apply a modern style to the GUI
    app.setStyle("Fusion")
    
    # Set a custom palette for the GUI
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#FFFFFF"))
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor("#F0F0F0"))
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor("#000000"))
    app.setPalette(palette)
    
    window.show()
    sys.exit(app.exec_())
