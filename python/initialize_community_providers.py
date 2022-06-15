'''
NAME
    initialize_community_providers.py


PURPOSE
    A  utility module  providing a function to perform a subprocess\n
    call to the host system's PowerShell terminal in order to execute\n
    an associated  Import-FakeProviders.ps1  utility script.


FUNCTION
    Defines  parse_all_faker_providers()


DEPENDENCIES
    Project Files:\n
        Import-FakeProviders.ps1\n
    
    Standard Library Modules:\n
        subprocess\n
        json
'''

def parse_all_faker_providers():
    '''
    NAME
        parse_all_faker_providers


    SYNOPSIS
        Performs a call to the host system's PowerShell terminal as a\n
        subprocess, initiating the execution of  Import-FakeProviders.ps1,\n
        and using it's output for additional processing. 


    DESCRIPTION
        Imports the python  Faker Class,  which provides a compliment\n 
        of Standard 'Providers' (genres/categories) of fake data, along\n 
        with all of the extended  Community Providers  contributed by\n 
        it's user base which have been approved by the faker dev team.\n

        Each additonal Community Provider is first imported, and then\n 
        added to the list of  faker  Providers via it's  add_provider()\n 
        method.


    PROCESS
        #1 Import The Required Standard Library Dependencies 

        #2 Call PowerShell To Invoke  Import-FakeProviders.ps1  As A Parallel Subprocess  

        #3 Convert And Export The JSON-Formatted Result Of The Subproccess  


    INPUT
        None.

    
    OUTPUT
        a  <dict>  consisting of the converted JSON output from\n 
        Import-FakeProviders.ps1 
        

    PARENT MODULE
        initialize_community_providers.py
    '''

    # 1 Import The Required Standard Library Dependencies 
    #####################################################################################
    import subprocess  #  The subprocess module performs parallel system calls to the OS,     
    import json        #  while the json module converts JSON to a dict. 
    #####################################################################################


    # 2 Call PowerShell To Invoke  Import-FakeProviders.ps1  As A Parallel Subprocess  
    ############################################################################################
    subproc = subprocess.run(                                                  # subproc  will
        [                                                                      # store the 
            r'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', # result of a 
            r'$(C:\\Users\\harry\\powershell\\Import-FakerProviders.ps1)'      # system call
        ],                                                                     # to PowerShell,
        stdout=subprocess.PIPE,                                                # which runs 
        stderr=subprocess.STDOUT,                                              # the dependency,  
        shell=True                                                             # and returns
    )                                                                          # a JSON string
    ############################################################################################


    # 3 Convert And Export The JSON-Formatted Result Of The Subproccess  
    #######################################################################################
    return (                                        # json.loads() converts a utf-8 encoded
        json.loads(subproc.stdout.decode('utf-8'))  # string representation of the subproc 
    )                                               # result into a python dict
    #######################################################################################



if __name__ == "__main__":

    parse_all_faker_providers()
    

