// See https://aka.ms/new-console-template for more information

//Drivers speed check and license suspension check
Console.WriteLine("Enter speed limit and speed");
Console.WriteLine("Enter speed limit and press enter");
int userNumber = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Enter speed and press enter");
int userNumber2 = Convert.ToInt32(Console.ReadLine());

string result = (userNumber > userNumber2) ? "OK" : "Not OK";
int points = 0;

for(var i =userNumber2; i>userNumber; i -= 5)
{
    points++;
}

if(points >= 12)
{
    Console.WriteLine("License Suspended");
}

Console.WriteLine(points);
