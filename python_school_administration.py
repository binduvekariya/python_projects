import csv

def write_into_csv(info_list):
    with open("student_info.csv","a" , newline = "") as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","contact_number","Email_ID"])
        writer.writerow(info_list)

if __name__ == "__main__":
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter the information about student {} in the following format (name age contact_no. email_ID): ".format(student_num))
        print("Entered information " + student_info)

        student_list = student_info.split(" ")
        print("\n The Entered information is: \n Name:{}\n Age:{}\n Contact_number:{}\n Email-ID:{}"
            .format(student_list[0],student_list[1],student_list[2],student_list[3]))
        
        choice_check = input("Is the Entered info is correct ? (Yes/No): ")
        if choice_check.lower() == "yes".lower():
            write_into_csv(student_list)
            con_check = input("You want to Enter info for another student (yes/no): ")
            if con_check.lower() == "yes".lower():
                condition = True
                student_num +=1
            elif con_check.lower() == "no".lower():
                condition = False
        elif choice_check.lower() == "no".lower():
            print("\n Please re-enter the values ")

