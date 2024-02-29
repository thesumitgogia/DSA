#include <iostream>
#include "dummyArray1000.c++"
using namespace std;
// Function to swap elements
void swap(int *arr, int a, int b)
{

    // Temporarily store arr[a]
    int temp = arr[a]; // save a

    // Assign arr[b] to arr[a]
    arr[a] = arr[b]; // swap a and b

    // Assign temp to arr[b]
    arr[b] = temp; // restore temp
}
// Function to swap elements
int partition(int *arr, int l, int r) // partition function
{
    int pivot = arr[r], i = l - 1; // set pivot and i
    for (int j = l; j < r; j++)    // loop from l to r-1
        if (arr[j] < pivot)        // if current element less than pivot
            swap(arr, ++i, j);     // increment i and swap
    swap(arr, ++i, r);             // swap pivot and arr[i]
    return i;                      // return the pivot index
}
// Function to implement QuickSort
void quicksort(int *arr, int l, int r)
{
    // If left index is less than right index
    if (l < r)
    {
        // Partition the array and get the pivot position
        int pi = partition(arr, l, r);
        // Recursive call on the left side of the pivot
        quicksort(arr, l, pi - 1);
        // Recursive call on the right side of the pivot
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