
List<int> ints = new List<int>();

    for(var i=0; i<=100; i++)
{
    if(i % 3 == 0)
    {
        ints.Add(i);
    }
   // ints.Add(i);
}
int count = ints.Count();
string result = string.Join(", ", ints.ToArray());
Console.WriteLine(result);
Console.WriteLine(count);

