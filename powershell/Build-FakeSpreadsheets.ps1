function Build-FakeSpreadsheets {
   <#
   .SYNOPSIS
   
   
   .DESCRIPTION
   
   
   .NOTES   
   
   .PARAMETER DataPath
   
   .PARAMETER TitlePath
   
   .PARAMETER DestinationPath
   
   .INPUTS
   
   .OUTPUTS
   
   #>
    [CmdletBinding()]
 
    param (
        [string] $DataPath = '..\python\to_powershell\data.csv',
        [string] $TitlePath = '..\python\to_powershell\title.txt',
        [string] $DestinationPath = '.\to_excel'
    )

    begin {
        Import-Module ImportExcel
        $Data = Get-Content $DataPath
        $Title  = Get-Content $TitlePath
    }
    
    process {
       $data | ConvertFrom-Csv | Export-Excel "..\powershell\$DestinationPath\$Title.xlsx"
    }

    end{
        remove-item $DataPath,$TitlePath
    }
 
 }

 Build-FakeSpreadsheets