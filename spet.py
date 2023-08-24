import sys
import os
import argparse

import spotipy
import spotipy.util as util
from parser import parse

scope = "playlist-read-collaborative"

def login(username) -> str:
	return util.prompt_for_user_token(
    	username,
    	scope,
    	client_id= os.getenv("SPOTIPY_CLIENT_ID"),
    	client_secret= os.getenv("SPOTIPY_CLIENT_SECRET"),
    	redirect_uri= os.getenv("SPOTIPY_REDIRECT_URI"),
	)


def get_commands_playlists(token, username, playlist_id):
	commands = []
	sp = spotipy.Spotify(auth=token)
	playlists = sp.user_playlists(username)

	playlist = next((p for p in playlists["items"] if p["id"] == playlist_id), None)
	if playlist:
		result_list = sp.user_playlist(
			username, playlist["id"], fields="tracks,next"
		)
		for i, item in enumerate(result_list["tracks"]["items"]):
			track = item["track"]
			commands.append(
				{
					"name": track["name"],
					"artist": track["artists"][0]["name"],
					"album": track["album"]["name"],
				}
			)
		parse(commands)
	else:
		print("Playlist not found")


def get_playlists(token, username):
	sp = spotipy.Spotify(auth=token)
	playlists = sp.user_playlists(username)

	for playlist in playlists["items"]:
		print(f"id: {playlist.get('id')} name: {playlist.get('name')}")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("username", help="spotify username")
	parser.add_argument("--display-playlists", help="display playlist", action="store_true")
	parser.add_argument("-p", "--playlist-id", help="playlist ID", type=str)

	args = parser.parse_args()

	if args.display_playlists:
		get_playlists(login(args.username), args.username)
		sys.exit()

	if args.playlist_id:
		get_commands_playlists(login(args.username), args.username, args.playlist_id)
		sys.exit()
