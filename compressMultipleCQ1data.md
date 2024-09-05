# Compressing multiple data sets from CQ1 microscope

When compressing multiple data sets, using Jetraw UI is not advised since
 
 1. Jetraw UI only compresses TIFF files. All other files such as JPG, PNG, CQ1 metadata files will not be copied to the destination folder.
 2. It can be annoying to drag & drop many input folders into Jetraw UI.

This page explains how to automate the compression of multiple data sets from CQ1 while safely copying all non-TIFF files.
We will use the command line tool [dpcore](https://github.com/Jetraw/Jetraw?tab=readme-ov-file#command-line-utilities).

## Preparation

**Pre-requisite:** Compression with Jetraw UI is working on your computer.

It will be useful to add `dpcore` and `jetraw` immediately accessible from your terminal.

1. In the terminal type: 
`vim ~/.zshrc` (In older systems it might be .bashr)
2. Type “i” to start editing the text and copy the following line:
`export PATH=$PATH:/Applications/Jetraw\ UI.app/Contents/jetraw/bin`
3. Hit “ESC” followed by “:wq” to save the changes.
4. Quit the terminal application.
5. Restart terminal and execute `jetraw -h` or `dpcore -h`. You should get the help menu. 

# Instructions for MacOS

You have multiple datasets as subdirectory in the parent directory "path\_input". You want to compress all tiff files and copy everything else to the destination directory "path\_output". 

```
dpcore -c -d /path_output/. -i 306296 path_input --preserve-extension --copy-others --recursive
```

The compression options are:
- `306296`
- `306296_bin2x`
- `306296_bin4x`

# Instructions for Windows

Similar to above but replace `/` with `\`.


```
dpcore -c -d \path_output\. -i 306296 path_input --preserve-extension --copy-others --recursive
```
