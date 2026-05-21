@echo off
echo ============================================================
echo EJECUTANDO ANALISIS DE PELICULAS - CINE COLOMBIA
echo ============================================================
echo.

cd /d "%~dp0"
python analisis_pandas.py

echo.
echo ============================================================
echo ANALISIS COMPLETADO
echo ============================================================
echo.
echo Presiona cualquier tecla para cerrar...
pause > nul
