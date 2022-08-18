'''
NAME
    Make_Fake_Launcher.py


PURPOSE
    Instantiates a new Make_Fake Class based on a given category profile,\n
    writes 4 Excel files representing a Fake Company's Employee, Customer,\n
    Inventory, and Transaction Data and Summarizes and uploads to OneDrive a\n
    a list of the attributes related to the Class.


FUNCTION

    #1 Defines  Launch_Make_Fake()  


DEPENDENCIES
        Make_FakeCompany.py\n
'''
def Launch_Make_Fake( params : dict ):
    '''
    NAME
        Launch_Make_Fake


    DESCRIPTION
        Given a Dicitonary of parameters, instantiates the Make_Fake Class corresponding to\n
        a 'category' parameter specified in the input Dictonary, then exports the output produced\n 
        by each of the Class's methods in order for it to be converted to an excel spreadsheet.\n

        Following this, the Class's String Method, which summarizes it's attribute values,\n 
        is exported as a plain text file to a specified OneDrive storage location.


    PROCESS
        # 1.i   Instantiate a new Make_Fake Class based on a given category profile.\n

        # 1.ii  Write 4 Excel files representing a Fake Company's Employee, Customer,\n
                Inventory, and Transaction  Data\n

        # 1.iii Summarize and upload to OneDrive a list of the attributes related to the Class.


    INPUTS

        <dict>
        params  -  contains the parameterized inputs for the Class constructor.

    
    DEPENDENCIES
        Make_FakeCompany.py
    '''
    # 1.i  Instantiate a new Make_Fake Class based on a given category profile.
    ###########################################################################################
    if params['category'] == 'Egregiously Overpriced Generic Widget Wholesaler': 
        from Make_FakeCompany import FakeCompany   #
        fake_company = FakeCompany(**params)       #
        fake_sales_employees = "Sales"             #
    ###########################################################################################


    # 1.ii  Write 4 Excel files representing a Fake Company's Employee, Customer,
    #       Inventory, and Transaction  Data
    ###########################################################################################
    fake_employees = fake_company.MakeFakeEmployees()["As_DataFrame"]  #
    fake_customers = fake_company.MakeFakeCustomers()["As_DataFrame"]  #
    fake_inventory = fake_company.MakeFakeInventory()["As_DataFrame"]  #
                                                                       #
                                                                       #
    fake_company.To_Excel(                                             #
                                                                       #
        fake_employees.to_csv(),                                       #
        f'{fake_company.Name} - {fake_company.Category} - Employees'   #
                                                                       #
    )                                                                  #
                                                                       #
    fake_company.To_Excel(                                             #
                                                                       #
        fake_customers.to_csv(),                                       #
        f'{fake_company.Name} - {fake_company.Category} - Customers'   # 
                                                                       #
    )                                                                  #
                                                                       #
    fake_company.To_Excel(                                             #
                                                                       #
        fake_inventory.to_csv(),                                       #  
        f'{fake_company.Name} - {fake_company.Category} - Inventory'   #
                                                                       #
    )                                                                  #
                                                                       #
    fake_company.To_Excel(                                             #
                                                                       #
        fake_company.MakeFakeTransactions(                             #
            fake_inventory,                                            #
            fake_customers,                                            #
            fake_employees.loc[                                        #
                fake_employees["Department"] == fake_sales_employees   #
            ]                                                          #
        ).to_csv(),                                                    #
                                                                       #
        f'{fake_company.Name} - {fake_company.Category} - Transactions'#
                                                                       #
    )                                                                  #
    ###########################################################################################


    # 1.iii Summarize and upload to OneDrive a list of the attributes related to the Class.
    ###########################################################################################
    with open(                                      #
        r'C:\Users\harry\OneDrive - Service-Centric Solutions\Make_Fake Data' 
        +                                           #
        f'\{fake_company.Name}.txt', 'w'            #
    ) as To_OneDrive:                               #
        To_OneDrive.write(str(fake_company))        #
    ###########################################################################################