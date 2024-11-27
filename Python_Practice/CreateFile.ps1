Param(                                                                  # Param block to accept parameters 
   [Parameter(Mandatory, HelpMessage = "Please provide a valid path")]  # Mandatory parameter 
   [string]$Path                                                        # Path parameter & assign its type 
) 
New-Item -Path $Path -ItemType File             # Create a file at the specified path & set its type to File 
Write-Host "File created at path $Path"         # Display a message 

#  This script creates a file at the specified path.
#  To run this script, open a PowerShell window and run the following command from the directory where the script is saved:
#  .\CreateFile.ps1 -Path "C:\Users\Public\Documents\NewFile.txt" or ".\CreateFile.ps1 -Path ".\NewFile.txt"

#  The script will create a file named NewFile.txt at the specified path, but if you did not list a path then
#  the file will be created in the current directory.
