import os, glob

flag_jetraw = True
flag_omecompanion = True

dldir = '/Users/keisuke/Downloads'
path_bfconvert = '/Users/keisuke/bftools/bfconvert'

# dldir = 'C:\\Users\\ishihara\\Downloads'
# bfconvert = 'C:\\Users\\ishihara\\bftools\\bfconvert'

inputdir = os.path.join(dldir, 'M44test')
files = glob.glob(os.path.join(inputdir, '*.vsi'))

# Nfiles = len(files)
# for file in files:
# 	print(file)

file = files[0]

series    = '-series 0'
jetraw    = '-compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304'

# overwr    = '-overwrite' # the overwrite parmeter is not working in macOS

myin  = os.path.join(dldir, 'M44test/myfile.vsi')

if flag_jetraw:
	jetraw = '-compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304'
else:
	jetraw = ''

if flag_omecompanion:
	companion = '-option ometiff.companion ' + os.path.join(dldir, 'out', 'myfile.companion.ome')
	myout     = os.path.join(dldir, 'out/myfile-S%sC%c.ome.tif')
else:
	companion = ''
	myout     = os.path.join(dldir, 'out/myfile-S%sC%c.tif')

mylist = [path_bfconvert, series, jetraw, companion, myin, myout]

cmdstr = ' '.join(mylist)

# print(cmdstr)
os.system(cmdstr)
		