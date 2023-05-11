string answer = "okkk";
int collect = 0;
List<int> ints = new List<int>();
while(true)
{
    Console.WriteLine("Type Ok to add all number together");

    answer = Console.ReadLine();
    if( answer == "Ok" || answer == " " || answer == "ok")
    {
        break;
    } 


    collect=  Convert.ToInt32(answer);
  //  Console.WriteLine(collect);
    ints.Add(collect);





}
var resultsOfSum =0;
foreach(var inter in ints)
{
    resultsOfSum += inter;
}

string result = string.Join(", ", ints.ToArray());
Console.WriteLine(result);
Console.WriteLine(resultsOfSum);