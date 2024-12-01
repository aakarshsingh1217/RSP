// classes are like a cookie cutter, it's something you use to make cookies with/whatever
// object you're creating.

#include <iostream>

class Cookie {
    private:
        std::string color;

    public:
        Cookie (std::string color) {
            // this color = color, changing the private variable color
            // this refers to a specific instance of whatever you're creating.
            this->color = color;
        }

    // we can create other member functions in the cookie class.

    std::string getColor() {
        return color;
    }

    void setColor (std::string color) {
        this->color = color;
    }
};

int main() {
    // we can now create a new instance of a class like this. varName is cookieOne which is
    // a pointer to a cookie and that's how it will work whenever you create an object with
    // a class, whatever var that you set equal to that object you've created will be a
    // pointer to that object. and in this case, that object is a cookie. new keyword will
    // make it where we run the constructor and we pass the constructor the color green,
    // when we do all of this it will create a green cookie, this cookie has the color
    // green, that keyword this is referring to the specific instance of cookie.
    Cookie* cookieOne = new Cookie("green");

    // diff var name, this cookie is blue, this particular instance of cookie called
    // cookieTwo is blue.
    Cookie* cookieTwo = new Cookie("blue");

    cookieOne->setColor("yellow");

    std::cout << "C1: " << cookieOne->getColor() << std::endl;
    std::cout << "C2: " << cookieTwo->getColor() << std::endl;

    return 0;
}

// use classes for linked lists for example, you'd create a constructor for a LL
// , a member func append a node of a partic val, remove last item a list, prepend
// , insert, remove etc.