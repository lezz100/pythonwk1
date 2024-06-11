#Creates a new file in write mode
with open('my_file.txt','w') as file:
    file.write("Hello world! I love python")
    file.write("Python is quite versatile and used in a variety of fields")
    file.write("And 1 of them is  data analysis")

    print("File 'my_file.txt' created successfully.")

    #Read the contents of 'my_file.txt'
    with open('my_file.txt', 'r') as file:
        file_contents = file.read()
        print("\nContents of 'my_file.txt' :\n")
        print(file_contents)

    with open('my_file.txt', 'a') as file:
        file.write("This is an additional line. \n")
        file.write("On where else pythin can be used\n")
        file.write("Which is Machine Learning and AI.")

        print("Text appended to 'my_file.txt' successfully")
    try:
        #Open "my_file.txt" in append mode
        with open('my_file.txt', 'a') as file:
            #Append the lines
            file.write("Python is indeed versatile")
            print("Text appended to 'my_file.txt' successfully")
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied. Check file permissions.")
    finally:
        print("File handling completed.")