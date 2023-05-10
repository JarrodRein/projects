// See https://aka.ms/new-console-template for more information
Console.WriteLine("Enter height and width");
Console.WriteLine("Enter height and press enter");
int userNumber = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Enter width and press enter");
int userNumber2 = Convert.ToInt32(Console.ReadLine());



string result = (userNumber > userNumber2) ? "Portrait" :  "LandScape";
Console.WriteLine(result);