import requests
import os
import urllib.parse


def convert_midi_to_mp3_bear(midi_file, mp3_file):
    upload_url = 'https://cts.ofoct.com/upload.php'
    convert_url = 'https://cts.ofoct.com/convert-file_v2.php'

    #Uploading midi to bearaudiotool
    with open(midi_file, 'rb') as f:
        files = {
            'myfile': (midi_file, f, 'audio/midi')
        }
        data = {}

        response = requests.post(upload_url, files=files, data=data)
        temp_file_name = response.text[2:-2]

    #Starting conversion process from midi to mp3
    if response.status_code == 200:
        print("Converting...")
        params = {
            'cid': 'midi2audio',
            'output': 'MP3,WAV,OGG,AAC,WMA',
            'tmpfpath': response.text[2:-2],  
            'row': 'file1',
            'sourcename': os.path.basename(midi_file),  
            'outformat': 'mp3', 
            'AudioQuality': '19',
            'AudioEncoder': '1',
            'AudioSamplingRate': '11',
            'AudioChannels': '1',
            'rowid': 'file1',
        }
        clickResponse = requests.get(convert_url, params=params)

        if clickResponse.status_code != 200:
            print(f"Failed to convert the file. Status code: {clickResponse.status_code}")
            return
    else:
        print(f"Failed to upload the file. Status code: {response.status_code}")
        return
          


    #Downloads the mp3
    file_name = urllib.parse.quote(os.path.basename(midi_file))

    download_url = f'https://cts.ofoct.com/get-file.php?type=get&genfpath=/tmp/{temp_file_name}.mp3&downloadsavename={file_name}.mp3'
    downloadResponse = requests.get(download_url)

    if (downloadResponse.status_code == 200):
        with open(mp3_file, 'wb') as f:
            f.write(downloadResponse.content)
    else:
        print(f"Failed to download the file. Status code: {downloadResponse.status_code}")


if __name__ == "__main__":
    midi_file = 'miditest/Mizore and Ririka Oboe Duet.mid'
    mp3_file = 'miditest/Mizore and Ririka Oboe Duet.mp3'

    convert_midi_to_mp3_bear(midi_file, mp3_file)