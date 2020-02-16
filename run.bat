    @echo off
    setlocal enableextensions enabledelayedexpansion
    set /a "x = 0"

:more_to_process
    if %x% leq 5 (
		python run.py TOKEN_HERE
		pause
		echo.
		echo.
        goto :more_to_process
    )