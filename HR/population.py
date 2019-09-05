#/Tómas Ingi Villalobos
#08/21/2019 - Háskóli Reykjavíkur


people = 307357870
user_input = int(input("Years: "))
seconds = 365*24*60*60
birth = seconds/7
death = seconds/13
immigrant = seconds/35
if user_input >= 0:
    user_input_float =(user_input)
    people_now = people + (user_input_float*birth) - (user_input_float*death) + (user_input_float*immigrant)
    print ("New population after", user_input, "years is", (int(people_now)))        
else:
    print ("Invalid input!")
    
