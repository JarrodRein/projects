#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box{
    int temp;
    int l; 
    int b; 
    int h;
    
    public:
    Box(){
        this->l =0;
        this->b =0;
        this->h =0;

    }
    
    Box(int x, int y, int z){
        this->l = x;
        this->b = y;
        this->h = z;
    }
    
    Box(Box &box){
        this->l = box.l;
        this->b = box.b;
        this->h = box.h;
    }
    
    // int getLength(); // Return box's length
    int getLength(){
     return this->l;   
    }
// int getBreadth (); // Return box's breadth
    int getBreadth(){
        return this->b;
    }
// int getHeight ();  //Return box's height
    int getHeight(){
        return this->h;
    }
// long long CalculateVolume(); // Return the volume of the box

long long CalculateVolume(){
    long long res;
    res = (long long) this->l * (long long) this->b * (long long) this->l;
    return res;
}
};



void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}