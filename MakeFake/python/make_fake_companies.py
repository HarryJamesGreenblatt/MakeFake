'''
this shit needs comments...
'''

# 1) Storage Of The Data Providers As Global Variables Named  fake  And  phony 
#####################################################################################################
import initialize_fake_data_providers                          # Brings in multiple modules and  
                                                               # classes: 
fake  = initialize_fake_data_providers.load_all_providers()[0] # --> faker's Fake() Class + Community
phony = initialize_fake_data_providers.load_all_providers()[1] # --> the full  mimesis  module
#####################################################################################################



# 2) The Company Class
#####################################################################################
class Company:
    '''
    This shit needs comments.
    '''

    # 2.a) Constructor and Overloads
    #################################################################################
    def __init__(
    self, 
    name          =  fake.company(), 
    category      =  phony.Finance().company_type(), 
    employee_size =  phony.Numeric().integer_number(10,500), 
    city          =  fake.city(), 
    state         =  fake.state_abbr(), 
    zip_code      =  fake.zipcode(), 
    departments   =  [
        "Management",
        "Accounting",
        "Sales",
        "Marketing",
        "Security",
        "IT"
    ]
    ):
        '''
        this shit needs comments
        '''
        self.Name         =  name
        self.Category     =  category
        self.EmployeeSize =  employee_size
        self.City         =  city
        self.State        =  state
        self.ZipCode      =  zip_code
        self.Departments  =  departments
    
    
    
    def __repr__(self):
        '''
        this shit needs comments.
        '''
        return(  
            f"Name: {self.Name}\n" +
            f"Category: {self.Category}\n" +
            f"Number of Employees: {self.EmployeeSize}\n" +
            f"City:  {self.City}\n" +
            f"State: {self.State}\n" +
            f"Zip Code: {self.ZipCode}\n" +
            f"Departments: {self.Departments}\n" +
            f"Payroll: {self.MakeFakePayroll().keys()}\n" 
        )
    #################################################################################
        

    # 2.b) State Methods
    ########################################################
    def GetCity(self):
        '''
        this shit needs comments
        '''
        return self.City


    def GetState(self):
        '''
        this shit needs comments
        '''
        return self.State

    
    def GetZipCode(self):
        '''
        this shit needs comments
        '''
        return self.ZipCode
    ######################################################



    # 3) Generating A Fake, Randomized "Payroll" Dictionary
    #################################################################################
    def MakeFakePayroll(self):                                  
        '''
        this shit needs comments
        '''

        fake_payroll_base = [                                   #

            {
                "provider_source":fake, 
                "provider_attribute":"iana_id",        
                "column_name":"Employee ID"
            },
            {
                "provider_source":fake, 
                "provider_attribute":"first_name",     
                "column_name":"First Name"
            },
            {
                "provider_source":fake, 
                "provider_attribute":"last_name",      
                "column_name":"Last Name"},
            {
                "provider_source":fake, 
                "provider_attribute":"date",           
                "column_name":"Date Of Birth"
            },
            {
                "provider_source":fake, 
                "provider_attribute":"phone_number",   
                "column_name":"Phone Number"
            },
            {
                "provider_source":fake, 
                "provider_attribute":"street_address", 
                "column_name":"Address"
            },
            {
                "provider_source":self, 
                "provider_attribute":"GetCity",        
                "column_name":"City"
            },
            {
                "provider_source":self, 
                "provider_attribute":"GetState",       
                "column_name":"State"
            },
            {
                "provider_source":self, 
                "provider_attribute":"GetZipCode",     
                "column_name":"Zip Code"
            }

        ]
    
        fake_payroll = { 

            fake_payroll_base[i]["column_name"] : 
            [ 
                getattr( 
                    fake_payroll_base[i]["provider_source"], 
                    fake_payroll_base[i]["provider_attribute"] #
                )()
                for _ in range( self.EmployeeSize ) 
            ]  

            for i in range( len(fake_payroll_base) ) 

        }

        fake_payroll["Phone Number"]  =  [

            phony.Person().telephone()

            for _ in range(self.EmployeeSize) 

        ]

        fake_payroll["City"]          =  [ 

            phony.Choice()([
                self.City, 
                phony.Address().city(),
                fake.city()
            ])

            for _ in range(self.EmployeeSize) 
        ]
        
        fake_payroll["Zip Code"]      =  [ 

            phony.Choice()([
                self.ZipCode, 
                fake.zipcode_in_state(self.State),
                fake.zipcode_in_state(self.State)
            ])

            for _ in range(self.EmployeeSize) 
        ]

        fake_payroll["Date Of Birth"]  =  [ 

            phony.Datetime().date(1959,1995).strftime('%m/%d/%Y') 
             
            for _ in range(self.EmployeeSize) 

        ]

        fake_payroll["Hire Date"]    =  [ 
            
            phony.Datetime().formatted_date()    
            
            for _ in range(self.EmployeeSize) 

        ]

        fake_payroll["Salary"]       =  [ 
            
            phony.Finance().price(50000, 108000) 
            
            for _ in range(self.EmployeeSize) 

        ]
        
        fake_payroll["Department"]   =  [ 
            
            phony.Choice()(self.Departments)     
            
            for _ in range(self.EmployeeSize) 

        ]
        
        return fake_payroll
    #################################################################################