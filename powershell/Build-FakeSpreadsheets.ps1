function Build-FakeSpreadsheets {
   <#
   .SYNOPSIS
    Reads a csv file produced by an external script, converts the data it contains
    into a PowerShell object, and then exports that object as an Excel Spreadsheet
    named after the data contained in a text file which is also produced by the 
    same external script.   
   
   .DESCRIPTION
    Utilizing the Import-Excel module, it is possible to convert a powershell object
    directly to Excel format. 
   
    The Make_FakeCompany class's  To_Excel  method produces two files:

        One is a csv file containing the data produced by the   Make_FakeCompany
        MakeFakeEmployees,  MakeFakeCustomers,  MakeFakeInventory,   and   
        MakeFakeTransactions  methods.  
   
        The other is a text file containing the  Fake Company Name  and  the  
        Data Category   of the  Excel Spreadsheet  which is to be generated.

    Build_FakeSpreadsheets accesses these files, converts the csv content to 
    a powershell object, and then invokes the Export-Excel cmdlet to convert
    the object to a Excel Spreadsheet having a name matching what is written in   
    the text file 

   .PARAMETER DataPath
   The file path to_powershell's csv data which will be converted and exported.
   
   .PARAMETER TitlePath
   The file path to_powershell's text file containing the title and category of the
   csv data.
   
   .PARAMETER DestinationPath
   The destination file path where the resulting Excel Spreasheets will be generated. 
   
   .INPUTS
   None
   
   .OUTPUTS
   Does not produce output, but causes a side effect of generating 4 Excel Spreadsheets a capturing all  
   Make_FakeCompany  data.
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