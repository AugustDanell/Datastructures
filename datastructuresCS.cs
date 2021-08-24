using System.IO;
using System;
using System.Collections;
using System.Collections.Generic;

class stack{
    // Class members:
    List<int> internal_list = new List<int>();
    int elements = 0;
    
    public void push(int elem){
        internal_list.Add(elem);
        elements ++;
    }
    
    public int pop(){
        if(elements > 0){
            elements --;
            int elem = internal_list[elements-1];
            internal_list.RemoveAt(elements-1);
            return elem;
        }
        
        Console.WriteLine("Please don't pop an empty list!");
        return -1;
    }
}

class Program
{
    static void Main()
    {   
        
    }
}
