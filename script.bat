copy "C:\Users\seanl\Music\Apowersoft\Streaming Audio Recorder\Recording\*" %cd%\resources\Dumb\ 
del %cd%\resources\output\temp.flac
@FOR %%i IN (%cd%\resources\Dumb\*.flac) DO (ffmpeg -i %%i -ac 1 resources\output\temp.flac & ren resources\output\temp.flac %%~ni & del %%i )
del %cd%\resources\Dumb\*.flac
