conference
==========

Conference web-site


Additional static pages should be added to the /pages directory of the
appropriate conference directory.

These can be accessed by the link /<conf_id>/<page_name>

conf_id is a 2 letter code followed by the year.  (e.g. NY2012, SV2013)
page_name is the name of the html file WITHOUT the .html extension
page_name can include additional folder levels as long as the folder
exists in the pages folder of the conference 
(e.g. about/press = pages/about/press.html)

These pages are strictly static and will go into the main container of 
the basic website wrapped with the header, navmenu, sidebar, etc.

Dynamically created pages may extend wrapper.html and replace the {% block %}
sections.  


Additionally, it is possible to get the page content from a conference folder 
and wrap it in the style of a different conference  That will happen using:

/<conf_id>/<conf_style_id>/<page_name>

