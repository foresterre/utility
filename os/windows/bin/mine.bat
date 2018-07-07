
set user="%userdomain%\%username%"

REM https://ss64.com/nt/takeown.html; ignore error if not a folder
takeown /f %1 /a /r /d Y

REM https://ss64.com/nt/icacls.html
icacls "%1" /setowner %user% /T /C
