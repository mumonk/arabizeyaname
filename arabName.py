def main():
  she = " ibnat "
  he = " ibn "
  gender = ""

  while gender != "M" or "F":
    gender = input("Gender of name (M/F): ")
    if gender == "M" or "F":
      break
  if gender == "F":
    pronoun = she
  else:
    pronoun = he
  firstName = input("Enter your first name: ")
  fatFirstName = input("Enter your father's first name: ")
  print("")
  firstName = str(firstName)
  fatFirstName = str(fatFirstName)
  shortbizedName = firstName + pronoun + fatFirstName
  longChoice = input("Do you want the long-form (including last name, grandfather. and/or origin) name? |Y/N|: ")
  longChoice = longChoice.upper()

  if longChoice[0] == "Y":
    lastName = str(input("Enter your last name: "))
    print("")
    longerChoice = str(input("Do you want to use 1: your grandfather's name or 2: your place of origin? |1/2/Both|: "))
    if longerChoice[0] == "1":
      grandFatName = str(input("Enter your grandfather's first name: "))
      grandLongName = firstName + " al " + lastName + pronoun + fatFirstName  + " ibn " + grandFatName
      print("")
      print("Your arabized name is: " + grandLongName)
    elif longerChoice[0] == "2":
      whereFrom = str(input("Enter your place of origin (e.g Tribe, City, Country): "))
      locatedName = firstName + " al " + lastName + pronoun + fatFirstName + " al " + whereFrom + "i"
      print("")
      print("Your arabized name is: " + locatedName)
    else:
      grandFatName = str(input("Enter your grandfather's first name: "))
      whereFrom = str(input("Enter your place of origin (e.g Tribe, City, Country): "))
      longestName = firstName + " al " + lastName + pronoun + fatFirstName + " ibn " + grandFatName + " al " + whereFrom + "i"
      print("")
      print("Your arabized name is: " + longestName)
  else:
    print("Your arabized name is: " + shortbizedName)
    return


main()
