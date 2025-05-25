step 1: object identification
opject name:
propertie of opject
    1) states: fixed values with opject
    2)behavior : what object fuctioning

step 2:
converstion real world object into computer world object
we should use class as te, plate to convert object
rules to convert
1) object name convert into class name
2) all states convert into variables
3) all bejavior convert to fucntion or methods

step 3:
instantion step 
creating ont to many copy of the class rules by using class name below follow the syntax
ref_var = classname()

example
object identification
object name:Car
staate: wheel number, window, driver, sets, color, etc...
behavior: open the door, close the door, is call moving, is it not moving, hand braking, engin start, engin stop, etc...

```python
class Car:
    driver=1;
    wheels=4;
    color="black";
    name="BMW";
    def startcar(self):
        print("car started...")
    def stopcar(self):
        print("car stopped...")
    def handbrake(self):
        print("hand brack relised...")

nova = Car();
print("Car Details:- ");
print(nova.driver);
print(nova.wheels);
print(nova.color);
print(nova.name);
nova.startcar();
nova.handbrake();
nova.stopcar();
```

question 2:
Identifi any 10 opjects with there properties, and convert it into repactive code.

```python
# 1
class Tree:
    hight = 200;
    root_len = 400;
# 2
class Os:
    kernal = "linux";
    shell = "zhs";
# 3
class Tv:
    dim = (55, 70);
    name = "Sony";
# 4
class Human:
    name = "yuvraj";
    addras = "Benglaru";
# 5
class Animal:
    num_Lag = 4;
    _type = "loin";

# 6
class University:
    loc = "Bengaluru";
    name = "Reva";
# 7
class Plante:
    position = 3;
    name = "earth";

# 8
class Company:
    name = "AV locals";
    num_emp = 50000;

# 9
class Shoes:
    size = 9;
    brand_name = "Adidas";

# 10
class Cave:
    depth = 500;
    local_habitats = ["bats", "insets", "canapids"];

```

question 2: 
> write a syntax for class.
> write a syntax for instanstation.
> write a program the given number is armstrong or not.
> write a program to print jagged array.

Answer 1:- 
```python
class <class_name>:
    <states>
    # ex:- name="nico"
    def __init__(self):
        # <constructer>.

    def <behavior_name>(<arguments>):
        # <normal behavior>
        return <if_something>;

    def <class_method_name>(self, <arguments>):
        # <class_method>
        return <if_something>;

    def __del__(self):
        # <destructor>
```

Answer 2:- 
```python
x = <class_name>(<counstructer-arguments-if-any>);

```

Answer 3:- 
```cpp
# include <iostream>

int main(){
    int value = 0, count = 0, temp, g = 0;
    std::cout << "Enter a number:- ";
    std::cin >> value;
    temp = value;
    while (temp > 0) {
        g = (temp % 10);
        count += (g * g * g);
        temp /= 10;
    }
    if(count == value){
        std::cout << "The number " << value << " is a Armstornge number.\n";
    }
    else{
        std::cout << "The number " << value << " is not a Armstornge number.\n";
    }

    return 0;
}
```

Answer 4:- 

```cpp
# include <iostream>

int main(){
    int size = 3;
    int* jagged_array[size];
    jagged_array[0] = new int[size] {0,1,2};
    jagged_array[1] = new int[size] {3,4,5};
    jagged_array[2] = new int[size] {6,7,8};
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++){
            std::cout << "[ " << i << " , " << j << " ] = " << jagged_array[i][j] << "\n";
        }
    }
    return 0;
}
```

Is_a, Has_a

Is a relationship, which works when the super class is of a same type, which work by strange classes.

question:
> write a code of differenciating between Is_a and Has_a relationship in the cpp.

Polimorfisiom:- 

polly :- many;
morfisiom :- behavior;

single entity behavior like different forms;

types of Polimorfisiom:
1. compile time Polimorfisiom (static binding) (early binding);
> method overloding:- having a same fucntion with different parameter is know as method overloding;
> ex:- 
```java
    class Flipkart{
        void payment(int phonepe){
            System.out.println("payment done by phonepe."):
        }
        void payment(string gpay){
            System.out.println("payment done by Gpay."):
        }
        void payment(float amazon){
            System.out.println("payment done by Amazon."):
        }
    }

    public class Mcareva{
        public static void main(String[] args){
            System.out.println("hey dear students");
            Flipkart f = new Flipkart();
        }
    }
```

2. run time Polimorfisiom (dynamic binding) (late binding);
> 

Encapsulation:- 
It allows to do modification for privit attributs or private function using getter and setter. ;

Abstraction:- 
it is used to hide the implementation part ahe hide the complex functilaty and only show the relevent part for the user. and for the security part too.;

[0,1,0,1,0,0,1];

[1,1,1,0,0,0,0];

Exception Handling:- 
Exception is a undefined setuation by the programming language or the compiler.
 or 
Exception is a run time handle but the exception 

stl:-







| keywords   |    desc |
|----------|---------|
| try |  where code that might through exception. |
| throw | raise or through an exception. |
| catch | this block is run and it will catch the error and the message from the throw.  |
| const char* <fucntion-name>() | This fucntion returns pointer to constant character string |
| const char* what() | this method name came from exception.(in the exception class) |
| noexcept | Garanty that, this method will not through an exception it self. |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |
| . | . |


question (x) :- 


stl:- 
| container | algorithums | itrator | Fucntion objects |
|--|---|---|---|
| vactor:- it is dynamic array, it can grow in | | | |
| size and decrease in size while time, it is part of vactor stl. |  |  |  |
| built-in function |  | | |
| . | | | |
| . | | | |
| . | | | |
| . | | | |
| . | | | |
| . | | | |
| . | | | |
| . | | | |


| built-in function |  |
|--- |---  |
| v.empty() | True if vector is empty. |
| v.clear() | clears the vector storage. |
| v.front() | return the first element. |
| v.back() | returns the last element. |
| v.begin() | itrator to the first element. |
| v.end() | itrator to the last element. |


write a program to find the squire root of a number using binary search ?

write using 2 number u can't using arthmetic operator.
