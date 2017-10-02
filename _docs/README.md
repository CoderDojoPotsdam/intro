# Documentation

This documentation should clarify how to do what you want with this repository.
If it does not appear here, [please create an issue and ask][new-issue].

## How to create add a tutorial

If you want to add a tutorial to the page, you can [edit][edit-tutorials] the [tutorials.yml][tutorials] file.
Each tutorial must have the following attributes:

```yaml
lightbot:
  title: Lightbot
  description: Control a robot and help it light the ground.
  url: http://lightbot.com/hour-of-code.html
  links:
  - name: Online
    url: http://lightbot.com/flash.html
  - name: iOS
    url: http://lightbot.com/redirect-ios-codehour.html
  - name: Android
    url: http://lightbot.com/redirect-android-codehour.html
  categories:
  - symbols
  - hour-of-code
  - offline
```

Additionally, some attributes can be translated:

```yaml
lightbot:
  title:
    en: Lightbot
    de: Lightbot
  description:
    en: Control a robot and help it light the ground.
    de: Steuere einen Roboter und hilf ihm, die Karte anzuleuchten.
  url:
    en:http://lightbot.com/hour-of-code.html
    de: http://lightbot.com/hour-of-code.html
  links:
  - name:
      en: online
      de: Online
    url:
      en: http://lightbot.com/flash.html
      de: http://lightbot.com/flash.html
  # ...
  categories:
  - symbols
  - hour-of-code
  - offline
```

## How to transtlate

If you like to translate a tutorial to different languages,
first, check that your language is in the [list of languages][languages]. If not, add it.
Then, you can translate [tutorials][tutorials] and

## How to add a web page

If you want to add a new page, you can copy an existing one.
Here is an example for an `overview` page.

```yaml
---
layout: overview
image: https://raw.githubusercontent.com/CoderDojoPotsdam/organize/master/logo/logo-256.png
title: CoderDojo Potsdam
structure:
- category: symbols
  structure:
  - lightbot
  - spritebox
  - scratchjr
- category: blocks
  structure:
  - blockly
  - code.org
---
```

The `image` is a link to an image which should be used to display the logo of the page.
`title` is the title of the page.
`structure` is te structure of the page.
Each element in the structure starts with a `-`.
Each element in the structure can be either

- a tutorial, which is marked by the tutorial id, e.g.
  ```yaml
  - lightbot
  ```
- a category, in which case the we write
  ```yaml
  - category: symbols
  ```
  Each category can have a `structure` attribute which allows to embed more tutorials or categories.
  This example opens the category "symbols" and adds the tutorial `lightbot` to it.
  ```yaml
  - category: symbols
    structure:
    - lightbot
  ```


## How to use the offline version

This website also has an offline version.
The offline version is updated by [travis][travis] and can be accessed via the [offline-build branch][offline-build].

You can download the [offline version][offline-build-download].
You can extract it, store it e.g. on a USB device or serve it via a webserver.

To keep your local copy updated, you can install git.
Then, you clone the repository once:

    git clone --branch offline-build https://github.com/CoderDojoPotsdam/intro.git

Everytime you want to update the local copy, run

    git pull

## How to build the offline version

You can build the offline version.
To clone the offline material, execute this command:

`git clone --branch offline https://github.com/CoderDojoPotsdam/intro.git _site/offline`

Then, you can run the jekyll command to build and serve the offline website:

`jekyll serve --trace`

Now, your webpage should be available at http://localhost:4000/.
Notice that some additional links appear which are only available as offline verison.

## How to add offline content

Offline links are supported in the `links` section of a tutorial.
If your links look like this:

```yaml
links:
- name: Online
  url: http://lightbot.com/flash.html
```

You can also add an offline link to a file stored in the
[offline branch][offline-branch].
Offline links are only displayed if the offline verison is generated, see above.

Here, you can see that we add an offline link
to the [lightbot/index.html][offline-branch-lightbot] file:
```yaml
  links:
  - name: Online
    url: http://lightbot.com/flash.html
  - name: Offline
    url: offline/lightbot/index.html
    offline: true
```

[new-issue]: https://github.com/CoderDojoPotsdam/intro/issues/new
[edit-tutorials]: https://github.com/CoderDojoPotsdam/intro/edit/master/_data/tutorials.yml
[tutorials]: https://github.com/CoderDojoPotsdam/intro/blob/master/_data/tutorials.yml
[languages]: https://github.com/CoderDojoPotsdam/intro/blob/master/_data/languages.yml
[offline-build]: https://github.com/CoderDojoPotsdam/intro/tree/offline-build
[offline-build-download]: https://github.com/CoderDojoPotsdam/intro/archive/offline-build.zip
[travis]: https://travis-ci.org/CoderDojoPotsdam/intro/
[offline-branch]: https://github.com/CoderDojoPotsdam/intro/tree/offline
[offline-branch-lightbot]: https://github.com/CoderDojoPotsdam/intro/blob/offline/lightbot/index.html
