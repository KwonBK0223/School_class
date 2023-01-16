#include "student.h"

using namespace std;

unique_ptr<StudentInfo> make_student(){
    unique_ptr<StudentInfo> si(new StudentInfo);
    int n = 0;
    cin >> si->name;
    for(int i =0;i<3;i++){
        cin >> si->scores[i];
        n += si->scores[i];
    }
    si->sum=n;
    si->average=(double)n/3;
    return si;

}

void print(const StudentInfo& si) {
    cout<<si.name<<" "<<si.scores[0]<<" "<<si.scores[1]<<" "<<si.scores[2]<<" "<<si.sum<<" "<<si.average<<endl;

}

void print_all(const vector<unique_ptr<StudentInfo>>& vec) {
    for (auto& i:vec)
        print(*i);
}