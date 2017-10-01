lightbot
========

From https://github.com/cdpoffline/lightbot

Update web page:

    rm -rf lightbot.com lightbot.zip
    wget -c -N -p -k "http://lightbot.com/flash.html"

Update zip file:

    rm -f lightbot.zip
    sudo apt-get install zip # debian
    zip -r -9 -o lightbot.zip lightbot.com
