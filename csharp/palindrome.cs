/******************************************************************************
// Palindrome checking - recursive version
*******************************************************************************/
using System;
class Palindrome {
    
  public static bool IsPalindrome(string str)
    {
        if (str.Length <= 1)
            return true;
        else
        {
            if ( str[0] != str[ str.Length - 1 ] )
                return false;
            else
                return  IsPalindrome( str.Substring( 1, str.Length-2 ) );
        }   
    }  
    
  public static void Main() {
    Console.WriteLine("abba" + " - " +IsPalindrome("abba"));
    Console.WriteLine("1234321" + " - " +IsPalindrome("1234321"));
    Console.WriteLine("ala ma ala" + " - " +IsPalindrome("ala ma ala"));
    Console.WriteLine("a" + " - " +IsPalindrome("a"));
  }
}

 