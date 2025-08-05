internal class Program
{
    private static void Main(string[] args)
    {
        string s = "Hello, World!";
        int[] ints = new int[s.Length];
        for (int i = 0; i < ints.Length; i++)
            ints[i] = i;

        string res = "";

        foreach (int num in ints)
        {
            Console.Write(s[num].ToString());
            res += s[num];
        }

        Console.WriteLine(res);
    }
}