using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;





namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter number between 1-10");
            int userNumber = Convert.ToInt32(Console.ReadLine());
            string result = (userNumber > 0 && userNumber < 10) ? "Valid" : "Invalid";
            Console.WriteLine(result);

        }
    }
}