### Karat Sleuth presentation

This is for our Software Evolution presentation regarding large commits made to github, 
as well as our size metrics tool developed in pythin. The presentation written in markdown and
rendered as a presentation using [Reveal.js](https://github.com/hakimel/reveal.js).

#### Editing

For a basic overview of markdown see [John Gruber's
documentation](http://daringfireball.net/projects/markdown/). Though the
[markdown parser](https://github.com/chjj/marked) reveal.js uses actually
supports quite a few more extensions.

You will want to edit the `presentation.md` file. Each slide is separated by
two empty lines. 

For an example of a markdown presentation check out any of Dr.Collards notes,
or [my first SEV
presentation](https://github.com/EvanPurkhiser/Presentations/blob/gh-pages/presentations/04-09-13-SEV-software-aging.md).

#### Viewing the presentation

The easiest way to view the presentation is to use pythons built in HTTP
server.

````sh
$ cd presentations
$ python -m SimpleHTTPServer
Serving HTTP 0.0.0.0 port 8000 ...
```

Then in a web browser load <http://localhost:8000/presentation.html>. If your
changes don't show up as you're editing the presentation then you may have to
clear you're cache or do a hard refresh.

#### Other Themes

If anyone on the team is insterested, we could use a different reveal.js theme. Check them out [here](http://lab.hakim.se/reveal-js/#/themes).
