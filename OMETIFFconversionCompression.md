## OME-TIFF conversion followed by compression

Pre-requisite: Jetraw UI compression is working in your environment.

Microscopy data formats are vendor-specific and often do not give direct access to tiff files. We combine bfconvert and Jetraw to achieve simultaneous file conversion and compression. The output is Jetraw-compressed OME-TIFF files.

### Setting up `bfconvert`

1. Download the Bio-Formats commandline tools, [bftools](https://www.openmicroscopy.org/bio-formats/downloads/). Match the Bio-Formats version with above (e.g. bftools.zip from [6.10.1](https://downloads.openmicroscopy.org/bio-formats/6.10.1/artifacts/) or [6.11.1](https://downloads.openmicroscopy.org/bio-formats/6.11.1/artifacts/)) to be on the safe side.
2. Install [Java Runtime](http://www.java.com).
3. (macOS only) To use the unix executable, change the permission in terminal via `chmod +x ./bfconvert`. 
4. Download and unzip the dataset [M44test](https://biocenterat-my.sharepoint.com/personal/keisuke_ishihara_imp_ac_at/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkeisuke%5Fishihara%5Fimp%5Fac%5Fat%2FDocuments%2FJetraw%5FVBCBioOptics&ga=1) or [CQ1test](https://pitt-my.sharepoint.com/:f:/g/personal/ishihara_pitt_edu/Evv0tv71q_tEqesE9icsRrMBDx-TMT8x5M08SQDYM55uWA?e=zPFdwI).
5. In command prompt or terminal, change directory to your bftools folder and enter the command

Windows:
```
.\bfconvert -series 0 C:\Users\ishihara\Downloads\M44test\myfile.vsi C:\Users\ishihara\Downloads\out\myfile-S%%sC%%c.tif
```

macOS:
```
./bfconvert -series 0 ~/Downloads/M44test/myfile.vsi ~/Downloads/out/myfile-S%sC%c.tif
```

The argument `-series 0` instructs bfconvert to skip the thumbnail image (series 1) in the VSI file. See [documentation](https://docs.openmicroscopy.org/bio-formats/6.10.1/users/comlinetools/conversion.html) for more options.

### Setting up `bfconvert` with Jetraw compression

1. Go to your bftools directory and replace *bioformats_package.jar* with a copy of the Jetraw proprietary version (restricted access links: [VBC](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx) and Ishihara lab).
2. In command prompt or terminal, enter the command

Windows:
```
.\bfconvert -compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304 -series 0 C:\Users\ishihara\Downloads\M44test\myfile.vsi C:\Users\ishihara\Downloads\out\myfile-S%%sC%%c.tif
```

macOS:
```
./bfconvert -compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304 -series 0 ~/Downloads/M44test/myfile.vsi ~/Downloads/out/myfile-S%sC%c.tif
```

You will find that M44test dataset shrinks from 607MB to 110MB. This is a ~82% reduction in file size!


## Utility scripts for batch compression

Pre-requisite: `bfconvert -compression Jetraw` is working in your environment.

To process all image files in a given directory, we will use a Python script that makes multiple calls of bfconvert.

*under development but ready for testing*

On command prompt or terminal:

```
python batch_bfconvertJetraw.py
```