# OctoPrint-CustomBackground

OctoPrint plugin to change the background image on the temperature graph.

![screenshot](screenshot.png)

![screenshot](settings.png)

Once installed upload files into the local side (not SD) and the page will refresh with no background or set url in settings to an address of an image you want to use.

### Setup

Install via the bundled Plugin Manager or manually using this URL:

https://github.com/jneilliii/OctoPrint-CustomBackground/archive/master.zip

### Changelog

* Version 0.1.0 released 08/27/2017
  * Initial release
* Version 0.2.0 released 08/27/2017
  * Added the ability to upload images (jpg,bmp,png) via OctoPrint's Files area.
* Version 0.3.0 released 09/01/2017
  * Fixed sizing of image to cover the entire temp_graph div.
  * Added preprocessor to automatically update plugin settings on file upload.
* Version 0.4.0 released 09/01/2017
  * Added automatic reload of page.
* Version 0.5.0 released 09/01/2017
  * Added image fill options to settings to control the css backgroiund-size property.
  
### To-Do
* [X] Figure out how to upload a custom file to the system in lieu of using a url.
* [X] Figure out how to automatically refresh page after file upload.
