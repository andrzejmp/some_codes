/******************************************************************************
Fibonacci numbers
*******************************************************************************/
using System;
class Finonacci {
    
  public static long Fibo (int n)
  {
      int fibo = 0;
      int a = 1;
      int b = 1;
      if(n<3) return 1;
      
      for(int i=3; i<=n; i++)
      {
          fibo = a + b;
          b = a;
          a = fibo ;
      }
      
      return fibo;
  }
  
   public static long Fibo2 (int n)
  {
      if (n<3) return 1;
	  
      return Fibo2(n-1) + Fibo2(n-2);
  }
    
  static void Main() {

     for (int i=1;i<=45;i++) 
     Console.WriteLine(i + " " + Fibo(i) +" " +Fibo2(i));
      
  }
}
