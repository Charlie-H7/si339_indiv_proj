import template as temp
from config import api_key

# Holds video links in order (Col,doug,etc)
video_list = ["https://www.youtube.com/embed/U7e7iUhBLLg?si=Qd4wUdAerEpFCdNz"]
name_list = ["Name 1"]
   
desc_list = [
"""ColossalIsCrazy, a 77 year old clown with a smoking addiction.  He makes videos for the purpose of criticizing other content creators through satirical and edgy commentary."""

]

def render_templates(head, foot, name, embed_url, desc) :
    
    comment_data = ""

    # Access Api data

    creator_data = f"""
        <h1>{name}</h1>
    </header>

    <div>
        <!-- Video -->
         <!-- Descr -->
          <!-- comments -->
        <iframe width="560" height="315" src="{embed_url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        <p class="descr">
            {desc}
        </p>

<!-- Comments -->
    <div>
        test
    </div>
"""