#include <vector>
#include <string>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include "aoc_utils.h"
#include <algorithm>
#include<stack>

namespace Day9 {
	void Solve() {
		std::vector<std::vector<int>> grid;
		std::map<int, int> cellvalues;
		aoc::LoadGridInput("input_day9.txt", grid, cellvalues, true);
		size_t width = grid[0].size();
		size_t height = grid.size();
		std::map<int, std::vector<int>> neighbors;
		int total_risk = 0;
		std::vector<int> minlocs;
		for (size_t x = 0; x < width; ++x) {
			for (size_t y = 0; y < height; ++y) {
				bool minimum = true;
				int currentcell = aoc::coord2i({ x,y }, width, height);
				neighbors[currentcell] = {};
				if (x != 0) {
					neighbors[currentcell].push_back(aoc::coord2i({ x - 1,y }, width, height));
					if (grid[y][x - 1] <= grid[y][x]) {
						minimum = false;
					}
				}
				if (x != width - 1) {
					neighbors[currentcell].push_back(aoc::coord2i({ x + 1,y }, width, height));
					if (grid[y][x + 1] <= grid[y][x]) {
						minimum = false;
					}
				}
				if (y != 0) {
					neighbors[currentcell].push_back(aoc::coord2i({ x ,y - 1 }, width, height));
					if (grid[y - 1][x] <= grid[y][x]) {
						minimum = false;
					}
				}
				if (y != height - 1) {
					neighbors[currentcell].push_back(aoc::coord2i({ x ,y + 1 }, width, height));
					if (grid[y + 1][x] <= grid[y][x]) {
						minimum = false;
					}
				}
				if (minimum) {
					total_risk += grid[y][x] + 1;
					minlocs.push_back(aoc::coord2i({ x,y }, width, height));
				}
			}
		}
		std::cout << "Solutions day 9:\n================\n" ;
		std::cout << "Total risk: " << total_risk << "\n";

		std::vector<int> bsizes;
		std::set<int> visited;
		for (auto cellnr : minlocs) {
			int count = 1;
			std::queue<int> queue;
			queue.push(cellnr);
			visited.insert(cellnr);
			while (!queue.empty()) {
				int curr = queue.front();
				queue.pop();
				for (int n : neighbors[curr]) {
					if (visited.find(n) == visited.end() && cellvalues[n] > cellvalues[curr] && cellvalues[n] != 9) {
						count++;
						queue.push(n);
						visited.insert(n);
					}
				}
			}
			//std::cout << "Minloc: " << cellnr << ", size of basin: " << count << '\n';
			bsizes.push_back(count);
		}
		std::sort(bsizes.rbegin(), bsizes.rend());
		std::cout << "Product of 3 largest basins: " << bsizes[0] * bsizes[1] * bsizes[2]<<'\n';
	}
}

namespace Day10 {
	void Solve() {
		std::vector<std::vector<int>> grid;
		std::map<int, int> cellvalues;
		aoc::LoadGridInput("input_day10.txt", grid, cellvalues, false);
		std::set<int> openers = { 40,60,91,123 }; // (, <, [, {
		std::map<int, int> matching_openers = { {41,40},{62,60},{93,91},{125,123} };
		std::map<int, int> matching_closers = { {40,41},{60,62},{91,93},{123,125} };
		std::map<char, int> corr_rewards = { {')',3},{']',57},{'}',1197},{'>',25137}};
		std::map<char, int> compl_rewards = { {'(',1},{'[',2},{'{',3},{'<',4} };
		std::vector<long long int> compl_scores;
		int corr_score = 0;
		for (auto line : grid) {
			bool valid = true;
			std::stack<int> stack;
			for (int entry : line) {
				std::cout << char(entry);
				if (openers.find(entry) != openers.end()) { // opener
					stack.push(entry);
					continue;
				}
				else if (!stack.empty() && stack.top() == matching_openers[entry]) {
					stack.pop();
					continue;
				}
				else {
					valid = false;
					std::cout << " Expected " << char(matching_closers[stack.top()]) << " but found " << char(entry) << " instead. ";
					corr_score += corr_rewards[char(entry)];
					break;
				}
			}
			if (valid) {
				long long int compl_score = 0;
				while (!stack.empty()) {
					char curr = char(stack.top());
					stack.pop();
					compl_score = 5 * compl_score + compl_rewards[curr];
				}
				compl_scores.push_back(compl_score);
			}
			std::cout << "Valid?: "<<valid<<'\n';
		}
		std::cout << "Correction Score: " << corr_score << '\n';
		std::sort(compl_scores.begin(), compl_scores.end());
		size_t numscores = compl_scores.size();
		std::cout << "Completion Score: " << compl_scores[numscores / 2];
	}
}

int main() {
	//Day9::Solve();
	Day10::Solve();
}
