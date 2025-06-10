temps = [[0.0 for h in range(24)] for d in range (31)]
#the matrix is magically updated here
total = 0.0
for day in temps:
    total += day[11]

average = total/31
print("Average temperature at noon: ",  average)

#section summary
#A four column/ four row table - a two dimensional array(4 x 4)

table = [[":(",":)" , ":(",":)"  ], 
         [":)",":(" , ":)",":)"  ],
         [":(",":)" , ":)",":("  ],
         [":(",":)" , ":)",":("  ]]

print(table)
print(table[0][0])
print(table[0][3])