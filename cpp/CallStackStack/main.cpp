/**
 * A demonstration of using the call stack as an algorithmic stack.
 *
 * Translated from callstackstack.py.
 * Inspired by Justin Jaffray's blog post:
 * http://justinjaffray.com/reflections-on-stacking-stacks/
 */

#include <assert.h>


template <char l, char r>
struct BracketPair {
	static constexpr char opener = l;
	static constexpr char closer = r;
};

template<typename... Args>
class Brackets {
	public:
		static constexpr char closer_of(char c) {
			return '\0';
		}
		static constexpr char opener_of(char c) {
			return '\0';
		}
};
template<typename T, typename... Args>
class Brackets<T, Args...> {
	using super = Brackets<Args...>;
	public:
		static constexpr char closer_of(char c) {
			return c == T::opener ? T::closer : super::closer_of(c);
		}
		static constexpr char opener_of(char c) {
			return c == T::closer ? T::opener : super::opener_of(c);
		}
};

using CommonBrackets = Brackets<
	BracketPair<'<', '>'>,
	BracketPair<'{', '}'>,
	BracketPair<'(', ')'>,
	BracketPair<'[', ']'>
>;


int main() {
	assert(CommonBrackets::closer_of('<') == '>');
	assert(CommonBrackets::closer_of('>') == '\0');
	assert(CommonBrackets::closer_of('e') == '\0');
	assert(CommonBrackets::opener_of('}') == '{');
	assert(CommonBrackets::opener_of('{') == '\0');
	assert(CommonBrackets::opener_of('e') == '\0');
	
	return 0;
}
