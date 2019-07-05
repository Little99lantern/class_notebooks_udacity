#include "headers/initialize_beliefs.h"

using namespace std;

vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {



	static int height = grid.size();
	static int width = grid[0].size();
	static int area = height * width;

	// calculate initial grid values
	static float prob_per_cell = 1.0 / ( (float) area) ;

	// 减少for循环
	// vector< vector <float> > newGrid;
	// vector<float> newRow;
	// int i, j;
	// for (j=0; j<width; j++) {
	// 		newRow.push_back(prob_per_cell);
	// }
	// for (i=0; i<height; i++) {
	// 	newGrid.push_back(newRow);
	// }

	// 不用for循环
	// static vector<float> newRow (width, prob_per_cell); 不用for循环
	// static vector< vector <float> > newGrid (height, newRow);
	// return newGrid;

	return vector< vector <float> > (height, vector <float> (width, prob_per_cell));
}