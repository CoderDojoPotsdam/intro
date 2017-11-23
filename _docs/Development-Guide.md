Development Setup
=================

You want to change this code and see how your changes integrate into the website?
This setup tutorial should get you started and answer all questions.
If questions are still left or you notice uncertainty or work you did that
can make it easier for others, please edit this document.

Clone the Repository
--------------------

In order to work on the repository, you need the source code.

1. Install Git  
   - Ubuntu:
     ```
     sudo apt-get install git
     ```
   - Windows & Mac: [Github Desktop][github-desktop]
2. Clone the repository  
   ```
   git clone --origin upstream https://github.com/CoderDojoPotsdam/intro.git
   cd intro
   ```
Your intro folder should look like [this][branch-master].

Now, you are ready to build the site.
For the following commands to work, your command line should be in the
intro directory.

Install Ruby
------------

This site is a site which is not only HTML but also templates and variables,
to remove duplication in the HTML code and generate a static site.
Thus this page is generated and you can see the generated code at
[on the internet][site].

You will need to install Ruby.
You can get it from the [Downloads Page][download-ruby].
Please install it on your computer.

Install GitHub Pages
--------------------

In order to build the github pages, we use [Jekyll][jekyll] and install it as follows:

1. Install Bundler  
   Open your command line and execute the following command:
   ```
   gem install bundler
   ```
2. Install the packages  
   You can install all packages required for this site with the followind command.
   ```
   bundle install
   ```
   Note: You must be in the repository root next to the `Gemfile` in
   the command line to make this work.
   Your output should look like this:
   ```
    Fetching gem metadata from https://rubygems.org/...........
    Fetching version metadata from https://rubygems.org/..
    Fetching dependency metadata from https://rubygems.org/.
    Resolving dependencies...
    Using concurrent-ruby 1.0.5
    Using minitest 5.10.3
    Using thread_safe 0.3.6
    Using public_suffix 2.0.5
    Using bundler 1.15.4
    Using coffee-script-source 1.11.1
    Using execjs 2.7.0
    Using colorator 1.1.0
    Using ffi 1.9.18
    Using multipart-post 2.0.0
    Using forwardable-extended 2.6.0
    Using gemoji 3.0.0
    Using net-dns 0.8.0
    Using rb-fsevent 0.10.2
    Using kramdown 1.14.0
    Using liquid 4.0.0
    Using mercenary 0.3.6
    Fetching rouge 2.2.1
    Installing rouge 2.2.1
    Using safe_yaml 1.0.4
    Using mini_portile2 2.3.0
    Using jekyll-paginate 1.1.0
    Using jekyll-swiss 0.4.0
    Using unicode-display_width 1.3.0
    Fetching i18n 0.9.1
    Installing i18n 0.9.1
    Fetching tzinfo 1.2.4
    Installing tzinfo 1.2.4
    Using addressable 2.5.2
    Using coffee-script 2.4.1
    Fetching ethon 0.11.0
    Installing ethon 0.11.0
    Using rb-inotify 0.9.10
    Using faraday 0.13.1
    Using pathutil 0.16.0
    Using nokogiri 1.8.1
    Using terminal-table 1.8.0
    Using activesupport 4.2.9
    Using jekyll-coffeescript 1.0.2
    Using typhoeus 0.8.0
    Using sass-listen 4.0.0
    Using listen 3.0.6
    Using sawyer 0.8.1
    Using html-pipeline 2.7.1
    Fetching sass 3.5.3
    Installing sass 3.5.3
    Using jekyll-watch 1.5.0
    Using octokit 4.7.0
    Using jekyll-sass-converter 1.5.0
    Using github-pages-health-check 1.3.5
    Using jekyll-gist 1.4.1
    Fetching jekyll 3.6.2
    Installing jekyll 3.6.2
    Using jekyll-avatar 0.5.0
    Using jekyll-default-layout 0.1.4
    Using jekyll-feed 0.9.2
    Using jekyll-github-metadata 2.9.3
    Using jekyll-mentions 1.2.0
    Using jekyll-optional-front-matter 0.2.0
    Using jekyll-readme-index 0.1.0
    Using jekyll-redirect-from 0.12.1
    Fetching jekyll-relative-links 0.5.1
    Installing jekyll-relative-links 0.5.1
    Using jekyll-seo-tag 2.3.0
    Using jekyll-sitemap 1.1.1
    Using jekyll-titles-from-headings 0.4.0
    Using jemoji 0.8.1
    Using minima 2.1.1
    Using jekyll-theme-architect 0.1.0
    Using jekyll-theme-cayman 0.1.0
    Using jekyll-theme-dinky 0.1.0
    Using jekyll-theme-hacker 0.1.0
    Using jekyll-theme-leap-day 0.1.0
    Using jekyll-theme-merlot 0.1.0
    Using jekyll-theme-midnight 0.1.0
    Using jekyll-theme-minimal 0.1.0
    Using jekyll-theme-modernist 0.1.0
    Using jekyll-theme-primer 0.5.2
    Using jekyll-theme-slate 0.1.0
    Using jekyll-theme-tactile 0.1.0
    Using jekyll-theme-time-machine 0.1.0
    Fetching github-pages 169
    Installing github-pages 169
    Bundle complete! 1 Gemfile dependency, 75 gems now installed.
    Use `bundle info [gemname]` to see where a bundled gem is installed.
   ```

