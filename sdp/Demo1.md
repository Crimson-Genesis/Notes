# Recursion:
    1. A function which calls it self.
    2. The output of that fuction will be infinite loop only.

Program (1):-
```java
class Demo1{
    void m1(){
        System.out.println("m1 function is called.");
        m2();
    }
    void m2(){
        System.out.println("m2 function is called.");

    }
}

public class Demo{
    public static void main(String[] args) {
        Demo1 d = new Demo1();
        d.m1();
    }
}
```
Output:- 
```java
❯ javac Demo.java
❯ java Demo
m1 function is called.
m2 function is called.
```
Program (2):-
```java
class Demo2{
    void m1(int n){
        if (n < 5){
            System.out.print(n);
            m1(n + 1);
        }
        System.out.print(n);
    }
}
```
Output:-
```java
❯ javac Demo.java
❯ java Demo
01234543210
```

Program (3):-
```java
class Demo3{
    int n = 0;
    void m1(int n1, int n2){
        System.out.println(n2);
        this.n += 1;
        if (n >= 10){
            return;
        }
        else{
            m1(n2, n1 + n2);
        }
    }
}
```
Output:-
```java
❯ javac Demo.java
❯ java Demo
1
1
2
3
5
8
13
21
34
55
```

# Data Structure:
Program (4):- 
```java
class Demo4{
    void m1(String c){
        int a = 10, b = 20;
        System.out.println("Before Swap a:-"+a+" b:-"+b);
        if (c == "temp"){
            int temp = a;
            a = b;
            b = temp;

        }else if (c == "+-"){
            a = a + b;
            b = a - b;
            b = a - b;
        }else if (c == "x||"){
            a = a ^ b;
            b = a ^ b;
            a = a ^ b;
        }else if (c == "*/"){
            a = a * b;
            b = a / b;
            a = a / b;
        }
        System.out.println("After  Swap a:-"+a+" b:-"+b);
    }
}
```
Output:-
```java
❯ javac Demo.java
❯ java Demo
Before Swap a:-10 b:-20
After  Swap a:-20 b:-10
Before Swap a:-10 b:-20
After  Swap a:-30 b:-20
Before Swap a:-10 b:-20
After  Swap a:-20 b:-10
Before Swap a:-10 b:-20
After  Swap a:-20 b:-10
```

Program (5):-
```java
class Demo5 {
    void m1() {
        int a[] = { 10, 9,8,7,6,5,4,3,2,1,0 };
        System.out.println("Before Sorting...");
        for (int i : a) {
            System.out.print(i + " ");
        }
        int check;
        for (int i = 1; i < a.length; i++) {
            check = 1;
            for (int j = 1; j < a.length; j++) {
                for (int x : a) {
                    System.out.print(x + " ");
                }
                System.out.println();
                if (a[j - 1] > a[j]) {
                    a[j - 1] = a[j - 1] ^ a[j];
                    a[j] = a[j - 1] ^ a[j];
                    a[j - 1] = a[j - 1] ^ a[j];
                }
                else{
                    check++;
                }
            }
            if (check == a.length){
                break;
            }
        }
    }
}
```
Output:-
```java
// Too Fucking long...
```

Program (6):-
```java
class Demo6 {
    Scanner sc = new Scanner(System.in);
    int counter = 1;
    void Login(){
        while(true){
            System.out.println("Enter your name:- ");
            String name = sc.next();
            System.out.println("Enter Password :- ");
            String pass = sc.next();
            if ("nigga@6969".equals(name) && "6969".equals(pass)){
                System.out.println("Login Success...");
                break;
            }else{
                System.out.println("Login Failed");
                System.out.println("Attempt Failed " + counter);
                counter++;
                if(counter > 3){
                    System.err.println("Your accoutn suspended due to multiple attempt....");
                    System.exit(-1);
                }
            }
        }
    }
}
```
Output:-
```java
// Some TCS shit.
```

Program (7):-
```java
    int a[] = {1,2,9,8,7,6,5,4,3,2,4,56,4,3,23,4,54,33,3,4,3,3,4,333,3,3,3,4,-1,45,6,6,7,7,7,6,6};
    void search(){
        System.out.println("Enter a number to find:- ");
        int num = sc.nextInt();
        int index = 1;
        for (int i : a) {
            if(num == i){
                System.out.println("Found the value at "+index);
                break;
            }
            index++;
        }
    }
```
Output:-
```java
❯ javac Demo.java
❯ java Demo
Found the value at 1
```

Program (8):-
```java

```
Output:-
```java

```

# Complexity:
    The amount of Time and space required to finish that algorithem.
## Types of Complexity:
    Time:- The amount of time required to finish that algorithem.
        Notations:
            Best case:- 
            Average case:-
            Worst case:- 

    Sapce:- The amount of space required to finish that algorithem.
        Notations:
            Instration space:- Number of Line.
            Data space:- Number of Variable.
            File space:- Number of Files.


