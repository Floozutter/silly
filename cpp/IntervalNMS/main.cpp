/**
 * An example of non-maximum suppression (using intervals instead of boxes).
 * For Dad.
 */

#include <vector>
#include <forward_list>
#include <numeric>
#include <algorithm>
#include <iostream>


struct Interval {
	int start, end;
	double confidence;
};


double intersection_over_union(Interval a, Interval b) {
	int inter = (
		std::max(0, std::min(a.end, b.end))
		- std::max(a.start, b.start)
	);
	int onion = (a.end - a.start) + (b.end - b.start) - inter;
	return static_cast<double>(inter) / static_cast<double>(onion);
}

std::vector<Interval> suppress_nonmax(
	const std::vector<Interval>& input,
	double iou_threshold
) {
	std::vector<Interval> output;
	std::forward_list<std::vector<Interval>::size_type> indices(input.size());
	
	// Populate indices with the indices of the input vector.
	std::iota(indices.begin(), indices.end(), 0);
	// Sort indices by descending confidence.
	indices.sort([&input](auto a, auto b) -> bool {
		return input[a].confidence > input[b].confidence;
	});
	
	while (!indices.empty()) {
		// Take the index corresponding to the Interval with the highest
		// confidence, and copy that Interval to the output vector.
		auto front_index = indices.front();
		indices.pop_front();
		output.push_back(input[front_index]);
		
		// Remove remaining indices that have an IOU with the front index
		// higher than the given threshold.
		indices.remove_if(
			[front_index, iou_threshold, &input](auto other_index) -> bool {
				return intersection_over_union(
					input[front_index],
					input[other_index]
				) > iou_threshold;
			}
		);
	}
	
	return output;
}

std::ostream& operator<<(
	std::ostream& out,
	const std::vector<Interval>& intervals
) {
	for (Interval i : intervals) {
		out << "\t[" << i.start << ", " << i.end << "], ";
		out << "c = " << i.confidence << ";" << std::endl;
	}
	return out;
}


int main() {
	const double threshold = 0.5;
	const std::vector<Interval> input{
		{3, 6, 0.8},
		{7, 9, 0.5},
		{4, 6, 0.9},
		{1, 3, 0.4},
		{8, 10, 0.6}
	};
	const std::vector<Interval> output = suppress_nonmax(input, threshold);
	
	std::cout << "IOU Threshold: " << threshold << std::endl << std::endl;
	std::cout << "Input Intervals:" << std::endl << input << std::endl;
	std::cout << "Output Intervals:" << std::endl << output << std::endl;
	
	return 0;
}
