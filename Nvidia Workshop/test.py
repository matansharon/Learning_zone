#write a a basic gradio app
import gradio as gr

def sketch_recognizer(sketch):
    return sketch

iface = gr.Interface(fn=sketch_recognizer, inputs="text", outputs="text")
iface.launch(share=True)
