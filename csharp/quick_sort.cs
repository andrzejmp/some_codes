/******************************************************************************
quicsort
*******************************************************************************/
using System;
using System.Collections.Generic;
class Program 
{
     public static void QuickSort(List<int> list, int left, int right) 
	{
		if (left < right)
		{
			int pivot = Partition(list, left, right);

			if (pivot > 1) {
				QuickSort(list, left, pivot - 1);
			}
			if (pivot + 1 < right) {
				QuickSort(list, pivot + 1, right);
			}
		}
	
	}
        
     public static int Partition(List<int> list, int left, int right)
	{
		int pivot = list[left];
		while (true) 
		{

			while (list[left] < pivot) 
			{
				left++;
			}

			while (list[right] > pivot)
			{
				right--;
			}

			if (left < right)
			{
				if (list[left] == list[right]) return right;

				int tmp = list[left];
				list[left] = list[right];
				list[right] = tmp;
			}
			else 
			{
				return right;
			}
		}
	}
        
	public static void PrintOutAll(List<int> list)
	{
		for (int i = 0; i < list.Count; i++)
		{
			Console.Write(list[i] + " ");
		}
		Console.WriteLine();
	}

	static void Main() 
	{
		List<int> theList = new List<int>();
		Random random = new Random();
				
		for (int i = 0; i < 10; i++)
		{
			theList.Add(random.Next(0, 30));
		}
		
		Console.WriteLine("Unsorted list:");
		PrintOutAll(theList);     

		QuickSort(theList, 0, theList.Count-1);
		
		Console.WriteLine("Sorted list: ");
		PrintOutAll(theList);
		Console.Write("\n");
				
	}
}
