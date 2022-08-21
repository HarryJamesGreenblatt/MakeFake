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
        Name: The Driver Knife\n
        Category: Restaurant\n
        Domain: The-Driver-Knife.net\n
        # of Employees: 72\n
        # of Customers: 116\n
        # of Inventory Items: 692\n
        City:  Webstermouth\n
        State: RI\n
        Zip Code: 02893\n
        Departments: [\n
        'Management',
        'Bar Staff',
        'Wait Staff',
        'Kitchen Staff',
        ]\n
        Employee Attributes: [\n
        'Employee ID',
        'First Name',
        'Last Name',
        'Email',
        'Date Of Birth',
        'SSN',
        'Phone Number',
        'Address',
        'City',
        'State',
        'Zip Code',
        'Hire Date',
        'Salary',
        'Department',
        ]\n
        Customer Attributes: [\n
        'Customer ID',
        'First Name',
        'Last Name',
        'Card Provider',
        'Card Number',
        'CVV',
        'Expiration Date',
        ]\n
        Inventory Attributes: [\n
        'Product ID',
            'Product',
            'Product Quantity',
            'Unit',
            'Cost Per Unit',
        ]\n

    PARENT MODULE
        FakeCompany.py
    '''

    # 2._) Overload Of The FakeCompany  Constructor  
    #################################################################################################
    def __init__(                                                 # 
    self,                                                         # 
    name = phony.Choice()                                         #
    ([                                                            #
        'A ' +                                                    #
        phony.Choice()(['Taste', 'Pinch', 'Dash']) +              #
        ' of ' +                                                  #
        phony.Text().word().title(),                              #
                                                                  #
        'The ' +                                                  #
        phony.Text().word().title() +                             #
        ' ' +                                                     #
        phony.Choice()(['Spoon', 'Fork', 'Knife', 'Plate'])       #
    ]),                                                           #
    category        =  "Restaurant",                              #
    employee_size   =  phony.Numeric().integer_number(1,100),     #
    customer_size   =  phony.Numeric().integer_number(100,1500),  #
    inventory_size  =  phony.Numeric().integer_number(1,750),     #
    city            =  fake.city(),                               #
    state           =  fake.state_abbr(),                         #
    zip_code        =  fake.zipcode(),                            #
    departments     =  [                                          #
        "Management",                                             #
        "Bar Staff",                                              #
        "Wait Staff",                                             #
        "Kitchen Staff",                                          #
    ]                                                             #
    ):                                                            #
        self.Name          =  name                                #
        self.Category      =  category                            #
        self.EmployeeSize  =  employee_size                       #
        self.CustomerSize  =  customer_size                       #
        self.InventorySize =  inventory_size                      #
        self.City          =  city                                #
        self.State         =  state                               #
        self.ZipCode       =  fake.zipcode_in_state(state)        #
        self.Departments   =  departments                         # 
    #################################################################################################


    # 2.E) Overload  Of The  FakeCompany  MakeFakeEmployees Method  
    #################################################################################################
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
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        FakeRestaurantEmployees = FakeCompany(               # 
            name                =   self.Name,               # The FakeCompany 
            category            =   self.Category,           # (superclass)  
            employee_size       =   self.EmployeeSize,       # MakeFakeEmployees Method 
            inventory_size      =   self.InventorySize,      # MakeFakeInventory Method 
            customer_size       =   self.CustomerSize,       # MakeFakecustomers Method 
            city                =   self.City,               # is invoked using  
            state               =   self.State,              # the  FakeRestaurant 
            zip_code            =   self.ZipCode,            # (subclass) constructor 
            departments         =   self.Departments         # parameters
        ).MakeFakeEmployees()['As_OrderedDict']              #
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        
        # 2.E.ii)   Replace any  Payroll Attributes  which are inconsistent 
        #            with the  FakeRestaurant's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        FakeRestaurantEmployees["Date Of Birth"] = [         # 
                                                             #  
            phony.Datetime().date(                           # Adjust the default range     
                1985,                                        # of Employee Birth Dates    
                2000                                         # to simulate a younger  
            ).strftime('%m/%d/%Y')                           # demographic,  
                                                             # for each of the        
            for _ in range(self.EmployeeSize)                # 'EmployeeSize' many rows     
                                                             # 
        ]                                                    #
                                                             #
        FakeRestaurantEmployees["Salary"]       =  [         # Adjust the default range    
                                                             # of Employee Salaries   
            phony.Finance().price(50000, 75500)              # to simulate low income  
                                                             # levels, 
            for _ in range(self.EmployeeSize)                # for each of the       
                                                             # 'EmployeeSize' many rows    
        ]                                                    # 
                                                             # 
        FakeRestaurantEmployees['Employee ID']  = [          # Adjust the default range      
                                                             # of Employee ID Numbers    
            fake.iana_id()[5:8]                              # to not exceed 5 digits
            +                                                #
            fake.iana_id()[:3]                               #
                                                             # in length,   
            for _ in range(self.EmployeeSize)                # for each of the       
                                                             # 'EmployeeSize' many rows    
        ]                                                    #
                                                             #
        FakeRestaurantEmployees["Email"]   =  [              # 
                                                             #
            phony.Choice()                                   #
            ([                                               #
                                                             #
                phony.Person().email(),                      #
                                                             #
                phony.Choice()([                             # '.', and appends the   
                    record[0].lower(),                       #
                    record[0][0],                            #
                ])                                           # Replace the default          
                +                                            # Email with a list      
                phony.Choice()([                             # '.', and appends the   
                    '.',                                     #
                    '_',                                     #
                    '',                                      #
                ])                                           # produced via a      
                +                                            # comprehension that     
                phony.Choice()([                             # '.', and appends the   
                    record[1].lower(),                       #
                    record[1][0],                            #
                ])                                           # concatenates each    
                +                                            # Employee Record's    
                '@'                                          # First and Last Name,     
                +                                            # deliminates them with a      
                phony.Choice()([                             # '.', and appends the   
                    'google',                                #
                    'yahoo',                                 #
                    'outlook'                                #
                ])                                           #
                +                                            #
                '.com'                                       #
            ])                                               #
                                                             # result with the object's  
            for record in zip(                               # Domain Attribute,thereby     
                FakeRestaurantEmployees["First Name"],       # simulating a   
                FakeRestaurantEmployees["Last Name"]         # Domain-joined Email   
            )                                                # Address,  
                                                             # for each of the                                     
        ]                                                    # 'employee_size' many rows 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.E.iii)  Filter out any  Coulumn Attributes which are inconsistent
        #           with a  Restaurant Customers  Data Context.  
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        del (                                                #
            FakeRestaurantEmployees['Username'],             #
            FakeRestaurantEmployees['Password']              #
        )                                                    #
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.E.iv)   Export the  Fake Payroll,  which is now a   dict of lists.     
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return {                                             # Returns a dict of dicts 
            'As_OrderedDict': FakeRestaurantEmployees,       # which makes accessible   
            'As_DataFrame'  : DataFrame(                     # multiple output formats, 
                FakeRestaurantEmployees                      # including both a python    
            )                                                # OrdredDict  and  a pandas  
        }                                                    # DataFrame.
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    #################################################################################################


    # 2.C) A Method To Generate A Fake, Randomized "Customers" Dictionary
    #################################################################################################
    def MakeFakeCustomers(self):
        '''
        NAME
            MakeFakeCustomers


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly generated fake data,\n 
            specifically modeled to resemble a collection of Restaurant "Customers". 
            

        DESCRIPTION
            Utililizes the  FakeRestaurant.MakeFakeEmployees() Method Overload,  which modifies\n
            a  copy  of the  supclass method's resultant dictionary of lists in a way that more \n
            closely simulates a "Restaurant" dataset and specifically ressembles Customer Data.\n 

            Once the  copy  of the  Customer Dictionary  has been adapted to the specificity of the\n 
            "Restaurant" profile, the  copy is then re-modified in a process where the FakeRestaurant's\n
            adjusted attriubutes are filtered to simulate a data context resembling "Customers".


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

        # 2.C.i)   Retrieve a copy of the  Fake Payroll Dictionary  produced by the superclass's  
        #          MakeFakeEmployees  Method  to simplify code refactoring efforts. 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        FakeRestaurantCustomers = FakeCompany(               # 
            name                =   self.Name,               # 
            category            =   self.Category,           # The FakeCompany (superclass)   
            employee_size       =   self.EmployeeSize,       # MakeFakeInventory Method is invoked 
            customer_size       =   self.CustomerSize,       # using the FakeRestaurant (subclass)     
            inventory_size      =   self.InventorySize,      # constructor parameters.    
            city                =   self.City,               # 
            state               =   self.State,              # 
            zip_code            =   self.ZipCode,            # the has_custom_size  switch indicates  
            departments         =   self.Departments         # the dict's length will match the  
        ).MakeFakeCustomers(                                 # CustomerSize  
            has_custom_size =   True,                        # 
            custom_size     =   self.CustomerSize            # 
        )['As_OrderedDict']                                  # 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.C.ii)  Filter out any  Coulumn Attributes which are inconsistent with a Restaurant's
        #          Customers  Data Context.  
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        del(                                                 # 
            FakeRestaurantCustomers["Username"],             # Restaurant Customers aren't likely to  
            FakeRestaurantCustomers["Password"],             # have their 'Username', 'Password',    
            FakeRestaurantCustomers["Email"],                # 'Email', 'Phone Number', 'Address',   
            FakeRestaurantCustomers["Phone Number"],         #  'State', 'City', or  'Zip Code' 
            FakeRestaurantCustomers["Address"],              # collected.      
            FakeRestaurantCustomers["City"],                 # 
            FakeRestaurantCustomers["State"],                # As such, these attributes are     
            FakeRestaurantCustomers["Zip Code"]              # deleted.    
        )                                                    #
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.C.iii)  Export  FakeRestaurantCustomers  as a  dictionary  containing versions 
        #           of itself in  multiple formats.     
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return {                                             # 
            'As_OrderedDict': FakeRestaurantCustomers,       # Returns a dict of dicts which makes 
            'As_DataFrame'  : DataFrame(                     # accessible multiple output formats, 
                FakeRestaurantCustomers                      # including both a python OrdredDict 
            )                                                # and a pandas DataFrame.         
        }                                                    # 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    #################################################################################################


   # 2.I) Overload  Of The  FakeCompany  MakeFakeInventory  Method  
    #################################################################################################
    def MakeFakeInventory(self):
        '''
        NAME
            MakeFakeInventory


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly  generated  fake data,\n 
            specifically modeled to ressemble a simplified Inventory for a Restaurant.


        DESCRIPTION
            An  Overload  for the  FakeCompany.MakeFakeInventory() Method  which modifies a  copy\n 
             of the  superclass method's resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles a  Restaurant.\n 

            Once the  copy  of the Inventory Dictionary has been adapted to the specificity of the\n
            "Restaurant" profile, the  copy is then returned as output, thereby replacing the\n
            the original end value of the  superclass's MakeFakeInventory() Method.   


        PROCESS
            #2.I.i) 
                Retrieve a copy of the  Fake Inventory Dictionary  produced by\n  
                the superclass's  MakeFakeInventory  Method  to simplify code\n
                refactoring efforts.      

            #2.I.ii) 
                Replace any  Inventory Attributes  which are inconsistent\n 
                with the  FakeRestaurant's Profile  with  adjusted values. 
                 
            #2.I.iii)
                Export the  Fake Inventory,  which is now a   dict of lists.

            #2.I.iv)   
                Exports  FakeRestaurantInventory  as a  dictionary  containing versions of 
                itself in  multiple formats.         


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Inventory's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            FakeCompany
        '''

        # 2.I.i)   Retrieve a copy of the  Fake Inventory Dictionary  produced by  
        #          the superclass's  MakeFakeInventory  Method  to simplify code
        #          refactoring efforts.      
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        FakeRestaurantInventory = FakeCompany(               # 
            name                =   self.Name,               # 
            category            =   self.Category,           # 
            employee_size       =   self.EmployeeSize,       #   The FakeCompany (superclass)   
            inventory_size      =   self.InventorySize,      #   MakeFakeInventory Method is invoked 
            customer_size       =   self.CustomerSize,       #   using the FakeRestaurant (subclass)     
            city                =   self.City,               #   constructor parameters.    
            state               =   self.State,              #  
            zip_code            =   self.ZipCode,            # 
            departments         =   self.Departments         # 
        ).MakeFakeInventory()['As_OrderedDict']              #
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        
        # 2.I.ii)   Replace any  Inventory Attributes  which are inconsistent with the  
        #           FakeRestaurant's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        FakeRestaurantInventory["Product ID"] = [            # 
            phony.Choice()                                   # 
            ([                                               # 
                fake.iban()[3:7],                            # Adjust the "Product ID" attribute  
                fake.iban()[4:5]                             # to provide a Randomized Choice  
                +                                            # between different sliced ranges within 
                fake.iban()[1:4]                             # a random serialized 'iban' number. 
            ])                                               # for each of the InventorySize many  
            for _ in range( int(self.InventorySize) )        # rows. 
        ]                                                    #  
                                                             # and  
        FakeRestaurantInventory["Product"] = [               #                                        
            phony.Choice()                                   # Adjust the "Product" attribute to 
            ([                                               # provide a Randomized Choice between 
                phony.Food().spices(),                       # a random Spice, Vegetable, or Fruit 
                phony.Food().vegetable(),                    # for each of the InventorySize many  
                phony.Food().fruit()                         # rows.        
            ])                                               #  
            for _ in range( int(self.InventorySize) )        # and  
                                                             #                                        
        ]                                                    # Provide a "Unit" attribute representing 
                                                             # a static Weight Unit, 'Lbs.', helping    
        FakeRestaurantInventory["Unit"] =   [                # to establish some additional context     
                                                             # to other attributes, 
            "Lbs."                                           # for each of the InventorySize many        
                                                             # rows                                   
            for _ in range(int(self.InventorySize))          #  
        ]                                                    # and 
                                                             #                                           
        FakeRestaurantInventory["Cost Per Unit"] = [         # Provide a "Cost Per Unit" attribute    
                                                             # giving a randomized Price ranging from        
             phony.Finance().price(                          #  $1 to  $8 dollars         
                1,                                           # for each of the InventorySize many                                                     
                8                                            # rows.                                         
            )                                                #
                                                             #
            for _ in range( int(self.InventorySize) )        # 
        ]                                                    #     
                                                             #    
                                                             #                                           
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.I.iii)  Filter out any  Coulumn Attributes which are inconsistent with a  Restaurant's 
        #           Inventory  Data Context.  
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        del (                                                # The "Year" and "Price" attributes 
            FakeRestaurantInventory['Year'],                 # native to the base Class's 
            FakeRestaurantInventory['Price']                 # implmenentation of this method aren't
        )                                                    # consistent with a Restaurant context.
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.I.iv)   Exports  FakeRestaurantInventory  as a  dictionary  containing versions of 
        #           itself in  multiple formats.     
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return {                                             # 
            'As_OrderedDict': FakeRestaurantInventory,       # Returns a dict of dicts which makes   
            'As_DataFrame'  : DataFrame(                     # accessible multiple output formats, 
                FakeRestaurantInventory                      # including both a python OrdredDict  
            )                                                # and  a pandas   DataFrame.     
        }                                                    # 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    #################################################################################################


        # 2.T) Overload  Of The  FakeCompany  MakeFakeTransactions  Method
    #################################################################################################
    def MakeFakeTransactions( self, fake_inventory, fake_customers, fake_sales_employees ):
        '''
        NAME
            MakeFakeTransactions


        SYNOPSIS
            Concatenates the  pandas  DataFrame objects  produced via  the\n 
            MakeFakeEmployees(), MakeFakeCustomers()  and the   MakeFakeInventory()  
            methods into a  new dataset,  simulating a  Transaction History  between their\n    
            combined records.\n


        DESCRIPTION
            Following instantiation of the FakeCompany superclass, should it's\n
            MakeFakeEmployees(), MakeFakeCustomers()  and  MakeFakeInventory()  methods be 
            invoked, respective dictionaries are produced, each contaning  pandas\n
            DataFrame objects (accessible by calling with ['AsDataFrame'] specfied).\n

            The respective  DataFrame objects  can then be used as input to\n
            the  MakeFakeTransactions  method, which will use  pandas \n
            concat() method  to essentially glue the two datasets together,\n
            taking certain considerations depending on which of the two \n
            input data sets has a larger size.\n


        PROCESS
            #2.T.i)
                Store the  greater_size  of the two  DataFrame  inputs.    

            #2.T.ii)
                Use the  pandas.concat()  method  to export a  new  pandas  DataFrame\n    
                consisting  of  merged data  from three input sources.   


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

        # 2.T.i)     Store the  greater_size  of the two  DataFrame  inputs.  
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        greater_size = (                                     # 
                                                             # let  greater_size  be the length of   
            len(fake_inventory)                              # the fake_inventory input if it is  
                                                             # larger than the fake_customers 
            if                                               # input,  
                len(fake_inventory) > len(fake_customers)    # 
                                                             # otherwise,
            else                                             #                                                                   
                len(fake_customers)                          # greater_size will be the length of    
                                                             # fake_customers   
        )                                                    # 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#

        # 2.T.ii)   Use the  pandas.concat()  method  to export a  new  pandas  DataFrame    
        #           consisting  of  merged data  from three input sources.   
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return concat(                                       #  Since the  fake_inventory and   
            [                                                #  fake_customers  are  DataFrame   
                                                             #  objects, accessing one of their   
                Series(                                      #  'columns' returns a pandas  Series    
                    [                                        #  object.  
                        fake.isbn10()                        #       
                        for _ in range(greater_size)         #  As such, concat() can take a  list     
                    ],                                       #  consisting of a sequence of concatenated    
                    name='Transaction ID'                    #  'columns' represented by pandas Series   
                ),                                           #  objects  
                                                             # 
                Series(                                      #      
                    [                                        #      
                        phony.Choice()                       #  The columns will consist of:   
                        (                                    #      
                            fake_customers[                  #    Randomly generated   
                                'Customer ID'                #        "Transaction ID"s  
                            ].to_list()                      #    for each of the greater_size  
                        )                                    #    many rows  
                        for _ in range(greater_size)         #      
                    ],                                       #     
                    name='Customer ID'                       #    and     
                ),                                           #     
                                                             #          
                Series(                                      #    Randomly selected  "Customer ID"s      
                    [                                        #    from the  fake_customers  input source      
                        phony.Choice()                       #    for each of the greater_size       
                        (                                    #    many rows       
                            fake_sales_employees[            #    
                                'Employee ID'                #              
                            ].to_list()                      #    and           
                        )                                    #
                        for _ in range(greater_size)         #              
                    ],                                       #    Randomly selected  "Employee ID"s             
                    name='Employee ID'                       #    from the  fake_employees  input source             
                ),                                           #    for each of the greater_size              
                                                             #    many rows           
                Series(                                      #    
                    [                                        #                  
                        phony.Choice()                       #    and              
                        ([                                   #    
                            phony.Food().dish(),             #                      
                            phony.Food().drink()             #    Randomly generated 'Menu Item' Choices                   
                        ])                                   #    between                     
                        for _ in range(greater_size)         #    a phony Food Dish  and  a phony Drink                  
                    ],                                       #    for each of the greater_size many rows                     
                    name='Menu Item'                         #                             
                ),                                           #    
                                                             #                          
                Series(                                      #    and                      
                    [                                        #    
                        phony.Choice()                       #                              
                        (                                    #    A Randomly selected  "Product"s                          
                            fake_inventory[                  #    from the  fake_inventory  input source                          
                                'Product'                    #    designated as a "Main Ingredient"                          
                            ].to_list()                      #    for each of the greater_size                              
                        )                                    #    many rows                           
                        for _ in range(greater_size)         #    
                    ],                                       #                                  
                    name='Main Ingredient'                   #    and                              
                ),                                           #    
                                                             #                                      
                Series(                                      #    A Randomly selected  "Product"s                                  
                    [                                        #    from the  fake_inventory  input source                                  
                        phony.Choice()                       #    designated as a "Secondary Ingredient"                                  
                        (                                    #    for each of the greater_size                                     
                            fake_inventory[                  #    many rows                  
                                'Product'                    #   
                            ].to_list()                      #   
                        )                                    #    and
                        for _ in range(greater_size)         #
                    ],                                       # 
                    name='Secondary Ingredient'              #    Randomly geerated  "Payment" Amounts                                     
                ),                                           #    ranging between $12 to $70                                  
                                                             #    for each of the greater_size                                        
                                                             #    many rows                     
                Series(                                      #    
                    [                                        #   
                        phony.Choice()                       #    and
                        ([                                   # 
                            phony.Finance(                   #   
                            ).price(                         #    Randomly geerated  "Quantity"s                                         
                                12,                          #    ranging between 1 and 4 Units                                     
                                70                           #    Purchased for each of the                                           
                            )                                #    greater_size many rows                      
                        ])                                   #
                        for _ in range(greater_size)         #  
                    ],                                       #    and                     
                    name='Payment'                           #  
                ),                                           # 
                                                             #    Randomly geerated  "Payment Dates"                                             
                Series(                                      #    spanning from 2020 to 2022                                        
                    [                                        #    for each of the greater_size                                             
                        phony.Choice()                       #    many rows                      
                        ([                                   # 
                            phony.Numeric(                   #                             
                            ).integer_number(                #  
                                1,                           #  
                                4                            #  After all that,
                            )                                #  
                        ])                                   #  
                        for _ in range(greater_size)         #  
                    ],                                       #     
                    name='Quantity'                          #  passing the axis=1 option                                              
                ),                                           #  ensures the proper format           
                                                             #  for the resulting            
                Series(                                      #  DataFrame object.           
                    [                                        #         
                        phony.Datetime().date(               #         
                            2020,                            #                                
                            2022                             #  Once the core columns are           
                        ).strftime('%m/%d/%Y')               #  concatenated, the deltas          
                                                             #  bewteen the datasets are        
                        for _ in range(greater_size)         #  accounted for simply by            
                    ],                                       #  throwing away any 'na',           
                    name='Payment Date'                      #  a.k.a empty values, then          
                )                                            #  'shuffling' the  dataset by          
                                                             #  sorting the DataFrame by the         
            ],                                               #  'Transaction ID'.   
                                                             # 
            axis=1                                           # 
                                                             # 
        ).dropna().sort_values("Transaction ID")             # 
        #||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        #############################################################################################
#####################################################################################################
