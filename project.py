import csv


artists = []
with open('Top50.csv', mode='r', encoding="utf8") as f:
    for l in f.readlines():
        mylist = l.split(",")
        row_name = mylist[0]
        track_name = mylist[1]
        time = mylist[2]
        artists.append({'Artist':row_name, 'Song' : track_name})
    artistname = []
    for x in range(9):
        artistname.append(artists[x]["Artist"])
    print(artistname)

    songname = []
    for x in range(9):
        songname.append(artists[x]["Song"])
    print(songname)

    dictionary = []
    for x in range(9):
        dictionary.append({artistname[x] : songname[x] })
    print(dictionary)

