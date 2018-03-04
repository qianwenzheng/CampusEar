copy "C:\Users\seanl\Music\Apowersoft\Streaming Audio Recorder\Recording\*" %cd%\resources\Dumb\ 
@FOR %%i IN (%cd%\resources\Dumb\*.flac) DO (ffmpeg -i %%i -ac 1 resources\output\temp.flac & ren resources\output\temp.flac %%~ni)
del %cd%\resources\Dumb\*.flac
