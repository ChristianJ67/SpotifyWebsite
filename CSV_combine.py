fout=open("SpotifyHistory2-6.csv","a")

for line in open("SpotifyHistory2.csv"):
    fout.write(line)
    
for num in range(3,6):
    f = open("SpotifyHistory"+str(num)+".csv")
    f._next_() # skip the header
    for line in f:
         fout.write(line)
    f.close() 
fout.close()

