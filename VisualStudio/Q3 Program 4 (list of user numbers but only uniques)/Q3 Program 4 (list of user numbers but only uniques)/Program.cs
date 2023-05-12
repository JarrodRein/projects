string answer = "okkk";
int collect = 0;
int count = 0;
int counter = 0;
List<int> ints = new List<int>();
while (true)
{
    Console.WriteLine("Enter 5 unique numbers");

    answer = Console.ReadLine();
    if (answer == "Ok" || answer == "" || answer == "ok" || counter == 5)
    {
        break;
    }


    collect = Convert.ToInt32(answer);

    foreach (var num in ints)
    {
        if (num == collect)
        {
            Console.WriteLine("Enter new number");
            count++;
            continue;
        }

    }

    //  Console.WriteLine(collect);
    if (count == 0)
    {
        ints.Add(collect);
    }


    count = 0;
    counter++;

}
var resultsOfSum = 0;
foreach (var inter in ints)
{
    resultsOfSum += inter;
}

ints.Sort();
string result = string.Join(", ", ints.ToArray());
Console.WriteLine(result);
Console.WriteLine(resultsOfSum);