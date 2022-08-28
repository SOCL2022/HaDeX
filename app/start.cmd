@echo off


echo.
echo Loading azd .env file from current environment
echo.

@echo off
for /f "tokens=1* delims==" %%a in ('azd env get-values') do (
  set "%%a=%%~b"
)

if "%errorlevel%" neq "0" (
    echo Failed to load environm