rem http://streamripper.sourceforge.net/
"C:\Program Files (x86)\Streamripper\streamripper.exe" http://hyades.shoutca.st/tunein/tms.pls -u "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36" -A -a
REM http://hyades.shoutca.st/tunein/tms.pls
REM http://hyades.shoutca.st:8350/listen.pls?sid=1
rem http://hyades.shoutca.st:8350/index.html?sid=1
REM   -a [file]      - Rip to single file, default name is timestamped
REM   -A             - Don't write individual tracks
rem sleep $(($(date -d 14:30 +%s)-$(date +%s))) && while :; do "C:\Program Files (x86)\Streamripper\streamripper.exe" http://hyades.shoutca.st/tunein/tms.pls -u "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36" -A -a; sleep 15; done
