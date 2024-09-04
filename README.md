# compressiontools
 
This repository contains scripts and instructions for applying [Jetraw image compression](https://www.jetraw.com) to microscopy data. The repository is maintained by the Ishihara lab at the University of Pittsburgh and serves as an internal resource for the lab and its collaborators.

While this is a public repository, request for technical support should be directed to the [Jetraw team](https://www.jetraw.com/contact).


## 0. About Jetraw

[Jetraw technology](https://www.jetraw.com/jetraw-technology) achieves ~80% reduction of file size with essentially no loss of image quality thanks to its *metrologically correct* compression algorithm.

**Jetraw can only compress images from sCMOS cameras.** Thus, Jetraw compression is applicable to most modern widefield, lighsheet, and spinning disc confocal microscopes, but NOT applicable to detector-based systems such as scanning confocal and multiphoton microscopes.

Opening Jetraw images is free, while **image compression requires a software license and hardware specific parameters**.


## 1. Basic usage with Fiji and Jetraw UI

#### 1.1 Open compressed images in Fiji

Tested to work on: Windows/macOS + [Fiji 20231211-1317](https://downloads.imagej.net/fiji/archive/20231211-1317/) with Bio-Formats 7.1.0

All necessary files are found in these links (ask Keisuke for access): [for VBC](https://biocenterat-my.sharepoint.com/:f:/r/personal/keisuke_ishihara_imp_ac_at/Documents/Jetraw_VBCrestrictedaccess?csf=1&web=1&e=XizOPx)
and [for Pitt](https://pitt-my.sharepoint.com/:f:/r/personal/ishihara_pitt_edu/Documents/Jetraw_Pitt-IshiharaLab_restrictedaccess?csf=1&web=1&e=oOXouJ)

1. Install Jetraw UI from the link above.
 - Installation files are \*.msi for Windows and \*.dmg for macOS.
 - For Windows computer, make sure C:\Program Files\Jetraw\bin64 is added to the "Path" in Environmental Variables > System Variables. This may require admin privileges.
2. Determine the Bio-Formats version in your Fiji installation (go to: *path_to_fiji_app/jars/bio-formats/*).
3. Overwrite *formats-bsd-x.y.z.jar*  with the file of the same name, found in the link above.
4. Restart Fiji and check that you can open *CQ1-compressed.tiff* under the `\images` folder in this repository.

**Warning**: Avoid updating this Fiji installation or its Bio-Formats plugin as it can break the Jetraw image read capability. If this breaks, you will need to reinstall Fiji and repeat all the steps.

#### 1.2 Compress images with Jetraw UI

1. Obtain the DAT file specific to your microscope from the link above.
2. Obtain the associated software license key.
3. Open Jetraw UI. Load DAT file. Apply license key.
4. To compress an image (or all images within a folder):
 - Load an input image such as *CQ1-raw.tiff*.
 - Select *Action: compress*.
 - Select *identifier: 306296 No binning*. (Select appropriate setting for binned images.)
 - Specify *destination*.
 - Click *GO*.
5. Check that the resulting file size is smaller than the input.
6. Check that you can open the compressed image in Fiji.

**Note:** Jetraw UI will not copy non-TIFF files to the destination folder. One way to overcome this is to use the `--copy-others` flag when calling dpcore. Another is to use a custom script that copies non-TIFF files. see Advanced usage.

#### 1.3 Decompress images with Jetraw UI

1. Load a compressed image such as *CQ1-compressed.tiff*.
2. Select *Action: decompress*.
3.  Specify *destination*.
4. Click *GO*.


## 2. Advanced usage
- [Compressing multiple data sets from CQ1 microscope](compressMultipleCQ1data.md)
- [OME-TIFF conversion followed by compression](OMETIFFconversionCompression.md)
 - Use case 1: Microscopy data is not in TIFF format (e.g. Olympus, Nikon, Zeiss, Leica)
 - Use case 2: Reduce the number of tiff files in CQ1 data by stacking in Z or T.
- [pyJetraw](https://github.com/Jetraw/pyJetraw) from Jetraw
 - Use case: To directly open compressed images in Python

## 3. Other information

#### Microscopes tested by Keisuke

Note to self: add DAT file and default settings here

|       | Location | Microscope | Camera |
| ----- | ----- | ----- | ----- |
| M40   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Olympus spinning disc confocal      | Hamamatsu Orca Flash x 2 |
| M44   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Olympus spinning disc confocal      | Hamamatsu Orca Fusion    |
| M45   |  [VBC BioOptics](https://cores.imp.ac.at/biooptics/equipment/?xhtml=1%2F%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%5C%27From%2FRK%3D0%2FRS%3DUhWihNMQI1LWDV3V.sJxktWcMkU-)| Viventis Lightsheet LS1             | Andor Zyla 4.2 |
| CQ1 Daido | Ishihara lab | Yokogawa CQ1 spinning disc confocal | Hamamatsu Orca Flash |

#### Other resources

 - [Github - Jetraw/bioformats_jetraw](https://github.com/Jetraw/bioformats_jetraw)
 -	[Jetraw >Resources >Test Dataset](https://www.jetraw.com/downloads/software)
