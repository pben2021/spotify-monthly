from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import string
from dotenv import load_dotenv   
import os 

load_dotenv()  
CLIENT_ID =  os.environ.get('client_id')
CLIENT_SECRET = os.environ.get('client_secret')

class SelectionError(Exception):
    def __init__(self, message, errors):            
        self.message = 'Selection argument not valid'
            
        def __str__(self):
            return self.message

#function to filter Streaming history to past year. returns data frame that meets time constraint
def timeFilter(df):
    df['endTime'] = pd.to_datetime(df['endTime'])  

    date = datetime.today()
    enddate = enddate = str(date.year-1) + '-' + str(date.month) + '-'+ '01'
    df = df[df['endTime'] >= enddate]
    with pd.option_context('mode.chained_assignment', None):
        df.drop(df[(df.artistName == "Unknown Artist") & (df.trackName == "Unknown Track")].index, inplace=True)
    
    return df

# #function to sort tracks by month + count frequency. returns tuple of dataframes per months
def sortMonth(df):
    jan=df[df['endTime'].dt.month == 1] 
    feb=df[df['endTime'].dt.month == 2]
    mar=df[df['endTime'].dt.month == 3]
    apr=df[df['endTime'].dt.month == 4]
    may=df[df['endTime'].dt.month == 5]
    jun=df[df['endTime'].dt.month == 6]
    jul=df[df['endTime'].dt.month == 7]
    aug=df[df['endTime'].dt.month == 8]
    sep=df[df['endTime'].dt.month == 9]
    oc=df[df['endTime'].dt.month == 10]
    nov=df[df['endTime'].dt.month == 11]
    dec=df[df['endTime'].dt.month == 12]

    jan = jan.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    feb = feb.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    mar = mar.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    apr = apr.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    may = may.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    jun = jun.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    jul = jul.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    aug = aug.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    sep = sep.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    oc = oc.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    nov = nov.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    dec = dec.groupby(["artistName", "trackName"])["endTime"].count().reset_index(name="frequency").sort_values("frequency",ascending=False)
    
    return jan, feb, mar, apr, may, jun, jul, aug, sep, oc, nov, dec


# function returns list of top15 for given month nad list of bottom15 per given month + image url for the tracks
def get15(month):
    month = month[month['frequency'] >2]
    month= month.values.tolist()
    top15 = []
    bot15 = []
    
    i=0 #iterator for position in month list
    #get top15, not including deleted tracks or podcasts
    while len(top15) < 15 and i < len(month):
        url = get_album_art(month[i][1],month[i][0])
        if url is not False:
            top15.append(month[i] + [url])
        i+=1
    
    i=-1
    if len(month) > 30:
        #get top15, not including deleted tracks or podcasts
        while len(bot15) < 15 and i*-1 < len(month):
            url = get_album_art(month[i][1],month[i][0])
            if url is not False:
                bot15.append(month[i] +[url])
            i-=1
    #just return everything after the first 15 songs if statement false
    else:   
        bot15 = month[15:]
        i=15
        while len(bot15) < 15 and i<len(month):
            url = get_album_art(month[i][1],month[i][0])
            if url is not False:
                bot15.append(month[i]+ [url])
            i+=1
    
    monthid = 0
    all30 = []
    for song in top15:
        month_dic = {'id':monthid, 'title':song[1], 'artist':song[0], 'url': song[3],'place':'top'}
        all30.append(month_dic)
        monthid+=1
    monthid = 0
    for song in bot15:
        month_dic = {'id':monthid, 'title':song[1], 'artist':song[0], 'url': song[3], 'place':'bot'}
        all30.append(month_dic)
        monthid+=1
    return all30


#returns json if selection == allMonths
def getMonthArt(df):
    monthName = ['january','february','march','april','may','june','july','august','september','october','november','december']
    
    data = []
    isTop = False
    i = 0
    monthid = 0

    for month in df:
        while not isTop and i < len(month): #make sure top song is not a podcast
            topsong =  month['trackName'].iloc[i]
            topartist = month['artistName'].iloc[i]

            url = get_album_art(topsong, topartist)
            if url is False:
                i+=1
                continue
            else: 
                data.append({'id':monthid, 'month':monthName[monthid], 'url':url})
                isTop = True
        i=0
        monthid+=1
        isTop = False
    return data

#function to filter podcasts & deleted tracks and get album/artist art. Returns False if not a track else, returns url
def get_album_art(name, artist):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))   
    remove = string.punctuation
    remove = remove.replace("-", "")
        
    name = name.translate({ord(char): None for char in remove})
    artist = artist.translate({ord(char): None for char in remove}) 

    try:
        results = spotify.search(q=name+' ' +'artist:'+ artist, type='track') #first search for artist and track
    except Exception:
        results = spotify.search(q=name, type='track') #if 404 NOT FOUND raised, search for just artist until track found
        for track in results['tracks']['items']:
            if track['artists'][0]['name'] == artist:
                return track['album']['images'][0]['url']
    except:
        return False
    items = results['tracks']['items']

    #if at least 1 result reurned, then it is song
    if len(items) > 0:
        artist = items[0]
        try:
            url = artist['album']['images'][0]['url']
        except:
            url = "https://img.freepik.com/free-vector/blue-pink-halftone-background_53876-99004.jpg?w=2000" 
    else: #not a song
        url = False
    return(url)

#MAIN FUNCTION that recieves the file names as input and returns a json for reactui to read            
def main(files, selection=None, month=None): 
    ''' FOR TESTING
    # files = input('Input file names(place comma between each json name. Must be in same folder): ') #get file names as input
    # files = files.split(",")
    # files = loadJSON(files)
    '''

    if len(files) > 0:
    #convert files (in form of jsons) to pandas dataframe for cleanup
        df = pd.DataFrame()
        for frame in files:
            df = pd.concat([df, pd.DataFrame.from_records(frame)])

        filtered = timeFilter(df)  #filter songs to only this past year
        allMonths = sortMonth(filtered) #tuple of sorted songs by month
        #return the json for top song for all months
        if selection == 'allMonths': 
            return getMonthArt(allMonths)
        
        #return json for top and bottom 15 songs for month
        elif selection == 'perMonth':
            month_to_id ={'january':0,'february':1,'march':2,'april':3,'may':4,'june':5,'july':6,'august':7,'september':8,'october':9,'november':10,'december':11}
            thisMonth = allMonths[month_to_id[month]]
            if len(thisMonth) == 0:
                return []
            return get15(thisMonth)
        else:
            raise SelectionError
    else: return

if __name__ == '__main__':
    main()
# StreamingHistory0.json,StreamingHistory1.json,StreamingHistory2 copy.json,StreamingHistory3 copy.json,StreamingHistory4.json