<#
.SYNOPSIS
   Processes a text file representing the list of Community Providers 
   available in the python faker module, converting the result into 
   JSON format.

.DESCRIPTION
   Reads and processes a text file representing the list of available 
   faker methods contributed by faker's user community. The methods 
   are refered to as 'Community Providers' from the context of the 
   faker module.

   COLLECTING PROVIDER METHOD BASE NAMES AND GENERATING COLUMN HEADERS
   The source file is the COUMMUNITTY PROVIDER LIST (see NOTES section). 
   Import-FakeProviders  runs two  perl  string substitutions on this list, 
   one reduces each method in the list down to it's base name, (i.e  ssn,  
   android_platform_token ), while the other also tranforms the list down to 
   it's  base_name,  but additionally removes the underscore and converts each 
   word to Title Case, (i.e. Ssn, Android Platform Token), which is suitale
   for use as  column_headers   in a table.
   
   IMPLEMENTING THE BASE NAMES AND COLUMN HEADERS AS A HASH TABLE
   Following  perl  processing, a local variable called  community_providers
   stores each   base_name   and   column_header   result  in a hash table whose 
   keys match those names stated above. 

   CONVERTING THE HASH TABLE INTO JSON
   The hash table containing the  PROVIDER METHOD BASE NAMES  and the  COLUMN 
   HEADERS is finally converted into JSON format  via  the   ConvertTo-Json
   cmdlet. By converting the data into a neutral format, the full data structure can be 
   easily piped into python for a simple conversion using  json.loads()   

.NOTES   
   PROCCESSING OF THE COMMUNITY PROVIDER LIST
   The Community Provider List is statically generated in a
   standalone process triggered by invoking faker from a command line 
   interface using the following command:

      faker -i
   
   this produces a comprensive list of additional custom providers, 
   describing their syntax along with providing usage and output 
   examples, as expressed in the excerpt below:
   
      ### faker.providers.ssn

         fake.ssn()
                     # Z155222055

      ### faker.providers.user_agent

         fake.android_platform_token()
                     # Android 2.3.7

   However, only the methods themselves are desirable:

      fake.ssn()
      fake.android_platform_token()
      .
      .
      .
   
   In order to transform the source document to the desired ouput format,
   the full document was piped into  perl  and processed using the following
   regular expression substition:
   
      /(fake\..+\(.*)\)/ and print qq|$1)|;

.PARAMETER FilePathToCommunityProviderList
   The file path to the Community Provider List.

.PARAMETER PerlCodeToNormalizeCommunityProviderBaseNames
   The perl substitution expression designed to transform the Community Provider List'
   into a list of PROVIDER METHOD BASE NAMES.

.PARAMETER PerlCodeToNormalizeColumnHeaders
   The perl substitution expression designed to transform the Community Provider List'
   into a list of TITLE CASED representaions of the PROVIDER METHOD BASE NAMES which 
   would be suitable to use as COLUMN HEADERS. 

.INPUTS
   NONE

.OUTPUTS
   A string representing the  community_providers  hash table converted to  JSON 

      PS C:\Users\harry\powershell> (.\Import-FakeData.ps1).GetType()

      IsPublic IsSerial Name                                     BaseType     
      -------- -------- ----                                     --------     
      True     True     String                                   System.Object
#>
function Import-FakeData {

    [CmdletBinding()]
 
    param (
        [string] $Env = 'C:\Users\harry\python\thunderDome\Scripts\Activate.ps1',   
        [string] $PythonScript = '..\python\Make_FakeCompany_Client.py'
    )

    begin {
        & $Env
    }
    
    process {
       python $PythonScript
    }

   #  end{

   #  }
 
 }

 Import-FakeData