# Copyright (c) 2016 foresterre
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# script input argument:
#   checksum file of the same directory (same directory as checksum file)
# purpose:
#   verify checksums (from ) of files in single directory
# expected layout of checksum file:
#   [sha256 checksum 1] [file name 1]
#   [sha256 checksum 2] [file name 2]
#   [sha256 checksum .] [file name .]
#   [sha256 checksum N] [file name N]
# output file layout:
#   [file name 1] [Exists (Y/N)] [Correct hash (Y/N) if exists]
#   [file name 2] [Exists (Y/N)] [Correct hash (Y/N) if exists]
#   [file name .] [Exists (Y/N)] [Correct hash (Y/N) if exists]
#   [file name N] [Exists (Y/N)] [Correct hash (Y/N) if exists]

# todo:
# + documentation
# + process checksum file
# + check whether file still exists
# ...

$dirArgument = $args[0]
$requiredArgumentStr = "The first argument should be an existing checksum file. Usage: ./Hash-FilesInFolder [checksum file]"

# verify input information
if ($dirArgument -eq $null) {
    Write-Host "Error, no argument provided!"
    Write-Host $requiredArgumentStr
    Exit
}

$dirTestPath = Test-Path $dirArgument
if (-Not $dirTestPath) {
    Write-Host "Error, path not found!"
    Write-Host $requiredArgumentStr
    Exit
}


# config
$outputFileName = "checksum-verify-list.txt"
$outputFilePath = Join-Path -Path $dirArgument -ChildPath $outputFileName # TODO: get directory from [checksum file]


# clean output
$outputFileExist = Test-Path $outputFilePath
if ($outputFileExist) {
    Write-Host "Output file 'TODO: outputFilePath' does already exist, cleaning file..."
    Clear-Content $outputFilePath
} else {
    Write-Host "Created output file: 'checksum.sha256\'".
    Out-File $outputFileName
}


# process input TODO: split lines and verify
$dirFiles = Get-ChildItem $dirArgument -File | Where-Object { $_.Name -ne "checksum.sha256" }

$dirFiles | ForEach-Object {
    $fPath = $_.FullName
    $hash = Get-FileHash $fPath -Algorithm SHA256

    $hashFmt = $hash.Hash
    $fNameFmt = $_.Name #Resolve-Path -Relative $fPath
    $resultFmt =  "$hashFmt $fNameFmt"

    Write-Host "Appending hash: ", $resultFmt

    $resultFmt | Out-File $outputFilePath -Append
}
