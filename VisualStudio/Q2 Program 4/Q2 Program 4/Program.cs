int answer = 0;
Random rnd = new Random();
int collect = rnd.Next(1, 10);
//Console.WriteLine(collect);
//List<int> ints = new List<int>();
int count = 0;



while (true)
{
    Console.WriteLine("Type number between 1-10 to guess random number");

    answer = Convert.ToInt32(Console.ReadLine());
    if (answer == collect)
    {
        Console.WriteLine("Correct Guess!");

        break;
    }
    else if (count == 3){
        Console.WriteLine("Game over");
        break;

    }
    else
    {
        count++;
        Console.WriteLine("Guess Again");

    }


   





}
//var resultsOfSum = 0;
//foreach (var inter in ints)
//{
//    resultsOfSum += inter;
//}

//string result = string.Join(", ", ints.ToArray());
//Console.WriteLine(result);
//Console.WriteLine(resultsOfSum);