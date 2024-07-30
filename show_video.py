from IPython.display import HTML, display

def embed_video(video_url):
    """
    Embeds a video and provides an 'Open in New Tab' button.

    Args:
    video_url (str): The URL of the video to embed.
    """
    # HTML and CSS code to create the video window with an "Open in New Tab" button
    video_window_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            .video-container {{
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }}
            video {{
                width: 100%;
                height: auto;
                border-radius: 4px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            }}
            .button-container {{
                margin-top: 10px;
            }}
            .button-container a {{
                text-decoration: none;
            }}
            .button {{
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }}
            .button:hover {{
                background-color: #45a049;
            }}
        </style>
    </head>
    <body>
        <div class="video-container">
            <h2>Embedded Video</h2>
            <video controls>
                <source src="{video_url}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <div class="button-container">
                <a href="{video_url}" target="_blank">
                    <button class="button">Open in New Tab</button>
                </a>
            </div>
        </div>
    </body>
    </html>
    """

    # Display the HTML content in Google Colab
    display(HTML(video_window_html))

