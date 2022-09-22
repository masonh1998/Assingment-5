
current_tuition = int(15000)
increase = float(input("Enter increase percentage: ""%"))

#decimal converts percentage to decimal form
decimal = increase*.01

print ("Year\t","Tuition")
print ('-----------------')

year1 = current_tuition + current_tuition *decimal
print(1,'\t',format(year1, '.2f'))

for x in range(2,11):
    year1 += year1 *.005
    print(x,'\t',format(year1, '.2f'))
    
     