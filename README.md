# compressiontools
 
This repository contains scripts and instructions for applying [Jetraw image compression](https://www.jetraw.com) to microscopy data. The repository is maintained by Ishihara lab at the University of Pittsburgh and serves as an internal resource for the lab and collaborators.

Jetraw achieves ~80% reduction of file size with essentially no loss of image quality thanks to its *metrologically correct* compression algorithm.

**Jetraw can only compress images from sCMOS cameras.** Thus, Jetraw compression is applicable to most modern widefield, lighsheet, and spinning disc confocal microscopes, but NOT applicable to detector-based systems such as scanning confocal and multiphoton microscopes.

Opening Jetraw images is free, while **image compression requires a software license and a hardware specific parameter file**.


## Initial set up

#### To open images in Fiji

Refer to [official documentation](https://github.com/Jetraw/bioformats_jetraw).

1. Install Jetraw UI ([Jetraw UI](https://www.jetraw.com/downloads/software)).
2. Install the special bioformats plugin for Fiji.
3. Check that you can open `M40-compressed.tiff` in Fiji. This is an image of ....

Note: It is recommended to NOT update Fiji and the bioformats plugin. If you do, the bioformats version may change and you will need to reinstall Fiji and use the correct verson of the plug in from Step `2`.

<!--For Python, similarly install necessary packages (link).-->

#### To compress images

1. Obtain the `.dat` parameter file that is specific to your microscope ([VBC](https://biocenterat-my.sharepoint.com/:f:/g/personal/keisuke_ishihara_imp_ac_at/ErPO_7xw7lVKpNxMvQoY8N8B_CrWwhno9pOy0Sr8faB47g?e=3Tuo1R), Ishihara lab).
2. Obtain the associated software license key by contacting the relevant person for your institute.
2. Open Jetraw UI and load the `.dat` file.
3. Apply the Jetraw UI license key.
4. Drag and drop`M40-raw.tiff` and compress your 
5. Check that the resulting file size is smaller than the input.
6. Check that you can open the compresed in Fiji.


## Utility scripts for batch compression


<!--

Input data requirements for Python script:


- Bioformat files (e.g. OME-TIFF, Olympus `.vsi`, Zeiss `.czi`, Nikon `.nd2`).

-->
