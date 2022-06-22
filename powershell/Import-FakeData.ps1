function Import-FakeData {
   <#
   .SYNOPSIS
   
   .DESCRIPTION
   
   .NOTES   
   
   .PARAMETER VirtualEnv
   
   .PARAMETER PythonScript
   
   .INPUTS
   
   .OUTPUTS
   #>
    [CmdletBinding()]
 
    param (
        [string] $VirtualEnv = 'C:\Users\harry\python\thunderDome\Scripts\Activate.ps1',   
        [string] $PythonScript = '..\python\Make_FakeCompany.py'
    )

    begin {
        & $VirtualEnv
    }
    
    process {
       python $PythonScript
    }
 
 }

 Import-FakeData