try:
    #create file
    with open("report.txt","w")as file:
        file.write("Rahul-85\n")
        file.write("priya-90\n")
        file.write("rohan-78\n")
        file.write("sneha-92\n")
        file.write("Amit-65\n")
    with open ("report.txt","r") as file:
        print("students scoring more than 80:")
        for line in file:
            name, marks = line.strip().split("-")
            if int(marks) > 80:
                print(name,  marks)
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation complete.")                    