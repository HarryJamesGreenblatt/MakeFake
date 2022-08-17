'''
NAME
    Make_Fake_Launcher.py


PURPOSE



FUNCTIONS
        #1 Instantiates a new Make_Fake Class based on a given category profile
        #2 Writes 4 Excel files representing a Fake Company's Employee, Customer, Inventory, and Transaction  Data
        #3 Summarizes and uploads to OneDrive a list of the attributes related to the Class.


DEPENDENCIES
        Make_FakeCompany.py\n
'''
def Launch_Make_Fake( params : dict ):
    '''
    NAME
        Launch_Make_Fake


    SYNOPSIS
        


    DESCRIPTION
        


    PROCESS
        #1)
            Define  respective paths to temporary  'staging files'  used\n
            for capturing each dataset in csv format, to be collected in\n 
            a  powershell script  operating in  parallel.\n   

        #2)
            Open a file handle to the provided  paths  and  write  the\n 
            comnpany_data  and the  company_title  to them.\n

        #3)
            Call PowerShell to invoke  Build-FakeSpreadsheets.ps1\n 
            as a  parallel  subprocess\n  


    INPUTS

        <dict>
        params  -  contains the parameterized inputs for the Class constructor.

                            
    OUTPUT

    
    DEPENDENCIES
        Make_FakeCompany.py
    '''
    # 2.^.i   Define  respective paths to temporary  'staging files'  used
    #         for capturing each dataset in csv format, to be collected in 
    #         a powershell script operating in parallel.   
    #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
    if params['category'] == 'Egregiously Overpriced Generic Widget Wholesaler':
        from Make_FakeCompany import FakeCompany
        fake_company = FakeCompany(**params)


    fake_employees = fake_company.MakeFakeEmployees()["As_DataFrame"]
    fake_customers = fake_company.MakeFakeCustomers()["As_DataFrame"]
    fake_inventory = fake_company.MakeFakeInventory()["As_DataFrame"]


    fake_company.To_Excel(

        fake_employees.to_csv(),
        f'{fake_company.Name} - {fake_company.Category} - Employees'

    )

    fake_company.To_Excel(

        fake_customers.to_csv(),
        f'{fake_company.Name} - {fake_company.Category} - Customers'

    )

    fake_company.To_Excel(

        fake_inventory.to_csv(),
        f'{fake_company.Name} - {fake_company.Category} - Inventory'

    )

    fake_company.To_Excel(

        fake_company.MakeFakeTransactions(
            fake_inventory,
            fake_customers, 
            fake_employees.loc[
                fake_employees["Department"] == "Sales"
            ] 
        ).to_csv(),
        
        f'{fake_company.Name} - {fake_company.Category} - Transactions'

    )

    with open(r'C:\Users\harry\OneDrive - Service-Centric Solutions\Make_Fake Data'+f'\{fake_company.Name}.txt', 'w') as To_OneDrive:
        To_OneDrive.write(str(fake_company))