employeeNameId={
    1:"Vivek",
    2:"Arun",
    3:"Surjana",
    4:"John",
    5:"Mohan",
    500: "Mohan Prakash"
}
#print(employeeNameId[500])
employeeNameId.setdefault(500,"Default Value")
print(employeeNameId[500])
print(employeeNameId)


