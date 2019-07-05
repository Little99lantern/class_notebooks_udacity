/*
vector基础
未完成
*/

#include <iostream>
#include <vector>
using namespace std;

void print_matrix(vector <float> p){
    for (int i=0; i<p.size(); i++){   // measurements.size()
        cout << p[i] << " ";
    }
    cout << endl;
}

void print_matrix2(vector <vector <float> >p){
    for (int i=0; i<p.size(); i++){   // measurements.size()
        for (int j=0; i<p[0].size(); i++){
            cout << p[i][j] << " ";
        }
    }
    cout << endl;
}

int main(){

    vector <float> p (5, 0.2); 
    print_matrix(p);

    vector < vector < float > > p2 = {
        p,
        p,
    };
    print_matrix2(p2);

    // vector < vector < float > > p3 (p2);
}