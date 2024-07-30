from IPython.display import HTML, display

def display_video(video_url):
    view_html = f"""
    <div style="text-align: center;">
      <video id="videoPlayer" width="640" height="360" controls>
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <br>
      <button onclick="document.getElementById('videoPlayer').load();" 
              style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
        Refresh Video
      </button>
    </div>
    """
    display(HTML(view_html))
