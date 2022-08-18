'''
NAME
    Make_Fake_Launcher.py


PURPOSE
    A client to facilitate the invocation of the  Launch_Make_Fake  function.


FUNCTION
    # 1 Defines  Launch_Make_Fake()  


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
    if params['category'] == 'Egregiously Overpriced Generic Widget Wholesaler': # if the 
        from Make_FakeCompany import FakeCompany      #'category' parameter matches a Widget
        fake_company = FakeCompany(**params)          # Wholesaler, instantiate the FakeCompany
        fake_sales_employees = "Sales"                # class, which has 'Sales' employees.
    ###########################################################################################


    # 1.ii  Write 4 Excel files representing a Fake Company's Employee, Customer,
    #       Inventory, and Transaction  Data
    ###########################################################################################
    fake_employees = fake_company.MakeFakeEmployees()["As_DataFrame"]  # Store the results of 
    fake_customers = fake_company.MakeFakeCustomers()["As_DataFrame"]  # each Make_Fake method
    fake_inventory = fake_company.MakeFakeInventory()["As_DataFrame"]  # in variables 
                                                                       # corresponding to 
                                                                       # 
    fake_company.To_Excel(                                             # 
                                                                       # fake_employees 
        fake_employees.to_csv(),                                       # fake_customers  
        f'{fake_company.Name} - {fake_company.Category} - Employees'   # and 
                                                                       # fake_inventory
    )                                                                  # 
                                                                       # 
    fake_company.To_Excel(                                             # invoke the Make_Fake  
                                                                       # To_Excel method  
        fake_customers.to_csv(),                                       # to export the    
        f'{fake_company.Name} - {fake_company.Category} - Customers'   # fake_employee data   
                                                                       # 
    )                                                                  # 
                                                                       # invoke the Make_Fake   
    fake_company.To_Excel(                                             # To_Excel method   
                                                                       # to export the     
        fake_inventory.to_csv(),                                       # fake_customer data   
        f'{fake_company.Name} - {fake_company.Category} - Inventory'   # 
                                                                       # 
    )                                                                  # invoke the Make_Fake   
                                                                       # To_Excel method     
    fake_company.To_Excel(                                             # to export the      
                                                                       # fake_inventory data     
        fake_company.MakeFakeTransactions(                             # 
            fake_inventory,                                            # 
            fake_customers,                                            # 
            fake_employees.loc[                                        # invoke the Make_Fake    
                fake_employees["Department"] == fake_sales_employees   # To_Excel method      
            ]                                                          # to export the      
        ).to_csv(),                                                    # Transaction data    
                                                                       # produced by the    
        f'{fake_company.Name} - {fake_company.Category} - Transactions'# MakeFakeTransactions 
                                                                       # method.
    )                                                                  #
    ###########################################################################################


    # 1.iii Summarize and upload to OneDrive a list of the attributes related to the Class.
    ###########################################################################################
    with open(                                      # Open a file handle associated via the 
        r'C:\Users\harry\OneDrive - Service-Centric Solutions\Make_Fake Data' 
        +                                           # specified OneDrive file path, and then
        f'\{fake_company.Name}.txt', 'w'            # write the Make_Fake Class's string
    ) as To_OneDrive:                               # representation, a list of Class Attributes,
        To_OneDrive.write(str(fake_company))        # to the specified OneDrive path as a .txt
    ###########################################################################################