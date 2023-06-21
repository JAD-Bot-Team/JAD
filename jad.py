
from tkinter import Tk, Text, Button, END, Label
from tkinter import ttk
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

def process_input():
    user_input = text_input.get("1.0", END).strip()
    if user_input.lower() == 'quit':
        root.quit()
    else:
        # Add the user message to the conversation
        output_text.insert(END, "User: " + user_input + "\n")
        # Generate a response from the chatbot
        response = generate_response(user_input)
        # Add the chatbot response to the conversation
        output_text.insert(END, "JAD: " + response + "\n\n")
        # Clear the user input field
        text_input.delete("1.0", END)

def voice_input():
    # Placeholder function for voice input functionality
    pass

def camera_input():
    # Placeholder function for camera input functionality
    pass

def show_chat_window():
    welcome_frame.pack_forget()
    chat_frame.pack()

root = Tk()
root.title('JAD')
root.geometry('500x750')

style = ttk.Style(root)
style.configure('.', font=('Arial', 12), foreground='white', background='black')

root.configure(background='black')

welcome_frame = ttk.Frame(root)
welcome_frame.pack(pady=100)

logo_label = Label(welcome_frame, text="JAD", font=("Arial", 24), fg="white", bg="black")
logo_label.pack(pady=10)

description_label = Label(welcome_frame, text='''Welcome to JAD!\n JAD is an AI-powered chatbot app.\n It allows users to have\n interactive conversations with an intelligent chatbot.\n The app integrates with OpenAI's text generation\n API to provide context-aware responses.''',font=("Arial", 14), fg="white", bg="black")

description_label.pack(pady=100)

get_started_button = Button(welcome_frame, text="Get Started", command=show_chat_window)
get_started_button.pack(pady=20)

chat_frame = ttk.Frame(root)

output_label = Label(chat_frame, text="JAD ANSWERS", bg="black", fg="white")
output_label.pack(pady=(20, 10))

output_text = Text(chat_frame, height=25, bg="black", fg="white")
output_text.pack(padx=10, pady=(5, 20), fill='x')

input_label = Label(chat_frame, text="ASK JAD...", bg="black", fg="white")
input_label.pack(pady=(10, 10))

text_input = Text(chat_frame, height=3, bg="black", fg="white")
text_input.pack(padx=10, fill='x')

button_frame = ttk.Frame(chat_frame)
button_frame.pack(pady=20)

camera_button = Button(button_frame, text="Camera", command=camera_input)
camera_button.pack(side="left", padx=10)

send_button = Button(button_frame, text="Send", command=process_input)
send_button.pack(side="left", padx=10)

voice_button = Button(button_frame, text="Voice", command=voice_input)
voice_button.pack(side="left", padx=10)

# button 1
btn1 = Button(button_frame, text='Quit !', command=root.destroy)
btn1.pack(side="left", padx=10)

welcome_frame.configure(style='TFrame')
chat_frame.configure(style='TFrame')

welcome_frame.tkraise()

root.mainloop()