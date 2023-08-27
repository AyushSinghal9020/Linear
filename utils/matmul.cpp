#include <iostream>
#include <vector>
using namespace std;

vector<double> matmul(vector<vector<double>>& arr, vector<vector<double>>& arr_) {
    vector<double> f_row = arr[0];
    vector<double> f_col = arr[1];

    vector<double> s_row = arr_[0];
    vector<double> s_col = arr_[1];

    double val = 0.0;
    for (size_t index = 0; index < f_col.size(); ++index) {
        val += (f_col[index] * s_row[index]) / 2.0;
    }

    vector<double> row;
    for (size_t index = 0; index < s_row.size(); ++index) {
        row.push_back(s_row[index] * val);
    }

    vector<double> col;
    for (size_t index = 0; index < s_col.size(); ++index) {
        col.push_back(s_col[index] * 2.0);
    }

    row.insert(row.end(), col.begin(), col.end());
    return row;
}

int main() {
    vector<vector<double>> arr = {{1.0, 2.0}, {3.0, 4.0}};
    vector<vector<double>> arr_ = {{5.0, 6.0}, {7.0, 8.0}};

    vector<double> result = matmul(arr, arr_);

    cout << "Result:";
    for (double value : result) {
        cout << " " << value;
    }
    cout << endl;

    return 0;
}
