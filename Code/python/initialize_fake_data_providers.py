'''
NAME
    initialize_fake_data_providers.py


PURPOSE
    A  utility module  providing  a function to initiate an import of\n 
    python's  faker  abd   mimesis  modules which are then further augmented\n
    by adding to then a suite of open-sourced class methods, oherwise known as\n 
    'Community Providers'.


FUNCTIONS
    load_all_providers()


DEPENDENCIES
    Third Party Modules:\n
        faker\n
        mimesis   
'''


def load_all_providers():    
    '''
    NAME
        load_all_providers


    SYNOPSIS
        Loads the  Faker Class  and it's  Community Providers\n
        in addition to the  memisis  Module, for use with associated programs.


    DESCRIPTION
        Imports the python  Faker Class  and  mimesis Module, which provide\n
        a compliment of Standard 'Providers' (genres/categories) of fake data, 
        along with all of the extended  Community Providers  contributed by\n 
        it's user base which have been approved by the faker dev team.\n

        Each additonal Community Provider is first imported, and then\n 
        added to the list of  faker  Providers via it's  add_provider()\n 
        method.


    PROCESS
        #1.a Instantiate The mimesis Module

        #1.b Instantiate The Faker Class

        #2 Import Community Providers 

        #3 Add Community Providers As Extensions To The Faker

        #4 Export The Extended Faker       


    INPUT
        None.

    
    OUTPUT
        Tuple: 
            load_all_providers()[0]  --  fake  - <faker.proxy.Faker> 
            load_all_providers()[1]  --  phony - <module> 


    PARENT MODULE
        initialize_faker.py
    '''
    
    # 1.A Instantiate The mimesis module
    #######################################################################
    import mimesis   #  Import the  mimesis  module, setting the 
                     #  variable  phony  as a reference instance of it's 
    phony = mimesis  #  collection of various Data Povider Classes
    #######################################################################


    # 1.B Instantiate The Faker Class
    #######################################################################
    from faker import Faker   #  Import the  faker  module, setting the 
                              #  variable  fake  as an instance of it's 
                              #  built-in 'Faker' Class, enabling access
    fake = Faker()            #  to each of faker's Standard data Poviders
    #######################################################################


    # 2. Import Faker's Custom Community Providers 
    ##############################################################################
    from  faker_airtravel          import  AirTravelProvider    # Import the full
    from  faker_credit_score       import  CreditScore          # compliment of 
    from  faker_microservice       import  Provider             # open source, or 
    from  faker_music              import  MusicProvider        # 'Community' 
    from  faker_vehicle            import  VehicleProvider      # Providers which 
    from  mdgen                    import  MarkdownPostProvider # will extend the 
    from  faker_web                import  WebProvider          # basic functions
    from  faker_wifi_essid         import  WifiESSID            # of the Standard 
    from  faker_biology.physiology import  CellType, Organ      # Faker Providers
    from  faker_biology.bioseq     import  Bioseq               #
    ##############################################################################
    

    # 3. Add Community Providers As Extensions To The Faker 
    ########################################################
    fake.add_provider(AirTravelProvider)    # Add each of 
    fake.add_provider(CreditScore)          # the Community 
    fake.add_provider(Provider)             # Providers to 
    fake.add_provider(MusicProvider)        # the Faker 
    fake.add_provider(VehicleProvider)      # Object so they  
    fake.add_provider(MarkdownPostProvider) # may be accessed  
    fake.add_provider(WebProvider)          # as though they 
    fake.add_provider(WifiESSID)            # were extended 
    fake.add_provider(CellType)             # methods to the
    fake.add_provider(Organ)                # Faker class 
    fake.add_provider(Bioseq)               #
    #########################################################


    # 4. Export The Extended Faker  
    ##############################################################################
    return ( 
        fake,        #  All extended  Faker  methods are now accessible via  fake 
        phony        #  All  mimesis  methods are now accessible via  phony 
    )    
    ##############################################################################



if __name__ == "__main__":

    load_all_providers()
