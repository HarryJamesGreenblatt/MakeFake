'''
NAME
    Make_FakeAthleticClub.py


PURPOSE
    Loads neccessary  external  modules   and   classes,  and provides internal  class\n
    definitions for the  FakeAthleticClub  subclass, which inhereits from the FakeCompany\n  
    superclass.


FUNCTIONS  
    #1 Imports the  FakeCompany  superclass

    #2 Defines The  FakeAthleticClub  subclass


DEPENDENCIES
    #1 initialize_fake_data_providers.py\n

    #2 Make_FakeCompany.py
'''


# 1) Defines The  FakeAthleticClub  subclass
#####################################################################################################
from Make_FakeCompany  import FakeCompany, phony, fake
from pandas import DataFrame
#####################################################################################################



# 2) Defines The  FakeAthleticClub  subclass
#####################################################################################################
class FakeAthleticClub( FakeCompany ):
    '''
    NAME
        FakeAthleticClub


    SYNOPSIS
        A  subclass  which  inherits  from the  FakeCompany  superclass.\n 
        Represents a company specializing in  Fitness and Nutition  services.    


    COMPONENTS
        #2._) Overload Of The  FakeCompany  Constructor
            i.  __init__()

        #2.E) Overload  Of The  FakeCompany  MakeFakeEmployees  Method 
            MakeFakeEmployees()  

        #2.C) Overload  Of The  FakeCompany  MakeFakeCustomers  Method
            MakeFakeCustomers()  


    ATTRIBUTE PARAMETERS
        name           -   Defines the Fake Company's Name\n
                           DEFAULT VALUE:  random fake company name\n 

        category       -   Defines what type of Fake Company it is\n
                           DEFAULT VALUE:  random fake company type\n

        employee_size  -   Defines the number of records to be produced
                           for Payroll or Personnel oreiented reports\n
                           DEFAULT VALUE:  random  integer  between  10  and  160\n

        customer_size    -   Defines the number of records to be produced
                           for Customer or Service oreiented reports\n
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
                                           Sales and Merchandise,  and   Diet and Nutrition

    
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
            'Diet and Nutrition'
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
        FakeCompany.py
    '''

    # 2._) Overload Of The FakeCompany  Constructor  
    ############################################################################
    def __init__(                                                #
    self,                                                        # A Contrsuctor                 
    name   =  ' '.join(phony.Text().words(1)).title()+" Fitness",# whose params 
    category      =  "Athletic Club",                            # are all              
    employee_size   =  phony.Numeric().integer_number(1,700),    # optional.
    customer_size   =  phony.Numeric().integer_number(1,700),    # 
    inventory_size  =  phony.Numeric().integer_number(1,700),    # Failure to                   
    city          =  fake.city(),                                # provide these            
    state         =  fake.state_abbr(),                          # in the caller         
    zip_code      =  fake.zipcode(),                             # results in the      
    departments   =  [                                           # generation of      
        "Management",                                            # a set of random      
        "Personal Training",                                     # values for each,     
        "Coaching Staff",                                        # except for      
        "Sales and Merchandise",                                 # "departments",      
        "Diet and Nutrition"                                     # which is set to     
    ]                                                            # a statically     
    ):                                                           # defined list
        self.Name         =  name                                # 
        self.Category     =  category                            # Once the     
        self.Domain       =  self.SetDomain()                    # 'state' 
        self.EmployeeSize =  employee_size                       # param becomes    
        self.CustomerSize =  customer_size                       # accessible, 
        self.InventorySize =  inventory_size                       # accessible, 
        self.City         =  city                                # replace the  
        self.State        =  state                               # zip_code  param 
        self.ZipCode      =  fake.zipcode_in_state(state)        # with one of   
        self.Departments  =  departments                         # phony's methods.  
    ############################################################################


    # 2.E) erload  Of The  FakeCompany  MakeFakeEmployees Method  
    ############################################################################
    def MakeFakeEmployees(self):
        '''
        NAME
            MakeFakeEmployees


        SYNOPSIS
            Creates a  dictionary of lists  consisting of randomly\n 
            generated  fake data,  specifically modeled to resemble a\n
            simplified Payroll for a company specializing in Fitness and\n 
            Nutrition Services.


        DESCRIPTION
            An  Overload  for the  FakeCompany.MakeFakeEmployees() Method\n
            which modifies a  copy  of the  superclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an\n
            Athletic Club.\n 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then returned as output, thereby replacing the\n
            the original end value of the  superclass's MakeFakeEmployees() 
            Method.   


        PROCESS
            #2.E.i 
                Retrieve a copy of the  Fake Payroll Dictionary  produced by\n  
                the superclass's  MakeFakeEmployees  Method  to simplify code\n
                refactoring efforts.      

            #2.E.i 
                Replace any  Payroll Attributes  which are inconsistent\n 
                with the  FakeAthleticClub's Profile  with  adjusted values. 
                 
            #2.E.i 
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
        FakeAthleticClubEmployees = FakeCompany(       # 
            name            =   self.Name,           # The FakeCompany 
            category        =   self.Category,       # (superclass)  
            employee_size   =   self.EmployeeSize,   # MakeFakeEmployees Method 
            inventory_size  =   self.InventorySize, # MakeFakeInventory Method 
            customer_size   =   self.CustomerSize,   # MakeFakecustomers Method 
            city            =   self.City,           # is invoked using  
            state           =   self.State,          # the  FakeAthleticClub 
            zip_code        =   self.ZipCode,        # (subclass) constructor 
            departments     =   self.Departments     # parameters
        ).MakeFakeEmployees()['As_OrderedDict']      #
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        
        # 2.E.ii)   Replace any  Payroll Attributes  which are inconsistent 
        #            with the  FakeAthleticClub's Profile  with  adjusted values. 
        #||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||||||#
        FakeAthleticClubEmployees["Date Of Birth"] = [ # 
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
        FakeAthleticClubEmployees["Salary"]       =  [ # Adjust the default range    
                                                     # of Employee Salaries   
            phony.Finance().price(50000, 75500)      # to simulate low income  
                                                     # levels, 
            for _ in range(self.EmployeeSize)        # for each of the       
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
                                                     # 
        FakeAthleticClubEmployees['Employee ID']  = [  # Adjust the default range      
                                                     # of Employee ID Numbers    
            fake.iana_id()[:5]                       # to not exceed 5 digits 
                                                     # in length,   
            for _ in range(self.EmployeeSize)        # for each of the       
                                                     # 'EmployeeSize' many rows    
        ]                                            # 
        #||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||||#

        # 2.E.iii)   Export the  Fake Payroll,  which is now a   dict of lists.     
        #|||||||||||||||||||||||||||||||#||||||||||||||||||||||||||||||||||||||#
        return {                                # Returns a dict of dicts 
            'As_OrderedDict': FakeAthleticClubEmployees,   # which makes accessible multiple  
            'As_DataFrame'  : DataFrame( # output formats, including both
                FakeAthleticClubEmployees                  # a python  OrdredDict  and  a  
            )                                   # pandas  DataFrame.
        }                                       #
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
            Utililizes the  FakeAthleticClub.MakeFakeEmployees() Method\n
            Overload,  which modifies a  copy  of the  supclass method's\n
            resultant dictionary of lists  in a way that more closely\n 
            simulates a dataset that specifically ressembles an Athletic Club. 

            Once the  copy  of the  Payroll Dictionary  has been adapted to\n
            the specificity of the "Athletic Club" profile, the  copy\n
            is then re-modified in a process where the FakeAthleticClub's\n
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
                with a  Athletic Company Customers  Data Context.  
            
            #2.C.iii)   
                Add  additional columns  to the  Customer Data Context\n 
                representing  a  Customer's  ID,  Membership Date,  and\n  
                Membership Plan.

            #2.C.iv) 
                Export the  Fake Customers,  which is now a   dict of lists.    


        INPUTS
            None

        
        OUTPUT
            a  <dict>  whose  keys  correspond to  Column Attribute Names\n
            amd whose  values  correspond to "rows" or "records" of  Customers.
        '''

        # 2.C.i)   Retrieve a copy of the  Fake Payroll Dictionary  produced   
        #          by the superclass's  MakeFakeEmployees  Method  to simplify 
        #          code refactoring efforts. 
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        FakeAthleticClubCustomers = FakeCompany(         # FakeCompany's 
            name            =   self.Name,               # (superclass)  
            category        =   self.Category,           # MakeFakeEmployees 
            employee_size   =   self.EmployeeSize,       # is invoked using  
            customer_size   =   self.CustomerSize,       # is invoked using  
            inventory_size  =   self.InventorySize,      # is invoked using  
            city            =   self.City,               # the  FakeAthleticClub 
            state           =   self.State,              # (subclass) constructor 
            zip_code        =   self.ZipCode,            # parameters
            departments     =   self.Departments         #
        ).MakeFakeCustomers(                             # the has_custom_size  
            has_custom_size =   True,                    # switch indicates  
            custom_size     =   self.CustomerSize        # the dict's length will 
        )['As_OrderedDict']                              # match the  CustomerSize
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#


        # 2.C.iii)   Add additional Columns Attributes to the Customer Data Context 
        #            representing  a  Customer's   Membership Date,  and  
        #            Membership Plan.
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        FakeAthleticClubCustomers["Membership Date"] = [ # Add a  Membership Date    
                                                         # column using  phony's      
            phony.Datetime().date(                       # method for random fake     
                2018,                                    # dates ranging between            
                2022                                     # 2018 and the 'current       
            ).strftime('%m/%d/%Y')                       # year', for each of the          
                                                         # 'CustomerSize' many rows  
            for _ in range(self.CustomerSize)            # 
                                                         # 
        ]                                                #
                                                         #
        FakeAthleticClubCustomers['Membership Plan'] =  [# Add a  Membership Plan    
                                                         # column using  phony's     
            phony.Choice()([                             # method selecting       
                "Silver",                                # between random choices             
                "Gold",                                  # of Silver, Gold, and        
                "Platinum"                               # Platinum  Membership,   
            ])                                           # for each of the   
                                                         # 'CustomerSize' many rows 
            for _ in range(self.CustomerSize)            # 
        ]                                                #
                                                         #
        #||||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#

        # 2.C.iv)  Export  FakeAthleticClubCustomers  as a  dictionary  
        #           containing versions of itself in  multiple formats.     
        #|||||||||||||||||||||||||||||||||||||||||||||||#||||||||||||||||||||||#
        return {                                        # Returns a dict of dicts 
            'As_OrderedDict': FakeAthleticClubCustomers,# which makes accessible  
            'As_DataFrame'  : DataFrame(                # multiple output formats,
                FakeAthleticClubCustomers               # including both a python     
            )                                           # OrdredDict  and a   
        }                                               # pandas DataFrame.
        #|||||||||||||||||||||||||||||||||||||||||||||||#|||||||||||||||||||||||#
    #############################################################################
#####################################################################################################
