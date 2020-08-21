# OctoPrint-CustomBackground

OctoPrint plugin to change the background image on the temperature graph.

![screenshot](screenshot.png)

![screenshot](settings.png)

### Setup

Install via the bundled Plugin Manager or manually using this URL:

https://github.com/jneilliii/OctoPrint-CustomBackground/archive/master.zip

### Configuration

Once installed upload image into the local storage and the page will refresh automatically with new background. Once refreshed you can delete the uploaded image and it will not impact the background. Adjust Image Fill method and [Background Position](https://www.w3schools.com/cssref/pr_background-position.asp) in Custom Background settings as needed.

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
  * Added gif image support.
* Version 0.6.0 released 09/17/2017
  * Removed url field in favor of file upload method.
  * Uploaded file is copied into plugin's data folder, files can now be deleted without impacting the background.
  * Uses routes hook to map plugin's data folder for loading copied image.
* Version 0.7.0 released 10/17/2017
  * Added background position settings.
* Version 0.8.0 released 12/09/2017
  * Changed url to include full url to deal with issues related to X-Script-Name redirects in haproxy to multiple OctoPrint instances.
* Version 0.9.0 released 03/24/2018
  * Added ability to change branding icon. File uploaded must be named "icon".
* Version 0.10.0 released 04/13/2018
  * Added reset button to put the interface back to stock.
  
### To-Do
* [X] Figure out how to upload a custom file to the system in lieu of using a url.
* [X] Figure out how to automatically refresh page after file upload.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker by clicking issues above.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Sponsors
- Andreas Lindermayr
- [@Mearman](https://github.com/Mearman)
- [@TxBillbr](https://github.com/TxBillbr)
- Gerald Dachs
- [@TheTuxKeeper](https://github.com/thetuxkeeper)
- @tideline3d

###

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
