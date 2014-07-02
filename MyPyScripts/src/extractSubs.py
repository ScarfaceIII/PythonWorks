'''
Created on 29/mar/2014

Revision 1 on 17/04/2014
  -better "season-and-episode' recognition
  -try-catch on file rename, to avoid crash
  -self-explaining header
  -main definition and preparation for user-configurable script

@author: Massimo

  This is a simple sub extract and rename tool. it will extract all your *.srt files from your *zip files 
  in a given directory, and it will rename them, accordingly to their respective video files in another 
  given directory.
  
  The next three variables are the two paths and there is a flag for optionally deleting the zip files
  modify them, according to your configuration
'''
pathZip = 'D:\\'
pathVideo = pathZip + 'uTorrent\\Complete\\'
zipDelete = 'NO' # edit to 'YES' if you want zip deletion

#shutil has to be used if source and destination files are on different disks, otherwise, better use os.rename
import zipfile, os, re, sys #, shutil

def main():
#   var = raw_input("Please enter something: ")
#   print "you entered", var
  
  zipFiles = [ fn for fn in  os.listdir(pathZip) if fn.endswith('.zip')]
 
  for zipFile in zipFiles:
    with zipfile.ZipFile(pathZip + zipFile, "r") as z:
      for fn in  z.namelist():
        if fn.endswith('.srt'):
          #print fn
          z.extract(fn,pathZip)
    if zipDelete == 'YES':
      os.remove(zipFile)
  
  subFiles = [ fn for fn in  os.listdir(pathZip) if fn.endswith('.srt')]
  # it's a quite long list, but checking for 'starts with' later is more flexible for mixed series subtitles
  # e.g.: one sub for 'How I Met Your Mother' and one for 'New Girl'...
  vidFiles = [ fn for fn in  os.listdir(pathVideo) if (fn.endswith('.avi') | fn.endswith('.mkv') | fn.endswith('.mp4'))]
  
  for sf in subFiles:
    fileNameStart = sf[:2] # only two letters to avoid '30.Rock' example, plus not many series have same initials
    # two conditions: "s00e00" and "00x00"...well lower and upper case...
    subMatch = re.search(r'\d+[eExX]\d+', sf)
    if subMatch:
      
      seasonNumber = subMatch.group()[:2]
      episodeNumber = subMatch.group()[-2:]
#       print 'episode: %s, season: %s' % (episodeNumber, seasonNumber)

      for vf in vidFiles:
        match = re.search(r'^%s[\w.\d\s-]*%s[eEx]%s[\w.\d\s-]+' % (fileNameStart,seasonNumber,episodeNumber), vf)
        if match:
          #print vf
          
          newFileName = match.group()
          # TODO: try-catch to avoid unhandled exception and go on
          try:
            os.rename(pathZip + sf, pathVideo + newFileName[:-4] + '.srt')
          except WindowsError:
            ## Control jumps directly to here if any of the above lines throws IOError.
            sys.stderr.write('problem writing:' + vf)

if __name__ == '__main__':
    main()
    
    