using System;

class Program {
 //-------------------    
    class Student 
    {
        public string name;
        public int age;
        public string field;
        public int grade;
    }
    
 //-------------------    
  static void Main() {
    
    Student alberto = new Student();
    Student asli = new Student();
    Student elif = new Student();
    Student angel = new Student();
    Student alicia = new Student();
    Student jan = new Student();
    
    alberto.name = "Alberto Rodriguez";
    alberto.age = 23;
    alberto.field = "Informatica";
    alberto.grade = 90;
    
    angel.name = "Angel Garcia";
    angel.age = 21;
    angel.field = "Mathematics";
    alberto.grade = 80;
    
    jan.name = "Janowski";
    jan.age = 25;
    jan.field = "Mathematics";
    jan.grade = 70;
    
    Student[] students = {alberto, angel, jan};
    
    
    for(int i=0; i<students.Length; i++)
    {
        Console.WriteLine(students[i].name + " is " + students[i].age   );
    }
    
    
  }
}

