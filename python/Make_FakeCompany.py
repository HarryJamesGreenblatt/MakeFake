'''
NAME
    Make_FakeCompany.py


PURPOSE
    Loads neccessary  external  modules  and  classes,  and provides  internal  class\n
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
from ast import Pass
import initialize_fake_data_providers                          # Brings in all neccessary modules and
import random, re, collections, pandas, subprocess             # classes:
                                                               #  
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
        Defines a  superclass  representing a  business enitity  entirely composed of   
        randomized  fake data.    


    COMPONENTS
        #2._  Constructor and Overloads
            i.  __init__(),
            ii. __repr__()

        #2.S  State Methods: Getters
            i.   GetCity(),
            ii.  GetState(),
            iii. GetZipCode()

        #2.E  A Method To Generate A Fake, Randomized "Employees" Dictionary
            MakeFakeEmployees()

        #2.C  A Method To Generate A Fake, Randomized "Customers" Dictionary
            MakeFakeCustomers()   

        #2.I  A Method To Generate A Fake, Randomized "Inventory" Dictionary
            MakeFakeInventory()

        #2.T  A Method To Generate A Fake, Randomized "Transactions" Dictionary
            MakeFakeTransactions()   


    ATTRIBUTE PARAMETERS
        name           -     Defines the Fake Company's Name\n
                             DEFAULT VALUE:  random fake company name\n 

        category       -     Defines what type of Fake Company it is\n
                             DEFAULT VALUE:  random fake company type\n

        employee_size  -     Defines the number of records to be produced for "Employee"
                             or Personnel reports\n
                             DEFAULT VALUE:  random  integer  between  1  and  1000\n
        
        customer_size   -    Defines the number of records to be produced for "Customer" 
                             or "Transaction" reports\n
                             DEFAULT VALUE:  random  integer  between  1  and  1000\n
        
        inventory_size   -   Defines the number of records to be produced for "Inventory" 
                             reports\n
                             DEFAULT VALUE:  random  integer  between  1  and  1000\n

        city            -    Defines the  US City  where the Company is located\n
                             DEFAULT VALUE:  random  fake  or  existing  US City\n

        state           -    Defines the  2-letter US State Abbreviation  where the Company is 
                             located\n
                             DEFAULT VALUE:  random  existing   2-letter US State Abbreviation\n 
   
        zip_code        -    Defines the  US Zip Code  where the Company is located\n
                             DEFAULT VALUE:  random  fake  or  existing  US Zip Code\n

        departments     -    Defines the list of possible departments to which employees at this 
                             Company might belong\n
                             DEFAULT VALUE:  Management, Accounting, Sales, Marketing, Security, IT\n  

    
    EXAMPLE OUTPUT
        Name: Reynolds-Baird\n
        Category: Limited Liability Limited Partnership\n
        Domain: Reynolds-Baird.org\n
        # of Employees: 868\n
        # of Customers: 543\n
        # of Inventory Items: 479\n
        City:  Bruceville\n
        State: OH\n
        Zip Code: 45113\n
        Departments: [
            'Management', 
            'Accounting', 
            'Sales', 
            'Marketing', 
            'Security', 
            'IT', 
        ]\n
        Employee Attributes: [
            'Employee ID', 
            'First Name', 
            'Last Name', 
            'Email', 
            'Username', 
            'Password', 
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
        Customer Attributes: [
            'Customer ID', 
            'First Name', 
            'Last Name', 
            'Email', 
            'Username', 
            'Password', 
            'Phone Number', 
            'Address', 
            'City', 
            'State', 
            'Zip Code', 
            'Card Provider', 
            'Card Number', 
            'CVV', 
            'Expiration Date', 
        ]\n
        Inventory Attributes: [
        'Stock ID', 
            'Product', 
            'Year', 
            'Price', 
            'Quantity', 
        ]

    PARENT MODULE
        Make_FakeCompany.py
    '''

    # 2._) Constructor and Overloads
    ############################################################################
    # 2._.i)   Constructor
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||
    def __init__(                                              # Contrsuctor                 
    self,                                                      # whose params                 
    name            =  fake.company(),                         # are all                  
    category        =  phony.Finance().company_type(),         # optional.
    employee_size   =  phony.Numeric().integer_number(1,750),  # 
    customer_size   =  phony.Numeric().integer_number(100,750),# 
    inventory_size  =  phony.Numeric().integer_number(100,750),# Failure to
    city            =  fake.city(),                            # provide these           
    state           =  fake.state_abbr(),                      # in the caller        
    zip_code        =  None,                                   # results in the     
    departments     =  [                                       # generation of     
        "Management",                                          # a set of random     
        "Accounting",                                          # values for each,    
        "Sales",                                               # except for     
        "Marketing",                                           # "departments",    
        "Security",                                            # which is set to    
        "IT"                                                   # a statically      
    ]                                                          # defined list
    ):                                                         # 
        self.Name            =  name                           # 
        self.Category        =  category                       # 
        self.Domain          =  self.SetDomain()               # Once the     
        self.EmployeeSize    =  employee_size                  # 'state' 
        self.CustomerSize    =  customer_size                  # param becomes   
        self.InventorySize   =  inventory_size                 # accessible,
        self.City            =  city                           # replace the 
        self.State           =  state                          # zip_code  param
        self.ZipCode         =  fake.zipcode_in_state(state)   # with one of  
        self.Departments     =  departments                    # phony's methods. 
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||
     
    # 2._.ii)  String Method Overload 
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||
    def __repr__(self):                                       #
                                                              #
        return(                                               # Overload of the
            f"Name: {self.Name}\n" +                          # superclass's  
            f"Category: {self.Category}\n" +                  # string method  
            f"Domain: {self.SetDomain()}\n" +                 # which will 
            f"# of Employees: {self.EmployeeSize}\n" +        # define how 
            f"# of Customers: {self.CustomerSize}\n" +        # the object
            f"# of Inventory Items: {self.InventorySize}\n" + # is represented 
            f"City:  {self.City}\n" +                         # in  output.  
            f"State: {self.State}\n" +                        # 
            f"Zip Code: {self.ZipCode}\n" +                   # When used in  
                                                              # calls to 
            "Departments: [\n"                                # print(), the 
            +                                                 # output will
            '\n'.join(                                        # reflect the 
                f"   '{ea}', "                                # generated 
                for ea in self.Departments                    # values for the 
            )                                                 # FakeCompany's
            +                                                 # Name, Category
            "\n]\n" +                                         # Domain, 
                                                              # EmployeeSize,
            "Employee Attributes: [\n"                        # CustomerSize,
            +                                                 # InventorySize,
            '\n'.join(                                        # City, State, 
                f"   '{ea}', "                                # and Zip Code.
                for ea in self.MakeFakeEmployees(             # 
                )['As_OrderedDict'].keys()                    # 
            )                                                 # In order to    
            +                                                 # facilatite     
            "\n]\n" +                                         # readability,  
                                                              # the 
            "Customer Attributes: [\n"                        # FakeCompany's    
            +                                                 # 
            '\n'.join(                                        # Departments,       
                f"   '{ea}', "                                # 
                for ea in self.MakeFakeCustomers(             # Employee        
                )['As_OrderedDict'].keys()                    # Attributes,        
            )                                                 # 
            +                                                 # Customer         
            "\n]\n" +                                         # Attributes,        
                                                              # 
            "Inventory Attributes: [\n"                       # and 
            +                                                 # 
            '\n '.join(                                       # Inventory           
                f"   '{ea}', "                                # Attributes             
                for ea in self.MakeFakeInventory(             # 
                )['As_OrderedDict'].keys()                    # are converted              
            )                                                 # to strings               
            +                                                 # which               
            "\n]\n"                                           # simulate
                                                              # code      
        )                                                     # indentation. 
    ##########################################################################
        

    # 2.S) State Methods
    ############################################################################
    
    # 2.S.i)   Getters
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

    # 2.S.ii)  Setters
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


    # 2.E) A Method To Generate A Fake, Randomized "Employees" Dictionary
    ############################################################################
    def MakeFakeEmployees(self, has_custom_size = False, custom_size = 0):                                  
        '''
        NAME
            MakeFakeEmployees


        SYNOPSIS
            Creates a  dictionary   of randomly generated  fake data,
            modeled to resemble a simplified  Data Context  simulating a Company's \n 
            Employees, and made available in   multiple export formats.


        DESCRIPTION
            Generates a list of  "Base Attributes"   made of fake data\n
            as an initial "profile" for data modeled to resemble a basic 
            Payroll sheet.\n

            While this process establishes a good foundation for such a model,\n
            the "Base Attributes" used provides some data elements which are\n 
            handled better by some of the  other modules and classes  that are \n 
            imported  via  initialize_fake_data_providers.py.\n

            Consequently, each of the Column Values having superior \n
            alternatives are then replaced by invoking the alternate Data\n 
            Provider's methods in an iterative pattern.\n

            Additional attribute columns, not included in the "Base Attributes"\n
            list, are then combined with the newly refreshed column data to \n
            produce a  dictionary,  itself containing 2 format versions of the\n
            refreshed data, enabling the ability to  export the data  as either an\n
            ordered dictionary of lists,  or as  a  pandas  DataFrame object.          


        PROCESS
            #2.E.i) 
                Initialize a local employee_size,  which can be optionally\n 
                bound either to a specified  Custom Size,  or to the\n
                object's inherited  EmployeeSize Attribute.\n 

            #2.E.ii) 
                Establish a  list of dicts  respresenting a "Base"\n 
                collection of data to be used as "Employee Attributes".\n 

            #2.E.iii) 
                Initialize an  ordered dictionary  whose  keys  represent\n
                column names  for  "Employee Attributes",  and whose values\n
                represent fake employee "records"  for as many rows specified\n
                by the  employee_size.\n

            #2.E.iv) 
                Replace certain  "Base Attributes"  with more capable\n
                counterparts, along with some  additional column attributes,\n
                to complete the  "Employee Attributes"  profile.\n
                 
            #2.E.v)
                Export  fake_employees, as a  dictionary  containing versions\n
                of itself in  multiple formats         


        INPUTS
            <bool>  has_custom_size  -   Indicates if a custom value is to be used\n
                                         DEFAULT VALUE:  False\n
            
            <int>   custom_size      -   Sets the value of the optional Custom Size\n
                                         DEFAULT VALUE:  0\n

        
        OUTPUT
            <Dict>
                KEY                   VALUE
                ---------------       -----------------------------------------------
                'As_DataFrame'    -   pandas  <DataFrame>  object

                'As_OrdredDict'   -   <OrderedDict>  whose  keys  correspond to\n
                                      the  Employees's  Column Names  and whose  values\n 
                                      correspond to "rows" or "records" of  Employees


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        # 2.E.i)   Initialize a local  employee_size,  which can be optionally 
        #          bound either to the specified  custom_size,  or to the
        #          object's inherited  EmployeeSize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        employee_size = (                                # if MakeFakeEmployees 
                                                         # is called with the
            self.EmployeeSize   if not has_custom_size   # has_custom_size flag,
            else                custom_size              # a custom_size is used
                                                         # to determine how many
        )                                                # records to generate
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.E.ii)   Establish a  list  of  dicts  respresenting a "Base"
        #           collection of data to be used as  "Employee Attributes".
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
        fake_employees_base = [                        # Let  
            {                                          # fake_employees_base
                "provider_source":fake,                # be a  list  of 
                "provider_method":"iana_id",           # dictionaries,
                "column_name":"Employee ID"            # each storing 3
            },                                         # key/value pairs,
            {                                          # whose  keys  will 
                "provider_source":fake,                # correspond to  
                "provider_method":"first_name",        # labels
                "column_name":"First Name"             # differentiating 
            },                                         # between the 
            {                                          # 
                "provider_source":fake,                # 'provider source',
                "provider_method":"last_name",         # 
                "column_name":"Last Name"              # 'provider method',
            },                                         # 
            {                                          # and
                "provider_source":fake,                # 
                "provider_method":"email",             # 'column_name',
                "column_name":"Email"                  # 
            },                                         # and whose  values 
            {                                          # will correspond to 
                "provider_source":fake,                # to the convention 
                "provider_method":"user_name",         # that the 
                "column_name":"Username"               # 
            },                                         # 'provider source'  
            {                                          # stores the actual
                "provider_source":fake,                # object from which the 
                "provider_method":"password",          # method would 
                "column_name":"Password"               # normally be invoked,  
            },                                         # 
            {                                          # 'provider method' 
                "provider_source":fake,                # represents the  
                "provider_method":"date",              # name of the method
                "column_name":"Date Of Birth"          # that is being invoked,
            },                                         # 
            {                                          # and
                "provider_source":fake,                # 
                "provider_method":"ssn",               # 'column_name'
                "column_name":"SSN"                    # represents the disired 
            },                                         # name for column in the
            {                                          # resultant data set. 
                "provider_source":fake,                # 
                "provider_method":"phone_number",      # Each "provider 
                "column_name":"Phone Number"           # source" will 
            },                                         # be either a 
            {                                          # reference  
                "provider_source":fake,                # to an  
                "provider_method":"street_address",    # imported    
                "column_name":"Address"                # Faker() class 
            },                                         # method, 
            {                                          # or one of the  
                "provider_source":self,                # object's City, 
                "provider_method":"GetCity",           # State, or 
                "column_name":"City"                   # ZipCode  
            },                                         # attributes.    
            {                                          # 
                "provider_source":self,                # This 
                "provider_method":"GetState",          # fake_employees_base
                "column_name":"State"                  # will be used to 
            },                                         # generate an ordered 
            {                                          # dicitonary.
                "provider_source":self,                # 
                "provider_method":"GetZipCode",        #    
                "column_name":"Zip Code"               #
            }                                          #
        ]                                              #
        #||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#

        # 2.E.iii)  Initialize an  ordered dictionary  whose  keys  represent   
        #           column names  for  "Employee Attributes",  and whose values    
        #           represent fake employee "records"  for as many rows specified  
        #           by the  employee_size.
        #|||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||#
        fake_employees = collections.OrderedDict({            # Using dict 
                                                              # comprehension,
            fake_employees_base[i]["column_name"] :           # each  key/value  
            [                                                 # pair stored in  
                getattr(                                      # fake_employees_base
                    fake_employees_base[i]["provider_source"],# is used to
                    fake_employees_base[i]["provider_method"] # iteratively store
                )()                                           # 'EmployeeSize' 
                for _ in range( employee_size )               # many rows
            ]                                                 # of fake data
                                                              # produced by 
            for i in range( len(fake_employees_base) )        # invoking the 
                                                              # provider methods 
        })                                                    # which it defined.
        #|||||||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||#

        # 2.E.iv)  Replace certain  "Base Attributes"  with more capable  
        #          counterparts, along with some  additional column attributes, 
        #          to complete the  "Employee Attributes"  profile.
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

        # 2.E.v)  Export  fake_employees, as a  dictionary  containing versions
        #         of itself in  multiple formats     
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
        return {                                # May be optionally accessed
            'As_OrderedDict': fake_employees,   # as a python  OrdredDict  
            'As_DataFrame'  : pandas.DataFrame( # or  as a  pandas  DataFrame, 
                fake_employees                  # depending on the use case.  
            )                                   #  
        }                                       #
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
    ############################################################################


    # 2.C) A Method To Generate A Fake, Randomized "Customers" Dictionary
    ############################################################################
    def MakeFakeCustomers(self, has_custom_size = False, custom_size = 0):
        '''
        NAME
            MakeFakeCustomers


        SYNOPSIS
            Creates a  Dictionary  composed  of both an  ordered dictionary     
            of lists   and a   pandas  DataFrame  object, each consisting\n  
            of randomly generated fake data.


        DESCRIPTION
            Utililizes a  MakeFakeEmployees() Method  Overload\n
            which modifies a  copy  of the  supclass's MakeFakePayroll method\n
            in a way that more closely simulates a dataset that specifically
            ressembles  Customer Data. 

            Once the  copy  of the  Ordered Payroll Dictionary  is then adapted\n 
            to simulate a  data context  resembling  "Customers",  rather than 
            "Employees". 


        PROCESS
            #2.C.i) 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakeEmployees  Method  to simplify code\n
                refactoring efforts.      

            #2.C.ii) 
                Filter out any  Coulumn Attributes which are not consistant\n
                with a  Athletic Company Customers  Data Context.  
            
            #2.C.iii)   
                Add additional  Columns Attributes  to the Customer Data  
                Context  representing  a  Customer's  ID,  along with their 
                Credit Card Information  incuding the  Card's:  

                      Provider, Number, CCV, and Expiration Date

            #2.C.iv) 
                Export  fake_customers, as a  dictionary  containing versions of\n 
                itself in  multiple formats         


        INPUTS
            <bool>  has_custom_size  -   Indicates if a custom value is to be used\n
                                         DEFAULT VALUE:  False\n
            
            <int>   custom_size      -   Sets the value of the optional Custom Size\n
                                         DEFAULT VALUE:  0\n
        
        OUTPUT
            <dict>
                KEY                  VALUE
                ---------------      -----------------------------------------------
                'As_DataFrame'   -   pandas  <DataFrame>  object

                'As_OrdredDict'  -   <OrderedDict>  whose  keys  correspond to\n
                                     Column Attribute Names  and whose  values\n 
                                     correspond to "rows" or "records" of  Customers.


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        # 2.C.i)   Initialize a local  customer_size,  which can be optionally 
        #          bound either to the specified  custom_size,  or to the
        #          object's inherited  CustomerSize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        customer_size = (                                # if MakeFakeCustomers 
                                                         # is called with the
            self.CustomerSize   if not has_custom_size   # has_custom_size flag,
            else                custom_size              # a custom_size is used
                                                         # to determine how many
        )                                                # records to generate
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.C.ii)   Retrieve a copy of the  Fake Payroll OrderedDict  produced   
        #           by the superclass's  MakeFakeEmployees  Method  to simplify 
        #           code refactoring efforts. 
        #|||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
        fake_customers  =  self.MakeFakeEmployees(      # the has_custom_size  
            has_custom_size = True,                     # switch indicates  
            custom_size     = customer_size             # the dict's length will
        )['As_OrderedDict']                             # match the  CustomerSize
        #|||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#

        # 2.C.iii)   Filter out any  Coulumn Attributes which are not consistant 
        #            with a  "Customers"  Data Context. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        del fake_customers['Salary']                     # Customers would 
        del fake_customers['Department']                 # not likely have 
        del fake_customers['Hire Date']                  # Salary, Department,
        del fake_customers['Date Of Birth']              # Hire Date, Date Of
        del fake_customers['Employee ID']                # Birth, Employee ID
        del fake_customers['SSN']                        # or SSN  Attributes
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.C.iii)    Add additional Columns Attributes to the Customer Data  
        #             Context representing  a  Customer's  ID,  along with their 
        #             Credit Card Information  incuding the  Card's: 
        #       
        #                   Provider, Number, CCV, and Expiration Date
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
                                                         # randomly selection   
            phony.Choice()                               # between a fake  or     
            ([                                           # a phony  User Name
                fake.user_name(),                        # (which actually do a
                phony.Person().username(),               # pretty good    
                phony.Person().password()                # impression of  
            ])                                           # passwords), or a far  
                                                         # more randomized  phony 
            for _ in range(customer_size)                # password, for each of 
                                                         # the 'employee_size'     
        ]                                                #  many rows 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.C.iv)  Export  fake_customers, as a  dictionary  containing versions
        #         of itself in  multiple formats     
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
        return {                                # Returns a dict of dicts 
            'As_OrderedDict': fake_customers,   # which makes accessible multiple  
            'As_DataFrame'  : pandas.DataFrame( # output formats, including both
                fake_customers                  # a python  OrdredDict  and  a  
            )                                   # pandas  DataFrame.
        }                                       #
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
    #############################################################################
    
    
    # 2.I) A Method To Generate A Fake, Randomized "Inventory" Dictionary
    #############################################################################
    def MakeFakeInventory(self, has_custom_size = False, custom_size = 0):
        '''
        NAME
            MakeFakeInventory


        SYNOPSIS
            Creates a  dict  composed  of both an  ordered dictionary\n     
            of lists and  a   pandas  DataFrame  object, both consisting\n  
            of randomly generated fake data,  specifically modeled to\n
            resemble an "Inventory" of  products.


        DESCRIPTION
            Using the  OrderedDict  class from the python collections module,
            creates an  ordered dictionary  whose  keys  correspond to 
            Attribute Names  relating to a generic "Inventory",  and whose 
            values each correspond to an  Inventory Record consisting of a
            List of random values, the  size  of which is defined either 
            by the object's InventorySize Attribute, or else by an optionally
            specified  custom_size.        

        PROCESS
            #2.I.i) 
                Initialize a local  inventory_size,  which can be optionally 
                bound either to the specified  custom_size,  or to the
                object's inherited  InventorySize  attribute. 

            #2.I.ii) 
                Define an  ordered dict  representing a  randomized 
                collection of  Attributes  which simulate a generic   
                Inventory.
                 
            #2.I.iii) 
                Export  fake_inventory  as a  dictionary  containing  versions of\n 
                itself in  multiple formats.    


        INPUTS
            <bool>  has_custom_size  -  Indicates if a custom value is to be used\n
                                        DEFAULT VALUE:  False\n
            
            <int>   custom_size      -  Sets the value of the optional Custom Size\n
                                        DEFAULT VALUE:  0\n
        

        OUTPUT
            <dict>
                KEY                   VALUE
                ---------------       -----------------------------------------------
                'As_DataFrame'    -   pandas  <DataFrame>  object

                'As_OrderedDict'   -   <OrderedDict>  whose  keys  correspond to\n
                                      Column Attribute Names  and whose  values\n 
                                      correspond to "rows" or "records" of  Inventory.


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        # 2.I.i)   Initialize a local  inventory_size,  which can be optionally 
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

        # 2.I.ii)   Define an  ordered dict  representing a  randomized 
        #           collection of  Attributes  which simulate a generic   
        #           Inventory.
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        fake_inventory = collections.OrderedDict({   # Let fake_inventory be an
                                                     # OrderedDict consisting of:  
            'Stock ID':[                             #  
                phony.Choice()([                     # A random "Stock ID"       
                    fake.iban()[:7],                 # for each of the      
                    fake.iban()[1:8],                # inventory_size  many rows   
                    fake.iban()[2:9],                #
                ])                                   # 
                for _ in range(inventory_size)       # 
            ],                                       # 
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
                    1111                             # from $1 to $1111 dollars, 
                )                                    # for each of the   
                for _ in range(inventory_size)       # inventory_size many rows
            ],                                       #
                                                     #
            'Stock Quantity':[                       # 
                phony.Numeric().integer_number(      # A phony, randomized  
                    0,                               # Quantity value ranging  
                    70                               # from 1 to 70 units, 
                )                                    # for each of the   
                for _ in range(inventory_size)       # inventory_size many rows
            ]                                        #
                                                     #
        })                                           #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#

        # 2.I.iii)  Export  fake_inventory  as a  dictionary  containing
        #           versions of itself in  multiple formats.     
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
        return {                                # Returns a dict of dicts 
            'As_OrderedDict': fake_inventory,   # which makes accessible multiple  
            'As_DataFrame'  : pandas.DataFrame( # output formats, including both
                fake_inventory                  # a python  OrdredDict  and  a  
            )                                   # pandas  DataFrame.
        }                                       #
        #|||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||#
    #############################################################################
        
    
    # 2.T) A Method To Generate A Fake, Randomized "Transactions" Dictionary
    #############################################################################
    def MakeFakeTransactions( self, fake_inventory, fake_customers ):
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
            fake_inventory    -   The  DataFrame  produced by invoking\n 
                                  FakeCompany().MakeFakeInventory['AsDataFrame']

            <pandas.DataFrame> 
            fake_customers    -   The  DataFrame  produced by invoking\n 
                                  FakeCompany().MakeFakeCustomers['AsDataFrame']


        OUTPUT
            A  new  pandas  DataFrame  object representing a  Transaction\n
            History  composed  of  concatenated  fake_inventory  and\n
            fake_customers  data.    


        PARENT:
            Make_FakeCompany.FakeCompany
        '''
        # 2.T.i)     Store the  lesser_size  of the two  DataFrame  inputs.  
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        lesser_size = (                                  # let  lesser_size  be
                                                         # the length of the 
            len(fake_inventory)                          # fake_inventory input
                                                         # if it is larger than
            if                                           # the fake_customers
                len(fake_inventory) < len(fake_customers)# input, 
                                                         #
            else                                         # otherwise,
                len(fake_customers)                      # lesser_size will be 
                                                         # the length of
        )                                                # fake_customers
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#

        # 2.T.ii)    Use the  pandas.concat()  method  to export a  new  pandas   
        #            DataFrame  consisting  of  merged data  from both input  
        #            sources.           
        #|||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        return pandas.concat(                       # Since the  fake_inventory
            [                                       # and  fake_customers  are
                                                    # DataFrame objects, 
                pandas.Series(                      # accessing one of their 
                    [                               # 'columns' returns a 
                        fake.isbn10()               # pandas  Series  object.
                        for _ in range(lesser_size) # 
                    ],                              # As such, concat() can 
                    name='Transaction ID'           # take a  list  consisting 
                ),                                  # of a sequence of 
                                                    # Series-representated
                fake_inventory['Product'],          # 'columns', in any order
                fake_inventory['Stock ID'],         # specified, and then 
                fake_customers['Customer ID'],      # combine those columns
                                                    # into a new DataFrame 
                fake_customers['First Name']        # object.
                +                                   #
                ' '                                 # To create a simple 
                +                                   # Transaction history,
                fake_customers['Last Name'],        # various Customer and 
                                                    # Inventory Attributes
                fake_customers['Address']           # that are selected, 
                +                                   # such as:
                ', '                                # 'Product', 'Stock ID',
                +                                   # 'Customer ID', 'Address'
                fake_customers['City']              # 'City', 'State', 'Zip Code'
                +                                   # 'Card Number', and  
                ', '                                # 'Price'  
                +                                   #
                fake_customers['State']             # are are combined with 
                +                                   #
                ' '                                 # A 'Transaction ID' 
                +                                   # derived by  fake's method
                fake_customers['Zip Code'],         # for producing 10 digit
                                                    # isbns.
                fake_customers['Card Number'],      #
                fake_customers['Card Provider'],    # and 
                fake_inventory['Price'],            #
                                                    # 
                pandas.Series(                      # A 'Quantity Sold' 
                    [                               # derived from python's  
                        random.choices(             # random module's 
                            population=[            # 'choices' method, 
                                1,                  # which assigns 
                                2,                  # weighted 
                                3,                  # probabilities
                                4,                  # to a given 
                                5                   # sequence.
                            ],                      #
                            weights=[               # where there will be a: 
                                0.6,                #  60% chance of '1.0'
                                0.2,                #  20% chance of '2.0'
                                0.1,                #  10% chance of '3.0'
                                0.07,               #   7% chance of '4.0'
                                0.03                #   3% chance of '5.0'
                            ],                      # being selected
                        )[0]                        # 
                                                    # 
                        for _ in range(lesser_size) # and
                    ],                              # 
                    name='Quantity Sold'            # 
                ),                                  # 
                                                    # A 'Payment Date'
                pandas.Series(                      # derived from  phony's 
                    [                               # method for producing
                        phony.Datetime().date(      # select dates between 
                            2020,                   # specified ranges. 
                            2022                    # 
                        ).strftime('%m/%d/%Y')      #
                                                    #
                        for _ in range(lesser_size) # 
                    ],                              # 
                    name='Payment Date'             # passing the axis=1 option                                     
                ),                                  # ensures the proper format  
                                                    # for the resulting   
            ],                                      # DataFrame object.   
                                                    # 
            axis=1                                  # Once the core columns are   
                                                    # concatenated, the deltas  
        ).dropna().rename(                          # bewteen the datasets are
            columns={                               # accounted for simply by   
                'Price':'Payment',                  # throwing away any 'na' (a.k.a  
                'Product':'Product Sold',           # empty) values, renaming  
                'Stock ID':'Product ID',            # some of the columns to suit  
                0:'Customer Name',                  # the context better, and then   
                1:'Customer Address'                # 'shuffling' the  dataset by    
            }                                       # sorting the DataFrame by the   
        ).sort_values("Transaction ID")             # 'Transaction ID'.
        #|||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||||#

    #############################################################################
    

    #############################################################################
    def To_Excel(self, company_data, company_name):

        csv_path   = '../python/to_powershell/data.csv'
        title_path = '../python/to_powershell/title.txt'


        with open(csv_path, 'w+') as csv, open(title_path, 'w+') as title:
            csv.write(company_data)
            title.write(company_name)


        # 2 Call PowerShell To Invoke  Build-FakeSpreadsheets.ps1  As A Parallel Subprocess  
        ############################################################################################
        subprocess.run(                                                  # subproc  will
            [                                                                      # store the 
                'powershell.exe', # result of a
                '..\\powershell\\Build-FakeSpreadsheets.ps1'      # system call,
            ],                                                                     # to PowerShell,
            stdout=subprocess.PIPE,                                                # which runs 
            stderr=subprocess.STDOUT,                                              # the dependency,  
            shell=True                                                             # and returns
        )                                                                          # a JSON string
        ############################################################################################
#####################################################################################################


if __name__ == "__main__":

    fake_company = FakeCompany()


    fake_company.To_Excel(

        fake_company.MakeFakeEmployees()["As_DataFrame"].to_csv(),
        f'{fake_company.Name} - Employees'

    )

    fake_company.To_Excel(

        fake_company.MakeFakeCustomers()["As_DataFrame"].to_csv(),
        f'{fake_company.Name} - Customers'

    )

    fake_company.To_Excel(

        fake_company.MakeFakeInventory()["As_DataFrame"].to_csv(),
        f'{fake_company.Name} - Inventory'

    )

    fake_company.To_Excel(

        fake_company.MakeFakeTransactions(
            fake_company.MakeFakeInventory()["As_DataFrame"],
            fake_company.MakeFakeCustomers()["As_DataFrame"] 
        ).to_csv(),
        
        f'{fake_company.Name} - Transactions'

    )

