# Deltemp-beta
Windows temporary file remover

This python program removes windows temporary files. The next folders can be affected:
<br />C:\Windows\Temp
<br />%localappdata%\Temp
<br />C:\Windows\Prefetch

The affected folders can be changed in the deltemp_setting.ini file.

Scheme of the deltemp_setting.ini:

[CONFIG] - configuration section (changes affected folders)
<br />delete_temp = True   <strong> - If it's True C:\Windows\Temp will be cleared!</strong>
<br />delete_%temp% = True   <strong> - If it's True %localappdata%\Temp will be cleared!</strong>
<br />delete_prefetch = False  <strong> - If it's True C:\Windows\Prefetch will be cleared!</strong>

[LOGGING]
<br />exceptionlogs = True <strong>  - If it's True, but log_all is False, only failed operations will be logged!</strong>
<br />log_all = False  <strong> - If it's True all operations will be logged!</strong>

<br />

The program have two versions based on language:
<br />HUN - Hungarian
<br />ENG - English
