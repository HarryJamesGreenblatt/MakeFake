function New-FakeCompany {
<#
    .SYNOPSIS
    Initializes the python virtual environment and runs the Make_FakeCompany.py Client. 

    .DESCRIPTION
    Ensures the availability of the required dependencies by loading the python virtual environment 
    containing all modules associated with the to project.

    The  Make_FakeCompany.py  class file contains a Client script that, when invoked directly, executes  
    a series of instructions producing  4 Excel Spreadsheets  which capture the  randomly generated fake 
    data produced by the  Make_FakeCompany Class's  MakeFakeEmployees,  MakeFakeCustomers,  
    MakeFakeInventory,  and  MakeFakeTransactions  methods.

    .PARAMETER VirtualEnv
    The file path to the python Virtual Environment.

    .PARAMETER PythonScript
    The filepath the Make_FakeConmpany.py

    .INPUTS
    None.

    .OUTPUTS
    Does not produce output, but causes a side effect of generating 4 Excel Spreadsheets a capturing all  
    Make_FakeCompany  data.
#>
    [CmdletBinding()]
 
    param (

        [string] $Name,
        [string] $Category,
        [Int32]  $EmployeeSize,
        [Int32]  $CustomerSize,
        [Int32]  $InventorySize,
        [string] $City,
        [string] $State,

        [string] $VirtualEnv = 'C:\Users\harry\python\thunderDome\Scripts\Activate.ps1',   

        [string] $PythonScript = 'C:\Users\harry\projects\Make_Fake\python\Make_FakeCompany.py'
    )

    begin {
        & $VirtualEnv
    }
    
    process {
        python $PythonScript $Name $Category $EmployeeSize $CustomerSize $InventorySize $City $State
    }
 
 }

 Export-ModuleMember -Function New-FakeCompany