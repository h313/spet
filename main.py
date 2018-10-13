import sys
import spotipy
import spotipy.util as util

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
		print(playlist)
