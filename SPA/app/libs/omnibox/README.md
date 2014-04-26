omnibox
=======

omnibox stuff for lizard-nxt.
This directive dynamically loads templates from the service based on the type you feed it.

In production the html is compiled to js with html2js using [grunt-html2js](https://github.com/karlgoldstein/grunt-html2js)

Usage
-----

Add 'omnibox', to your app dependencies (in `bower.json`). In your AppCtrl scope change the `$scope.box.type` parameter to the type of box/template you want to open. The search template included in the repo is transcluded around the dynamically loaded template.

Development
-----------
If you want to add or break something or run the example:
* clone the repo
* install the dependencies with `bower install` in the cloned repo
* run a simple server like `python -m SimpleHTTPServer`
* break away
