import os, glob
import shutil
import platform

inputdirs = ['20240115T150939_HEKfusion_001',
			 '20240118T154120_HEKfusion_004',
			 '20240123T161252_HEKfusion_007',
			 '20240125T145500_CT26fusion_006']

inputdirs = [os.path.join('Q:\\YRoot\\lab_user\\Keisuke', f) for f in inputdirs]
outparent = 'D:\\JetrawCQ1testing\\out'
jetraw_args = '-compression Jetraw -jetraw-identifier 306296 -tilex 2300 -tiley 2300' # for Daido Ishihara lab CQ1
path_bftools = 'C:\\Users\\ishihara\\bftools' # bftools directory setup for Jetraw, Fuji workstation

flag_jetraw = True
flag_omecompanion = False

indexing = 'S%sZ%z\S%sZ%zT%t'

for inputdir in inputdirs:

	outdir = os.path.join(outparent, os.path.basename(inputdir) + "_bfconvertJetraw")

	# prepare output directory
	if os.path.exists(outdir):
		shutil.rmtree(outdir)
	os.makedirs(outdir)

	# copy the ome.xml file
	shutil.copyfile(os.path.join(inputdir, 'MeasurementResult.ome.xml'), os.path.join(outdir, 'MeasurementResult.ome.xml'))

	file = os.path.join(inputdir, 'MeasurementResult.ome.tif')
	fnme = os.path.basename(inputdir) # filename minus extension

	# arguments - common for all files
	bfconvert = os.path.join(path_bftools, 'bfconvert')

	if flag_jetraw:
		jetraw = jetraw_args
	else:
		jetraw = ''

	# arguments - file specific
	if flag_omecompanion:
		companion = '-option ometiff.companion ' + os.path.join(outdir, fnme + '.companion.ome')
		ext_out   = '.ome.tif'
	else:
		companion = ''
		ext_out   = '.tif'

	myin  = file
	myout = os.path.join(outdir, indexing + ext_out)

	mylist = [bfconvert, jetraw, '-padded', companion, myin, myout]
	cmdstr = ' '.join(mylist)

	if platform.system() == 'Windows':
		cmdstr = cmdstr.replace("%", "%%")

	os.system(cmdstr)
