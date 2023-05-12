
string answer = "okkk";
string collect = " ";
List<string> ints = new List<string>();
while (true)
{
    Console.WriteLine("Type names and hit enter without typing name to continue");

    answer = Console.ReadLine();
    if (answer == "Ok" || answer == "" || answer == "ok")
    {
        break;
    }


    collect = answer;
    //  Console.WriteLine(collect);
    ints.Add(collect);





}

Console.WriteLine("Total count of names");

int result = ints.Count();
Console.WriteLine(result);



string results = string.Join(", ", ints.ToArray());

//Console.WriteLine(results);

if(result == 0)
{

}else if(result == 1)
    {
    Console.WriteLine("{0} likes your post.", results );
} else if(result == 2)
{
    Console.WriteLine("{0} and {1} like your post.", ints[0], ints[1]);
}
else
{
    result -= 2;
    Console.WriteLine("{0}, {1} and {2} others like your post.", ints[0], ints[1], result );
}