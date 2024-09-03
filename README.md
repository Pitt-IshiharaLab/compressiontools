# compressiontools
 
This repository contains scripts and instructions for applying [Jetraw image compression](https://www.jetraw.com) to microscopy data. The repository is maintained by the Ishihara lab at the University of Pittsburgh and serves as an internal resource for the lab and its collaborators.

While this is a public repository, request for technical support should be directed to the [Jetraw team](https://www.jetraw.com/contact).


## 0. About Jetraw

[Jetraw technology](https://www.jetraw.com/jetraw-technology) achieves ~80% reduction of file size with essentially no loss of image quality thanks to its *metrologically correct* compression algorithm.

**Jetraw can only compress images from sCMOS cameras.** Thus, Jetraw compression is applicable to most modern widefield, lighsheet, and spinning disc confocal microscopes, but NOT applicable to detector-based systems such as scanning confocal and multiphoton microscopes.

Opening Jetraw images is free, while **image compression requires a software license and hardware specific parameters**.


## 1. Basic usage

#### To open compressed images in Fiji

Tested to work on: Windows/macOS + [Fiji 20221201-1017](https://downloads.imagej.net/fiji/archive/20221201-1017/) with Bio-Formats 6.11.1

1. Install Jetraw UI ([Jetraw UI](https://www.jetraw.com/downloads/software)). **Note**: For Windows computer, make sure C:\Program Files\Jetraw\bin64 is added to the "Path" in Environmental Variables > System Variables. This may require admin privileges.
2. Determine the Bio-Formats version in your Fiji installation (go to: *path_to_fiji_app/jars/bio-formats/*).
3. Replace *formats-bsd-6.x.y.jar* with Jetraw's version. (6.11.1 JAR file for [VBC](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx) and [Ishihara lab](https://pitt-my.sharepoint.com/:f:/r/personal/ishihara_pitt_edu/Documents/Jetraw_Pitt-IshiharaLab_restrictedaccess?csf=1&web=1&e=oOXouJ), ask Keisuke for access.)
4. Restart Fiji and check that you can open *M44-compressed.tiff*.

**Warning**: Avoid updating this Fiji installation or its Bio-Formats plugin as it can break the Jetraw image read capability. If this breaks, you will need to reinstall Fiji and repeat all the steps.

<!--For Python, similarly install necessary packages (link).-->

#### To compress images

1. Obtain the DAT file specific to your microscope ([VBC](https://biocenterat-my.sharepoint.com/:f:/g/personal/keisuke_ishihara_imp_ac_at/ErPO_7xw7lVKpNxMvQoY8N8B_CrWwhno9pOy0Sr8faB47g?e=3Tuo1R), Ishihara lab, *public links*).
2. Obtain the associated software license key from the relevant person at your institute.
3. Open Jetraw UI. Load DAT file. Apply license key.
4. To compress an image:
 - Load an input image such as *M44-raw.tiff* (or *CQ1-raw.tiff*).
 - Select *Action: compress*.
 - Select *identifier: 000391 standard* (or *identifier: xxx*).
 - Click *GO*.
5. Check that the resulting file size is smaller than the input.
6. Check that you can open the compressed image in Fiji.


## 2. Advanced usage
- [Compressing multiple data sets from CQ1 microscope](compressMultipleCQ1data.md)
- [OME-TIFF conversion followed by compression](OMETIFFconversionCompression.md)
 - Use case 1: Microscopy data is not in TIFF format (e.g. Olympus, Nikon, Zeiss, Leica)
 - Use case 2: Reduce the number of tiff files in CQ1 data by stacking in Z or T.


## 3. Other information

#### Microscopes tested by Keisuke

Note to self: add DAT file and default settings here

|       | Location | Microscope | Camera |
| ----- | ----- | ----- | ----- |
| M40   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Olympus spinning disc confocal      | Hamamatsu Orca Flash x 2 |
| M44   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Olympus spinning disc confocal      | Hamamatsu Orca Fusion    |
| M45   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Viventis Lightsheet LS1             | Andor Zyla 4.2 |
| CQ1   | Ishihara lab | Yokogawa CQ1 spinning disc confocal | Hamamatsu Orca Flash |

#### Other resources

 - [Github - Jetraw/bioformats_jetraw](https://github.com/Jetraw/bioformats_jetraw)
 -	[Jetraw >Resources >Test Dataset](https://www.jetraw.com/downloads/software)
