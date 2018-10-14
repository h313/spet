# About
`spet` is an interpreter for a turing-complete programming language loosely based off of brainfuck based on Spotify playlists.

## Language Definition
The interpreter reads the playlist from the top down. Various attributes of the song, sorted in terms of importance, defines the behaviours of the songs. The data land is a list of 40000 bytes, which can be navigated through with a pointer. From top down, the songs evaluate to:
 
### Print Character
Any song from RADWIMPS' album `Your Name.` prints the character at the pointer location.

### Input Character
Any song by Coldplay grabs input from `stdin` depending on the number of letters in the first word of the song. For example, A Sky Full of Stars will take only the first letter of whatever input is in `stdin` and write it to the location of the pointer. However, Yellow will take the first six letters of `stdin` and write it, starting at the pointer location. The pointer stays at its position befure the input is called.

### Moving the pointer
Any song by Radiohead moves a pointer forward by `1` byte, while any song by Green Day moves a pointer back `1` byte.

### Incrementing and Decrementing a value
Any song from the Muse album `Drones` will decrement the value at the pointer by `1`, while any song from the Muse album `Origin of Symmetry` increments the value at the pointer by `1`. Decrementing causes the value to wrap around, so decrementing a `0` results in a `255`, while incrementing a `255` results in a `0`.

### Loops
If a song contains the word `Run` in its name, and if the data at the pointer is `0`, the program jumps forward to the song directly following the next song containing the word `Talk` in its name. If a song contains the word `Talk` in its name, and if the data at the pointer is nonzero, the program jumps back to the song directly in front of the nearest song containing the word `Run`.

### Setting values
If a song's album's first word has length less than 5, and does not satisfy any of the above definitions, the data at the pointer is set to the first character of the next song.

## Setup
`spet` requires a Spotify premium account to connect with the API. To set up `spet`'s interpreter, clone the repo and do a `pip install -r requirements.txt`. Then, [create a Spotify API key](https://developer.spotify.com/dashboard/applications) and set the redirect URL to something like `http://localhost:8888/callback`.

To run `spet`, `cd` into the `spet` directory and run `python3 main.py <username> <playlist_uri>`. The playlist URI can be found on the Spotify app's Share button, and looks something like `7hShQSKY5AU0YQaN833iEx`.
