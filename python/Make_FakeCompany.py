'''
NAME
    Make_FakeCompany.py


PURPOSE
    Loads neccessary  external  modules   and  classes, and provides  internal  class\n
    definitions for the  FakeCompany  superclass.   


FUNCTIONS
        #1 Stores Data Providers As Global Variables Named  fake  And  phony 

        #2 Defines The  FakeCompany  Class


DEPENDENCIES
    Project File:
        initialize_fake_data_providers.py\n

    Standard Library Module:\n
        re\n

    Third Party Module:\n
        pandas\n
'''

# 1) Stores Data Providers As Global Variables Named  fake  And  phony 
#####################################################################################################                             
from numbers import Number
import initialize_fake_data_providers, re, collections, pandas # Brings in all neccessary modules and 
                                                               # classes: 
fake  = initialize_fake_data_providers.load_all_providers()[0] # --> faker's Fake() Class + Community
phony = initialize_fake_data_providers.load_all_providers()[1] # --> the full  mimesis  module
#####################################################################################################



# 2) Defines The  FakeCompany  Class
#####################################################################################################
class FakeCompany:
    '''
    NAME
        FakeCompany


    SYNOPSIS
        Defines a Superclass representing a business enitity entirely composed of   
        randomized fake data.    


    COMPONENTS
        #2.a  Constructor and Overloads
            i.  __init__(),
            ii. __repr__()

        #2.b  State Methods: Getters
            i.   GetCity(),
            ii.  GetState(),
            iii. GetZipCode()

        #2.c  A Method To Generate A Fake, Randomized "Employees" Dictionary
            MakeFakeEmployees()

        #2.d  A Method To Generate A Fake, Randomized "Customers" Dictionary
            MakeFakeCustomers()   

        #2.e  A Method To Generate A Fake, Randomized "Inventory" Dictionary
            MakeFakeInventory()

        #2.f  A Method To Generate A Fake, Randomized "Transactions" Dictionary
            MakeFakeTransactions()   


    ATTRIBUTE PARAMETERS
        name           -   Defines the Fake Company's Name\n
                           DEFAULT VALUE:  random fake company name\n 

        category       -   Defines what type of Fake Company it is\n
                           DEFAULT VALUE:  random fake company type\n

        employee_size  -   Defines the number of records to be produced
                           for Employees or Personnel oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  10  and  500\n
        
        customer_size   -   Defines the number of records to be produced
                            or Customer or Service oreiented reports\n
                            DEFAULT VALUE:  random  integer  between  2  and  500\n

        city            -   Defines the  US City  where the Company is located\n
                            DEFAULT VALUE:  random  fake  or  existing  US City\n

        state           -   Defines the  2-letter US State Abbreviation  where the Company is 
                            located\n
                            DEFAULT VALUE:  random  existing   2-letter US State Abbreviation\n 
   
        zip_code        -    Defines the  US Zip Code  where the Company is located\n
                             DEFAULT VALUE:  random  fake  or  existing  US Zip Code\n

        departments     -   Defines the list of possible departments to which employees at this 
                            Company might belong\n
                            DEFAULT VALUE:  Management, Accounting, Sales, Marketing, Security, IT\n  

    
    EXAMPLE OUTPUT
        Name: Malone Group\n
        Category: Incorporated\n
        Number of Employees: 341\n
        City:  Reedbury\n
        State: MT\n
        Zip Code: 36398\n
        Departments: ['Management', 'Accounting', 'Sales', 'Marketing', 'Security', 'IT']\n
        Employees: dict_keys([
            'Employee ID',
            'First Name',
            'Last Name',
            'Date Of Birth',
            'Phone Number',
            'Address',
            'City',
            'State',
            'Zip Code',
            'Hire Date',
            'Salary',
            'Department'
        ])\n


    PARENT MODULE
        Make_FakeCompany.py
    '''

    # 2.a) Constructor and Overloads
    ############################################################################
    
    # 2.a.i)   Constructor
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||
    def __init__(                                              # Contrsuctor                 
    self,                                                      # whose params                 
    name            =  fake.company(),                         # are all                  
    category        =  phony.Finance().company_type(),         # optional.
    employee_size   =  phony.Numeric().integer_number(1,1000), # 
    customer_size   =  phony.Numeric().integer_number(1,1000), # 
    inventory_size  =  phony.Numeric().integer_number(1,1000), # 
    city            =  fake.city(),                            # provide these           
    state           =  fake.state_abbr(),                      # in the caller        
    zip_code        =  None,                                   # results in the     
    departments     =  [                                       # generation of     
        "Management",                                          # a set of random     
        "Accounting",                                          # values for each,    
        "Sales",                                               # except for     
        "Marketing",                                           # "departments",    
        "Security",                                            # which is set to    
        "IT"                                                   # a static list    
    ]                                                          # 
    ):                                                         # 
        self.Name            =  name                           # 
        self.Category        =  category                       # 
        self.Domain          =  self.SetDomain()               # Once the     
        self.EmployeeSize    =  employee_size                  # state 
        self.CustomerSize    =  customer_size                  # param is   
        self.InventorySize   =  inventory_size                 # accessible,
        self.City            =  city                           # replace the 
        self.State           =  state                          # zip_code  param
        self.ZipCode         =  fake.zipcode_in_state(state)   # with one of  
        self.Departments     =  departments                    # phony's methods. 
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||
     
    # 2.a.ii)  String Methpd Overload 
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||
    def __repr__(self):                                       #
                                                              #
        return(                                               # Overload of the
            f"Name: {self.Name}\n" +                          # class's string 
            f"Category: {self.Category}\n" +                  # method  
            f"Domain: {self.SetDomain()}\n" +                 # method  
            f"# of Employees: {self.EmployeeSize}\n" +        # 
            f"# of Customers: {self.CustomerSize}\n" +        # 
            f"# of Inventory Items: {self.InventorySize}\n" + # 
            f"City:  {self.City}\n" +                         # Customizes the 
            f"State: {self.State}\n" +                        # output this 
            f"Zip Code: {self.ZipCode}\n" +                   # object produces 
                                                              #
            "Departments: [\n"                                #
            +                                                 #
            '\n'.join(                                        #
                f"   '{ea}', "                                #
                for ea in self.Departments                    #
            )                                                 #
            +                                                 #
            "\n]\n" +                                         #
                                                              #
            "Employee Attributes: [\n"                        #
            +                                                 #
            '\n'.join(                                        #
                f"   '{ea}', "                                #
                for ea in self.MakeFakeEmployees(             #
                )['As_OrderedDict'].keys()                    #
            )                                                 #
            +                                                 #
            "\n]\n" +                                         #
                                                              #
            "Customer Attributes: [\n"                        #
            +                                                 #
            '\n'.join(                                        #
                f"   '{ea}', "                                #
                for ea in self.MakeFakeCustomers(             #
                )['As_OrderedDict'].keys()                    #
            )                                                 #
            +                                                 #
            "\n]\n" +                                         #
                                                              #
            "Inventory Attributes: [\n"                       #
            +                                                 #
            '\n '.join(                                       #
                f"   '{ea}', "                                #
                for ea in self.MakeFakeInventory(             #
                )['As_OrderedDict'].keys()                    #
            )                                                 #
            +                                                 #
            "\n]\n"                                           #
                                                              #
        )                                                     # 
    ##########################################################################
        

    # 2.b) State Methods
    ############################################################################

    # 2.b.i)   Getters
    #||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||||||
    def GetCity(self):           # retrieves the current value of the object's
        return self.City         #              City  attribute
                                 #
    def GetState(self):          # retrieves the current value of the object's 
        return self.State        #              State  attribute
                                 #
    def GetZipCode(self):        # retrieves the current value of the object's 
        return self.ZipCode      #             ZipCode  attribute
    #||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||||||


    # 2.b.ii)  Setters
    #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||
    def SetDomain(self):                             #
                                                     # List the common top-level  
        domains = [                                  # domains to provide a    
            'com',                                   # basis for random  
            'net',                                   # selection. 
            'org'                                    # The company name will 
        ]                                            # represent the domain name  
                                                     # and a randomly selected 
        org_name          =  self.Name               # top-level domain will be 
        top_level_domain  =  phony.Choice()(domains) # provided.
                                                     # 
        pattern = f'{org_name}.{top_level_domain}'   # This will represent a
                                                     # pattern to be porcessed
        Domain = re.sub(                             # by compounding string                                
            '.+@',                                   # replacement operations 
            '',                                      # via regular expression 
            phony.Person().email([                   # sustitutions.
                re.sub(                              # 
                    '--',                            # The regex expression
                    '-',                             # will replace empty
                    re.sub(                          # whitespaces or commas 
                        ',| ',                       # between words 
                        '-',                         # with a hyphon, and then 
                        pattern                      # go on to filter out  
                    )                                # any occurences of 
                )                                    # double hyphons that 
            ])                                       # may result in edge 
        )                                            # cases.
                                                     #
        return   Domain                              # 
    #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||

    ############################################################################


    # 2.c) A Method To Generate A Fake, Randomized "Employees" Dictionary
    ############################################################################
    def MakeFakeEmployees(self, has_custom_size = False, custom_size = 0):                                  
        '''
        NAME
            MakeFakeEmployees


        SYNOPSIS
            Creates a  dictionary  of  lists  consisting of randomly\n 
            generated  fake data,  modeled to resemble a simplified\n 
            Company Employees.


        DESCRIPTION
            Generates a "Base" list of fake data as an initial "profile"\n
            for data modeled to resemble a basic Employees sheet.\n

            While this process establishes a good foundation for such a model,\n
            the "Base" used provides some data elements which are handled\n 
            better by some of the other modules and classes that are imported\n 
            via initialize_fake_data_providers.py.\n

            Consequently, each of the Column Values having superior \n
            alternatives are then replaced by invoking substitute data\n 
            provider methods in an iterative pattern.\n

            Additional Attribute Columns, not included in the "Base" list,\n
            are then combined with the newly refreshed Column Data to produce\n
            dictionary of lists, which may ultimately be used directly as\n 
            input to a Pandas DataFrame.          


        PROCESS
            #2.c.i) 
                Initialize a local employee_size,  which can be optionally\n 
                bound either to a specified  Custom Size,  or to the\n
                object's inherited  EmployeeSize Attribute.\n 

            #2.c.ii) 
                Establish a  list of dicts  respresenting a "Base"\n 
                collection of data to be used as "Employees Attributes".\n 

            #2.c.iii) 
                Initialize an   ordered dict   whose  keys  represent\n  
                Column Names for these "Employees Attributes", and whose\n 
                values represent fake employee "records" for as many rows\n 
                specified by the object's EmployeeSize attribute.\n

            #2.c.iv) 
                Replace certain "Base" attributes with more capable\n 
                counterparts, along with additional column attributes,\n
                to complete the Employees attribute profile.\n
                 
            #2.c.v)
                Export the  Fake Employees,  which is now an  ordered dict of lists.    


        INPUTS
            <bool>  has_custom_size  -   Indicates if a custom value is to be used\n
                                         DEFAULT VALUE:  False\n
            
            <int>   custom_size      -   Sets the value of the optional Custom Size\n
                                         DEFAULT VALUE:  0\n

        
        OUTPUT
            <Dict>
                'As_DataFrame'   -  pandas  <DataFrame>  object

                'As_OrdredDict'  -  <OrderedDict>  whose  keys  correspond to\n
                                    the  Employees's  Column Names  and whose  values\n 
                                    correspond to "rows" or "records" of  Employees


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        # 2.c.i)   Initialize a local  employee_size,  which can be optionally 
        #            bound either to the specified  custom_size,  or to the
        #            object's inherited  EmployeeSize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        employee_size = (                                # if MakeFakeEmployees 
                                                         # is called with the
            self.EmployeeSize   if not has_custom_size   # has_custom_size flag,
            else                custom_size              # a custom_size is used
                                                         # to determine how many
        )                                                # records to generate
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.c.ii)   Establish a  list of dicts  respresenting a "Base"
        #            collection of data to be used as "Employees Attributes".
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        fake_employees_base = [                          # 
            {                                            # 
                "provider_source":fake,                  # 
                "provider_attribute":"iana_id",          # 
                "column_name":"Employee ID"              # Stores a dict
            },                                           # whose values
            {                                            # will be
                "provider_source":fake,                  # used in a 
                "provider_attribute":"first_name",       # follow on       
                "column_name":"First Name"               # call to
            },                                           # getattr(),
            {                                            # enabling each 
                "provider_source":fake,                  # to be passed 
                "provider_attribute":"last_name",        # iteratively 
                "column_name":"Last Name"                # as strings,
            },                                           # rather than   
            {                                            # being invoked  
                "provider_source":fake,                  # using the   
                "provider_attribute":"email",            # traditional  
                "column_name":"Email"                    #   method()  
            },                                           # 
            {                                            # 
                "provider_source":fake,                  # 
                "provider_attribute":"user_name",        # 
                "column_name":"Username"                 # 
            },                                           # 
            {                                            # 
                "provider_source":fake,                  # 
                "provider_attribute":"password",         #  
                "column_name":"Password"                 # 
            },                                           # 
            {                                            # 
                "provider_source":fake,                  # 
                "provider_attribute":"date",             # 
                "column_name":"Date Of Birth"            # 
            },                                           # 
            {                                            # 
                "provider_source":fake,                  # 
                "provider_attribute":"ssn",              # 
                "column_name":"SSN"                      # 
            },                                           # 
            {                                            # 
                "provider_source":fake,                  # 
                "provider_attribute":"phone_number",     # 
                "column_name":"Phone Number"             # 
            },                                           # 
            {                                            # Each "provider
                "provider_source":fake,                  # source" will
                "provider_attribute":"street_address",   # be either a
                "column_name":"Address"                  # reference 
            },                                           # to an 
            {                                            # imported   
                "provider_source":self,                  # Faker() class
                "provider_attribute":"GetCity",          # method,
                "column_name":"City"                     # or one of the 
            },                                           # object's City,
            {                                            # State, or
                "provider_source":self,                  # ZipCode 
                "provider_attribute":"GetState",         # attributes.   
                "column_name":"State"                    #
            },                                           #
            {                                            #
                "provider_source":self,                  #
                "provider_attribute":"GetZipCode",       #    
                "column_name":"Zip Code"                 #
            }                                            #
        ]                                                #

        # 2.c.iii) Initialize an  ordered dict  whose keys represent  column 
        #          names for "Employees" attributes, and whose values represent   
        #          fake employee "records"  for as many rows specified by the 
        #          object's EmployeeSize attribute.
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#
        fake_employees = collections.OrderedDict({             # Using dict 
                                                               # comprehension,
            fake_employees_base[i]["column_name"] :            # each  pair 
            [                                                  # in the 
                getattr(                                       # Employees base
                    fake_employees_base[i]["provider_source"], # dict is used 
                    fake_employees_base[i]["provider_attribute"]# to iteratively
                )()                                            # store
                for _ in range( employee_size )                # 'EmployeeSize' 
            ]                                                  # many rows
                                                               # of fake data
            for i in range( len(fake_employees_base) )         # keyed on what 
                                                               # the column's 
        })                                                     # name should be
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#

        # 2.c.iv)  Replace certain "Base" attributes with more capable  
        #          counterparts,along with additional column attributes, to 
        #          complete the Employees attribute profile.
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        fake_employees["Phone Number"]  =  [         # Replace the Phone Number 
                                                     # fake data method from  
            phony.Person().telephone()               # from  fake's  to  phony's 
                                                     # for each of the   
            for _ in range( employee_size )          # 'employee_size' many rows
                                                     # 
        ]                                            #
                                                     # 
        fake_employees["City"]          =  [         # Replace the  City      
                                                     # fake data method from       
            phony.Choice()([                         # from  fake's  to a      
                self.City,                           # randomly selected  choice   
                phony.Address().city(),              # between  fake's,  another  
                fake.city()                          # random one from  fake,    
            ])                                       # or one from  phony,  
                                                     # for each of the   
            for _ in range( employee_size )          # 'employee_size' many rows  
        ]                                            # 
                                                     # 
        fake_employees["Zip Code"]      =  [         # Replace the  Zip Code         
                                                     # fake data method from           
            phony.Choice()([                         # from  fake's  to a        
                self.ZipCode,                        # randomly selected  choice     
                fake.zipcode_in_state(self.State),   # between  fake's, or two    
                fake.zipcode_in_state(self.State)    # other random ones from    
            ])                                       # fake  within  the same   
                                                     # State as the object's   
            for _ in range( employee_size )          # for each of the    
        ]                                            # 'employee_size' many rows   
                                                     #
        fake_employees["Date Of Birth"]  =  [        # Add a  Date Of Birth 
                                                     # column using  phony's
            phony.Datetime().date(                   # fake data method for
                1959,                                # a providing random 
                1995                                 # dates between a 
            ).strftime('%m/%d/%Y')                   # specified min and max,
                                                     # for each of the    
            for _ in range( employee_size )          # 'employee_size' many rows  
                                                     #
        ]                                            # 
                                                     # 
        fake_employees["Hire Date"]    =  [          # Add a  Hire Date   
                                                     # column using  phony's    
            phony.Datetime().formatted_date()        # method for random fake    
                                                     # dates ranging between           
            for _ in range( employee_size )          # 2000 and the 'current      
                                                     # year', for each of the         
        ]                                            # 'employee_size' many rows   
                                                     # 
        fake_employees["Salary"]       =  [          # Add a  Salary  column   
                                                     # using  phony's fake data   
            phony.Finance().price( 50000, 125000 )   # method for random price    
                                                     # values, ranging         
            for _ in range( employee_size )          # from $50000 through    
                                                     # $125000, for each of the    
        ]                                            # 'employee_size' many rows    
                                                     # 
        fake_employees["Department"]   =  [          # Add a  Department  
                                                     # column using a
            phony.Choice()(self.Departments)         # randomly selected    
                                                     # choice from the
            for _ in range( employee_size )          # object's 'Departments'
                                                     # attribute, for each of
        ]                                            # 'employee_size' many rows
                                                     #
        fake_employees["Email"]   =  [               # Replace the default       
                                                     # Email with a list   
                                                     # produced via a   
            record[0].lower()                        # comprehension that  
            +                                        # concatenates each 
            '.'                                      # Employee Record's 
            +                                        # First and Last Name,  
            record[1].lower()                        # deliminates them with a    
            +                                        # '.', and appends the   
            f'@{self.Domain}'                        # result with the object's 
                                                     # Domain Attribute,thereby    
            for record in zip(                       # simulating a  
                fake_employees["First Name"],        # Domain-joined Email  
                fake_employees["Last Name"]          # Address, 
            )                                        # for each of the                                    
                                                     # 'employee_size' many rows 
        ]                                            #
                                                     # 
        fake_employees["Username"]   =  [            # Replace the default       
                                                     # Username with a list   
                                                     # produced via a   
            record[1].lower()                        # comprehension that  
            +                                        # concatenates each 
            record[0][0].lower()                     # Employee Record's 
                                                     # Last Name with the   
            for record in zip(                       # first letter of the 
                fake_employees["First Name"],        # record's First name,
                fake_employees["Last Name"]          # for each of the                                      
            )                                        # 'employee_size' many rows  
                                                     # 
        ]                                            # 
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 2.c.v)  Export fake_employees, which is now an  ordered dict of lists,
        #         as a  pandas  Dataframe object.     
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
        return {                                #
            "As_OrderedDict": fake_employees,   #  a Pandas DataFrame  
            "As_DataFrame"  : pandas.DataFrame( #
                fake_employees                  #
            )                                   #
        }                                       #
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
    ############################################################################


    # 2.d) A Method To Generate A Fake, Randomized "Customers" Dictionary
    ############################################################################
    def MakeFakeCustomers(self, has_custom_size = False, custom_size = 0):
        '''
        NAME
            MakeFakeCustomers


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            collection of  "Customer" Clients.


        DESCRIPTION
            Utililizes a  MakeFakeEmployees() Method  Overload\n
            which modifies a  copy  of the  supclass method's\n
            resultant  ordered dict of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles a Customer Data. 

            Once the  copy  of the  Payroll Dictionary  is then adapted to\n 
            simulate a data context  resembling "Customers",  rather than 
            "Employees". 


        PROCESS
            #2.d.i) 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakeEmployees  Method  to simplify code\n
                refactoring efforts.      

            #2.d.ii) 
                Filter out any  Coulumn Attributes which are not consistant\n
                with a  Athletic Company Customers  Data Context.  
            
            #2.d.iii)   
                Add  additional columns  to the  Customer Data Context\n 
                representing  a  Customer's  ID,  Membership Date,  and\n  
                Membership Plan.

            #2.d.iv) 
                Export the  Fake Customers,  which is now an  ordered dict of lists.    


        INPUTS
            <bool>  has_custom_size  -   Indicates if a custom value is to be used\n
                                         DEFAULT VALUE:  False\n
            
            <int>   custom_size      -   Sets the value of the optional Custom Size\n
                                         DEFAULT VALUE:  0\n
        
        OUTPUT
            <Dict>
                'As_DataFrame'  -   pandas  <DataFrame>  object

                'As_OrdredDict' -  <OrderedDict>  whose  keys  correspond to\n
                                   Column Attribute Names  and whose  values\n 
                                   correspond to "rows" or "records" of  Customers.


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        # 2.d.i)   Initialize a local  customer_size,  which can be optionally 
        #            bound either to the specified  custom_size,  or to the
        #            object's inherited  CustomerSize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        customer_size = (                                # if MakeFakeCustomers 
                                                         # is called with the
            self.CustomerSize   if not has_custom_size   # has_custom_size flag,
            else                custom_size              # a custom_size is used
                                                         # to determine how many
        )                                                # records to generate

        # 2.d.ii)   Retrieve a copy of the  Fake Payroll Dictionary  produced   
        #            by the superclass's  MakeFakeEmployees  Method  to simplify 
        #            code refactoring efforts. 
        #|||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        fake_customers  =  self.MakeFakeEmployees(    # the has_custom_size  
            has_custom_size = True,                   # switch indicates  
            custom_size     = customer_size           # the dict's length will
        )['As_OrderedDict']                           #  match the  CustomerSize
        #|||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 2.d.iii)   Filter out any  Coulumn Attributes which are not consistant 
        #            with a  Athletic Company Customers  Data Context. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        del fake_customers['Salary']                     # Club Customers would 
        del fake_customers['Department']                 # not likely have 
        del fake_customers['Hire Date']                  # Salary, Department,
        del fake_customers['Date Of Birth']              # Hire Date, Date Of
        del fake_customers['Employee ID']                # Birth, Employee ID
        del fake_customers['SSN']                        # or SSN  Attributes
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.d.iv)   Add additional Columns Attributes to the Customer Data Context 
        #            representing  a  Customer's  ID,  Membership Date,  and  
        #            Membership Plan.
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        fake_customers['Customer ID']  =  [              # Add a  Customer ID  
                                                         # column using  fake's
            fake.iana_id()[:4]                           # data method for      
                                                         # random id numbers, 
            for _ in range(customer_size)                # limiting the number of
                                                         # digits to 4,  for each 
        ]                                                # of 'CustomerSize'rows   
                                                         # 
        fake_customers.move_to_end(                      # Shift the Customer
                                                         # ID to the beginning of  
            'Customer ID',                               # ordrered dictionary 
            last=False                                   # 
                                                         #
        )                                                #         
                                                         #      
        fake_customers["Card Provider"] = [              # Add a  Membership Date    
                                                         # 2018 and the 'current       
            phony.Payment().credit_card_network()        # year', for each of the          
                                                         # 'CustomerSize' many rows  
            for _ in range(customer_size)                # 
                                                         # 
        ]                                                #
                                                         #
        fake_customers["Card Number"] = [                # Add a  Membership Date    
                                                         # 2018 and the 'current       
            phony.Payment().credit_card_number()         # year', for each of the          
                                                         # 'CustomerSize' many rows  
            for _ in range(customer_size)                # 
                                                         # 
        ]                                                #
                                                         #
        fake_customers["CVV"] = [                        # Add a  Membership Date    
                                                         # 2018 and the 'current       
            phony.Payment().cvv()                        # year', for each of the          
                                                         # 'CustomerSize' many rows  
            for _ in range(customer_size)                # 
                                                         # 
        ]                                                #
                                                         #
        fake_customers["Expiration Date"] = [            # Add a  Membership Date    
                                                         # 2018 and the 'current       
            phony.Payment().credit_card_expiration_date( # year', for each of the          
                22, 28                                   #
            )                                            # 'CustomerSize' many rows  
            for _ in range(customer_size)                # 
                                                         # 
        ]                                                #
                                                         #
        fake_customers['Email'] =  [                     # Modify the  Email    
                                                         # to be randomly  
            phony.Person().email([                       # selcted from popular 
                'gmail.com',                             # email domains, so that 
                'yahoo.com',                             # it doesn't correspond     
                'outlook.com'                            # to the object's Domain,   
            ])                                           # for each of the      
                                                         # 'CustomerSize' many rows    
            for _ in range(customer_size)                # 
        ]                                                # 
                                                         #
        fake_customers['Password'] =  [                  # Replace the default       
                                                         # Password with a    
                                                         #   
            phony.Choice()                               #
            ([                                           #
                fake.user_name(),                        #
                phony.Person().username(),               #
                phony.Person().password()                #
            ])                                           #
                                                         # 'employee_size' many   
            for _ in range(customer_size)                #  rows
                                                         # 
        ]                                                # 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.d.v)  Export fake_customers, which is now an  ordered dict of lists,
        #         as a  pandas  Dataframe object.     
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
        return {                                #
            "As_OrderedDict": fake_customers,   #  a Pandas DataFrame  
            "As_DataFrame"  : pandas.DataFrame( #
                fake_customers                  #
            )                                   #
        }                                       #
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
    #############################################################################
    
    
    # 2.e) A Method To Generate A Fake, Randomized "Inventory" Dictionary
    #############################################################################
    def MakeFakeInventory(self, has_custom_size = False, custom_size = 0):
        '''
        NAME
            MakeFakeInventory


        SYNOPSIS
            Creates an  ordered dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble an\n
            "Inventory" of  products.


        DESCRIPTION
            Using the  OrderedDict  class from the python collections module,
            creates an  ordered dictionary  whose  keys  correspond to 
            Attribute Names  relating to a generic "Inventory",  and whose 
            values each correspond to an  Inventory Record consisting of a
            List of random values, the  size  of which is defined either 
            by the object's InventorySize Attribute, or else by an optionally
            specified  custom_size.        

        PROCESS
            #2.e.i) 
                Initialize a local  inventory_size,  which can be optionally 
                bound either to the specified  custom_size,  or to the
                object's inherited  InventorySize  attribute. 

            #2.e.ii) 
                Define an  ordered dict  representing a  randomized 
                collection of  Attributes  which simulate a generic   
                Inventory.
                 
            #2.e.iii) 
                Export fake_inventory, which is now an ordered dict of lists.     


        INPUTS
            <bool>  has_custom_size  -  Indicates if a custom value is to be used\n
                                        DEFAULT VALUE:  False\n
            
            <int>   custom_size      -  Sets the value of the optional Custom Size\n
                                        DEFAULT VALUE:  0\n
        

        OUTPUT
            <dict>
                'As_DataFrame'   -   pandas  <DataFrame>  object

                'As_OrdredDict'  -  <OrderedDict>  whose  keys  correspond to\n
                                    Column Attribute Names  and whose  values\n 
                                    correspond to "rows" or "records" of  Inventory.


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        # 2.e.i)   Initialize a local  inventory_size,  which can be optionally 
        #          bound either to the specified  custom_size,  or to the
        #          object's inherited  InventorySize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        inventory_size = (                               # if MakeFakeInventory 
                                                         # is called with the
            self.InventorySize  if not has_custom_size   # has_custom_size flag,
            else                custom_size              # a custom_size is used
                                                         # to determine how many
        )                                                # records to generate
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.e.ii)   Define an  ordered dict  representing a  randomized 
        #           collection of  Attributes  which simulate a generic   
        #           Inventory.
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        fake_inventory = collections.OrderedDict({   # Let fake_inventory be an
                                                     # OrderedDict consisting of:  
            'Stock ID':[                             #  
                fake.iban()                          # A random "Stock Number"       
                for _ in range(inventory_size)       # for each of the      
            ],                                       # inventory_size  many rows   
                                                     # 
            'Product':[                              # A randomly selected 
                phony.Choice()                       # choice between:
                ([                                   #   
                                                     #
                    f'{fake.machine_make_model()}',  #  a fake machine make/model  
                                                     #
                    f'{fake.machine_make_model()}'   #  or a similar one that  
                    +                                #  that also features a  
                    f' ({fake.machine_category()})', #  Categorical Description 
                                                     #
                    phony.Hardware().phone_model(),  #  or a random Phone Model
                                                     #
                    phony.Hardware().manufacturer()  #  or a concatenation of:
                    +                                #  
                    ' '                              #   a random Electronics 
                    +                                #   Manufacturer Name
                    ' '.join(                        #  
                        phony.Text().words(          #   and 1 random word,   
                            1                        #   converted to Title Case   
                        )                            #
                    ).title(),                       #
                                                     #
                    fake.machine_make()              #  or a concatenation of:
                    +                                #                    
                    ' '                              #   a fake machine make/model
                    +                                #   Manufacturer Name
                    ' '.join(                        #         
                        phony.Text().words(          #   2 random words converted    
                            2                        #   to Title Case    
                        )                            #   
                    ).title()                        #   and a Categorical
                    +                                #   Description
                    f' ({fake.machine_category()})', #
                                                     #
                    phony.Hardware().graphics()      #  or a some random Computer 
                                                     #  Graphics card name,
                ])                                   #  
                                                     #  for each of the 
                for _ in range(inventory_size)       #  inventory_size many rows 
            ],                                       # 
                                                     #
            'Year':[                                 # 
                fake.machine_year()                  # A fake machine Manufacture 
                for _ in range(inventory_size)       # Date for each of the  
            ],                                       # inventory_size many rows
                                                     #
            'Price':[                                # 
                phony.Finance().price(               # A phony, randomized  
                    1,                               # monetary value ranging  
                    5000                             # from 1 to 5000 dollars, 
                )                                    # for each of the   
                for _ in range(inventory_size)       # inventory_size many rows
            ],                                       #
                                                     #
            'Quantity':[                             # 
                phony.Numeric().integer_number(      # A phony, randomized  
                    0,                               # monetary value ranging  
                    70                               # from 1 to 5000 dollars, 
                )                                    # for each of the   
                for _ in range(inventory_size)       # inventory_size many rows
            ]                                        #
                                                     #
        })                                           #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#

        # 2.e.iii)  Export fake_inventory, which is now an  ordered dict of lists,
        #         as a  pandas  Dataframe object.     
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
        return {                                #
            "As_OrderedDict": fake_inventory,   #  a Pandas DataFrame  
            "As_DataFrame"  : pandas.DataFrame( #
                fake_inventory                  #
            )                                   #
        }                                       #
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
    #############################################################################
        
    
    # 2.f) A Method To Generate A Fake, Randomized "Transactions" Dictionary
    #############################################################################
    def MakeFakeTransactions( self, fake_inventory, fake_customers ):
        '''
        NAME
            MakeFakeTransactions


        SYNOPSIS



        DESCRIPTION
    

        PROCESS
            #2.f.i) 


            #2.f.ii) 


        INPUTS

        
        OUTPUT


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
        # 2.f.i)   Initialize a local  transactions_size,  which can be optionally 
        #          bound either to the specified  custom_size,  or to the
        #          object's inherited  TransactionsSize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        larger_size = (                                  #
                                                         #
            len(fake_inventory)                          #
            if  len(fake_inventory) > len(fake_customers)#
                                                         #
            else                                         #
                len(fake_customers)                      #
                                                         #
        )                                                #
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.f.ii)   Define an  ordered dict  representing a  randomized 
        #           collection of  Attributes  which simulate a generic   
        #           Transactions.
        #|||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
                                                    #
        return pandas.concat(                       #
            [                                       #
                                                    #
                pandas.Series(                      #
                    [                               #
                        fake.isbn10()               #
                        for _ in range(larger_size) # 
                    ],                              #
                    name='Transaction ID'           #
                ),                                  #
                                                    #
                fake_inventory['Product'],          #
                fake_customers['Customer ID'],      #
                                                    #
                fake_customers['First Name']        #
                +                                   #
                ' '                                 #
                +                                   #
                fake_customers['Last Name'],        #
                                                    #
                fake_customers['Address']           #
                +                                   #
                ', '                                #
                +                                   #
                fake_customers['City']              #
                +                                   #
                ', '                                #
                +                                   #
                fake_customers['State']             #
                +                                   #
                ' '                                 #
                +                                   #
                fake_customers['Zip Code'],         #
                                                    #
                fake_customers['Card Number'],      #
                fake_customers['Card Provider'],    #
                fake_inventory['Price'],            #
                                                    #
                pandas.Series(                      #
                    [                               #
                        phony.Datetime().date(      # fake data method for
                            2020,                   # a providing random 
                            2022                    # dates between a 
                        ).strftime('%m/%d/%Y')      #
                                                    #
                        for _ in range(larger_size) #
                    ],                              #
                    name='Payment Date'             #
                ),                                  #
                                                    #                                   
            ],                                      #
                                                    #
            axis=1                                  #
                                                    #
        ).dropna().rename(                          #
            columns={                               #
                'Price':'Payment',                  #
                'Product':'Product Sold',           #
                0:'Customer Name',                  #
                1:'Customer Address'                #
            }                                       #
        ).sort_values("Transaction ID")             #
        #|||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||||#

    #############################################################################

#####################################################################################################