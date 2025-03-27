using System;

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

   if(String.IsNullOrWhiteSpace(input))
{
    System.Environment.Exit(-1);
}


//var lists = new List<string>();
string[] lists = new string[] { };

string[] listss = input.Split('-');
// lists =Convert.ToInt32( input.Split('-'));

//lists = listss;

int num1, num2, num3;

num1 = Convert.ToInt32(listss[0]);
num2 = Convert.ToInt32(listss[1]);

//Console.WriteLine(num1);
//Console.WriteLine(num2);

//for(int z=0; z<lists.Length; z++)
//{
//    Console.WriteLine(lists[z]);
//}


for (var i = 0; i <= listss.Length; i++)
{
    if(i == listss.Length)
    {
        break;
    }
    //  Console.WriteLine(listss[i]);
    num1 = Convert.ToInt32(listss[i]);
    //
    //num2 = Convert.ToInt32(listss[++i]);
    lists.Append(listss[i]);
    Console.WriteLine(lists[i]);

    //for (var z = 0; z <= lists.Length; z++)
    //{

    //  //  lists.Append(listss[i]);
    //    num2 = Convert.ToInt32(lists[z]);
    //    if (num1 == num2)
    //    {

    //        Console.WriteLine("Duplicates");
    //        System.Environment.Exit(-1);

    //    }


    //}
    
   
}