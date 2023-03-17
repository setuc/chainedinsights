import gradio as gr
import os

port = int(os.environ.get('WEBSITES_PORT', 5000))

def add_text(history, text):
    """_summary_
        The function returns a new history with the text added and an empty string (which is the output).
    Args:
        history (_type_): _history is the list of past outputs. It is a list of tuples (text, output).
        text (_type_): text is the text to be added to the history.

    Returns:
        _type_: This function returns a new history with the text added (which is the output).
    """
    history = history + [(text, None)]
    return history, ""


def add_file(history, file):
    """_summary_

    Args:
        history (_type_): history is the list of past outputs. It is a list of tuples (text, output).
        file (_type_): file is the filename to be added to the history.
    Returns:
        _type_: This function returns a new history with the filename added (which is the output).
    """
    history = history + [((file.name,), None)]
    return history


def bot(history):
    response = "**That's cool!**"
    history[-1][1] = response
    return history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot([], elem_id="chatbot").style(height=750)

    with gr.Row():
        with gr.Column(scale=0.85):
            txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter, or upload an image",
            ).style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])

    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(bot, chatbot, chatbot)
    btn.upload(add_file, [chatbot, btn], [chatbot]).then(bot, chatbot, chatbot)

demo.launch(share=True, inline=True, debug=True, server_port=port, show_api=False)
