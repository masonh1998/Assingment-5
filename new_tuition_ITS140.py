
current_tuition = int(15000)
increase = float(.04)

print ("Year\t","Tuition")
print ('-----------------')

for x in range(1,11):
    current_tuition += current_tuition*increase
    print(x,'\t',format(current_tuition, '.2f'))
    
     
    