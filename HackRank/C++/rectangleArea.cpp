#include <iostream>

using namespace std;
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle{
    private:
    
    public:
    int h;
    int w;
    Rectangle(){
        this->h=0;
        this->w=0;
    }
    void display(){
        cout << w << " " << h <<endl;
    }
    
};

class RectangleArea: public Rectangle{
    public: 
    void read_input(){
        cin >> w >> h;
    }
    void display(){
        cout << w *h << endl;
    }
};


int main()
{
    /*
     * Declare a RectangleArea object
     */
    RectangleArea r_area;
    
    /*
     * Read the width and height
     */
    r_area.read_input();
    
    /*
     * Print the width and height
     */
    r_area.Rectangle::display();
    
    /*
     * Print the area
     */
    r_area.display();
    
    return 0;
}