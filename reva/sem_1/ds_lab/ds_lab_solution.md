# Part - A
---

## **1. Insert & Delete at Desired Position in Array**
```c
#include <stdio.h>

void insert(int arr[], int *n, int pos, int val) {
    if (pos < 0 || pos > *n) return;
    for (int i = *n; i > pos; i--) arr[i] = arr[i - 1];
    arr[pos] = val, (*n)++;
}

void delete(int arr[], int *n, int pos) {
    if (pos < 0 || pos >= *n) return;
    for (int i = pos; i < *n - 1; i++) arr[i] = arr[i + 1];
    (*n)--;
}

int main() {
    int arr[100], n, ch, pos, val;
    printf("Enter array size: "), scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);

    while (1) {
        printf("\n1.Insert 2.Delete 3.Display 4.Exit: "), scanf("%d", &ch);
        if (ch == 4) break;
        if (ch == 1) scanf("%d %d", &pos, &val), insert(arr, &n, pos, val);
        else if (ch == 2) scanf("%d", &pos), delete(arr, &n, pos);
        else for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    }
}
```

---

## **2. 2D Array Manipulation & Matrix Multiplication**
```c
#include <stdio.h>

void multiply(int A[10][10], int B[10][10], int C[10][10], int r1, int c1, int c2) {
    for (int i = 0; i < r1; i++)
        for (int j = 0; j < c2; j++) {
            C[i][j] = 0;
            for (int k = 0; k < c1; k++) C[i][j] += A[i][k] * B[k][j];
        }
}

int main() {
    int A[10][10], B[10][10], C[10][10], r1, c1, r2, c2;
    printf("Enter size of Matrix A (rows cols): "), scanf("%d %d", &r1, &c1);
    printf("Enter size of Matrix B (rows cols): "), scanf("%d %d", &r2, &c2);
    if (c1 != r2) return printf("Multiplication not possible!\n"), 0;

    printf("Enter Matrix A:\n");
    for (int i = 0; i < r1; i++) for (int j = 0; j < c1; j++) scanf("%d", &A[i][j]);
    printf("Enter Matrix B:\n");
    for (int i = 0; i < r2; i++) for (int j = 0; j < c2; j++) scanf("%d", &B[i][j]);

    multiply(A, B, C, r1, c1, c2);

    printf("Result:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) printf("%d ", C[i][j]);
        printf("\n");
    }
}
```

---

## **3. String Operations: Compare, Concatenate, Length**
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[100], str2[100];
    printf("Enter string 1: "), scanf("%s", str1);
    printf("Enter string 2: "), scanf("%s", str2);

    printf("Compare: %d\n", strcmp(str1, str2));
    printf("Concatenate: %s\n", strcat(str1, str2));
    printf("Length: %d\n", strlen(str1));
}
```

---

## **4. Swap Variables (Call by Value & Reference)**
```c
#include <stdio.h>

void swap_by_value(int a, int b) { int temp = a; a = b; b = temp; }
void swap_by_reference(int *a, int *b) { int temp = *a; *a = *b; *b = temp; }

int main() {
    int x = 5, y = 10;
    swap_by_value(x, y);  // Won't swap
    printf("After call by value: %d %d\n", x, y);
    swap_by_reference(&x, &y);
    printf("After call by reference: %d %d\n", x, y);
}
```

---

## **5. Recursive Binary to Decimal Conversion**
```c
#include <stdio.h>

int binary_to_decimal(int n) {
    return (n == 0) ? 0 : (n % 10 + 2 * binary_to_decimal(n / 10));
}

int main() {
    int n;
    printf("Enter binary number: "), scanf("%d", &n);
    printf("Decimal: %d\n", binary_to_decimal(n));
}
```

---

## **6. Queue Operations (Insert, Delete, Display)**
```c
#include <stdio.h>

#define SIZE 5
int queue[SIZE], front = -1, rear = -1;

int isFull() { return (rear + 1) % SIZE == front; }
int isEmpty() { return front == -1; }

void insert(int val) {
    if (isFull()) { printf("Queue Full!\n"); return; }
    if (isEmpty()) front = rear = 0;
    else rear = (rear + 1) % SIZE;
    queue[rear] = val;
}

