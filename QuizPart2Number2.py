with open('data.txt','r') as file:

    class Employee:
        def __init__(self, id:str,name:str,position:str,salary:int):
            self.__id = id
            self.__name = name
            self.__position = position
            self.__salary = salary
        def get_id(self):return self.__id
        def get_name(self):return self.__name
        def get_position(self):return self.__position
        def get_salary(self): return self.__salary
        
        def __str__(self):
            return "|{},|{},|{},|{}|".format(self.__id,self.__name,self.__position,self.__salary)
        def new_staff(self,id,name,position,salary,over=False):
            validation = self.check_data(id,name,position,salary)
            if validation == True or over == True:
                with open(self.file_name,'a') as file:
                    file.write(str(id)+'|'+str(name)+'|'+str(position)+'|'+str(salary)+'\n')
                    return True
            return validation
