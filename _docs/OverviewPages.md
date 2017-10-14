Overview Pages
==============

Overview pages are placed in the [root of this repository](..).
They contain a list of tutorials which fit a certain purpose.

The structure and content of such a page are divided:
Tutorials can be found in the [tutorials.yml file][tutorials.yml] with all
translations, descriptions and links.
The overview pages only describe the structure of the tutorials and which
tutorials to use.
This way all pages profit from translations and improvements of existing
tutorials.

When new tutorials appear, they need to be added to the overview page manually.
You can watch this repository for new tutorials.
If you want to add a new page, you can copy an existing one.

Properties of an overview page
------------------------------

All overview pages are [Jekyll pages][jekyll-page].
All configuration is written between the two `---` at the beginning of the file.

Here is a basic configuration of such a page which contains only the necessary
configuration for a page without tutorials.

```yaml
---
layout: overview
image: img/logos/CoderDojoDahlemLogo.png
title: "Page Title"
---
<h2>This is a test page.</h2>
```

- `layout: overview` tells Jekyll to use the [overview.html][overview.html].
  The overview.html page reads all the configuration and adds HTML around the
  description `<h2>This is a test page.</h2>`.
- `title: Page Title` is the page title. It is used for the header of the page.
- `image: img/logos/CoderDojoDahlemLogo.png` This is the path of the logo
  relative to the overview file.
  Please keep in mind that we want this page to also work in case of a bad
  internet connection, so consider adding the logo to the
  [images folder][logo-folder].

Tutorial Structure
------------------

Surely, you want to add tutorials at your overview page.
This is where the `structure` configuration comes into play.

Here is an example for an `overview` page.

```yaml
---
layout: overview
image: img/logos/CoderDojoPotsdam_logo-256.png
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

`structure` is the structure of the page.
Each element in the structure starts with a `-`.
and can be either

- a tutorial, which is marked by the tutorial id, e.g.
  ```yaml
  - lightbot
  ```
- a category, in which case the we write
  ```yaml
  - category: symbols
  ```
  Each category can have a `structure` attribute which allows to embed more tutorials or categories.
  This example opens the category `symbols` and adds the tutorial `lightbot`
  to it.
  ```yaml
  - category: symbols
    structure:
    - lightbot
  ```

[tutorials.yml]: ../_data/tutorials.yml
[jekyll-page]: TODO
[overview.html]: ../_layouts/overview.html
[logo-folder]: ../img/logos/
