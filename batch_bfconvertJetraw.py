import os, glob
import shutil
import platform
from multiprocessing import Pool

flag_jetraw = True
flag_omecompanion = True

# for macOS
# dldir = '/Users/keisuke/Downloads'
# path_bftools = '/Users/keisuke/bftools'

# for Windows
dldir = 'D:\\JetrawTesting'
path_bftools = 'C:\\Users\\ishihara\\bftools'

N_CPUcores = 28

stacks = '-S%sC%c'
if platform.system() == 'Windows':
	stacks = stacks.replace("%", "%%")

inputdir = os.path.join(dldir, 'M44-input')
outdir = os.path.join(dldir, 'M44-JetrawOMETIFF')

# # prepare output directory
# if os.path.exists(outdir):
# 	shutil.rmtree(outdir)
# os.makedirs(outdir)

ext_in = '.vsi'

files = glob.glob(os.path.join(inputdir, '*' + ext_in))
Nfiles = len(files)

# arguments - common for all files
bfconvert = os.path.join(path_bftools, 'bfconvert')
series    = '-series 0'
if flag_jetraw:
	jetraw = '-compression Jetraw -jetraw-identifier 000391_standard -tilex 2304 -tiley 2304'
else:
	jetraw = ''
# overwr    = '-overwrite' # the overwrite parameter is not working in macOS or Windows, file size adds to pre-existing files

def convertcompress(file):

	fnme = os.path.basename(file).replace(ext_in, '')  # filename minus extension

	# arguments - file specific
	if flag_omecompanion:
		companion = '-option ometiff.companion ' + os.path.join(os.path.dirname(file).replace(inputdir, outdir), fnme + '.companion.ome')
		ext_out   = '.ome.tif'
	else:
		companion = ''
		ext_out   = '.tif'

	myin  = os.path.join(file)
	myout = os.path.join(os.path.dirname(file).replace(inputdir, outdir),  fnme + stacks + ext_out)
	option = '-option cellsens.fail_on_missing_ets True'

	mylist = [bfconvert, series, jetraw, option, companion, myin, myout]
	cmdstr = ' '.join(mylist)

	# print(myin)
	os.system(cmdstr)

# for cc, file in enumerate(files[::20]):
# 	convertcompress(file)

# convertcompress(files[0])

if __name__ == '__main__':

	datasets =  glob.glob(os.path.join(inputdir, "*"))

	for dataset in datasets:
		files = glob.glob(os.path.join(dataset, '*' + ext_in))

		with Pool(N_CPUcores) as p:
			p.map(convertcompress, files)

# print(cmdstr)
#os.system(cmdstr)
