Discount = 0

def welcome():
  global Money_gbp
  global currency
  Money_gbp = int(input("\nPlease enter the amount you would like to convert: "))
  if  Money_gbp > 2500:
    print("\nError we cannot accept amounts higher than 2500")
    welcome()

  print("\n Please choose from these currency's: \n")
  print("   1.Amercain dollar (USD)")
  print("   2.Euro (EUR)")
  print("   3.Brazillain real (BRL)")
  print("   4.Japanese yen (JPY)")
  print("   5.Turkish lira (TRY)\n")

  try:
    currency = int(input("\nPlease input the currency the desired currency you wish to convert to in numbers 1-5:  "))
  except:
    currency = int(input("\nPlease input the currency the desired currency you wish to convert to in numbers 1-5:  "))
    
  if currency == 1:
    USD()
  else:
    if currency == 2:
      EUR()
    else:
      if currency == 3:
        BRL()
      else:
        if currency == 4:
          JPY()
        else:
          if currency == 5:
            TRY()
  #i create another variable where we use a prompt to ask the user if they 
  #are a member of staff and we use lower to error check the input     
    # I create a function called staff
      # i then go on to create a variable called total_cost which adds up the currency and comission
def staff():
  comission = (Money_gbp/100)*fee
  answer = str(input("\nAre you a member of staff ? y/n : ").lower())
  if answer == "n":
    print("\nTotal currency changed is : ","£",changed_currency)
    print("\nDiscounts applied: no discounts applied")
    print("\nComission taken by staff: ","£",comission)
    #This part starts just like previous section but in this one no 
    #discounts are applied so results are just printed to the user
  else:
    if answer == "y":
      Discount = (Money_gbp/100)*5
      new_cost = Money_gbp - Discount
      comission = comission - 10
      print("\nTotal cost is : ","£",new_cost)
      print("Discounts applied: ","£",Discount)
      print("\nComission taken by staff: ","£",comission)
    else:
      print("\nUser has entered something other than y or n")
      staff()
      #function staff is called if y or n is not entered an error is raised
           
def Transction_fee():
  #keeps saying comssission thiry regradless of waht i do
  global  fee
  if Money_gbp <= 300 :
    fee = 3.5 
    staff()
  else:
    if Money_gbp >= 300 :
      fee = 3.0
      staff()
    else:
      if Money_gbp >= 750 :
        fee  = 2.5
        staff()
      else:
         if Money_gbp >= 1000:
           fee = 2.5
           staff()
         else:
           if Money_gbp >2000 :
             fee = 1.5
             staff()
           else:
             print("error")
             print("maximum amount is 2500 gbp")
             print("restart")
        
# this a really lengthy but in short depending on the currency choosen by the a fee is set and using that the comission is figured out       


def USD():
  global changed_currency
  changed_currency = Money_gbp * 1.40
  Transction_fee()

def EUR():
  global changed_currency
  changed_currency = Money_gbp * 1.14
  Transction_fee()

def TRY():
  global changed_currency
  changed_currency = Money_gbp * 5.68
  Transction_fee()

def JPY():
  global changed_currency
  changed_currency = Money_gbp * 151.05
  Transction_fee()

def BRL():
  global changed_currency
  changed_currency = Money_gbp * 4.77
  Transction_fee()

# all the above function take you to the transction fee function listed earlier and the currency is converted

  
#This function welcome first ask the user how much money they would like to convert.So if the amount is over 2500 the program raises an error and redirects the user to start of the code and Secondly, it prints out all the options the user has then it trys aksing for the currency if thats possibly.sucessful depending on the number entered the user will go to previously mentioned functions.
    
welcome()
#calls the function

#con : only annoyance about this is it eaccpect negative inputs