void delete() {
    if (isEmpty()) { printf("Queue Empty!\n"); return; }
    if (front == rear) front = rear = -1;
    else front = (front + 1) % SIZE;
}

void display() {
    if (isEmpty()) { printf("Queue Empty!\n"); return; }
    int i = front;
    while (1) {
        printf("%d ", queue[i]);
        if (i == rear) break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main() {
    int ch, val;
    while (1) {
        printf("\n1.Insert 2.Delete 3.Display 4.Exit: ");
        scanf("%d", &ch);
        if (ch == 4) break;
        if (ch == 1) { scanf("%d", &val); insert(val); }
        else if (ch == 2) delete();
        else if (ch == 3) display();
    }
}
```

---

## **7. Quick Sort**
```c
#include <stdio.h>

void quicksort(int arr[], int low, int high) {
    if (low >= high) return;
    int pivot = arr[high], i = low, j = high - 1, temp;
    while (i <= j) {
        while (i <= j && arr[i] < pivot) i++;
        while (i <= j && arr[j] > pivot) j--;
        if (i < j) temp = arr[i], arr[i] = arr[j], arr[j] = temp;
    }
    arr[high] = arr[i], arr[i] = pivot;
    quicksort(arr, low, i - 1);
    quicksort(arr, i + 1, high);
}

int main() {
    int n, arr[100];
    printf("Enter size: "), scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    quicksort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
}
```

---

## **8. Search Techniques (Linear & Binary Search)**
```c
#include <stdio.h>

int linear_search(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) if (arr[i] == key) return i;
    return -1;
}

int binary_search(int arr[], int low, int high, int key) {
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == key) return mid;
        (arr[mid] < key) ? (low = mid + 1) : (high = mid - 1);
    }
    return -1;
}

int main() {
    int n, arr[100], key;
    printf("Enter size: "), scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    printf("Enter key: "), scanf("%d", &key);
    printf("Linear Search: %d\n", linear_search(arr, n, key));
    printf("Binary Search (Sorted): %d\n", binary_search(arr, 0, n - 1, key));
}
```

---
# Part - B
---

## **9. Stack Operations (Push, Pop, Display)**
```c
#include <stdio.h>

#define SIZE 5
int stack[SIZE], top = -1;

void push(int val) { if (top < SIZE - 1) stack[++top] = val; else printf("Stack Full!\n"); }
void pop() { if (top >= 0) top--; else printf("Stack Empty!\n"); }
void display() { for (int i = 0; i <= top; i++) printf("%d ", stack[i]); printf("\n"); }

int main() {
    int ch, val;
    while (1) {
        printf("\n1.Push 2.Pop 3.Display 4.Exit: "), scanf("%d", &ch);
        if (ch == 4) break;
        if (ch == 1) scanf("%d", &val), push(val);
        else if (ch == 2) pop();
        else if (ch == 3) display();
    }
}
```

---

## **10. Infix to Postfix Conversion**
```c
#include <stdio.h>
#include <ctype.h>

#define SIZE 100
char stack[SIZE]; int top = -1;

void push(char c) { stack[++top] = c; }
char pop() { return stack[top--]; }
int precedence(char c) { return (c == '+' || c == '-') ? 1 : (c == '*' || c == '/') ? 2 : 0; }

void infix_to_postfix(char *infix, char *postfix) {
    int i = 0, j = 0;
    while (infix[i]) {
        if (isalnum(infix[i])) postfix[j++] = infix[i];
        else if (infix[i] == '(') push(infix[i]);
        else if (infix[i] == ')') while (top != -1 && stack[top] != '(') postfix[j++] = pop();
        else { while (top != -1 && precedence(stack[top]) >= precedence(infix[i])) postfix[j++] = pop(); push(infix[i]); }
        i++;
    }
    while (top != -1) postfix[j++] = pop();
    postfix[j] = '\0';
}

int main() {
    char infix[SIZE], postfix[SIZE];
    printf("Enter infix: "), scanf("%s", infix);
    infix_to_postfix(infix, postfix);
    printf("Postfix: %s\n", postfix);
}
```

---

## **11. Circular Queue (Insert, Delete, Display)**
```c
#include <stdio.h>

