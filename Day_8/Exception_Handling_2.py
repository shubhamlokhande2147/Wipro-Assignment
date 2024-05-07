class InvalidCustomerException(Exception):
    pass

class CustomerBusiness:
    def get_customer(self, cust_id):
        if cust_id == "":
            raise InvalidCustomerException()
        return cust_id

class AccountUI:
    def deposit_money_ui(self):
        try:
            cust_id = CustomerBusiness().get_customer("")
        except InvalidCustomerException:
            print("Invalid Customer Exception raised")
        except Exception:
            print("Exception raised")

a = AccountUI()
a.deposit_money_ui()
