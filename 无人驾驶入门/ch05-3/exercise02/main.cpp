// 请编写一个含有两个矩阵的 C++ 函数，并输出它们的乘积。你需要保证在这个函数中，两个矩阵可以相乘。如果矩阵一是 m 行 n 列，矩阵二是 w 行 z 列，那么 n 必须等于 w， 而最终得到的矩阵是 m 行 z 列

#include <iostream>
#include <vector>

using namespace std;

vector < vector <float> > multi_matrix(vector < vector <float> > matrix01, vector < vector <float> > matrix02);
void print_matrix(vector < vector <float> > matrix);

int main(){

    vector < vector <float> > matrix01;  //3*2
    vector < vector <float> > matrix02;  //2*4
    vector <float> row1 (2,1);
    vector <float> row2 (4,2);
    for (int i=0;i<3;i++){
        matrix01.push_back(row1);
    }
    for (int i=0;i<2;i++){
        matrix02.push_back(row2);
    }

    vector < vector <float> > rst = multi_matrix(matrix01, matrix02);  //3*4
    print_matrix(matrix01);
    print_matrix(matrix02);
    print_matrix(rst);
    return 0;
}

vector < vector <float> > multi_matrix(vector < vector <float> > matrix01, vector < vector <float> > matrix02){

    vector < vector <float> > multi_rst;  // multi_rst => m01_r * m02_c

    if (matrix01[0].size() == matrix02.size()){
        int r01 = matrix01.size();
        int n12 = matrix01[0].size();
        int c02 = matrix02[0].size();

        for (int r=0;r<r01;r++){
            vector <float> row;
            for (int c=0;c<c02;c++){
                float element=0;
                for (int n=0;n<n12;n++){
                    element = element + matrix01[r][n]*matrix02[n][c];
                }
                row.push_back(element);
            }
            multi_rst.push_back(row);
        }
    }
    return multi_rst;
}

void print_matrix(vector < vector <float> > matrix){
    for (int r=0;r<matrix.size();r++){
        for (int c=0;c<matrix[0].size();c++){
            cout << matrix[r][c] << " ";
        }
        cout << endl;
    }
    return;
}
