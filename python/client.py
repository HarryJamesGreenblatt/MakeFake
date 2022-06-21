from Make_FakeCompany   import FakeCompany

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


