#include <iostream>
using namespace std;

// Here we insert declarations  of the classes we want to make use of and global constants:
class stack;
class graph_node;
class graph;
const int MAX_SIZE = 200000;
// ---------------------------------------------------------------------

/* STACK
*  This is an adhoc implementation of the stack. It allocates an array of size 'MAX_SIZE', as is defined above. This array is an auxilary array
*  in which data is stored. However, any data above the current size is considered 'trash data' and will be written over if insertion() is called.
*  For example, if we have aux = [1,2...], size = 2. Now we call pop() -> aux = [1,2..], but size = 1, meaning that the 2 on index 1 is 'trashdata'.
*  If we now call insertion(3), we get aux = [1,3...], and pop() --> returns 3, and in aux [1,3..], the 3 is now considered to be 'trash data'.
*/

class stack{
    int max_size;
    int size = 0;
    int aux_array[MAX_SIZE];

public:
    void insertion(int n) {
        aux_array[size] = n;
        size += 1;
    }

    int pop(){
        size -= 1;
        return aux_array[size];
    }
    
};

class graph_node {

};


class graph {
private:
    int max_size;
    int size = 0;
    int aux_array[];

 public: 
    void set_max_size(int n) {
        max_size = n;
        aux_array[n];
    }




};

int main()
{
    std::cout << "Hello World!\n";
    stack s;
    s.insertion(4);
    std::cout << s.pop();
    
}
