# Match module code to module name
def getModuleName(modCode):
    match modCode:
        case "CSC1006":
            return "Mathematics II"
        case "CSC1007":
            return "Operating Systems"
        case "CSC1008":
            return "Data Structure & Algorithm"
        case "CSC1009":
            return "Object-Oriented Programming"
        case "CSC1010":
            return "Computer Networks"


# Take in user input for module code
modCode = input("Please enter the module code: ")

# Print corresponding module name based on module code
print("Module Name: ", getModuleName(modCode))
