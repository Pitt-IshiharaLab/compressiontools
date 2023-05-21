import os, glob


inputdir = '/Users/keisuke/Downloads/M44test'

files = glob.glob(os.path.join(inputdir, '*.vsi'))

Nfiles = len(files)

# for file in files:
# 	print(file)

file = files[0]

bfconvert = '/Users/keisuke/bftools/bfconvert'
series   = '-series 0'
jetraw   = '-compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304'
myin  = '/Users/keisuke/Downloads/M44test/myfile.vsi'
myout = '/Users/keisuke/Downloads/out/myfile-S%sC%c.ome.tif'

mylist = [bfconvert, series, jetraw, myin, myout]
cmdstr = ' '.join(mylist)

# print(cmdstr)
os.system(cmdstr)
		