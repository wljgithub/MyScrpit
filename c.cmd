@echo off

set scriptPath=E:\myGithub\myScript\autoCreatFile.py

set currentPath=%cd%

set /P fileName='enter the filename and create it.'


python %scriptPath% %currentPath% %fileName%