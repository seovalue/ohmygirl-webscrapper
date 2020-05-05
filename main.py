from youtube import get_recent_videos as get_youtube
from navertv import get_recent_videos as get_navertv
import pandas as pd
path = 'C:/Users/mgmgj/Documents/chromedriver.exe'

youtube_list = get_youtube(path)
navertv_list = get_navertv(path)

df = pd.DataFrame(youtube_list)
df.columns = ["title", "link"]
df.to_html("오마이걸_유튜브.html")


df = pd.DataFrame(navertv_list)
df.columns = ["title", "link"]
df.to_html("오마이걸_네이버tv.html")
