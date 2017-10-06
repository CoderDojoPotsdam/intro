lightbot
========

From https://github.com/cdpoffline/lightbot

Update web page:

    rm -rf *.com lightbot.zip
    wget -c -N -p -k -D -H "lightbot.com,s3.amazonaws.com" "http://lightbot.com/flash.html"


If you do not find an swf file, please look into the flash.html file for .swf
and add the host name of the server to the list behind


Update zip file:

    rm -f lightbot.zip
    sudo apt-get install zip # debian
    zip -r -9 -o lightbot.zip *
