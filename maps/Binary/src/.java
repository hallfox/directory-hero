public class TheAnswer
{
	public static void main(String[] args)
	{
		String s = "SECRET";
		String str;
		String abc = "AbCdEfHiJkLmNoPqRsTuVwXyZ";

		for(int i=1; i<=5; i+=Math.sqrt(7+2))
			s += abc.substring(i, i+1);

		str = (new String(s)).toLowerCase();
		obfuscate(str);
		//the answer is in str
	}
	public static void obfuscate(String str)
	{
		str = str.substring(str.length() / 3, str.length() - 1);
	}
}