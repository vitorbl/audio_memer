# youtube_dl

Download, trim and increase/decrease volume from YouTube audios.

```
python audio_download.py --url "https://www.youtube.com/watch?v=AUU_YHWCRWQ" --db "32" --end "1000"
```

This command will download the audio from [this video](https://www.youtube.com/watch?v=AUU_YHWCRWQ), then store in a file named audio.webm (for better audio), increase it by 32 decibels and make it end at 1000 mileconds.


It's also possible to download audios from reels. You must then include a Session ID, which is accountable in the cookies.

Also there is an issue regarding reels download. It tends to fail if you left the trailing backslash at the end of the url.