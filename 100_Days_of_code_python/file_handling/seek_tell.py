
# import os 
# with open('example.2txt', 'w') as file:
# with open('100_Days_of_code_python/file_handling/example.txt', 'r') as file:
with open('example2.txt', 'rb') as file:
    # print(file)
    print(file.seek(1000))  # Move 10 bytes backward from the beginning
    print(file.tell())
    # print(file.seek(-5,0))
    # file.seek(3,1)
    # content = file.write("jai shree ram \nHello")  # Read from the new position
    # content = file.writelines("jai shree ram \nHello")  # Read from the new position
    # l=["jai shree ram \n","Hello\n","ok \n","bye\n"]
    # content = file.writelines(l)  # Read from the new position
    content = file.read()  # Read from the new position
#     p=os.path.basename('example.2txt')
    # print(file.truncate(5))
    # print(f"Read content: {content}")
    # print(f"Read content: {len(content)}")
#     print(f"file path : {p} \n\n")

f=open("file.txt",'w')
print(f)
print(f.close())
f.close()