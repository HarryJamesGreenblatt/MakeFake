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

    .PARAMETER Name
    Defines the Name of the Fake Company to which each of the Reports reffer. 

    .PARAMETER Category
    Selects which  Category Profile  will be used to generate each of the the Fake Company Reports.

    .PARAMETER EmployeeSize
    Defines the number of Employee Records that are procuded in the Fake Company's Employee Report.

    .PARAMETER CustomerSize
    Defines the number of Customer Records that are procuded in the Fake Company's Customer Report.

    .PARAMETER InventorySize
    Defines the number of Inventory Records that are procuded in the Fake Company's Inventory Report.

    .PARAMETER City
    Defines which US City the Fake Company's Records will reflect.

    .PARAMETER State
    Defines which US State the Fake Company's Records will reflect. 
    Must be a 2-letter State Abbreviaiton,  i.e.  California -> CA.

    .PARAMETER VirtualEnv
    The file path to the python Virtual Environment.

    .PARAMETER PythonScript
    The filepath the Make_FakeConmpany.py

    .INPUTS
    Power Automate Desktop Flow
        'Create A New-FakeCompany With The Make_Fake Form' Outputs
            Name           
            Category       
            EmployeeSize   
            CustomerSize     
            InventorySize  
            City           
            State    

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
        [string] $PythonScript = 'C:\Users\harry\dev\projects\Make_Fake\python\Make_FakeCompany.py'
    )

    process {
        python $PythonScript $Name $Category $EmployeeSize $CustomerSize $InventorySize $City $State
    }
 
 }

 Export-ModuleMember -Function New-FakeCompany