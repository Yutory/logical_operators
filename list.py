#code = ["X","H","E","Z","L","L","!","P","O","-","N"," ","W","@","R","D","O","#"]
#Hello = code[1] + code[2] + code[4] + code[5] + code[8] + code[6]
#print(Hello) 
'''grid = [ 
["The", "sky","is"],
["full","of","stars"],
["shining","bright","tonight"]
]
print(grid[0][0:2])
 
print(
grid[0][0], 
grid[1][2],"are",
grid[2][0]
)
print(grid[2][-1],
grid[2][-2],
grid[2][-3])'''

'''playlist = ["song A", "song B", "song C"]
playlist[1] = "song D"
print(playlist)
playlist.append("song E")
print(playlist)
playlist.insert(0, "intro")
print(playlist)'''

desks = []
desks.append(input("student name1:"))
desks.append(input("student name2:"))
desks.append(input("student name3:"))
print(desks)
new_student = input("new_student name:")
desks[1] = "new_student"
print(desks)
desks.insert(1, "new_guy")
print(desks)


