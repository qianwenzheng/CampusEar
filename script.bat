@FOR %%i IN (C:\Users\seanl\Music\Apowersoft\Streaming Audio Recorder\Recording\*.flac) DO (ffmpeg -i %%i -ac 1 resources\output\temp.flac & ren resources\output\temp.flac %%~ni & del %%i)
