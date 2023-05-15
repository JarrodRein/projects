
string input = " ";
int num = 0;
Console.WriteLine("Enter numbers seperated by - ");

//num = Convert.ToInt32(Console.ReadLine());
//num *=2;
//while (true)
//{

//    input = Console.ReadLine();


//    //--num;
//}


input = Console.ReadLine();

var lists = new List<int>();

string[] listss = input.Split('-');
// lists =Convert.ToInt32( input.Split('-'));

int num1, num2, num3;

num1 = Convert.ToInt32(listss[0]);
num2 = Convert.ToInt32(listss[ 1]);

Console.WriteLine(num1);
Console.WriteLine(num2);


for (var i = 0; i <= listss.Length; i++)
{
    if (i == listss.Length)
    {
        Console.WriteLine("Consecutive");
        break;
    }
    //  Console.WriteLine(listss[i]);
    num1 = Convert.ToInt32(listss[i]);
    num2 = Convert.ToInt32(listss[++i]);

    if (num1 < num2  )
    {
       
        continue;
       
    }
    else if (num2 < num1)
    {
        Console.WriteLine("Not Consecutive");
        break;
    }
}