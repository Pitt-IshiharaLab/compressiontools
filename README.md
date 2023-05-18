# compressiontools
 
This repository contains scripts and instructions for applying [Jetraw image compression](https://www.jetraw.com) to microscopy data. The repository is maintained by Ishihara lab at the University of Pittsburgh and serves as an internal resource for the lab and collaborators.

Jetraw achieves ~80% reduction of file size with essentially no loss of image quality thanks to its *metrologically correct* compression algorithm.

**Jetraw can only compress images from sCMOS cameras.** Thus, Jetraw compression is applicable to most modern widefield, lighsheet, and spinning disc confocal microscopes, but NOT applicable to detector-based systems such as scanning confocal and multiphoton microscopes.

Opening Jetraw images is free, while **image compression requires a software license and a hardware specific parameter file**.


## Initial set up

#### To open images in Fiji

Refer to [official documentation](https://github.com/Jetraw/bioformats_jetraw).

1. Install Jetraw UI ([Jetraw UI](https://www.jetraw.com/downloads/software)).
2. Determine the Bio-Formats version in your Fiji installation by browsing *path_to_fiji_app/jars/bio-formats/*.
3. Replace the JAR file *formats-bsd-6.x.y.jar* with the corresponding version.
4. Restart Fiji and check that you can open *M40-compressed.tiff*.

Warning: Updating Fiji occasionally results in a new version of Bioformats plugin, which can break the Jetraw image read capability. To fix this, you will need to reinstall Fiji and replace the JAR file again.

<!--For Python, similarly install necessary packages (link).-->

#### To compress images

1. Obtain the DAT file that is specific to your microscope ([VBC](https://biocenterat-my.sharepoint.com/:f:/g/personal/keisuke_ishihara_imp_ac_at/ErPO_7xw7lVKpNxMvQoY8N8B_CrWwhno9pOy0Sr8faB47g?e=3Tuo1R), Ishihara lab).
2. Obtain the associated software license key by contacting the relevant person for your institute.
2. Open Jetraw UI and load the DAT file.
3. Apply the Jetraw UI license key.
4. To compress an image,
- Drag and drop an input image such as *M40-raw.tiff* or *CQ1-raw.tiff*
- Select *Operation compression* in the drop down menu.
- Select *Settings: xxx* in the drop down menu.
- Click *Compress*. 
5. Check that the resulting file size is smaller than the input.
6. Check that you can open the compressed image in Fiji.

Note: These steps can also be performed with [Jetraw >Resources >Test Dataset](https://www.jetraw.com/downloads/software).

## Utility scripts for batch compression


<!--

Input data requirements for Python script:


- Bioformat files (e.g. OME-TIFF, Olympus `.vsi`, Zeiss `.czi`, Nikon `.nd2`).

-->
