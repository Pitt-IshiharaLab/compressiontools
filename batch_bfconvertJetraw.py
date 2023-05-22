import os, glob


dldir = '/Users/keisuke/Downloads'
# dldir = 'C:\\Users\\ishihara\\Downloads'

inputdir = os.path.join(dldir, 'M44test')

files = glob.glob(os.path.join(inputdir, '*.vsi'))

Nfiles = len(files)

# for file in files:
# 	print(file)

file = files[0]

bfconvert = '/Users/keisuke/bftools/bfconvert'
# bfconvert = 'C:\\Users\\ishihara\\bftools'

series   = '-series 0'
jetraw   = '-compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304'
myin  = os.path.join(dldir, 'M44test/myfile.vsi')
myout = os.path.join(dldir, 'out/myfile-S%sC%c.ome.tif')

mylist = [bfconvert, series, jetraw, myin, myout]
cmdstr = ' '.join(mylist)

# print(cmdstr)
os.system(cmdstr)
		