'''
NAME
    Make_FakeRestaurant.py


PURPOSE
    Loads neccessary  external  modules   and   classes,  and provides internal  class\n
    definitions for the  FakeRestaurant  subclass, which inhereits from the FakeCompany\n  
    superclass.


FUNCTIONS  
    #1 Imports the necessary dependencies, including the   FakeCompany  superclass.

    #2 Defines The  FakeRestaurant  subclass, which inherits from the  FakeCompany  superclass.


DEPENDENCIES
    Project File:
        Make_FakeCompany.py\n

    Third Party Module:\n
        pandas\n
'''
# 1) Imports the necessary dependencies, including the  FakeCompany  superclass.
#####################################################################################################
from pandas import DataFrame, Series, concat
from Make_FakeCompany  import FakeCompany, phony, fake
#####################################################################################################



# 2) Defines The  FakeRestaurant  subclass, which inherits from the  FakeCompany  superclass.
#####################################################################################################
class FakeRestaurant( FakeCompany ):
    '''
    NAME
        FakeRestaurant.py


    SYNOPSIS
        A  subclass  which  inherits  from the  FakeCompany  superclass \n
        that is modeled to simulate a restaurant. 


    COMPONENTS
        #2._) Overload Of The  FakeCompany  Constructor
            __init__()

        #2.E) Overload  Of The  FakeCompany  MakeFakeEmployees  Method 
            MakeFakeEmployees()  

        #2.C) Overload  Of The  FakeCompany  MakeFakeCustomers  Method
            MakeFakeCustomers()  

        #2.I) Overload  Of The  FakeCompany  MakeFakeInventory  Method
            MakeFakeInventory()

        #2.T)  Overload  Of The  FakeCompany  MakeFakeTransactions  Method
            MakeFakeTransactions()     


    ATTRIBUTE PARAMETERS
        name           -     Defines the Fake Restaurant's Name\n
                             DEFAULT VALUE:  random fake restaurant name\n 

        category       -     Defines what type of Fake Restaurant it is\n
                             DEFAULT VALUE:  random fake restaurant type\n

        employee_size  -     Defines the number of records to be produced for "Employee"
                             or Personnel reports\n
                             DEFAULT VALUE:  random  integer  between  1  and  100\n
        
        customer_size   -    Defines the number of records to be produced for "Customer" 
                             or "Transaction" reports\n
                             DEFAULT VALUE:  random  integer  between  1  and  750\n
        
        inventory_size   -   Defines the number of records to be produced for "Inventory" 
                             reports\n
                             DEFAULT VALUE:  random  integer  between  1  and  750\n

        city            -    Defines the  US City  where the Restaurant is located\n
                             DEFAULT VALUE:  random  fake  or  existing  US City\n

        state           -    Defines the  2-letter US State Abbreviation  where the Restaurant is 
                             located\n
                             DEFAULT VALUE:  random  existing   2-letter US State Abbreviation\n 
   
        zip_code        -    Defines the  US Zip Code  where the Restaurant is located\n
                             DEFAULT VALUE:  random  fake  or  existing  US Zip Code\n

        departments     -    Defines the list of possible departments to which employees at this 
                             Restaurant might belong\n
                             DEFAULT VALUE:  Management, Bar Staff, Wait Staff, Kitchen Staff\n  

    
    EXAMPLE OUTPUT


    PARENT MODULE
        FakeCompany.py
    '''

    # 2._) Overload Of The FakeCompany  Constructor  
    ############################################################################
    def __init__(                                               # 
    self,                                                       # 
    name = phony.Choice()                                       #
    ([                                                          #
        'A ' +                                                  #
        phony.Choice()(['Taste', 'Pinch', 'Dash']) +            #
        ' of ' +                                                #
        phony.Text().word().title(),                            #
                                                                #
        'The ' +                                                #
        phony.Text().word().title() +                           #
        ' ' +                                                   #
        phony.Choice()(['Spoon', 'Fork', 'Knife', 'Plate'])     #
    ]),                                                         #
    category        =  "Restaurant",                            #
    employee_size   =  phony.Numeric().integer_number(1,100),   #
    customer_size   =  phony.Numeric().integer_number(100,1500),#
    inventory_size  =  phony.Numeric().integer_number(1,750),   #
    city            =  fake.city(),                             #
    state           =  fake.state_abbr(),                       #
    zip_code        =  fake.zipcode(),                          #
    departments     =  [                                        #
        "Management",                                           #
        "Bar Staff",                                            #
        "Wait Staff",                                           #
        "Kitchen Staff",                                        #
    ]                                                           #
    ):                                                          #
        self.Name          =  name                              #
        self.Category      =  category                          #
        self.EmployeeSize  =  employee_size                     #
        self.CustomerSize  =  customer_size                     #
        self.InventorySize =  inventory_size                    #
        self.City          =  city                              #
        self.State         =  state                             #
        self.ZipCode       =  fake.zipcode_in_state(state)      #
        self.Departments   =  departments                       # 
    ############################################################################


    # 2.E) Overload  Of The  FakeCompany  MakeFakeEmployees Method  
    ############################################################################
    def MakeFakeEmployees(self):
        '''
        NAME
            MakeFakeEmployees


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to ressemble a\n
            simplified Payroll for a Restaurant.


        DESCRIPTION
            An  Overload  for the  FakeCompany.MakeFakeEmployees() Method\n
            which modifies a  copy  of the  superclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an\n
            Restaurant.\n 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Restaurant" profile, the  copy\n
            is then returned as output, thereby replacing the\n
            the original end value of the  superclass's MakeFakeEmployees() 
            Method.   


        PROCESS
            #2.E.i 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakeEmployees  Method  to simplify code\n
                refactoring efforts.      

            #2.E.ii 
                Replace any  Payroll Attributes  which are inconsistent\n 
                with the  FakeRestaurant's Profile  with  adjusted values. 

            #2.E.iii 
                Filter out any remaining  Coulumn Attributes which are\n
                inconsistent with a  Restaurant Customers  Data Context.  
                 
            #2.E.iv
                Export the  Fake Payroll,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Payroll's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            FakeCompany
        '''

        # 2.E.i)   Retrieve a copy of the  Fake Payroll Dictionary  produced by  
        #            the superclass's  MakeFakeEmployees  Method  to simplify code
        #            refactoring efforts      
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#       
        FakeRestaurantEmployees = FakeCompany(          # 
            name                =   self.Name,          # The FakeCompany 
            category            =   self.Category,      # (superclass)  
            employee_size       =   self.EmployeeSize,  # MakeFakeEmployees Method 
            inventory_size      =   self.InventorySize, # MakeFakeInventory Method 
            customer_size       =   self.CustomerSize,  # MakeFakecustomers Method 
            city                =   self.City,          # is invoked using  
            state               =   self.State,         # the  FakeRestaurant 
            zip_code            =   self.ZipCode,       # (subclass) constructor 
            departments         =   self.Departments    # parameters
        ).MakeFakeEmployees()['As_OrderedDict']         #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        
        # 2.E.ii)   Replace any  Payroll Attributes  which are inconsistent 
        #            with the  FakeRestaurant's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        FakeRestaurantEmployees["Date Of Birth"] = [  # 
                                                      #  
            phony.Datetime().date(                    # Adjust the default range     
                1985,                                 # of Employee Birth Dates    
                2000                                  # to simulate a younger  
            ).strftime('%m/%d/%Y')                    # demographic,  
                                                      # for each of the        
            for _ in range(self.EmployeeSize)         # 'EmployeeSize' many rows     
                                                      # 
        ]                                             #
                                                      #
        FakeRestaurantEmployees["Salary"]       =  [  # Adjust the default range    
                                                      # of Employee Salaries   
            phony.Finance().price(50000, 75500)       # to simulate low income  
                                                      # levels, 
            for _ in range(self.EmployeeSize)         # for each of the       
                                                      # 'EmployeeSize' many rows    
        ]                                             # 
                                                      # 
        FakeRestaurantEmployees['Employee ID']  = [   # Adjust the default range      
                                                      # of Employee ID Numbers    
            fake.iana_id()[5:8]                       # to not exceed 5 digits
            +                                         #
            fake.iana_id()[:3]                        #
                                                      # in length,   
            for _ in range(self.EmployeeSize)         # for each of the       
                                                      # 'EmployeeSize' many rows    
        ]                                             #
                                                      #
        FakeRestaurantEmployees["Email"]   =  [       # 
                                                      #
            phony.Choice()                            #
            ([                                        #
                                                      #
                phony.Person().email(),               #
                                                      #
                phony.Choice()([                      # '.', and appends the   
                    record[0].lower(),                #
                    record[0][0],                     #
                ])                                    # Replace the default          
                +                                     # Email with a list      
                phony.Choice()([                      # '.', and appends the   
                    '.',                              #
                    '_',                              #
                    '',                               #
                ])                                    # produced via a      
                +                                     # comprehension that     
                phony.Choice()([                      # '.', and appends the   
                    record[1].lower(),                #
                    record[1][0],                     #
                ])                                    # concatenates each    
                +                                     # Employee Record's    
                '@'                                   # First and Last Name,     
                +                                     # deliminates them with a      
                phony.Choice()([                      # '.', and appends the   
                    'google',                         #
                    'yahoo',                          #
                    'outlook'                         #
                ])                                    #
                +                                     #
                '.com'                                #
            ])                                        #
                                                      # result with the object's  
            for record in zip(                        # Domain Attribute,thereby     
                FakeRestaurantEmployees["First Name"],# simulating a   
                FakeRestaurantEmployees["Last Name"]  # Domain-joined Email   
            )                                         # Address,  
                                                      # for each of the                                     
        ]                                             # 'employee_size' many rows 
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 2.E.iii)  Filter out any  Coulumn Attributes which are inconsistent
        #           with a  Restaurant Customers  Data Context.  
        #|||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||#
        del (                                         #
            FakeRestaurantEmployees['Username'],      #
            FakeRestaurantEmployees['Password']       #
        )                                             #
        #|||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||#

        # 2.E.iv)   Export the  Fake Payroll,  which is now a   dict of lists.     
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return {                                      # Returns a dict of dicts 
            'As_OrderedDict': FakeRestaurantEmployees,# which makes accessible   
            'As_DataFrame'  : DataFrame(              # multiple output formats, 
                FakeRestaurantEmployees               # including both a python    
            )                                         # OrdredDict  and  a pandas  
        }                                             # DataFrame.
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    ############################################################################


    # 2.C) A Method To Generate A Fake, Randomized "Customers" Dictionary
    ############################################################################
    def MakeFakeCustomers(self):
        '''
        NAME
            MakeFakeCustomers


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            collection of  "Customer" Clients  belonging to a company\n 
            specializing in  Fitness  and  Nutrition  Services.


        DESCRIPTION
            Utililizes the  FakeRestaurant.MakeFakeEmployees() Method\n
            Overload,  which modifies a  copy  of the  supclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an Athletic Club. 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then re-modified in a process where the FakeRestaurant's\n
            adjusted attriubutes are filtered to simulate a data context\n
            resembling  Athletic Club Clients,  a.k.a. "Customers",  rather\n
            than  Athletic Club Employees. 


        PROCESS
            #2.C.i) 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakeEmployees  Method  to simplify code\n
                refactoring efforts.      

            #2.C.ii) 
                Filter out any  Coulumn Attributes which are not consistant\n
                with a  Restaurant Customers  Data Context.  

            #2.C.iii) 
                Export  FakeRestaurantCustomers  as a  dictionary  containing versions\n 
                of itself in  multiple formats.      


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to  Column Attribute Names\n
            amd whose  values  correspond to "rows" or "records" of  Customers.
        '''

        # 2.C.i)   Retrieve a copy of the  Fake Payroll Dictionary  produced   
        #          by the superclass's  MakeFakeEmployees  Method  to simplify 
        #          code refactoring efforts. 
        #|||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
        FakeRestaurantCustomers = FakeCompany(          # FakeCompany's 
            name                =   self.Name,          # (superclass)  
            category            =   self.Category,      # MakeFakeEmployees 
            employee_size       =   self.EmployeeSize,  # is invoked using  
            customer_size       =   self.CustomerSize,  # is invoked using  
            inventory_size      =   self.InventorySize, # is invoked using  
            city                =   self.City,          # the  FakeRestaurant 
            state               =   self.State,         # (subclass) constructor 
            zip_code            =   self.ZipCode,       # parameters
            departments         =   self.Departments    #
        ).MakeFakeCustomers(                            # the has_custom_size  
            has_custom_size =   True,                   # switch indicates  
            custom_size     =   self.CustomerSize       # the dict's length will 
        )['As_OrderedDict']                             # match the  CustomerSize
        #|||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#

        # 2.C.ii)  Filter out any  Coulumn Attributes which are inconsistent
        #          with a  Restaurant Customers  Data Context.  
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
        del(                                           #
            FakeRestaurantCustomers["Username"],       #
            FakeRestaurantCustomers["Password"],       #
            FakeRestaurantCustomers["Email"],          #
            FakeRestaurantCustomers["Phone Number"],   #
            FakeRestaurantCustomers["Address"],        #
            FakeRestaurantCustomers["City"],           #
            FakeRestaurantCustomers["State"],          #
            FakeRestaurantCustomers["Zip Code"]        #
        )                                              #
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#

        # 2.C.iii)  Export  FakeRestaurantCustomers  as a  dictionary  
        #           containing versions of itself in  multiple formats.     
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
        return {                                       # Returns a dict of dicts 
            'As_OrderedDict': FakeRestaurantCustomers, # which makes accessible  
            'As_DataFrame'  : DataFrame(               # multiple output formats,
                FakeRestaurantCustomers                # including both a python     
            )                                          # OrdredDict  and a   
        }                                              # pandas DataFrame.
        #||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||#
    #############################################################################


   # 2.I) Overload  Of The  FakeCompany  MakeFakeInventory  Method  
    ############################################################################
    def MakeFakeInventory(self):
        '''
        NAME
            MakeFakeInventory


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to ressemble a\n
            simplified Payroll for a Restaurant.


        DESCRIPTION
            An  Overload  for the  FakeCompany.MakeFakeInventory() Method\n
            which modifies a  copy  of the  superclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an\n
            Restaurant.\n 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Restaurant" profile, the  copy\n
            is then returned as output, thereby replacing the\n
            the original end value of the  superclass's MakeFakeInventory() 
            Method.   


        PROCESS
            #2.E.i 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakeInventory  Method  to simplify code\n
                refactoring efforts.      

            #2.E.ii 
                Replace any  Payroll Attributes  which are inconsistent\n 
                with the  FakeRestaurant's Profile  with  adjusted values. 
                 
            #2.E.iii
                Export the  Fake Payroll,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Payroll's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            FakeCompany
        '''

        # 2.I.i)   Retrieve a copy of the  Fake Payroll Dictionary  produced by  
        #          the superclass's  MakeFakeInventory  Method  to simplify code
        #          refactoring efforts      
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#       
        FakeRestaurantInventory = FakeCompany(          # 
            name                =   self.Name,          # The FakeCompany 
            category            =   self.Category,      # (superclass)  
            employee_size       =   self.EmployeeSize,  # MakeFakeInventory Method 
            inventory_size      =   self.InventorySize, # MakeFakeInventory Method 
            customer_size       =   self.CustomerSize,  # MakeFakecustomers Method 
            city                =   self.City,          # is invoked using  
            state               =   self.State,         # the  FakeRestaurant 
            zip_code            =   self.ZipCode,       # (subclass) constructor 
            departments         =   self.Departments    # parameters
        ).MakeFakeInventory()['As_OrderedDict']         #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        
        # 2.I.ii)   Replace any  Payroll Attributes  which are inconsistent 
        #           with the  FakeRestaurant's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        FakeRestaurantInventory["Product ID"] = [    # 
            phony.Choice()                           #
            ([                                       # A random "Product ID"       
                fake.iban()[3:7],                    # for each of the      
                fake.iban()[4:5]                     #
                +                                    # inventory_size  many rows   
                fake.iban()[1:4]                     #
            ])                                       # 
            for _ in range( int(self.InventorySize) )#                                        
        ]                                            #
                                                     #
        FakeRestaurantInventory["Product"] = [       # 
            phony.Choice()                           #
            ([                                       # A random "Product ID"       
                phony.Food().spices(),               #
                phony.Food().vegetable(),            #
                phony.Food().fruit()                 #
            ])                                       # 
            for _ in range( int(self.InventorySize) )#      
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
                                                     #
        FakeRestaurantInventory["Unit"] =   [        #                                 
                                                     # python's random module's  
            "Lbs."                                   #
                                                     #
            for _ in range(int(self.InventorySize))  # inventory_size many rows 
        ]                                            #     
                                                     #
        FakeRestaurantInventory["Cost Per Unit"] = [ #                                      
                                                     # python's random module's  
             phony.Finance().price(                  # between: 
                1,                                   #  
                8                                    #  A phony, randomized     
            )                                        #
                                                     #
            for _ in range(int(self.InventorySize))  # inventory_size many rows 
        ]                                            #     
                                                     # 'EmployeeSize' many rows    
                                                     #                                           
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 2.I.iii)  Filter out any  Coulumn Attributes which are inconsistent\n
        #           with a  Restaurant Inventory  Data Context.  
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
        del (
            FakeRestaurantInventory['Year'], 
            FakeRestaurantInventory['Price']
        )
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#

        # 2.I.iv)   Export  FakeRestaurantInventory  as a  dictionary  
        #           containing versions of itself in  multiple formats.     
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return {                                      # Returns a dict of dicts 
            'As_OrderedDict': FakeRestaurantInventory,# which makes accessible   
            'As_DataFrame'  : DataFrame(              # multiple output formats, 
                FakeRestaurantInventory               # including both a python    
            )                                         # OrdredDict  and  a pandas  
        }                                             # DataFrame.
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    ############################################################################


        # 2.T) Overload  Of The  FakeCompany  MakeFakeTransactions  Method
    #############################################################################
    def MakeFakeTransactions( self, fake_inventory, fake_customers, fake_sales_employees ):
        '''
        NAME
            MakeFakeTransactions


        SYNOPSIS
            Concatenates the  pandas  DataFrame objects  produced via  the\n 
            MakeFakeCustomers()  and the   MakeFakeInventory()  methods into\n
            a  new dataset,  simulating a  Transaction History  between their\n    
            combined records.\n


        DESCRIPTION
            Following instantiation of the FakeCompany superclass, should it's\n
            MakeFakeCustomers()  and  MakeFakeInventory()  methods be invoked,\n
            respective dictionaries are produced, each contaning  pandas\n
            DataFrame objects (accessible by calling with ['AsDataFrame']\n
            specfied).\n

            The respective  DataFrame objects  can then be used as input to\n
            the  MakeFakeTransactions  method, which will use  pandas \n
            concat() method  to essentially glue the two datasets together,\n
            taking certain considerations depending on which of the two \n
            input data sets has a larger size.\n


        PROCESS
            #2.T.i)
                Store the  larger_size  of the two  DataFrame  inputs.  


            #2.T.ii)
                Use the  pandas.concat()  method  to export a  new  pandas   
                DataFrame  consisting  of  merged data  from both input  
                sources.            


        INPUTS
            <pandas.DataFrame> 
            fake_inventory        -   The  DataFrame  produced by invoking\n 
                                      FakeCompany().MakeFakeInventory['AsDataFrame']

            <pandas.DataFrame> 
            fake_customers        -   The  DataFrame  produced by invoking\n 
                                      FakeCompany().MakeFakeCustomers['AsDataFrame']

            <pandas.DataFrame> 
            fake_sales_employees  -   The  DataFrame  produced by invoking\n 
                                      FakeCompany().MakeFakeCustomers['AsDataFrame']
                                      and then filtering by the "Sales" Department


        OUTPUT
            A  new  pandas  DataFrame  object representing a  Transaction\n
            History  composed  of  concatenated  fake_inventory  and\n
            fake_customers  data.    


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        # 2.T.i)     Store the  lesser_size  of the two  DataFrame  inputs.  
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        greater_size = (                                  # let  greater_size  be
                                                         # the length of the 
            len(fake_inventory)                          # fake_inventory input
                                                         # if it is larger than
            if                                           # the fake_customers
                len(fake_inventory) > len(fake_customers)# input, 
                                                         #
            else                                         # otherwise,
                len(fake_customers)                      # greater_size will be 
                                                         # the length of
        )                                                # fake_customers
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.T.ii)    Use the  pandas.concat()  method  to export a  new  pandas   
        #            DataFrame  consisting  of  merged data  from both input  
        #            sources.           
        #|||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        return concat(                              # Since the  fake_inventory
            [                                       # and  fake_customers  are
                                                    # DataFrame objects, 
                Series(                             # accessing one of their 
                    [                               # 'columns' returns a 
                        fake.isbn10()               # pandas  Series  object.
                        for _ in range(greater_size)# 
                    ],                              # As such, concat() can 
                    name='Transaction ID'           # take a  list  consisting 
                ),                                  # of a sequence of 
                                                    # pandas Series represented
                Series(                             # 
                    [                               # The columns will consist of: 
                        phony.Choice()              #   
                        (                           #   A randomly selected 
                            fake_customers[         #       Employee's "Employee ID"
                                'Customer ID'       #   for each of the lesser_size
                            ].to_list()             #   many rows
                        )                           #
                        for _ in range(greater_size)#
                    ],                              # 
                    name='Customer ID'              #   and
                ),                                  # combine those columns
                                                    # into a new DataFrame object.
                Series(                             # 
                    [                               # The columns will consist of: 
                        phony.Choice()              #   
                        (                           #   A randomly selected 
                            fake_sales_employees[   #       Employee's "Employee ID"
                                'Employee ID'       #   for each of the lesser_size
                            ].to_list()             #   many rows
                        )                           #
                        for _ in range(greater_size)#
                    ],                              # 
                    name='Employee ID'              #   and
                ),                                  #
                                                    # into a new DataFrame object.
                Series(                             # 
                    [                               # The columns will consist of: 
                        phony.Choice()              #   
                        ([                          #       Employee's "Employee ID"
                            phony.Food().dish(),    #   for each of the lesser_size
                            phony.Food().drink()    #   for each of the lesser_size
                        ])                          #
                        for _ in range(greater_size)#
                    ],                              # 
                    name='Menu Item'                #   and
                ),                                  #
                                                    # into a new DataFrame object.
                Series(                             # 
                    [                               # The columns will consist of: 
                        phony.Choice()              #   
                        (                           #   A randomly selected 
                            fake_inventory[         #       Employee's "Employee ID"
                                'Product'           #   for each of the lesser_size
                            ].to_list()             #   many rows
                        )                           #
                        for _ in range(greater_size)#
                    ],                              # 
                    name='Main Ingredient'          #   and
                ),                                  #
                                                    # into a new DataFrame object.
                Series(                             # 
                    [                               # The columns will consist of: 
                        phony.Choice()              #   
                        (                           #   A randomly selected 
                            fake_inventory[         #       Employee's "Employee ID"
                                'Product'           #   for each of the lesser_size
                            ].to_list()             #   many rows
                        )                           #
                        for _ in range(greater_size)#
                    ],                              # 
                    name='Secondary Ingredient'     #   and
                ),                                  #
                                                    #   A column consisting of  
                                                    #   the fake Customer's  "Card Number" column,
                Series(                             #   along with the "Card Provider" column
                    [                               #   and the corresponding "Price" column
                        phony.Choice()              #
                        ([                          # are then combined with 
                            phony.Finance(          #                            
                            ).price(                # A 'Transaction ID'  
                                12,                 # derived by  fake's method 
                                70                  # for producing 10 digit
                            )                       # isbns.
                        ])                          #
                        for _ in range(greater_size)# and 
                    ],                              #                         
                    name='Payment'                  # A 'Quantity Sold' 
                ),                                  # 
                                                    #   the fake Customer's  "Card Number" column,
                Series(                             #   along with the "Card Provider" column
                    [                               #   and the corresponding "Price" column
                        phony.Choice()              #
                        ([                          # are then combined with 
                            phony.Numeric(          #                            
                            ).integer_number(       # A 'Transaction ID'  
                                1,                  # derived by  fake's method 
                                4                   # for producing 10 digit
                            )                       # isbns.
                        ])                          #
                        for _ in range(greater_size)# and 
                    ],                              #                         
                    name='Quantity'                 # A 'Quantity' 
                ),                                  # 
                                                    # and
                Series(                             #  
                    [                               # A 'Payment Date'  
                        phony.Datetime().date(      # derived from  phony's   
                            2020,                   # method for producing  
                            2022                    # select dates between   
                        ).strftime('%m/%d/%Y')      # specified ranges. 
                                                    #
                        for _ in range(greater_size)# 
                    ],                              # 
                    name='Payment Date'             # passing the axis=1 option                                     
                )                                   # ensures the proper format  
                                                    # for the resulting   
            ],                                      # DataFrame object.   
                                                    # 
            axis=1                                  # Once the core columns are   
                                                    # concatenated, the deltas  
        ).dropna().rename(                          # bewteen the datasets are
            columns={                               # accounted for simply by   
                                                    # throwing away any 'na',   
                0:'Customer Name',                  # a.k.a empty values, then   
                1:'Customer Address'                # 'shuffling' the  dataset by    
            }                                       # sorting the DataFrame by the   
        ).sort_values("Transaction ID")             # 'Transaction ID'.
        #|||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||||
#####################################################################################################