## Compressing multiple data sets from CQ1 microscope

When compressing multiple data sets, using Jetraw UI is not advised since
 
 1. Jetraw UI only compresses TIFF files. All other files such as JPG, PNG, CQ1 metadata files will not be copied to the destination folder.
 2. It can be annoying to drag & drop many input folders into Jetraw UI.

This page explains how to automate the compression of multiple data sets from CQ1 while safely copying all non-TIFF files.
We will use the command line tool [dpcore](https://github.com/Jetraw/Jetraw?tab=readme-ov-file#command-line-utilities).

**Pre-requisite:** Compression with Jetraw UI is working on your computer.

Open command prompt (Windows) or terminal (macOS), type `dcpore -h`, and hit enter.
You should see the usage instructions for dpcore.

## Instructions for MacOS

You have multiple datasets as subdirectory in the parent directory "path\_input". You want to compress all tiff files and copy everything else to the destination directory "path\_output". 

```
dpcore -c -d /path_output/. -i 306296 path_input --preserve-extension --copy-others --recursive
```

The compression options are:
- `306296`
- `306296_bin2x`
- `306296_bin4x`

## Instructions for Windows

Similar to above but replace `/` with `\`.


```
dpcore -c -d \path_output\. -i 306296 path_input --preserve-extension --copy-others --recursive
```
