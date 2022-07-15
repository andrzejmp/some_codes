import java.lang.Math;

interface EqFace1 
{
     void solve1(double a, double b); 
}

interface EqFace2 
{
     void solve2(double a, double b, double c); 
}

class Equation implements EqFace1, EqFace2
{
    public void solve2(double a, double b, double c) 
    {
        System.out.println(a+"x2 + "+ b+"x +" + c + " = 0");
        double delta = b*b - 4*a*c;
        if(delta >=0) 
        {
            double x1 = (-b - Math.sqrt(delta)) / (2*a);
            double x2 = (-b + Math.sqrt(delta)) / (2*a);
            System.out.println("x1 =" + x1 + " x2 =" + x2); 
        }
        else
        {
            System.out.println("No solution");
        }
    }
    
    public void solve1(double a, double b)
    {
        System.out.println("x = " + ( -b / a));
    }
    
}

class Main 
{
    public static void main(String args[]){
    Equation e1 = new Equation();
    e1.solve1(2, 4);
    
    Equation e2 = new Equation();
    e2.solve2(1, 5, 6);
    
 }
}

