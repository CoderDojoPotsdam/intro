# Documentation

This documentation should clarify how to do what you want with this repository.
If it does not appear here, [please create an issue and ask][new-issue] or join our [chat on gitter][gitter] to get help.

- Here, you can find guidance on how to change the content.
  - [In the Overview Section][overview-pages], you can read about how to
    customize this overview for your needs and create a new page.
- [The Development Guide][dev-guide] guides you through setup and contribution,
  teaching all you need to know.
- [In the Branches.md file][branches], you find a descriptive overview about the
  structure of this repository.

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

## How to add offline content to a tutorial

Offline links are supported in the `links` section of a tutorial.
If your links look like this:

```yaml
links:
- name: Online
  url: http://lightbot.com/flash.html
```

You can also add an offline link to a file stored in the
[offline branch][offline-branch].
Offline links are only displayed if the offline version is generated, see above.

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

### How to add offline content

The website works without any offline content.
Just some links are not displayed.
Offline content is optional:
If the content of the [offline branch][offline-branch] is in a folder named `offline`
next to the [index.html file][index-file], the website notices that there is offline content and
displays it.

To add the content to the offline branch and make it available for offline usage,
you need to modify the  [`offline` branch][offline-branch] by first checking out the branch.

    git checkout offline

Then, you add your new content:

- Create a new folder.
- Create a README.md file which describes what you did to create the folder.  
  This should include download links, context information, scripts, ... .
  The goal is to update this after some years when you are not around,
  so please add everything you can to describe what you did and where you got this from.
- Add the necessary files.  
  Sometimes, you add many files. In this case, it might be wise to put them into a new folder next to your README.md file.
  This way, they can be easily deleted and updated.
- If you like to create an `index.html` file which redirects to other files, you can copy and modify the file from
  the [lightbot offline folder][lightbot-index].

You can also have a look at the other content in the [offline branch][offline-branch] to find inspiration.


[new-issue]: https://github.com/CoderDojoPotsdam/intro/issues/new
[edit-tutorials]: https://github.com/CoderDojoPotsdam/intro/edit/master/_data/tutorials.yml
[tutorials]: https://github.com/CoderDojoPotsdam/intro/blob/master/_data/tutorials.yml
[languages]: https://github.com/CoderDojoPotsdam/intro/blob/master/_data/languages.yml
[offline-build]: https://github.com/CoderDojoPotsdam/intro/tree/offline-build
[offline-build-download]: https://github.com/CoderDojoPotsdam/intro/archive/offline-build.zip
[travis]: https://travis-ci.org/CoderDojoPotsdam/intro/
[offline-branch]: https://github.com/CoderDojoPotsdam/intro/tree/offline
[offline-branch-lightbot]: https://github.com/CoderDojoPotsdam/intro/blob/offline/lightbot/index.html
[gitter]: https://gitter.im/CoderDojoPotsdam/intro
[branches]: Branches.md
[index-file]: ../index.html
[lightbot-index]: https://github.com/CoderDojoPotsdam/intro/blob/offline/lightbot/index.html
[overview-pages]: OverviewPages.md
[dev-guide]: Development-Guide.md
