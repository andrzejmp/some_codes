using System;
using System.Collections.Generic;

namespace pass_function_as_parameter
{
    class Program
    {   


        public static int[] sortByInsertion(int[] arr, bool display = false)
        {
            long comparisons = 0;
            long swaps = 0;
            int currentValue;
            for (int i = 1; i < arr.Length; i++)
            {
                currentValue = arr[i];
                // Set the start of our inner loop to the same value as i
                
                int j = i;
                if (display)
                {
                    comparisons++;
                }    
                while (j > 0 && arr[j - 1] > currentValue)
                {
                    arr[j] = arr[j - 1];
                    j--;
                    if (display)
                    {
                        swaps++;
                    }
                }
                arr[j] = currentValue;
            }
            Console.WriteLine("Insertion method did " + swaps + " swaps. Comparisons: " + comparisons);
            return arr;
        }
        




         public static List<int> sortByInsertion2(List<int> arr, bool display = false)
        {
            long comparisons = 0;
            long swaps = 0;
            int currentValue;
            for (int i = 1; i < arr.Count; i++)
            {
                currentValue = arr[i];
                // Set the start of our inner loop to the same value as i
                
                int j = i;
                if (display)
                {
                    comparisons++;
                }    
                while (j > 0 && arr[j - 1] > currentValue)
                {
                    arr[j] = arr[j - 1];
                    j--;
                    if (display)
                    {
                        swaps++;
                    }
                }
                arr[j] = currentValue;
            }
            Console.WriteLine("Insertion method did " + swaps + " swaps. Comparisons: " + comparisons);
            return arr;
        }
        
        public static int[] buubleSorting(int[] arr, bool display)
        {
            
            long comparisons = 0;
            long swaps = 0;
            bool swapped;
            do
            {
                swapped = false;
                for (int i = 0; i < arr.Length - 1; i++)
                {
                    if (display) 
                    {
                        comparisons++;
                    }                        
                     if (arr[i] > arr[i + 1])
                    {
                        int tmp = arr[i + 1];
                        arr[i + 1] = arr[i];
                        arr[i] = tmp;
                        swapped = true;
                        if (display) 
                        {
                            swaps++;
                        }
                    }
                }
            } while (swapped == true);
            
            Console.WriteLine("Bubble sort method did " + swaps + " swaps. Comparisons: " + comparisons );
            return arr;
        }


        public static int getMin(int[] arr, int start)
        {
            int min = arr[start];
            int minIndex = start;
            for (int i = start + 1; i < arr.Length; i++)
                if (arr[i] < min)
                {
                    min = arr[i];
                    minIndex = i;
                }
            return minIndex;
        }

        public static int[] sortBySelection(int[] arr)
        {
            //long swaps = 0;
            int minIndex;
            for (int i = 0; i < arr.Length; i++)
            {
                int tmp = arr[i];
                minIndex = getMin(arr, i);
                if (i != minIndex)
                {
                   arr[i] = arr[minIndex];
                   arr[minIndex] = tmp;
                   //swaps++;      
                }
            }
            //Console.WriteLine("Insertion method did " + swaps + " swaps.");
            return arr;
        }




        public static void PrintOut( List<int> arr, int n, int everyNth)
        {
            for (int i = 0; i < n; i++)
            {
                if (i % everyNth == 1)
                {
                    Console.Write(arr[i] + " ");
                }
            }
        }

        public static void PrintOutArr( int[] arr, int n, int everyNth)
        {
            for (int i = 0; i < n; i++)
            {
                if (i % everyNth == 1)
                {
                    Console.Write(arr[i] + " ");
                }
            }
        }

        /*
        static int functionToPass(int x)
        {
            return x + 10;
        }
        
        
        static void function(Func<int, int> functionToPass)
        {
            int i = functionToPass(22);
            Console.WriteLine("i = {0}", i);
        }

        */

        static void Main(string[] args)
        {
            //function(functionToPass);
        

            DateTime start;
            TimeSpan timeItTook;
            int n = 50000; int th = 5000;
            int min = 0; int max = 500;
            Random random = new Random();

            List<int> listZero = new List<int>();
            List<int> listOne = new List<int>();
            List<int> listTwo = new List<int>();
            
            int[] listThree = new int[n];
            int[] listFour = new int[n];
            int[] listFive = new int[n];
            

            //the array of N random integers
            for (int i = 0; i < n; i++)
            {
                listZero.Add(random.Next(min, max));
                
                listOne.Add(0);
                listTwo.Add(0);
            }
            
            
            
            for (int i = 0; i < n; i++)
            {
                 listOne[i] = listZero[i];
                 listTwo[i] = listZero[i];
                 
                 listThree[i] = listZero[i];
                 listFour[i] = listZero[i];
                 listFive[i] = listZero[i];
            }
            
            
            Console.WriteLine("The original array has {0} values. Every {1}th is printed out. ", n, th);
            PrintOut(listZero, n, th);
            Console.WriteLine("\n------------------");

            Console.WriteLine("\nSorting a list by Insertion");
            start = DateTime.Now;
            listOne = sortByInsertion2(listOne, true);
            timeItTook = DateTime.Now - start;
            PrintOut(listOne, n, th);
            Console.WriteLine("\nIt took " + timeItTook);
            Console.WriteLine("------------------");


            Console.WriteLine("\nSorting ann array by Insertion ");
            start = DateTime.Now;
            listThree = sortByInsertion(listThree, true);
            timeItTook = DateTime.Now - start;
            PrintOutArr(listThree, n, th);
            Console.WriteLine("\nIt took " + timeItTook);
            Console.WriteLine("------------------");

            Console.WriteLine("\nSorting ann array by BubbleSort ");
            start = DateTime.Now;
            listThree = buubleSorting(listFour, true);
            timeItTook = DateTime.Now - start;
            PrintOutArr(listFour, n, th);
            Console.WriteLine("\nIt took " + timeItTook);
            Console.WriteLine("------------------");

            Console.WriteLine("\nSorting ann array by Selection ");
            start = DateTime.Now;
            listThree = buubleSorting(listFive, true);
            timeItTook = DateTime.Now - start;
            PrintOutArr(listFive, n, th);
            Console.WriteLine("\nIt took " + timeItTook);
            Console.WriteLine("------------------");



        }
    }
}




