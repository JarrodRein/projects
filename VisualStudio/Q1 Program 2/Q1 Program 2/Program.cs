// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter two numbers");
Console.WriteLine("Enter number one and press enter");
int userNumber = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Enter number two and press enter");
int userNumber2 = Convert.ToInt32(Console.ReadLine());

int result = userNumber * userNumber2;
Console.WriteLine(result);