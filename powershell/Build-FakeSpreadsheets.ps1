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

    .PARAMETER DestinationPath1
    The file path containing the csv data which will be converted and exported
    and the text file bearing the title, category, and report type of the csv data.

    .PARAMETER DestinationPath2
    The destination file path within the project repository where the Excel Spreadsheets 
    are sent.

    .PARAMETER DestinationPath3
    The file path to Service-Centric OneDrive, where the Spreadsheets are copied, which 
    triggers a Power Automate Cloud Flow that copies the Spreadsheets to the Service-Centric
    Solutions Sharepoint.

    .INPUTS
    None. 

    .OUTPUTS
    Does not produce output, but causes a side effect of generating 4 Excel Spreadsheets a capturing all  
    Make_FakeCompany  data and initiates Power Automate Cloud Flow triggered by the creation of OneDrive
    files that copies those files to the Service-Centric Solutions SharePoint.

    .NOTES
    Called in Parallel with a Make_Fake python script which creates the directories and files used.
#>
    [CmdletBinding()]
 
    param (
        [string] $DestinationPath1 = 'C:\Users\harry\projects\Make_Fake\python\to_powershell',
        [string] $DestinationPath2 = 'C:\Users\harry\projects\Make_Fake\powershell\to_excel',
        [string] $DestinationPath3 = 'C:\Users\harry\OneDrive - Service-Centric Solutions\Make_Fake Data'
    )

    begin {
        Import-Module ImportExcel

        $DataPath = "$DestinationPath1\data.csv"
        $TitlePath = "$DestinationPath1\title.txt"

        $Data = Get-Content $DataPath
        $Title  = Get-Content $TitlePath
    }
    
    process {
        $Data | ConvertFrom-Csv | Export-Excel "$DestinationPath2\$Title.xlsx"
    }

    end{
        Remove-Item $DataPath,$TitlePath
        Copy-Item `
            "$DestinationPath2\$Title.xlsx" `
            "$DestinationPath3\$Title.xlsx"
    }
 
}

Build-FakeSpreadsheets