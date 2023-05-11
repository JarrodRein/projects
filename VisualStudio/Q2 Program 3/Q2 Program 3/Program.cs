int num =0;

Console.WriteLine("Enter number for making a factorial!");
num = Convert.ToInt32(Console.ReadLine());
int num2 = 1;


for(var i = 1; i <=num; ++i)
{
    num2 *= i;
}

Console.WriteLine(num2);

