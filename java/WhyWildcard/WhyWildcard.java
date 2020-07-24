import java.util.List;
import java.util.Arrays;

public class WhyWildcard {
	public static void main(String[] args) {
		final List<Adventurer> partyA = Arrays.asList(
			new Adventurer("Poppy"),
			new Mage("Lulu")
		);
		introduce(partyA, "Top Laners");
		
		final List<Mage> partyB = Arrays.asList(
			new Mage("Anivia"),
			new Mage("Twisted Fate")
		);
		introduce(partyB, "Mid Laners");
	}
	
	private static void introduce(
		List<? extends Adventurer> party,  // Try javac with List<Adventurer>!
		String partyName
	) {
		System.out.printf("%s:%n", partyName);
		party.forEach(Adventurer::introduce);
	}
	
	private static class Adventurer {
		protected String name;
		public Adventurer(String name) {
			this.name = name;
		}
		
		public void introduce() {
			System.out.printf("Hi I'm %s. I'm an Adventurer!%n", this.name);
		}
	}
	
	private static class Mage extends Adventurer {
		public Mage(String name) {
			super(name);
		}
		
		@Override
		public void introduce() {
			System.out.printf("My name is %s. I'm a Mage.%n", this.name);
		}
	}
}
