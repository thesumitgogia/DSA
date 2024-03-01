#include <iostream>
#include "dummyArray1000.c++"
using namespace std;
void swap(int *arr, int a, int b)
{
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}
int partition(int *arr, int l, int r)
{
    int pivot = arr[r], i = l - 1;
    for (int j = l; j < r; j++)
        if (arr[j] < pivot)
            swap(arr, ++i, j);
    swap(arr, ++i, r);
    return i;
}
void quicksort(int *arr, int l, int r)
{
    if (l < r)
    {
        int pi = partition(arr, l, r);
        quicksort(arr, l, pi - 1);
        quicksort(arr, pi + 1, r);
    }
}
int main()
{
    for (int i = 0; i < n; i++)
        cout << A[i] << " ";
    quicksort(A, 0, n);
    cout << endl;
    for (int i = 0; i < n; i++)
        cout << A[i] << " ";
    return 0;
}