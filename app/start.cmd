@echo off


echo.
echo Loading azd .env file from current environment
echo.

@echo off
for /f "tokens=1* delims==" %%a in ('azd env get-values') do (
  set "%%a=%%~b"
)

if "%errorlevel%" neq "0" (
    echo Failed to load environment varaiables from azd environment
    exit /B %errorlevel%
)

echo.
echo Restoring backend python packages
echo.
cd backend
call pip install -r requirements.txt
if "%errorlevel%" neq "