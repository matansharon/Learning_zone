import gradio as gr

# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Create a basic interface with a text input and text output
iface = gr.Interface(
    fn=greet,             # the function to run
    inputs="text",        # input component type
    outputs="text",       # output component type
    title="Greeting App", # optional: give your app a title
    description="Enter your name and get a nice greeting!"
)

# Launch the app
iface.launch()
