if not exist "%appdata%/temp/empty" mkdir "%appdata%/temp/empty"
robocopy "%appdata%/temp/empty" %1 /purge
rmdir "%appdata%/temp/empty"
