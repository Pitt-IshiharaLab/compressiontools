# compressiontools
 
This repository contains scripts and instructions for applying [Jetraw image compression](https://www.jetraw.com) to microscopy data. The repository is maintained by the Ishihara lab at the University of Pittsburgh and serves as an internal resource for the lab and collaborators.

Jetraw achieves ~80% reduction of file size with essentially no loss of image quality thanks to its *metrologically correct* compression algorithm.

**Jetraw can only compress images from sCMOS cameras.** Thus, Jetraw compression is applicable to most modern widefield, lighsheet, and spinning disc confocal microscopes, but NOT applicable to detector-based systems such as scanning confocal and multiphoton microscopes.

Opening Jetraw images is free, while **image compression requires a software license and a hardware specific parameter file**.


## Initial set up

#### To open images in Fiji

Refer to [official documentation](https://github.com/Jetraw/bioformats_jetraw).

1. Install Jetraw UI ([Jetraw UI](https://www.jetraw.com/downloads/software)).
2. Determine the Bio-Formats version in your Fiji installation by browsing *path_to_fiji_app/jars/bio-formats/*.
3. Replace the JAR file *formats-bsd-6.x.y.jar* with the corresponding version.
 - VBC members can obtain 6.10.1 and 6.11.1 JAR files [here](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx) (restricted access).
 - Ishihara lab members can obatin 6.10.1 and 6.11.1 JAR files here (restricted access).
4. Restart Fiji and check that you can open *M44-compressed.tiff*.

Warning: Avoid updating Fiji or the Bio-Formats plugin as it can compromise the Jetraw image read capability. If this happens, you will need to reinstall Fiji and repeat all the steps.

<!--For Python, similarly install necessary packages (link).-->

#### To compress images

1. Obtain the DAT file that is specific to your microscope ([VBC](https://biocenterat-my.sharepoint.com/:f:/g/personal/keisuke_ishihara_imp_ac_at/ErPO_7xw7lVKpNxMvQoY8N8B_CrWwhno9pOy0Sr8faB47g?e=3Tuo1R), Ishihara lab, *public links*).
2. Obtain the associated software license key by contacting the relevant person for your institute.
2. Open Jetraw UI and load the DAT file.
3. Apply the Jetraw UI license key.
4. To compress an image:
 - Load an input image such as *M44-raw.tiff* (or *CQ1-raw.tiff*).
 - Select *Action: compress*.
 - Select *identifier: 000391 standard* (or *identifier: xxx*).
 - Click *GO*.
5. Check that the resulting file size is smaller than the input.
6. Check that you can open the compressed image in Fiji.

Note: These steps can also be performed on the dataset found under [Jetraw >Resources >Test Dataset](https://www.jetraw.com/downloads/software).

## Utility scripts for batch compression

#### Setting up `bfconvert`

Download the Bio-Formats commandline tools, [bftools](https://www.openmicroscopy.org/bio-formats/downloads/). Match the Bio-Formats version with above (e.g. bftools.zip from [6.10.1](https://downloads.openmicroscopy.org/bio-formats/6.10.1/artifacts/) or [6.11.1](https://downloads.openmicroscopy.org/bio-formats/6.11.1/artifacts/)) to be on the safe side. You will additionally need to install [Java Runtime](http://www.java.com).

To use the unix executable in MacOS, change the permission in terminal via `chmod +x ./bfconvert`.

Let's convert an Olympus VSI file to OME-TIFF. Change directory to your bftools folder and run:

```
./bfconvert -series 0 ~/Downloads/M44test/myfile.vsi ~/Downloads/out/myfile-S%sC%c.ome.tif
```
The argument `-series 0` skips the thumbnail image (series 1) in the VSI file.

For the dataset [M44test](https://biocenterat-my.sharepoint.com/personal/keisuke_ishihara_imp_ac_at/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fkeisuke%5Fishihara%5Fimp%5Fac%5Fat%2FDocuments%2FJetraw%5FVBCBioOptics&ga=1), the output should be four tiff files corresponding to z-stacks of the four channels. The total file size of the input and output are similar at ~637MB.

#### Setting up `bfconvert` with Jetraw compression

To enable Jetraw compression in `bfconvert`, replace the *bioformats_package.jar* with the proprietary version found (restricted access links for [VBC](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx) and Ishihara lab).

Now we can convert and compress simultaneously:

```
./bfconvert -compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304 -series 0 ~/Downloads/M44test/myfile.vsi ~/Downloads/out/myfile-S%sC%c.ome.tif
```

M44test dataset shrinks from 637MB to 116MB, which is ~82% reduction in file size. Make sure that you can browse the tiff files in Fiji.

#### Python script for batch conversion and compression

We basically want to repeat the above command for all files in a given directory. To do this, we will use a Python script.

<!--

```
./bfconvert -option ometiff.companion ~/Downloads/out/myfile.companion.ome ~/Downloads/M44test2/myfile.vsi ~/Downloads/out/myfile-S%sC%c.ome.tif
```

Input data requirements for Python script:

- Bioformat files (e.g. OME-TIFF, Olympus `.vsi`, Zeiss `.czi`, Nikon `.nd2`).

-->
