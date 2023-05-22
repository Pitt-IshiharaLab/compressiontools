# compressiontools
 
This repository contains scripts and instructions for applying [Jetraw image compression](https://www.jetraw.com) to microscopy data. The repository is maintained by the Ishihara lab at the University of Pittsburgh and serves as an internal resource for the lab and its collaborators. While we make this repository publicly available, request for technical support should be directed to [Jetraw staff](https://www.jetraw.com/contact).


## About Jetraw

[Jetraw image compression](https://www.jetraw.com) achieves ~80% reduction of file size with essentially no loss of image quality thanks to its *metrologically correct* compression algorithm. (see [Technology](https://www.jetraw.com/jetraw-technology))

**Jetraw can only compress images from sCMOS cameras.** Thus, Jetraw compression is applicable to most modern widefield, lighsheet, and spinning disc confocal microscopes, but NOT applicable to detector-based systems such as scanning confocal and multiphoton microscopes.

Opening Jetraw images is free, while **image compression requires a software license and a hardware specific parameter file**.


## Initial set up

#### To open images in Fiji

Refer to [official documentation](https://github.com/Jetraw/bioformats_jetraw).

Tested to work on: Windows/macOS + [Fiji 20221201-1017](https://downloads.imagej.net/fiji/archive/20221201-1017/) with Bio-Formats 6.11.1

1. Install Jetraw UI ([Jetraw UI](https://www.jetraw.com/downloads/software)).
2. Determine the Bio-Formats version in your Fiji installation by browsing *path_to_fiji_app/jars/bio-formats/*.
3. Replace the JAR file *formats-bsd-6.x.y.jar* with the corresponding version. (6.11.1 JAR file for [VBC](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx) and Ishihara lab.)
4. Restart Fiji and check that you can open *M44-compressed.tiff*.

Warning: Avoid updating Fiji or the Bio-Formats plugin as it can compromise the Jetraw image read capability. If this happens, you will need to reinstall Fiji and repeat all the steps.

<!--For Python, similarly install necessary packages (link).-->

#### To compress images

1. Obtain the DAT file that is specific to your microscope ([VBC](https://biocenterat-my.sharepoint.com/:f:/g/personal/keisuke_ishihara_imp_ac_at/ErPO_7xw7lVKpNxMvQoY8N8B_CrWwhno9pOy0Sr8faB47g?e=3Tuo1R), Ishihara lab, *public links*).
2. Obtain the associated software license key by contacting the relevant person for your institute.
3. Open Jetraw UI. Load DAT file. Apply license key.
4. To compress an image:
 - Load an input image such as *M44-raw.tiff* (or *CQ1-raw.tiff*).
 - Select *Action: compress*.
 - Select *identifier: 000391 standard* (or *identifier: xxx*).
 - Click *GO*.
5. Check that the resulting file size is smaller than the input.
6. Check that you can open the compressed image in Fiji.

Note: These steps can also be performed on the dataset found under [Jetraw >Resources >Test Dataset](https://www.jetraw.com/downloads/software).

## Utility scripts for batch compression

Pre-requisite: You can compress images with Jetraw UI in your environment.

#### Setting up `bfconvert`

1. Download the Bio-Formats commandline tools, [bftools](https://www.openmicroscopy.org/bio-formats/downloads/). Match the Bio-Formats version with above (e.g. bftools.zip from [6.10.1](https://downloads.openmicroscopy.org/bio-formats/6.10.1/artifacts/) or [6.11.1](https://downloads.openmicroscopy.org/bio-formats/6.11.1/artifacts/)) to be on the safe side.
2. Install [Java Runtime](http://www.java.com).
3. (macOS only) To use the unix executable, change the permission in terminal via `chmod +x ./bfconvert`.

Let's convert an Olympus VSI file to OME-TIFF. Change directory to your bftools folder and run:

```
./bfconvert -series 0 ~/Downloads/M44test/myfile.vsi ~/Downloads/out/myfile-S%sC%c.ome.tif
```
The argument `-series 0` instructs bfconvert to skip the thumbnail image (series 1) in the VSI file. See [documentation](https://docs.openmicroscopy.org/bio-formats/6.10.1/users/comlinetools/conversion.html) for more options.

For the dataset [M44test](https://biocenterat-my.sharepoint.com/personal/keisuke_ishihara_imp_ac_at/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkeisuke%5Fishihara%5Fimp%5Fac%5Fat%2FDocuments%2FJetraw%5FVBCBioOptics&ga=1), the output should be four tiff files corresponding to z-stacks of the four channels. The file size of the input and output are both ~637MB.

#### Setting up `bfconvert` with Jetraw compression

To enable Jetraw compression in `bfconvert`, replace the *bioformats_package.jar* with the Jetraw proprietary version (restricted access links for [VBC](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx) and Ishihara lab).

Now we can convert and compress simultaneously:

```
./bfconvert -compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304 -series 0 ~/Downloads/M44test/myfile.vsi ~/Downloads/out/myfile-S%sC%c.ome.tif
```

M44test dataset shrinks from 637MB to 116MB. This is a ~82% reduction in file size!

### Python script for batch conversion and compression

To repeat the above command for all files in a given directory, we will use a Python script.


#### Supported microscopes

Note to self: add DAT file and default settings here

|       | Location | Microscope | Camera |
| ----- | ----- | ----- | ----- |
| M40   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Olympus spinning disc confocal      | Hamamatsu Orca Flash x 2 |
| M44   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Olympus spinning disc confocal      | Hamamatsu Orca Fusion    |
| M45   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Viventis Lightsheet LS1             | Andor Zyla 4.2 |
| CQ1   | Ishihara lab | Yokogawa CQ1 spinning disc confocal | Hamamatsu Orca Flash |


<!--

```

Input data requirements for Python script:

- Bioformat files (e.g. OME-TIFF, Olympus `.vsi`, Zeiss `.czi`, Nikon `.nd2`).

-->
