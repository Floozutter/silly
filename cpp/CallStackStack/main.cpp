/**
 * A demonstration of using the call stack as an algorithmic stack.
 *
 * Translated from callstackstack.py.
 * Inspired by Justin Jaffray's blog post:
 * http://justinjaffray.com/reflections-on-stacking-stacks/
 */

#include <assert.h>


template <char> struct CloserOf {
	static constexpr char value = '\0';
};
template <char> struct OpenerOf {
	static constexpr char value = '\0';
};
#define ADD_BRACKET_PAIR(opener, closer) \
	template <> struct CloserOf<opener> { \
		static constexpr char value = closer; \
	}; \
	template <> struct OpenerOf<closer> { \
		static constexpr char value = opener; \
	};
ADD_BRACKET_PAIR('<', '>')
ADD_BRACKET_PAIR('{', '}')
ADD_BRACKET_PAIR('(', ')')
ADD_BRACKET_PAIR('[', ']')
#undef ADD_BRACKET_PAIR


bool is_opener(char c) {
	return CloserOf<c>::value != '\0';
}


int main() {
	assert(CloserOf<'<'>::value == '>');
	assert(CloserOf<'>'>::value == '\0');
	assert(CloserOf<'e'>::value == '\0');
	assert(OpenerOf<'}'>::value == '{');
	assert(OpenerOf<'{'>::value == '\0');
	assert(OpenerOf<'e'>::value == '\0');
	
	return 0;
}
