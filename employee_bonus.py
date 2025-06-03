from datetime import date
class BonusCalculator:
    def calculate_bonus(d1,d2):
        id=d1.get('id')
        dob=d1.get('dob')
        salary=d2.get('salary')
        if type(id)!=type(1) or type(salary) !=type(1):
            raise ValueError("Type should be integer")
        if type(dob)!=type(" "):
            raise ValueError("Type should be string")
        dob=dob.split("-")
        year=int(dob[0])
        month=int(dob[1])
        day=int(dob[2])
        d1 = date(year,month,day)# employee dob
        d2 = date(2014,9,1)#y,m,d  (given date)
        delta = d2-d1
        #print("Days ",delta.days)
        years=delta.days/365
        #print("Years ",years)
        age=int(years)
        if (age<25 or age>60) and salary<5000:
            salary+=100
        elif  age<25 or age>60:
            salary+=200
        elif salary<5000:
            salary+=100
        elif age in range(25,31):
            salary+=salary*20/100
        elif age in range(31,61):
            salary+=salary*30/100
        emp_result={}
        emp_result['id']=id
        emp_result['salary']=salary
        return emp_result




















# def calculate_bonus(id,dob,salary):
#     d1={"ID":id,"DOB":dob}
#     d2={"ID":id,"Salary":salary}
#     #print(id,dob,salary)
#     print(d1)
#     print(d2)
#     dob=dob.split("-")
#     year=int(dob[0])
#     month=int(dob[1])
#     day=int(dob[2])
#     #date1 = datetime.datetime(1987,7, 2)# employee dob
#     date1 = datetime.datetime(year,month, day)# employee dob
#     date2 = datetime.datetime(2014, 9, 1)#y,m,d  (given date)
#     time_difference = relativedelta(date2, date1)
#     age = time_difference.years
#     #print(time_difference)
#     #print(time_difference.days)
#     #print(age, "years")
#     print("salary without bonus",salary)
#     if age in range(25,31):
#         salary+=salary*20/100
#     elif age in range(31,61):
#         salary+=salary*30/100
#     print("salary with bonus",salary)
#     emp_result={}
#     emp_result['ID']=id
#     emp_result['Salary']=salary
#     print(emp_result)
#
#
#
# if __name__=="__main__":
#     id=int(input("Enter Employee ID"))
#     dob=input("Enter Employee Date Of Birth(YYYY-MM-DD)")
#     salary=int(input("Enter Employee salary"))
#     calculate_bonus(id,dob,salary)
