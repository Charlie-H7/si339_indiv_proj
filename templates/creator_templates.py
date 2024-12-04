import template as temp
from config import api_key
import json
import re
from googleapiclient.discovery import build

# Holds video links in order (Col,doug,etc)
video_list = ["https://www.youtube.com/embed/SkiCHrDHv74?si=9sLLwNXBCKnQtzBU", "https://www.youtube.com/embed/HyqK2Tsujho?si=DBtVqidhZew70wGx", "https://www.youtube.com/embed/Hcz_zqvhuAI?si=oEL6jSjd5tjR0bTW", "https://www.youtube.com/embed/cPZP-yC6j70?si=FGKDBAc5pTUQwKsr", "https://www.youtube.com/embed/ut9JQq3X3VY?si=FAP2E-RNFbBu8jxE"]
name_list = ["Colossal Is Crazy", "DougDoug", "Took2Much", "TierZoo", "RDCworld1"]
   
desc_list = [
"""Colossal Is Crazy, a 77 year old clown with a smoking addiction.  He makes videos for the purpose of criticizing other content creators through satirical and edgy commentary.""",
"""DougDoug, self proclaimed solver of problems no one has. He makes videos completing challanges involving his twitch chat, most often involving gaming challenges.""",
""" Took2Much, a channel that covers stories about the cartel from our neighbors to the south. If your are interested in the cartel or like watching videos with dark/scary themes this channel is a nice addition.""",
"""TierZoo a channel that puts a fun spin on eductational content ranking species of animals in tier lists often combining this with game references""",
"""RDCWorld1 is a YouTube channel known for their comedic sketches, with a focus on pop culture, using concepts such as anime, sports, and video games, among other ideas."""
]

# Establishes connection to youtube api
youtube = build('youtube', 'v3', developerKey=api_key)

def render_templates(head, foot, name, embed_url, desc, idx) :
    
    comment_data = ""
    head_html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../css/reset.css">
        <link rel="stylesheet" href="../css/creator_styling.css">"""
    
    if(idx != 0):
        head_html += f"\n<link rel=\"stylesheet\" href=\"../css/creator_styling{str(idx)}.css\">"

    pattern = r"(?<=\/embed\/)[^?]+"
    match = re.search(pattern, embed_url)



    # Access Api data
         #comments_response = youtube.commentThreads().list(
    comments_response = youtube.commentThreads().list(
        # part='snippet,replies', #Required (Optional 'replies' to include replies)
        part='snippet', #Required (Optional 'replies' to include replies)
        videoId=match.group(), # 'v' query in video url: value is regex that gets the v query
        maxResults=6,  # Adjust as needed
        textFormat="plainText", # textFormat is used to get plain text response instead of html (def)
        order='relevance' #†his makes sure that the order is the same based on the website (im guessing originally sorted on date)
    ).execute()
    
    # Pretty-print the JSON {yipee}
    formatted_json = json.dumps(comments_response, indent=3)

    # print(comments_response[0]['snippet']['topLevelComment']['snippet']['textDisplay'])
    
    # print(f"{formatted_json}\n")
    # print(formatted_json[0])
    # print(formatted_json[0]['snippet']['topLevelComment']['snippet']['textDisplay'])

    # Get all comments from json into a list data struct
    # for comment in comments_response['items']:
    #     replies = [] # reset on new top_lvl comment
      # Get all comments from json into a list data struct
    for comment in comments_response['items']:
        replies = [] # reset on new top_lvl comment
        

        # Tuple holding 'base' comment and id of that comment
        #comment_dat = (comment['snippet']['topLevelComment']['snippet']['textDisplay'],
        #               comment['snippet']['topLevelComment']['id'])

        # Hold the text for the current comment
        comment_temp = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        username = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        # print(username)
        # print(comment_temp)
        # print()

        comment_data += f"""
            <div class="comment_block">
                <div class="username">{username}</div>
                <p class="comment">
                    {comment_temp}
                </p>                
            </div>
            """

## HEYYYY


    creator_data = f"""
        <h1>{name}</h1>
    </header>

    <div class="main-data">
        <!-- Video -->
         <!-- Descr -->
          <!-- comments -->
        <iframe class="video" width="560" height="315" src="{embed_url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        <p class="descr">
            {desc}
        </p>
    </div>

<!-- Comments -->
    <div class="comment-container" tabindex="0">
        <h2 class="comment-seg">Comments:</h2>
        {comment_data}
    </div>
"""
    
    # print(head+creator_data+foot)
    return head_html+head+creator_data+foot

# render_templates(temp.head_html, temp.foot, "hi","https://www.youtube.com/embed/U7e7iUhBLLg?si=Qd4wUdAerEpFCdNz","1")
for idx,creator in enumerate(video_list):
    rendered_html = render_templates(temp.head_html, temp.foot, name_list[idx], creator, desc_list[idx], idx)

    with open(f"/Users/charliehernandez/Desktop/SI339/si339_indiv_proj-main/creator_pages/creator{idx}.html",'w') as fh:
        fh.write(rendered_html)