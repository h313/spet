import sys
import spotipy
import spotipy.util as util
from parser import parse

commands = []

if len(sys.argv) > 2:
	playlist_id = sys.argv[2]
	username = sys.argv[1]
else:
	print("Usage: %s username playlist_id")
	sys.exit()

token = util.prompt_for_user_token(username,'playlist-read-collaborative')

if token:
	sp = spotipy.Spotify(auth=token)
	playlists = sp.user_playlists(username)
	for playlist in playlists['items']:
		if playlist_id == playlist['id']:
			result_list = sp.user_playlist(username, playlist['id'],
				fields="tracks,next")
			for i, item in enumerate(result_list['tracks']['items']):
				track = item['track']
				commands.append({'name': track['name'],
					'artist': track['artists'][0]['name'],
					'album': track['album']['name']})

parse(commands)