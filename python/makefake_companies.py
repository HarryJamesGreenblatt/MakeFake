'''
NAME
    make_fake_companies.py


PURPOSE
    Loads neccessary  external  modules   and  classes, and provides  internal  class\n
    definitions for the  FakeCompany  superclass, and each of the  subclass  Fakecompany\n  
    "categories" which inherit from it.    


SUPERCLASS
    FakeCompany( 
        name,
        category,
        employee_size,
        city,
        state,
        zip_code,
        departments 
    )


SUBCLASSES
    FakeAthleticCompany( 
        name,
        category,
        employee_size,
        member_size,
        city,
        state,
        zip_code,
        departments 
    )


PROCESS
        #1 Storage Of The Data Providers As Global Variables Named  fake  And  phony 

        #2 Defining The  FakeCompany  Class
        
        #3 Defining The  FakeAthleticCompany  Class


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



# 2) Defining The FakeCompany Class
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

        #2.b  State Methods
            i.   GetCity(),
            ii.  GetState(),
            iii. GetZipCode()

        #2.c A Method To Generate A Fake, Randomized "Payroll" Dictionary
            i.  MakeFakePayroll()   


    ATTRIBUTE PARAMETERS
        name           -   Defines the Fake Company's Name\n
                           DEFAULT VALUE:  random fake company name\n 

        category       -   Defines what type of Fake Company it is\n
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
    def __init__(                                            # Contrsuctor                 
    self,                                                    # whose params are                
    name          =  fake.company(),                         # all optional.                 
    category      =  phony.Finance().company_type(),         #                   
    employee_size =  phony.Numeric().integer_number(10,500), # Failure to  
    city          =  fake.city(),                            # provide these 
    state         =  fake.state_abbr(),                      # in the caller 
    zip_code      =  fake.zipcode(),                         # results in the  
    departments   =  [                                       # generation of  
        "Management",                                        # a set of random  
        "Accounting",                                        # values for each, 
        "Sales",                                             # except for  
        "Marketing",                                         # "departments", 
        "Security",                                          # which is set to 
        "IT"                                                 # a static list 
    ]                                                        # 
    ):                                                       # Once the   
        self.Name         =  name                            # state
        self.Category     =  category                        # param is 
        self.EmployeeSize =  employee_size                   # accessible, 
        self.City         =  city                            # clobber
        self.State        =  state                           # the zip_code
        self.ZipCode      =  fake.zipcode_in_state(state)    # param with an  
        self.Departments  =  departments                     # improvement. 
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


    # 2.c) A Method To Generate A Fake, Randomized "Payroll" Dictionary
    ############################################################################
    def MakeFakePayroll(self, has_custom_size = False, custom_size = 0):                                  
        '''
        NAME
            MakeFakePayroll


        SYNOPSIS
            Creates a  dictionary  of  lists  consisting of randomly\n 
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
            alternatives are then replaced by invoking substitute data\n 
            provider methods in an iterative pattern.\n

            Additional Attribute Columns, not included in the "Base" list,\n
            are then combined with the newly refreshed Column Data to produce\n
            dictionary of lists, which may ultimately be used directly as\n 
            input to a Pandas DataFrame.          


        PROCESS
            #2.c.i.1 
                Initialize a local employee_size,  which can be optionally\n 
                bound either to a specified  Custom Size,  or to the\n
                object's inherited  EmployeeSize Attribute.\n 

            #2.c.i.2 
                Establish a  list of dicts  respresenting a "Base"\n 
                collection of data to be used as "Payroll Attributes".\n 

            #2.c.i.3 
                Initialize a  dict of lists  whose  keys  represent\n  
                Column Names for these "Payroll Attributes", and whose\n 
                values represent fake employee "records" for as many rows\n 
                specified by the object's EmployeeSize attribute.\n

            #2.c.i.4 
                Replace certain "Base" attributes with more capable\n 
                counterparts, along with additional column attributes,\n
                to complete the Payroll attribute profile.\n
                 
            #2.c.i.5 
                Export the  Fake Payroll,  which is now a   dict of lists.    


        INPUTS
            <bool>  has_custom_size  -   Indicates if a custom value is to be used\n
                                         DEFAULT VALUE:  False\n
            
            <int>   custom_size      -   Sets the value of the optional Custom Size\n
                                         DEFAULT VALUE:  0\n

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Payroll's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            make_fake_companies.FakeCompany
        '''

        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        # 2.c.i.1)   Initialize a local  employee_size,  which can be optionally 
        #            bound either to the specified  custom_size,  or to the
        #            object's inherited  EmployeeSize  attribute. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        employee_size = (                                # if MakeFakePayroll is
                                                         # called with the
            self.EmployeeSize   if not has_custom_size   # has_custom_size flag,
            else                custom_size              # a custom_size is used
                                                         # to determine how many
        )                                                # records to generate
        #||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||#
        # 2.c.i.2)   Establish a  list of dicts  respresenting a "Base"
        #            collection of data to be used as "Payroll Attributes".
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
        # 2.c.i.3) Initialize a  dict of lists  whose keys represent  column 
        #          names for "Payroll" attributes, and whose values represent   
        #          fake employee "records"  for as many rows specified by the 
        #          object's EmployeeSize attribute.
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#
        fake_payroll = {                                       # Using dict 
                                                               # comprehension,
            fake_payroll_base[i]["column_name"] :              # each  pair 
            [                                                  # in the 
                getattr(                                       # payroll base
                    fake_payroll_base[i]["provider_source"],   # dict is used 
                    fake_payroll_base[i]["provider_attribute"] # to iteratively
                )()                                            # store
                for _ in range( employee_size )                # 'EmployeeSize' 
            ]                                                  # many rows
                                                               # of fake data
            for i in range( len(fake_payroll_base) )           # keyed on what 
                                                               # the column's 
        }                                                      # name should be
        #||||||||||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||#
        # 2.c.i.4) Replace certain "Base" attributes with more capable  
        #          counterparts,along with additional column attributes, to 
        #          complete the Payroll attribute profile.
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        fake_payroll["Phone Number"]  =  [           # Replace the Phone Number 
                                                     # fake data method from  
            phony.Person().telephone()               # from  fake's  to  phony's 
                                                     # for each of the   
            for _ in range( employee_size )          # 'employee_size' many rows
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
            for _ in range( employee_size )          # 'employee_size' many rows  
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
            for _ in range( employee_size )          # for each of the    
        ]                                            # 'employee_size' many rows   
                                                     #
        fake_payroll["Date Of Birth"]  =  [          # Add a  Date Of Birth 
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
        fake_payroll["Hire Date"]    =  [            # Add a  Hire Date   
                                                     # column using  phony's    
            phony.Datetime().formatted_date()        # method for random fake    
                                                     # dates ranging between           
            for _ in range( employee_size )          # 2000 and the 'current      
                                                     # year', for each of the         
        ]                                            # 'employee_size' many rows   
                                                     # 
        fake_payroll["Salary"]       =  [            # Add a  Salary  column   
                                                     # using  phony's fake data   
            phony.Finance().price(50000, 125000)     # method for random price    
                                                     # values, ranging         
            for _ in range( employee_size )          # from $50000 through    
                                                     # $125000, for each of the    
        ]                                            # 'employee_size' many rows    
                                                     # 
        fake_payroll["Department"]   =  [            # Add a  Department  
                                                     # column using a
            phony.Choice()(self.Departments)         # randomly selected    
                                                     # choice from the
            for _ in range( employee_size )          # object's 'Departments'
                                                     # attribute, for each of
        ]                                            # 'employee_size' many rows
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#
        # 2.c.i.5)   Export the  Fake Payroll,  which is now a   dict of lists.     
        #|||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||||||||#
        return fake_payroll   # so it can be used as input to a Pandas DataFrame                                        
        #|||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||||||||||||#
    ############################################################################
#####################################################################################################



# 3) Defining The FakeAthleticClub Class
#####################################################################################################
class FakeAthleticClub( FakeCompany ):
    '''
    NAME
        FakeAthleticClub


    SYNOPSIS
        A  subclass  which  inherits  from the  FakeCompany  superclass.\n 
        Represents a company specializing in  Fitness and Nutition  services.    


    COMPONENTS
        #3.a) Overload Of The FakeCompany  Constructor
            i.  __init__()

        #3.b) Overload  Of The FakeCompany  MakeFakePayroll Method 
            i.  MakeFakePayroll()  


        #2.c A Method To Generate A Fake, Randomized "Members" Dictionary
            i.  MakeFakeMembers()  


    ATTRIBUTE PARAMETERS
        name           -   Defines the Fake Company's Name\n
                           DEFAULT VALUE:  random fake company name\n 

        category       -   Defines what type of Fake Company it is\n
                           DEFAULT VALUE:  random fake company type\n

        employee_size  -   Defines the number of records to be produced
                           for Payroll or Personnel oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  10  and  160\n

        member_size    -   Defines the number of records to be produced
                           for Member or Service oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  2  and  500\n

        city           -   Defines the  US City  where the Company is located\n
                           DEFAULT VALUE:  random  fake  or  existing  US City\n

        state          -   Defines the  2-letter US State Abbreviation  where the Company is 
                           located\n
                           DEFAULT VALUE:  random  existing   2-letter US State Abbreviation\n 
   
        zip_code       -   Defines the  US Zip Code  where the Company is located\n
                           DEFAULT VALUE:  random  fake  or  existing  US Zip Code\n

        departments    -   Defines the list of possible departments to which employees at this 
                           Company might belong\n
                           DEFAULT VALUE:  Management, Personal Training, Coaching Staff,\n 
                                           Sales and Merchandise, Diet and Nutrition\n  
                                           Marketing, Maintenance\n  

    
    EXAMPLE OUTPUT
        Name: Pull Applications Fitness\n
        Category: Athletic Club\n
        Number of Employees: 25\n
        City:  New Andrewshire\n
        State: DC\n
        Zip Code: 20018\n
        Departments: [
            'Management',
            'Personal Training',
            'Coaching Staff',
            'Sales and Merchandise',
            'Diet and Nutrition',
            'Marketing',
            'Maintenance'
        ]\n
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

    # 3.a) Overload Of The FakeCompany  Constructor  
    ############################################################################
    def __init__(                                                #
    self,                                                        # A Contrsuctor                 
    name   =  ' '.join(phony.Text().words(2)).title()+" Fitness",# whose params 
    category      =  "Athletic Club",                            # may all be                
    employee_size =  phony.Numeric().integer_number(10,160),     # optionally                   
    member_size   =  phony.Numeric().integer_number(2, 500),     # priovided,                      
    city          =  fake.city(),                                # with the   
    state         =  fake.state_abbr(),                          # exception of    
    zip_code      =  fake.zipcode(),                             # "departments",   
    departments   =  [                                           # which     
        "Management",                                            # initializes   
        "Personal Training",                                     # as a static  
        "Coaching Staff",                                        # list.  
        "Sales and Merchandise",                                 #  
        "Diet and Nutrition",                                    # 
        "Marketing",                                             #
        "Maintenance"                                            #
    ]                                                            #
    ):                                                           #
        self.Name         =  name                                # Once the   
        self.Category     =  category                            # state
        self.EmployeeSize =  employee_size                       # param is 
        self.MemberSize   =  member_size                         # accessible, 
        self.City         =  city                                # clobber
        self.State        =  state                               # the zip_code
        self.ZipCode      =  fake.zipcode_in_state(state)        # param with an  
        self.Departments  =  departments                         # improvement.
    ############################################################################


    # 3.b) Overload  Of The  FakeCompany  MakeFakePayroll Method  
    ############################################################################
    def MakeFakePayroll(self):
        '''
        NAME
            MakeFakePayroll


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            simplified Payroll for a company specializing in Fitness and\n 
            Nutrition Services.


        DESCRIPTION
            An  Overload  for the  FakeCompany.MakeFakePayroll() Method\n
            which modifies a  copy  of the  superclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an\n
            Athletic Club.\n 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then returned as output, thereby replacing the\n
            the original end value of the  superclass's MakeFakePayroll() 
            Method.   


        PROCESS
            #3.b.i.1 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakePayroll  Method  to simplify code\n
                refactoring efforts.      

            #3.b.i.2 
                Replace any  Payroll Attributes  which are inconsistent\n 
                with the  FakeAthleticClub's Profile  with  adjusted values. 
                 
            #3.b.i.3 
                Export the  Fake Payroll,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to the  Payroll's  Column Names\n
            amd whose  values  correspond to "rows" or "records" of  Employees
            

        PARENT:
            make_fake_companies.FakeAthleticCompany
        '''

        # 3.b.i.1)   Retrieve a copy of the  Fake Payroll Dictionary  produced by  
        #            the superclass's  MakeFakePayroll  Method  to simplify code
        #            refactoring efforts      
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#       
        FakeAthleticClubPayroll = FakeCompany(       # 
            name            =   self.Name,           # The FakeCompany 
            category        =   self.Category,       # (superclass)  
            employee_size   =   self.EmployeeSize,   # MakeFakePayroll Method 
            city            =   self.City,           # is invoked using  
            state           =   self.State,          # the  FakeAthleticCompany 
            zip_code        =   self.ZipCode,        # (subclass) constructor 
            departments     =   self.Departments     # parameters
        ).MakeFakePayroll()                          #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        
        # 3.b.i.2)   Replace any  Payroll Attributes  which are inconsistent 
        #            with the  FakeAthleticClub's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        FakeAthleticClubPayroll["Date Of Birth"] = [ # 
                                                     #  
            phony.Datetime().date(                   # Adjust the default range     
                1985,                                # of Employee Birth Dates    
                2000                                 # to simulate a younger  
            ).strftime('%m/%d/%Y')                   # demographic,  
                                                     # for each of the        
            for _ in range(self.EmployeeSize)        # 'EmployeeSize' many rows     
                                                     # 
        ]                                            #
                                                     #
        FakeAthleticClubPayroll["Salary"]       =  [ # Adjust the default range    
                                                     # of Employee Salaries   
            phony.Finance().price(50000, 75500)      # to simulate low income  
                                                     # levels, 
            for _ in range(self.EmployeeSize)        # for each of the       
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
                                                     # 
        FakeAthleticClubPayroll['Employee ID']  = [  # Adjust the default range      
                                                     # of Employee ID Numbers    
            fake.iana_id()[:5]                       # to not exceed 5 digits 
                                                     # in length,   
            for _ in range(self.EmployeeSize)        # for each of the       
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 3.b.i.3)   Export the  Fake Payroll,  which is now a   dict of lists.     
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return FakeAthleticClubPayroll  # for use as input in a Pandas DataFrame
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
    ############################################################################


    # 3.c) A Method To Generate A Fake, Randomized "Members" Dictionary
    ############################################################################
    def MakeFakeMembers(self):
        '''
        NAME
            MakeFakeMembers


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            collection of  "Member" Clients  belonging to a company\n 
            specializing in  Fitness  and  Nutrition  Services.


        DESCRIPTION
            Utililizes the  FakeAthleticCompany.MakeFakePayroll() Method\n
            Overload,  which modifies a  copy  of the  supclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an Athletic Club. 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then re-modified in a process where the FakeAthleticClub's\n
            adjusted attriubutes are filtered to simulate a data context\n
            resembling  Athletic Club Clients,  a.k.a. "Members",  rather\n
            than Athletic Club Employees. 


        PROCESS
            #3.c.i.1 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakePayroll  Method  to simplify code\n
                refactoring efforts.      

            #3.c.i.2 
                Filter out any  Coulumn Attributes which are not consistant\n
                with a  Athletic Company Members  Data Context.  
            
            #3.c.i.3)   
                Add  additional columns  to the  Member Data Context\n 
                representing  a  Member's  ID,  Membership Date,  and\n  
                Membership Plan.

            #3.c.i.4) 
                Export the  Fake Members,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to  Column Attribute Names\n
            amd whose  values  correspond to "rows" or "records" of  Members.
            

        PARENT:
            make_fake_companies.FakeAthleticCompany
        '''

        # 3.c.i.1)   Retrieve a copy of the  Fake Payroll Dictionary  produced   
        #            by the superclass's  MakeFakePayroll  Method  to simplify 
        #            code refactoring efforts. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        FakeAthleticClubMembers = FakeCompany(           # The FakeCompany  
            name            =   self.Name,               # (superclass)  
            category        =   self.Category,           # MakeFakePayroll Method 
            employee_size   =   self.EmployeeSize,       # is invoked using  
            city            =   self.City,               # the  FakeAthleticCompany 
            state           =   self.State,              # (subclass) constructor 
            zip_code        =   self.ZipCode,            # parameters
            departments     =   self.Departments         #
        ).MakeFakePayroll(                               # the has_custom_size  
            has_custom_size =   True,                    # switch indicates  
            custom_size     =   self.MemberSize          # the dict's length will 
        )                                                # match the  MemberSize
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 3.c.i.2)   Filter out any  Coulumn Attributes which are not consistant 
        #            with a  Athletic Company Members  Data Context. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        del FakeAthleticClubMembers['Salary']            # Club members would 
        del FakeAthleticClubMembers['Department']        # not likely have a
        del FakeAthleticClubMembers['Hire Date']         # Salary, Department,
        del FakeAthleticClubMembers['Date Of Birth']     # Hire Date, Date Of
        del FakeAthleticClubMembers['Employee ID']       # Birth or Employee ID
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 3.c.i.3)   Add  additional columns  to the Member Data Context 
        #            representing  a  Member's  ID,  Membership Date,  and  
        #            Membership Plan.
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        FakeAthleticClubMembers['Member ID']  =  [       # Add a  Member ID  
                                                         # column using  fake's
            fake.iana_id()[:4]                           # data method for      
                                                         # providing random id 
            for _ in range(self.MemberSize)              # numbers, limiting the 
                                                         # number of digits to 4,
        ]                                                # for each of the    
                                                         # 'MemberSize' many rows
        FakeAthleticClubMembers["Membership Date"]  =  [ #  
                                                         # Add a  Membership Date  
            phony.Datetime().formatted_date()            # column using  phony's   
                                                         # method for random fake   
            for _ in range(self.MemberSize)              # dates ranging between          
                                                         # 2000 and the 'current     
        ]                                                # year', for each of the        
                                                         # 'MemberSize' many rows
                                                         #  
        FakeAthleticClubMembers['Membership Plan'] =  [  # 
                                                         # Add a  Membership Plan   
            phony.Choice()([                             # column using  phony's    
                "Silver",                                # method selecting      
                "Gold",                                  # between random choices            
                "Platinum"                               # of Silver, Gold, and       
            ])                                           # Platinum  Membership,  
                                                         # for each of the  
            for _ in range(self.MemberSize)              # 'MemberSize' many rows
        ]                                                # 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 3.c.i.4)   Export the  Fake Members,  which is now a   dict of lists.     
        #|||||||||||||||||||||#|||||||||||||||||||||||||||||||||||||||||||||||||#
        return FakeAthleticClubMembers  # for use as input in a Pandas DataFrame
        #|||||||||||||||||||||#|||||||||||||||||||||||||||||||||||||||||||||||||#
    #############################################################################
#####################################################################################################
