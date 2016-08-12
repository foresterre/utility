if not exist "%appdata%/temp/empty" mkdir "%appdata%/temp/empty"
robocopy "%appdata%/temp/empty" %1 /purge
rmdir /S /Q %1
rmdir "%appdata%/temp/empty"
