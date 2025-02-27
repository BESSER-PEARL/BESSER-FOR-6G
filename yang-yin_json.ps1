# Create output folder if it doesn't exist
$JsonFolder = ".\json_3gpp"
if (!(Test-Path $JsonFolder)) {
    New-Item -ItemType Directory -Path $JsonFolder
}

# Setup search paths for pyang
$SearchPaths = ".\yang-models\;.\yang-models\external-yams"
Write-Host "Using search paths: $SearchPaths"

# Process main YANG files
Write-Host "Processing main YANG files..."
Get-ChildItem -Path .\yang-models\ -Filter *.yang -Recurse | ForEach-Object {
    Write-Host "Converting $($_.FullName) to YIN format..."
    $yinFile = "$($_.BaseName).yin"
    # Use both directories in the search path
    pyang -p $SearchPaths -f yin -o $yinFile $_.FullName
}

# Process external YANG files explicitly
Write-Host "Processing external YANG files..."
Get-ChildItem -Path .\yang-models\external-yams\ -Filter *.yang | ForEach-Object {
    Write-Host "Converting $($_.FullName) to YIN format..."
    $yinFile = "$($_.BaseName).yin"
    # Use both directories in the search path
    pyang -p $SearchPaths -f yin -o $yinFile $_.FullName
}

# Convert all YIN files to JSON
Write-Host "Converting YIN files to JSON..."
Get-ChildItem -Filter *.yin | ForEach-Object {
    $yinFile = $_.FullName
    $jsonFile = "$JsonFolder\$($_.BaseName).json"

    # Run Python script to convert YIN to JSON
    Write-Host "Converting $yinFile to $jsonFile..."
    python .\convert_yin_to_json.py $yinFile $jsonFile

    # Remove the YIN file after conversion
    Remove-Item $yinFile
}

Write-Host "✅ All YANG files (including external) converted to JSON and stored in $JsonFolder!"
