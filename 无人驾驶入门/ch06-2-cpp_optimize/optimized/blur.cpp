#include "headers/blur.h"
#include "headers/zeros.h"

using namespace std;

vector < vector <float> > blur(vector < vector < float> > &grid, float blurring) {

	// initialize variables
	static int height = grid.size();
	static int width = grid[0].size();

	// calculate blur factors
	static float center = 1.0 - blurring;
	static float corner = blurring / 12.0;
	static float adjacent = blurring / 6.0;


	// 2D vector reprenting the blur filter
	static vector < vector <float> > window = {
		{corner, adjacent, corner},
		{adjacent, center, adjacent},
		{corner, adjacent, corner}
	};
	

	// variables for blur calculations
	static vector <int> DX = {-1,0,1};
	static vector <int> DY = {-1,0,1};
	
	int i, j;
	int ii;
	int jj;
	int new_i;
	int new_j;

	// initialize new grid to zeros
	vector < vector <float> > newGrid = zeros(height,width);

	// blur the grid and store in a new 2D vector
	for (i=0; i< height; i++ ) {
		for (j=0; j<width; j++ ) {
			for (ii=0; ii<3; ii++) {
				for (jj=0; jj<3; jj++) {
					new_i = (i + DY[ii] + height) % height;
					new_j = (j + DX[jj] + width) % width;
					newGrid[new_i][new_j] += grid[i][j] * window[ii][jj];
				}
			}
		}
	}

	return newGrid;
}
