import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb






with open('StreamingHistory2.json') as f:
    data = json.load(f)

result_list = data
artist_name_L = []
song_L = []
date_L = [] #time is in milliseconds


for result in result_list:
    artist_name = result["artistName"]
    artist_name_L.append(artist_name)
    
    track_name = result["trackName"]
    song_L.append(track_name)
    
    date_listened = result["endTime"]
    date_L.append(date_listened)
    

songs = pd.DataFrame (
    {"artistName": artist_name_L,
     "trackName": song_L,
     "endTime": date_L
     })

all_songs = songs.to_csv('History5.csv')




descending_order = ["artistName"].value_counts().sort_values(ascending=False).index
ax = sb.countplot(y = ["artistName"], order=descending_order)

sb.despine(fig=None, ax=None, top=True, right=True, left=False, trim=False)
sb.set(rc={'figure.figsize':(6,7.2)})

ax.set_ylabel('')    
ax.set_xlabel('')
ax.set_title('Songs per Artist in Top 50', fontsize=16, fontweight='heavy')
sb.set(font_scale = 1.4)
ax.axes.get_xaxis().set_visible(False)
ax.set_frame_on(False)

y = ['artistName'].value_counts()
for i, v in enumerate(y):
    ax.text(v + 0.2, i + .16, str(v), color='black', fontweight='light', fontsize=14)
    
plt.savefig('top50_songs_per_artist.jpg', bbox_inches="tight")







