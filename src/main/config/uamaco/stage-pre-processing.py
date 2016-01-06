#!/usr/bin/python

import sys, os, re, datetime, shutil,  uuid, commands

def rreplace(s, old, new, occurrence):
  li = s.rsplit(old, occurrence)
  return new.join(li)

source_file_backup_dir="/data/temp-archive/uamaco"
control_dir= "/data/control/uamaco"

#uuid_str = uuid.uuid1();
today = datetime.datetime.now()
uuid_str = date_str_cltr=today.strftime('%Y%m%d')

# read the local file from standard input
input_file=sys.stdin.readline().strip()

# make sure that we're dealing with a local file
if input_file.find("file:") != 0:
  print >> sys.stderr, "Expecting input file scheme to be 'file:': '%s'" % input_file
  sys.exit(1)

# trim away the scheme
input_file=input_file.replace("file:", "")

# make sure what we are left with is a file that exists
if not os.path.exists(input_file):
  print >> sys.stderr, "Path isn't valid: '%s'" % input_file
  sys.exit(2)

filename = os.path.basename(input_file)

# count no. of lines and append to control file
wc_command = "%s%s%s" % ("wc -l ",input_file,"|cut -d' '  -f1")
line_count = commands.getoutput(wc_command)

date_str_cltr=today.strftime('%Y%m%d')

line_to_be_appended = "%s|%s" % (filename,line_count)
line_to_be_appended = "%s|%s" % (line_to_be_appended,uuid_str)
 
append_to_file = commands.getoutput("echo "+"\""+line_to_be_appended+"\""+" >> "+control_dir+"/"+date_str_cltr+".ctrl")

# Create backup of orginal file in backup folder
shutil.copy2(input_file, source_file_backup_dir)

#Replace _ with @

new_file=rreplace(input_file,'_','@',1)
shutil.move(input_file, new_file)
new_file="file:"+new_file



# write it to standard output
print new_file,
