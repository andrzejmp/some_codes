//Employee v. 01
using System;

class Program
{
    //-------------------    
    public class Employee
    {
        private int id;
        private string firstName;
        private string lastName;
        private DateTime dateOfBirth;
        private double salary;
        public Employee()
        {
            Counter++;
        } //default constructor

        public Employee(int p_id, string p_firstName, string p_lastName, DateTime p_dateOfBirth, double p_salary)
        {
            id = p_id;
            firstName = p_firstName;
            lastName = p_lastName;
            dateOfBirth = p_dateOfBirth;
            salary = p_salary;
            Counter++;
        }

        //Properties
        public string FirstName
        {
            get { return firstName; }
            set { firstName = value; }
        }

        public string LastName
        {
            get { return lastName; }
            set { lastName = value; }
        }

        public DateTime DateOfBirth
        {
            get { return dateOfBirth; }
            set { dateOfBirth = value; }
        }

        public double Salary
        {
            get { return salary; }
            set { salary = value; }
        }



        private static int Counter = 0; //counts emplyoess

        public static int CountEmplyoess()
        {
            return Counter;
        }

        public void promotion(double rise)
        {
            Salary = salary * (1 + rise / 100);            
        }

        //-------------------------------------

        public static void ShowEmployess(Employee[] listOfEmployess)
        {
            string job_;
            foreach (Employee empl in listOfEmployess)
            {
                Type type = empl.GetType();
                string stringType = type.ToString();                    
                int pos = stringType.IndexOf('.');
                    
                if (stringType.Substring(pos + 9, 4) == "Spec")
                {
                    Specialist spec = (Specialist)empl;
                    job_ = spec.Job;
                }
                else
                {
                    job_ = "";                    
                }
                DateTime birthDate = empl.DateOfBirth;
                string bd = birthDate.ToString().Substring(0, 10);
                Console.WriteLine("{0, -10} {1, 5} {2, 15 } {3, 10} {4, 25}", empl.LastName, empl.FirstName, bd, empl.Salary, job_);
            }

        } // end of ShowComputers



        //---------------------------------------
    } //class Emplyee


    public class Specialist : Employee
    {
        public Specialist(int p_id, string p_firstName, string p_lastName, DateTime p_dateOfBirth, double p_salary, string p_job)
            : base(p_id, p_firstName, p_lastName, p_dateOfBirth, p_salary)
        {
            job = p_job;
        }
        // private member variables
        private string job;

        // public properties
        public string Job
        {
            get { return job; }
            set { job = value; }
        }
    } //end of class Specialist 

    

    public static double getAverageSalary(Employee[] list)
    {
        double total = 0;
        for (int i = 0; i < list.Length; i++)
        {
            total += list[i].Salary;
        }
        return total / list.Length;
    }


    //-------------------    
    static void Main()
    {
        Employee e1 = new Employee(1, "John", "Smith", new DateTime(2002, 01, 14), 2200);
        Employee e2 = new Employee(2, "Anna", "Bula", new DateTime(1998, 04, 24), 2100);

        e2.DateOfBirth = new DateTime(2002, 02, 14);

        Specialist e3 = new Specialist(3, "Edek", "Beker", new DateTime(1993, 04, 24), 4000, "Java Specialist");
        Specialist e4 = new Specialist(4, "Roger", "Walters", new DateTime(1994, 05, 21), 3400, "Web Development");
        Specialist e5 = new Specialist(5, "Ken", "Moltke", new DateTime(1995, 07, 11), 3900, "C# Proggrammer");
        Specialist e6 = new Specialist(6, "Willy", "Abced", new DateTime(1985, 11, 12), 3100, "Network administrator");

        Employee[] listOfEmloyess = { e1, e2, e3, e4, e5, e6 };
        
        Console.WriteLine("\nWe have " + Employee.CountEmplyoess() + " employess.");
        
        Console.WriteLine("\n-------------------------------------------------------------------");
        Console.WriteLine("The List od all Employees\n");
        Employee.ShowEmployess(listOfEmloyess);

        Console.WriteLine("\n-------------------------------------------------------------------");
        Console.WriteLine("The average salary is " + getAverageSalary(listOfEmloyess));
        Console.WriteLine("-------------------------------------------------------------------\n");

        Console.WriteLine("Salary of {0} {1} ({2}) before promostion: {3} " , e5.LastName, e5.FirstName, e5.Job, e5.Salary);
        e5.promotion(20);
        Console.WriteLine("Salary of {0} {1} ({2}) before promostion: {3} ", e5.LastName, e5.FirstName, e5.Job, e5.Salary);


        Console.WriteLine("-------------------------------------------------------------------\n");




        Employee.ShowEmployess(listOfEmloyess);
        Console.ReadLine();
    }

}

