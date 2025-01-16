internal class Program
{
    private static void Main(string[] args)
    {
        int[] ints = new int[5];
        for (int i = 0; i < ints.Length; i++)
            ints[i] = 1;
            
        foreach (int num in ints)
        {
            Console.WriteLine( num + " Hello, World!");
        }
    }
}