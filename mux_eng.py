import sys
import os
import subprocess

import meta
import upload_video


def usage_and_exit():
    print("""mux eng/rus audio files into a Goswami Maharaj's video
usage: mux "yyyy-mm-dd goswamimj.mp4"
(or drag and drop the file onto me)""")
    exit()

def mux_eng(filename):
    eng_mp4 = meta.get_work_filename(filename, ' eng.mp4')
    cmd = ['ffmpeg', '-y',
           '-i', filename,
           '-c', 'copy',
           '-movflags', '+faststart']
    cmd += meta.ffmpeg_meta_args(filename)
    cmd += meta.get_ss_args(filename)
    cmd += [eng_mp4]
    subprocess.run(cmd, check=True)

    title = meta.get_youtube_title_eng(filename)

    description = meta.get_youtube_description_eng(filename)

    upload_video.upload(eng_mp4, title=title, description=description)


def main():
    try:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('file "%s" not found' % filename)
            print('')
            usage_and_exit()
        mux_eng(filename)
    except IndexError:
        usage_and_exit()

if __name__ == '__main__':
    main()
