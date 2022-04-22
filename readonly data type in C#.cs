class abc
{
    readonly int a;
    readonly static int b;
    public abc(int a)
    {
        a=x;
        Console.WriteLine("a="+a);
    }
    public abc()
    {
        b=100
        Console.WriteLine("b="+b);
    }
}
class Test
{
    public static void Main()
    {
        abc x=new abc();
        abc y=new abc(3);
    }
}