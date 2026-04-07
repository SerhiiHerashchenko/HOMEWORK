internal class Program
{
    private static void Main(string[] args)
    {
        uint number = 22U;

        string numberStr = number.ToString().Trim();
        int count = 0;


        for (int i = 1; i < numberStr.Length; i++)
        {
            System.Console.WriteLine(numberStr[i - 1]);
            System.Console.WriteLine(numberStr[i]);
            if (numberStr[i - 1] == numberStr[i] && numberStr[i] == '2')
                count++;
        }

        Console.WriteLine(number + " " + count);
    }
}