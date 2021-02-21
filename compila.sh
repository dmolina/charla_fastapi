python -m http.server 8100 >/dev/null
(ls *fast.md | entr pandoc -t revealjs *fast.md -s -o index.html --css=custom.css -V revealjs-url=https://unpkg.com/reveal.js@3.9.1/) &
