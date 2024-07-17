console.log('Hello');

const lyricsDiv = $('.lyrics');

$.get('https://api.lyrics.ovh/v1/Coldplay/Adventure_of_a_lifetime')
  .then((data) => {
    console.log(data);
    const lyricsText = data.lyrics;

    lyricsDiv.append(lyricsText);
  })
  .catch((e) => {
    lyricsDiv.append(e.statusText);
  });

console.log('BYE');
