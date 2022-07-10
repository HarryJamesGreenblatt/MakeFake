# Make_Fake  

$\\\,$   
#### Overview
Generates *Excel Spreadsheets* consisting of $\quad\text{randomized fake data} \quad$ modeled to simululate a Company's `Employee`, `Customer`,`Inventory`, and `Transaction` Reports.  
$\\\,$   
#### Usage
##### <center>Invocation Metods</center>
###### Microsoft Form $\longrightarrow$ Power Automate Flow
> May be invoked without parameters, providing randomly selected default attributes...
> $\\\,$   
> ![fukkedup](/images/Make_Fake_Form_Without_Params.jpg)
> $\\\,$   
> $\\\,$   
> ...or may be alternatively invoked using custom parameters to define the attributes.
> $\\\,$   
> ![fukkedup](/images/Make_Fake_Form_With_Params.jpg)

$\\\,$   

###### PowerShell
```powershell
Import-Module New-FakeCompany.psm1

# May be invoked without parameters, providing randomly selected default attributes...
New-FakeCompany

# ...or may be alternatively invoked using custom parameters to define the attributes.
New-FakeCompany `
    -$Name='Western Widgets' `
    -$Category='Egregiously Overpriced Generic Widget Wholesaler' `
    -$EmployeeSize=179 `
    -$CustomerSize=497 `
    -$InventorySize=505 `
    -$City='Allentown' `
    -$State='PA'
``` 

$\\\,$   

###### Python 
   
```python
from Make_FakeCompany.py import FakeCompany()

# May be invoked without parameters, providing randomly selected default attributes...
fake_company_with_random_attributes = FakeCompany()

# ...or may be alternatively invoked using custom parameters to define the attributes.
fake_company_i_made_up = FakeCompany(
    name='Western Widgets',
    category='Egregiously Overpriced Generic Widget Wholesaler'
    employee_size=179
    customer_size=497
    inventory_size=505
    city='Allentown'
    state='PA'
)
``` 

