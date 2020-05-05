from youtube import get_recent_videos as get_youtube
from navertv import get_recent_videos as get_navertv
import pandas as pd
import os

print("Checking for new videos of ohmygirl ...")
path = os.getcwd()+ "/chromedriver.exe"
path = path.replace("\\","/")
#path = 'C:/Users/mgmgj/Documents/chromedriver.exe'

youtube_list = get_youtube(path)
navertv_list = get_navertv(path)

try:
    youtube = pd.DataFrame(youtube_list)
    youtube.columns = ["title", "link"]
    youtube.to_html("오마이걸_유튜브.html")

    navertv = pd.DataFrame(navertv_list)
    navertv.columns = ["title", "link"]
    navertv.to_html("오마이걸_네이버tv.html")

    print("Done! You can see html files in your directory.")
except:
    print('Error!')