#define SIZE 5
int queue[SIZE], front = -1, rear = -1;

int isFull() { return (rear + 1) % SIZE == front; }
int isEmpty() { return front == -1; }

void insert(int val) {
    if (isFull()) return;
    if (isEmpty()) front = rear = 0;
    else rear = (rear + 1) % SIZE;
    queue[rear] = val;
}

void delete() {
    if (isEmpty()) return;
    if (front == rear) front = rear = -1;
    else front = (front + 1) % SIZE;
}

void display() {
    if (isEmpty()) return;
    int i = front;
    while (1) {
        printf("%d ", queue[i]);
        if (i == rear) break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main() {
    int ch, val;
    while (1) {
        printf("\n1.Insert 2.Delete 3.Display 4.Exit: "), scanf("%d", &ch);
        if (ch == 4) break;
        if (ch == 1) scanf("%d", &val), insert(val);
        else if (ch == 2) delete();
        else if (ch == 3) display();
    }
}
```

---

## **12. Linked List Operations**
```c
#include <stdio.h>
#include <stdlib.h>

struct Node { int data; struct Node *next; };
struct Node *head = NULL;

void insert_begin(int val) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = val, newNode->next = head, head = newNode;
}

void insert_end(int val) {
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node)), *temp = head;
    newNode->data = val, newNode->next = NULL;
    if (!head) head = newNode; else { while (temp->next) temp = temp->next; temp->next = newNode; }
}

void delete_begin() { if (head) { struct Node *temp = head; head = head->next; free(temp); } }
void delete_end() { if (!head) return; if (!head->next) { free(head), head = NULL; return; } struct Node *temp = head, *prev; while (temp->next) prev = temp, temp = temp->next; prev->next = NULL, free(temp); }
void display() { struct Node *temp = head; while (temp) { printf("%d ", temp->data); temp = temp->next; } printf("\n"); }

int main() {
    int ch, val;
    while (1) {
        printf("\n1.Insert Begin 2.Insert End 3.Delete Begin 4.Delete End 5.Display 6.Exit: "), scanf("%d", &ch);
        if (ch == 6) break;
        if (ch == 1 || ch == 2) scanf("%d", &val);
        if (ch == 1) insert_begin(val);
        else if (ch == 2) insert_end(val);
        else if (ch == 3) delete_begin();
        else if (ch == 4) delete_end();
        else if (ch == 5) display();
    }
}
```

---

## **13. Insertion Sort in C (Turbo C++ & GCC Compatible)**

```c
#include <stdio.h>

void insertion_sort(int arr[], int n) {
    for (int i = 1, j, key; i < n; i++) {
        key = arr[i], j = i - 1;
        while (j >= 0 && arr[j] > key) arr[j + 1] = arr[j], j--;
        arr[j + 1] = key;
    }
}

int main() {
    int n, arr[100];
    printf("Enter size: "), scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    insertion_sort(arr, n);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
}
```

---

## **14. Binary Search Tree with Inorder, Preorder & Postorder Traversal**
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *left, *right;
};

// Create a new node
struct Node* newNode(int val) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = val, temp->left = temp->right = NULL;
    return temp;
}

// Insert a node into BST
struct Node* insert(struct Node* root, int val) {
    if (!root) return newNode(val);
    if (val < root->data) root->left = insert(root->left, val);
    else root->right = insert(root->right, val);
    return root;
}

// Inorder Traversal (LNR)
void inorder(struct Node* root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Preorder Traversal (NLR)
void preorder(struct Node* root) {
    if (!root) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Postorder Traversal (LRN)
void postorder(struct Node* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

int main() {
    struct Node* root = NULL;
    int ch, val;

    while (1) {
        printf("\n1.Insert 2.Inorder 3.Preorder 4.Postorder 5.Exit: ");
        scanf("%d", &ch);
        if (ch == 5) break;
        if (ch == 1) scanf("%d", &val), root = insert(root, val);
        else if (ch == 2) inorder(root), printf("\n");
        else if (ch == 3) preorder(root), printf("\n");
        else if (ch == 4) postorder(root), printf("\n");
    }
}
```
---
