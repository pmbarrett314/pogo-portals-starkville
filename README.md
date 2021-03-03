# pogo-portals-starkville
Data for the pokemon go stops and gyms in starkville

## Setup
### This is a little out of date since IITC updated.

0. Have an Ingress account and know how to log in to the online intel map.
1. Install a userscript manager extension for your browser.
    * [Tampermonkey Firefox](https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/)
    * [Greasemonkey Firefox](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/)
    * [Tampermonkey Chrome](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en)
2. Install [IITC](https://iitc.me/desktop/) (Ingress Intel Total Conversion) to your userscript manager. It's a script that modifies the ingress intel map in various ways, including allowing for other plugins.
    * [Click here to install](https://static.iitc.me/build/release/total-conversion-build.user.js)
3. Click the icon for your userscript manager extension and go to the dashboard. Edit "IITC: Ingress intel map total conversion. Add the following lines at the top near the lines that look similar.
```
// @include        http://intel.ingress.com/*
// @include        https://intel.ingress.com/*
// @match          http://intel.ingress.com/*
// @match          https://intel.ingress.com/*
```
4. Install the [IITC Pokemon Go plugin](https://github.com/TiagoDGomes/iitc-plugin-pogo). It adds the ability to mark Pokemon Go portals and Gyms on the ingress intel map.
    * [Click here to install](https://github.com/TiagoDGomes/iitc-plugin-pogo/raw/master/iitc-plugin-pogo.user.js)
5. Open the ingress intel map and configure the plugin as desired by going to `PoGo Settings`
    * I recommend showing level 14 and 17 cells as these are the ones that are relevant for Pokemon Go gyms and portals.
    * I check all of `Highlight Cells that might get a Gym`, `Highlight centers of Cells with a Gym`, and `Hide Ingress Portal Details`
6. Load the data by going to `PoGo Actions` > `Import Pogo`, and selecting the `gyms_stops.json` file from this repo and refreshing the page

## Contributing
If you'd like to add data for stops/gyms in the Starkville/MSU/Golden Triangle area, do the following:

0. Have done the things in Setup. Also have a github account and basic familiarity with git and Github.
1. Mark the new gyms and stops in the pogo plugin interface.
2. Export your data by going to `PoGo Actions` > `Export Pogo`
3. Move the file into the root of this repo and rename it `gyms_stops.json`
4. Run the `sort_json.py` script on the `gyms_stops.json` file. This should make it where the json file is something that git can handle the differences in pretty easily.
    * From the command line, you should be able to navigate into the repository and type `./sort_json.py gyms_stops.json`
5. Commit and make a pull request as normal and I'll merge it.
