server
======

The server served the [offline-build branch][offline-build].
If it runs locally, this allows the [intro] page to serve offline content.

[offline-build]: https://github.com/CoderDojoPotsdam/intro/tree/offline-build
[intro]: https://coderdojopotsdam.github.io/intro/

Installation
------------

If you want to install the server, you will need to have Python 3 and the
corresponding pip installer.
Under Ubuntu, do the following:

    sudo apt-get install python3 pip-python3

To install the offline server, do this:

    pip3 install https://github.com/CoderDojoPotsdam/intro/archive/server.zip

Note that you might want to use the `--user` switch if you do not have
administrator rights.

Also, either download or clone the offline version of the website.

- [Download]
- Clone: `git clone --branch offline-build https://github.com/CoderDojoPotsdam/intro.git`

Run the server
--------------

In order to run the server, you can use this command after installation:

    python3 -m intro_offline_server path/to/intro

This gives the following output:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Development
-----------

If you like to develop on this server, you can install `virtualenv`

    pip3 install --user virtualenv

Setup your python environment:

    virtualenv -p python3 ENV
    source ENV/bin/activate
    pip install -r requirements.txt

If you add a new package to requirements.txt, also run this command:

    pip install pip-tools
    pip-compile requirements.txt
