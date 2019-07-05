#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector <float> p (5, 0.2);  //p = [0.2, 0.2, 0.2, 0.2, 0.2]
string world[5] = {"green", "red", "red", "green", "green"};   //world = ['green', 'red', 'red', 'green', 'green']
string measurements[2] = {"red", "green"};  //measurements = ['red', 'green']

vector <int> motions (2, 1);  // motions = [1,1]

float pHit = 0.6;
float pMiss = 0.2;
float pExact = 0.8;
float pOvershoot = 0.1;
float pUndershoot = 0.1;

vector <float> sense(vector <float> p, string Z);
vector <float> move01(vector <float> p, int U);
void print_matrix(vector <float> p);

int main(){


    //for k in range(len(measurements)):
    //    p = sense(p, measurements[k])
    //    p = move(p, motions[k])
    for (int i=0; i<2; i++){   // measurements.size()
        p = sense(p, measurements[i]);
        print_matrix(p);
        p = move01(p, motions[i]);
        print_matrix(p);
    }
    cout << endl;
    return 0;
}

//def sense(p, Z):
vector <float> sense(vector <float> p, string Z){
    //q=[]
    vector <float> q;

    //for i in range(len(p)):
    //    hit = (Z == world[i])
    //    q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    for (int i=0;i<p.size();i++){
        bool hit = (Z == world[i]);
        q.push_back(p[i] * (hit * pHit + (1-hit) * pMiss));
    }

    //s = sum(q)
    float s = 0;
    for (int i=0;i<q.size();i++){
        s = s + q[i];
    }

    //for i in range(len(q)):
    //    q[i] = q[i] / s
    for (int i=0;i<q.size();i++){
        q[i] = q[i]/s;
    }

    //return q
    return q;
}

//def move(p, U):
vector <float> move01(vector <float> p, int U){
    //q = []
    vector <float> q;

    //for i in range(len(p)):
    //    s = pExact * p[(i-U) % len(p)]
    //    s = s + pOvershoot * p[(i-U-1) % len(p)]
    //    s = s + pUndershoot * p[(i-U+1) % len(p)]
    //    q.append(s)
    float s;
    for (int i=0;i<p.size();i++){
        s = pExact * p[(i-U) % p.size()];
        s = s + pOvershoot * p[(i-U-1) % p.size()];
        s = s + pUndershoot * p[(i-U+1) % p.size()];
        q.push_back(s);
    }

    //return q
    return q;
}

void print_matrix(vector <float> p){
    for (int i=0; i<p.size(); i++){   // measurements.size()
        cout << p[i] << " ";
    }
    cout << endl;
}
