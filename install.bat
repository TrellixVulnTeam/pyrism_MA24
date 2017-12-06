@echo off
    setlocal enableextensions disabledelayedexpansion

    set "env=.env"
    set here=%~dp0
    set "PYSDL2_DLL_PATH=%here:\=/%.lib/"

    for /f "tokens=*" %%l in ('type "%env%"^&cd.^>"%env%"'
    ) do for /f "tokens=1 delims== " %%a in ("%%~l"
    ) do if /i "%%~a"=="PYSDL2_DLL_PATH:" (
            >>"%env%" echo(PYSDL2_DLL_PATH: %PYSDL2_DLL_PATH%
    ) else (
        >>"%env%" echo(%%l
    )

    type "%env%"

    endlocal
