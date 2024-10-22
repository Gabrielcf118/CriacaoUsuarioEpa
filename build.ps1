$exclude = @("venv", "EPAusuario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "EPAusuario.zip" -Force