@FOR %%i IN (%cd%\resources\*.flac) DO (ffmpeg -i %%i -ac 1 resources\output\temp.flac & ren resources\output\temp.flac %%~ni)
