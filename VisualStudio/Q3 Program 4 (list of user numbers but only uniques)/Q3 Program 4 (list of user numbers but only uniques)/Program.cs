using System;
using System.Collections.Generic;

string answer = "okkk";
int collect = 0;
int count = 0;
int counter = 0;
List<int> ints = new List<int>();
List<int> intss = new List<int>();

while (true)
{
    Console.WriteLine("Enter any amount of numbers and type Quit to quit");

    answer = Console.ReadLine();
    if (answer == "Quit" || answer == "" || answer == "quit" )
    {
        break;
    }


    collect = Convert.ToInt32(answer);

    ints.Add(collect);
    //  Console.WriteLine(collect);
    


}

var noDupes = ints.Distinct().ToList();

//for(var i =0; i < ints.Count; i++)
//{
//    for(var z = 0; z < ints.Count; z++)
//    {
//        if (intss.Contains(ints[i])) { continue; }
       
//    }
//}


string result = string.Join(", ", ints.ToArray());
Console.WriteLine(result);


string results = string.Join(", ", noDupes.ToArray());
Console.WriteLine(results);