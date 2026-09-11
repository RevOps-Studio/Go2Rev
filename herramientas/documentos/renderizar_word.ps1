param([Parameter(Mandatory=$true)][string]$InputDoc,[Parameter(Mandatory=$true)][string]$OutputPdf)
$ErrorActionPreference='Stop'
$InputDoc=[IO.Path]::GetFullPath($InputDoc)
$OutputPdf=[IO.Path]::GetFullPath($OutputPdf)
$taskWord=$null
$taskDoc=$null
try {
  $taskWord=New-Object -ComObject Word.Application
  $taskWord.Visible=$false
  $taskWord.DisplayAlerts=0
  $taskDoc=$taskWord.Documents.Open($InputDoc,$false,$true)
  $taskDoc.Repaginate()
  $taskDoc.ExportAsFixedFormat($OutputPdf,17)
  Write-Output $OutputPdf
} finally {
  if($null -ne $taskDoc){$taskDoc.Close(0); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($taskDoc)}
  if($null -ne $taskWord){$taskWord.Quit(); [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($taskWord)}
}
