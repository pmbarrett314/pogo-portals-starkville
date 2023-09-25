# pogo-portals-starkville
Data for the pokemon go stops and gyms in starkville

## Setup

0. Have an Ingress account and know how to log in to the online intel map.
1. Install IITC-CE per the instructions at https://iitc.app/download_desktop.html
    * Any of the methods should be fine, I just switched from Tampermonkey to the IITC Button.
2. Install the Pogo plugin per the instructions at https://gitlab.com/NvlblNm/pogo-s2/
    * You should just be able to click [here](https://gitlab.com/AlfonsoML/pogo-s2/raw/master/s2check.user.js?inline=false)
3. Open the ingress intel map and configure the plugin as desired by going to `PoGo Settings`
    * I recommend showing level 14 and 17 cells as these are the ones that are relevant for Pokemon Go gyms and portals.
    * I check all of "Highlight Cells that might get a Gym", "This is PoGo!", and "Analyze Portal Data"
4. Load the data by going to `PoGo Actions` > `Import Gyms and Pokestops`, and selecting the `gyms_stops.json` file from this repo and refreshing the page

## Contributing
If you'd like to add data for stops/gyms in the Starkville/MSU/Golden Triangle area, do the following:

0. Have done the things in Setup. Also have a github account and basic familiarity with git and Github.
1. Mark the new gyms and stops in the pogo plugin interface.
2. Export your data by going to `PoGo Actions` > `Export Gyms and Pokestops`
3. Move the file into the root of this repo and rename it `gyms_stops.json`
4. Run the `sort_json.py` script on the `gyms_stops.json` file. This should make it where the json file is something that git can handle the differences in pretty easily.
    * From the command line, you should be able to navigate into the repository and type `./sort_json.py gyms_stops.json`
5. Commit and make a pull request as normal and I'll merge it.
