/**
 * CalvinPrinter goes brrr.
 */

#include <iostream>
#include <queue>

class CalvinPrinter {
	public:
		void takeRequest(std::string name, std::string str) {
			std::cout << name << " requested a print!" << std:: endl;
			q.push(str);
		}
		void batchPrint() {
			std::cout << std::endl << "DROPPING THE LOAD: " << std::endl;
			while (!q.empty()) {
				std::cout << "\t" << q.front() << std::endl;
				q.pop();
			}
			std::cout << std::endl;
		}
	private:
		std::queue<std::string> q;
};

int main() {
	CalvinPrinter calp;
	calp.takeRequest("literally me", "nice cock");
	calp.takeRequest("vic", "previous requester is short");
	calp.takeRequest("Regan", "17");
	// Oh, a convenient time for printing!
	calp.batchPrint();
	calp.takeRequest("mikle", "we’re not fucking made of sand");
	calp.takeRequest("matt", "i main every champ");
	// Another convenient time for printing!
	calp.batchPrint();
}
