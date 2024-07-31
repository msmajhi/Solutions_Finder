from IPython.display import HTML, display, Markdown

def display_question():
    with open("question.txt", "r") as f:
      text = f.read().replace('\n', '<br>')
      
    display(Markdown("# Question:"))
    display(Markdown(text))
    display(Markdown("# Solution:"))



def display_video():

    with open('final_video.txt', 'r') as file:
        video_url = file.read()

    view_html = f"""
    <div style="text-align: center;">
      <video id="videoPlayer" width="640" height="360" controls>
        <source src="{video_url}" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <br>
      <div style="display: flex; justify-content: center; gap: 10px; margin-top: 10px;">
        <button onclick="document.getElementById('videoPlayer').load();" 
                style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
          Refresh Video
        </button>
        <a href="{video_url}" target="_blank" style="text-decoration: none;">
          <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
            Open in New Tab
          </button>
        </a>
      </div>
    </div>
    """
    display(HTML(view_html))

def display_solution():
    display_question()
    display_video()
