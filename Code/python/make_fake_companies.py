'''
NAME
    make_fake_companies.py


PURPOSE
    Loads neccessary  external  modules   and  classes, and provides  internal  class  definitions\n
    for the  Company  superclass, and each of the  subclass  company  "categories" which inherit\n 
    from it.    


SUPERCLASS
    Company( name, category, employee_size, city, state, zip_code, departments ) 


PROCESS
        #1 Storage Of The Data Providers As Global Variables Named  fake  And  phony 

        #2 Defining The Company Class


DEPENDENCIES
    initialize_fake_data_providers.py\n
'''

# 1) Storage Of The Data Providers As Global Variables Named  fake  And  phony 
#####################################################################################################
import initialize_fake_data_providers                          # Brings in all neccessary modules and  
                                                               # classes: 
fake  = initialize_fake_data_providers.load_all_providers()[0] # --> faker's Fake() Class + Community
phony = initialize_fake_data_providers.load_all_providers()[1] # --> the full  mimesis  module
#####################################################################################################



# 2) Defining The Company Class
#####################################################################################################
class Company:
    '''
    NAME
        Company


    SYNOPSIS
        Defines a Superclass representing a business enitity entirely composed of   
        randomized fake data.    


    COMPONENTS
        #2.a  Constructor and Overloads
            i.  __init__(),
            ii. __repr__()

        #2.b  State Methods
            i.   GetCity(),
            ii.  GetState(),
            iii. GetZipCode()

        #2.c  Generating A Fake, Randomized "Payroll" Dictionary
            i.  MakeFakePayroll()   


    ATTRIBUTE PARAMETERS
        name           -   Defines the Company Name\n
                           DEFAULT VALUE:  random fake company name\n 

        category       -   Defines what type of Company it is\n
                           DEFAULT VALUE:  random fake company type\n

        employee_size  -   Defines the number of records to be produced
                           for Payroll or Personnel oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  10  and  500\n

        city           -   Defines the  US City  where the Company is located\n
                           DEFAULT VALUE:  random  fake  or  existing  US City\n

        state          -   Defines the  2-letter US State Abbreviation  where the Company is 
                           located\n
                           DEFAULT VALUE:  random  existing   2-letter US State Abbreviation\n 
   
        zip_code       -   Defines the  US Zip Code  where the Company is located\n
                           DEFAULT VALUE:  random  fake  or  existing  US Zip Code\n

        departments    -   Defines the list of possible departments to which employees at this 
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
        Payroll: dict_keys([
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
        make_fake_companies.py
    '''

    # 2.a) Constructor and Overloads
    ############################################################################
    def __init__(                                            #
    self,                                                    #
    name          =  fake.company(),                         #
    category      =  phony.Finance().company_type(),         # Contrsuctor                 
    employee_size =  phony.Numeric().integer_number(10,500), # whose params are                
    city          =  fake.city(),                            # all optional                 
    state         =  fake.state_abbr(),                      #                  
    zip_code      =  fake.zipcode(),                         # 
    departments   =  [                                       # 
        "Management",                                        # Failure to 
        "Accounting",                                        # provide these
        "Sales",                                             # in the caller
        "Marketing",                                         # results in the 
        "Security",                                          # generation of 
        "IT"                                                 # a set of random 
    ]                                                        # values for each,
    ):                                                       # except for 
        self.Name         =  name                            # "departments",
        self.Category     =  category                        # which is set to
        self.EmployeeSize =  employee_size                   # a static list
        self.City         =  city                            #
        self.State        =  state                           #
        self.ZipCode      =  zip_code                        #
        self.Departments  =  departments                     #
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||| 
    def __repr__(self):                                      #
                                                             #
        return(                                              # Overload of the
            f"Name: {self.Name}\n" +                         # class's string 
            f"Category: {self.Category}\n" +                 # method  
            f"Number of Employees: {self.EmployeeSize}\n" +  # 
            f"City:  {self.City}\n" +                        # Customizes the 
            f"State: {self.State}\n" +                       # output this 
            f"Zip Code: {self.ZipCode}\n" +                  # object produces 
            f"Departments: {self.Departments}\n" +           # when used with 
            f"Payroll: {self.MakeFakePayroll().keys()}\n"    # print()
        )                                                    # 
    ############################################################################
        

    # 2.b) State Methods
    ############################################################################
    def GetCity(self):           # retrieves the current value of the object's
        return self.City         #              City  attribute
    #||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||||||
    def GetState(self):          # retrieves the current value of the object's 
        return self.State        #              State  attribute
    #||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||||||
    def GetZipCode(self):        # retrieves the current value of the object's 
        return self.ZipCode      #             ZipCode  attribute
    ############################################################################


    # 2.c) Generating A Fake, Randomized "Payroll" Dictionary
    ############################################################################
    def MakeFakePayroll(self):                                  
        '''
        NAME
            MakeFakePayroll


        SYNOPSIS
            Creates a  python dictionary of lists consisting of randomly\n 
            generated  fake data,  modeled to resemble a simplified\n 
            Company Payroll.


        DESCRIPTION
            Generates a "Base" list of fake data as an initial "profile"\n
            for data modeled to resemble a basic Payroll sheet.\n

            While this process establishes a good foundation for such a model,\n
            the "Base" used provides some data elements which are handled\n 
            better by some of the other modules and classes that are imported\n 
            via initialize_fake_data_providers.py.\n

            Consequently, each of the Column Values having superior \n
            alternatives are then replaced by invoking substitute data provider\n 
            methods in an iterative pattern.\n

            Additional Attribute Columns, not included in the "Base" list,\n
            are then combined with the newly refreshed Column Data to produce\n
            dictionary of lists, which may ultimately be used directly as input\n 
            to a Pandas DataFrame.          


        PROCESS
            #i.1 Establish a  list of dicts  respresenting a "Base" 
                 collection of data to be used as "Payroll Attributes".\n 

            #i.2 Initialize a  dict of lists  whose  keys  represent  
                 Column Names for these "Payroll Attributes", and whose values\n  
                 represent fake employee "records" for as many rows specified\n 
                 by the object's EmployeeSize attribute.\n

            #i.3 Replace certain "Base" attributes with more capable\n 
                counterparts, along with additional column attributes,\n
                to complete the Payroll attribute profile.\n
                 
            #i.4 Export the  Fake Payroll,  which is now a   dict of lists.    


        INPUT
            None.

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Payroll's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            make_fake_companies.Company()
        '''
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#
        # i.1) Establish a  list of dicts  respresenting a "Base" selection of 
        #      columns.
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        fake_payroll_base = [                            # 
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
                "column_name":"Last Name"},              # as strings,
            {                                            # rather than 
                "provider_source":fake,                  # being invoked
                "provider_attribute":"date",             # using the 
                "column_name":"Date Of Birth"            # traditional
            },                                           #   method()
            {                                            # syntax
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
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        # i.2) Initialize a  dict of lists  whose  keys  represent  column names  
        #      for "Payroll" attributes, and whose  values  represent fake  
        #      empployee "records" for as many rows specified by the object's
        #      EmployeeSize attribute.
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#
        fake_payroll = {                                       # Using dict 
                                                               # comprehension,
            fake_payroll_base[i]["column_name"] :              # each  pair 
            [                                                  # in the 
                getattr(                                       # payroll base
                    fake_payroll_base[i]["provider_source"],   # dict is used 
                    fake_payroll_base[i]["provider_attribute"] # to iteratively
                )()                                            # store
                for _ in range( self.EmployeeSize )            # 'EmployeeSize' 
            ]                                                  # many rows
                                                               # of fake data
            for i in range( len(fake_payroll_base) )           # keyed on what 
                                                               # the column's 
        }                                                      # name should be
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#
        # i.3) Replace certain "Base" attributes with more capable counterparts, 
        #      along with additional column attributes, to complete the Payroll
        #      attribute profile.
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        fake_payroll["Phone Number"]  =  [           # Replace the Phone Number 
                                                     # fake data method from  
            phony.Person().telephone()               # from  fake's  to  phony's 
                                                     # for each of the   
            for _ in range(self.EmployeeSize)        # 'EmployeeSize' many rows
                                                     # 
        ]                                            #
                                                     # 
        fake_payroll["City"]          =  [           # Replace the  City      
                                                     # fake data method from       
            phony.Choice()([                         # from  fake's  to a      
                self.City,                           # randomly selected  choice   
                phony.Address().city(),              # between  fake's,  another  
                fake.city()                          # random one from  fake,    
            ])                                       # or one from  phony,  
                                                     # for each of the   
            for _ in range(self.EmployeeSize)        # 'EmployeeSize' many rows  
        ]                                            # 
                                                     # 
        fake_payroll["Zip Code"]      =  [           # Replace the  Zip Code         
                                                     # fake data method from           
            phony.Choice()([                         # from  fake's  to a        
                self.ZipCode,                        # randomly selected  choice     
                fake.zipcode_in_state(self.State),   # between  fake's, or two    
                fake.zipcode_in_state(self.State)    # other random ones from    
            ])                                       # fake  within  the same   
                                                     # State as the object's   
            for _ in range(self.EmployeeSize)        # for each of the    
        ]                                            # 'EmployeeSize' many rows   
                                                     #
        fake_payroll["Date Of Birth"]  =  [          # Add a  Date Of Birth 
                                                     # column using  phony's
            phony.Datetime().date(                   # fake data method for
                1959,                                # a providing random 
                1995                                 # dates between a 
            ).strftime('%m/%d/%Y')                   # specified min and max,
                                                     # for each of the    
            for _ in range(self.EmployeeSize)        # 'EmployeeSize' many rows  
                                                     #
        ]                                            # 
                                                     # 
        fake_payroll["Hire Date"]    =  [            # Add a  Hire Date   
                                                     # column using  phony's    
            phony.Datetime().formatted_date()        # method for random fake    
                                                     # dates ranging between           
            for _ in range(self.EmployeeSize)        # 2000 and the 'current      
                                                     # year', for each of the         
        ]                                            # 'EmployeeSize' many rows   
                                                     # 
        fake_payroll["Salary"]       =  [            # Add a  Salary  column   
                                                     # using  phony's fake data   
            phony.Finance().price(50000, 125000)     # method for random price    
                                                     # values, ranging         
            for _ in range(self.EmployeeSize)        # from $50000 through    
                                                     # $125000, for each of the    
        ]                                            # 'EmployeeSize' many rows    
                                                     # 
        fake_payroll["Department"]   =  [            # Add a  Department  
                                                     # column using a
            phony.Choice()(self.Departments)         # randomly selected    
                                                     # choice from the
            for _ in range(self.EmployeeSize)        # object's 'Departments'
                                                     # attribute, for each in
        ]                                            # 'EmployeeSize' many rows
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        # i.4) Export the  Fake Payroll,  which is now a   dict of lists.     
        #|||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||#
        return fake_payroll         # to be used as input for a Pandas DataFrame                                        
    ############################################################################
#####################################################################################################