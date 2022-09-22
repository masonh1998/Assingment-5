
current_tuition = int(15000)
increase = float(input("Enter increase percentage: ""%"))

#decimal converts percentage to decimal form
decimal = increase*.01

print ("Year\t","Tuition")
print ('-----------------')

for x in range(1,11):
    current_tuition += current_tuition*decimal
    print(x,'\t',format(current_tuition, '.2f'))
    
     
    