Build the Site
--------------

Ruby and all required ruby packages are installed.
Now, you are ready to build the website.

```
jekyll serve --trace
```
The output should look like this:
```
Configuration file: /home/user/intro/intro/_config.yml
            Source: /home/user/intro/intro
       Destination: /home/user/intro/intro/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
                    done in 0.114 seconds.
 Auto-regeneration: enabled for '/home/user/intro/intro'
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
```

Now, you can browse the website at [localhost:4000][local].
A `_site` directory is created where you can view the current build of the site.
Once you make a change, the site automatically rebuilds.

Build the Offline Site
----------------------

Some tutorials have offline content enabled if it is available.
You can make it available by cloning the `offline` branch.

1. Create a directory `_site/offline`  
   ```
   mkdir -p _site/offline
   ```
2. Add this repository to the `_site/offline` folder
   ```
   git clone --origin upstream --branch offline https://github.com/CoderDojoPotsdam/intro.git _site/offline
   ```

Now, if you serve the page on [localhost:4000][local],
and refresh it, you should be able to see additional offline links.

Prepare for Your Contributions
------------------------------

We would like to make it easy for you to contribute changes to this
repository.
To get started, you will need to know Git basics which you can learn in about
[15 Minutes with this Git tutorial][try-git].
You can take the time now and the following will look less like magic.

To start contributing, please [fork the repository][fork] to your user account.
I assume, you are in the `intro` folder.
Then, use the following command to allow synchronization with your fork.
Please replace `CoderDojoPotsdam` with your github username.
```
git remote add origin https://github.com/CoderDojoPotsdam/intro.git
git remote add ssh git@github.com:CoderDojoPotsdam/intro.git
```
You can do the same to the `offline` version:
```
cd _site/offline
git remote add origin https://github.com/CoderDojoPotsdam/intro.git
git remote add ssh git@github.com:CoderDojoPotsdam/intro.git
cd ../..
```

Contribute a Change
-------------------

You have edited a file of the site and wish to distribute the changes.


1. Checkout the branch you want to contribute to and update it.
   In this case, it is the `master` branch.
   ```
   git checkout master
   git pull upstream master
   ```
   This also works with feature branches.
2. Create a branch
   ```
   git checkout -b name-of-the-feature-i-want-to-contribute
   ```
3. Add the files
   ```
   git add .
   ```
4. Commit the changes with a message explaining **what** you did and **why** you
   did it.
   ```
   git commit -m'Problem: XY is wrang because ...

   Solution: ABC addresses this problem because ...'
   ```
5. Push the changes to your fork
   ```
   git push --set-upstream origin name-of-the-feature-i-want-to-contribute
   ```
6. [Compare your changes across forks][compare] and create a pull-request.
   The team wants to review, give feedback and thank you within 3 days.

That is what it takes to contribute.

Activate Github Pages
---------------------

In case you want us to review a huge change with one click, you can
add the Github Pages funcitonality to your fork.

To do this, enter the Settings of your repository.
Then, scroll down to view GitHub Pages.
Activate the Github Pages for the master branch.
After a while, when the build is done, you can view your site under
https://YourUserName.github.io/intro
(This works if you just forked and did not rename the repository, so the
  fork is still called `intro`.)

Activate Travis
---------------

Every pull-request you make will be checked by [Travis][travis].
In general, there is no need for you to activate it for your fork.

If you like to activate it for your fork, you can do so.
Questions can be answered and you can edit this document to make clear how to
do that.

Community
---------

Have fun developing.
We are here to answer your questions.
You can get in contact over the [issues][issues] if you like to work on
something specific.
However, if you just want to hang out and have a nice time,
please [chat with us][chat].

[site]: https://CoderDojoPotsdam.GitHub.io/intro
[download-ruby]: https://www.ruby-lang.org/en/downloads/
[local]: http://localhost:4000
[jekyll]: https://jekyllrb.com/
[github-desktop]: https://desktop.github.com/
[branch-master]: https://github.com/CoderDojoPotsdam/intro/tree/master
[fork]: https://github.com/CoderDojoPotsdam/intro/fork
[try-git]: https://try.github.io
[compare]: https://github.com/CoderDojoPotsdam/intro/compare
[issues]: https://github.com/CoderDojoPotsdam/intro/issues
[chat]: https://gitter.im/CoderDojoPotsdam/intro
[travis]: https://travis-ci.org/CoderDojoPotsdam/intro
