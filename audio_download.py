from video2audio import convert_video_to_audio_ffmpeg
from pydub import AudioSegment
from instascrape import Reel
import argparse
import pafy


parser = argparse.ArgumentParser()
parser.add_argument('--url', help='Video URL from youtube.')
parser.add_argument('--db', help='DBs to increase/decrease (optional)', default='')
parser.add_argument('--start', help='Mileseconds to start the audio (option)', default='')
parser.add_argument('--end', help='Mileseconds to start the end (option)', default='')
parser.add_argument('--session_id', help='Session ID for instagram (reels only, get from cookies)', default='')
parser.add_argument('--filepath',
 help='File name excluded the extensions eg "audio." (default is audio + extension). It can include path to store', 
 default='audio.'
)

args = parser.parse_args()
url = args.url
filepath = args.filepath.split('.')[0] + '.'
out_extension = 'mp3'


if url == None:
    raise Exception('URL missing from arguments.')

if 'https://www.youtube.com/' in url:
    video = pafy.new(url)
    
    bestaudio = video.getbestaudio()
    video_name = filepath + 'webm'   
    bestaudio.download(filepath=video_name)

else:
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    "cookie": f'sessionid={args.session_id};'
    }
    
    # Passing Instagram reel link as argument in Reel Module
    insta_reel = Reel(url)
    
    # Using  scrape function and passing the headers
    insta_reel.scrape(headers=headers)
    
    # Giving path where we want to download reel to the
    # download function
    video_name = filepath + 'mp4'   
    insta_reel.download(fp=video_name)

convert_video_to_audio_ffmpeg(video_file=video_name, output_ext=out_extension)

audio_ = AudioSegment.from_mp3(filepath + out_extension)
if (args.db != ''):
    db_add = float(args.db)
    audio_ += db_add
if args.end != '':
    audio_ = audio_[:int(args.end)]
if args.start != '':
    audio_ = audio_[int(args.start):]
audio_.export(filepath + out_extension)