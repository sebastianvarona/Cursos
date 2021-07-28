import 'dart:io';

const List songs = [
  {
    'artist': 'Generic Artist1',
  },
  {
    'artist': 'Generic Artist1',
  },
  {
    'artist': 'Generic Artist2',
  },
  {
    'artist': 'Generic Artist3',
  },
  {
    'artist': 'Generic Artist3',
  },
  {
    'artist': 'Generic Artist4',
  },
  {
    'artist': 'Generic Artist5',
  },
  {
    'artist': 'Generic Artist6',
  },
  {
    'artist': 'Generic Artist7',
  },
  {
    'artist': 'Generic Artist8',
  }
];

const List playlists = [
  {'name': 'Favourites', 'sonNum': '140'},
  {'name': 'Latin', 'sonNum': '67'},
  {'name': 'Rock', 'sonNum': '56'},
  {'name': 'Trap', 'sonNum': '98'},
  {'name': 'House', 'sonNum': '54'},
  {'name': 'Pop', 'sonNum': '98'},
  {'name': 'Electro', 'sonNum': '140'},
  {'name': 'Reggae', 'sonNum': '67'},
  {'name': 'Soul', 'sonNum': '56'},
  {'name': 'Dubstep', 'sonNum': '54'}
];

List artists = List.generate(songs.length, (index) {
  return songs[index]['artist'];
});
var cArtists = artists.toSet();

main(List<String> args) {
  print(songs[1]['artist']);
  print(artists);
  print(cArtists);
}
