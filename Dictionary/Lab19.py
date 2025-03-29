employeeNameId={
    1:"Vivek",
    2:"Arun",
    3:"Surjana",
    4:"John",
    5:"Mohan"
}
#print(employeeNameId[500])
employeeNameId.setdefault(500,"Default Value")
print(employeeNameId[500])
print(employeeNameId)


