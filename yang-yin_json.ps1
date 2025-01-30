# Create output folder if it doesn't exist
$JsonFolder = ".\json_3gpp"
if (!(Test-Path $JsonFolder)) {
    New-Item -ItemType Directory -Path $JsonFolder
}

# Convert all YANG files to YIN format
Get-ChildItem -Path .\yang-models\ -Filter *.yang | ForEach-Object {
    $yinFile = "$($_.BaseName).yin"
    pyang -p .\yang-models\ -f yin -o $yinFile $_.FullName
}

# Convert all YIN files to JSON
Get-ChildItem -Filter *.yin | ForEach-Object {
    $yinFile = $_.FullName
    $jsonFile = "$JsonFolder\$($_.BaseName).json"

    # Run Python script to convert YIN to JSON
    python .\convert_yin_to_json.py $yinFile $jsonFile

    # Remove the YIN file after conversion (optional)
    Remove-Item $yinFile
}

Write-Host "✅ All YANG files converted to JSON and stored in json_3gpp!"
