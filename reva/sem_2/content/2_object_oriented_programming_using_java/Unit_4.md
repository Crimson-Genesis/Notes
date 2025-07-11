# Unit - 4 -> Introduction to GUI and JDBC Programming
Swing Introduction, Introduction to basic Widgets in java.
Java Swing Apps, Layout Managers.
Introduction to JDBC, JDBC Drivers.
DB Connectivity Steps, Connectivity with various Databases.

## Content -> 
### **Swing Introduction (Java GUI Programming)**

---

### **1. What is Swing?**

* **Swing** is a part of **Java Foundation Classes (JFC)** used to create **Graphical User Interface (GUI)** applications in Java.
* It is a **lightweight**, **platform-independent**, and **component-based** GUI toolkit.
* It is built on top of the **Abstract Window Toolkit (AWT)** but provides **more powerful and flexible components**.

---

### **2. Key Characteristics of Swing**

| Feature                     | Description                                                             |
| --------------------------- | ----------------------------------------------------------------------- |
| **Lightweight**             | Does not depend on native OS GUI; written entirely in Java              |
| **Pluggable Look and Feel** | Allows GUI to appear like Windows, Motif, or Metal (Java look)          |
| **Rich Set of Components**  | Provides more widgets than AWT (e.g., tables, trees, sliders, tooltips) |
| **MVC Architecture**        | Uses Model-View-Controller architecture for components                  |
| **Customizable**            | Allows complete control and custom rendering of UI components           |
| **Event Driven**            | Uses event listeners to handle user actions                             |

---

### **3. Swing vs AWT**

| Aspect          | AWT                         | Swing                           |
| --------------- | --------------------------- | ------------------------------- |
| Library         | Java's original GUI toolkit | Extension of AWT (part of JFC)  |
| Components      | Heavyweight                 | Lightweight                     |
| Look and Feel   | Depends on OS               | Pluggable Look and Feel         |
| Extensibility   | Limited                     | Highly extensible               |
| Component Count | Fewer components            | Rich set of advanced components |

---

### **4. Commonly Used Swing Packages**

* `javax.swing.*` → Core Swing classes
* `java.awt.*` → Basic windowing and event classes (still used for layout and events)

---

### **5. Core Classes and Interfaces in Swing**

| Class / Interface | Description                           |
| ----------------- | ------------------------------------- |
| `JFrame`          | Top-level main window                 |
| `JPanel`          | Generic container to group components |
| `JButton`         | Push button                           |
| `JLabel`          | Display a text or image               |
| `JTextField`      | Single-line text input                |
| `JTextArea`       | Multi-line text input                 |
| `JCheckBox`       | Checkbox component                    |
| `JRadioButton`    | Radio button                          |
| `JComboBox`       | Dropdown list (combo box)             |
| `JList`           | Scrollable list                       |
| `JTable`          | Tabular data display                  |
| `JScrollPane`     | Adds scrollbars to components         |

---

### **6. Basic Swing Application Structure**

```java
import javax.swing.*;

public class MyApp {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My First Swing App"); // create frame
        JButton button = new JButton("Click Me");        // create button

        frame.add(button);               // add button to frame
        frame.setSize(300, 200);         // set frame size
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);          // display the frame
    }
}
```

---

### **7. Event Handling in Swing**

* Swing is **event-driven**: user actions generate events which are handled via **listener interfaces**.

#### Example:

```java
button.addActionListener(new ActionListener() {
    public void actionPerformed(ActionEvent e) {
        System.out.println("Button clicked");
    }
});
```

---

### **8. Swing GUI Creation Approaches**

| Approach              | Description                                  |
| --------------------- | -------------------------------------------- |
| **Manual Code-Based** | Write all layout and component code manually |
| **GUI Builder Tools** | Use tools like NetBeans GUI Builder          |

---

### **9. Threading: Swing and Event Dispatch Thread (EDT)**

* All Swing component updates should occur on the **Event Dispatch Thread (EDT)** to prevent thread-related issues.

```java
SwingUtilities.invokeLater(() -> {
    new MyApp(); // safely create GUI
});
```

---

### **10. Advantages of Swing**

* Platform-independent (Java-based)
* Flexible and extensible components
* Custom Look and Feel
* Better graphics rendering
* Works with MVC design

---

### **11. Disadvantages of Swing**

* Slightly **slower performance** than native GUI frameworks
* **Complex for beginners** compared to simple AWT
* More **manual management** required (threading, layout, etc.)

---

### **12. Conclusion**

* **Swing is the standard Java GUI toolkit** for building feature-rich, cross-platform desktop applications.
* It offers **extensive control over UI components**, behavior, and appearance.

### **Introduction to Basic Widgets in Java (Swing Widgets)**

---

### **1. What Are Widgets?**

* In Java Swing, **widgets** are also known as **GUI components**.
* They are used to **interact with users** and build **graphical interfaces**.
* Examples: Buttons, Text fields, Labels, Checkboxes, etc.

---

### **2. Package Used**

All Swing widgets are part of the package:

```java
import javax.swing.*;
```

---

### **3. Commonly Used Basic Swing Widgets**

| Component          | Class Name       | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| **Label**          | `JLabel`         | Displays static text or image                          |
| **Button**         | `JButton`        | Performs an action when clicked                        |
| **Text Field**     | `JTextField`     | Allows single-line text input                          |
| **Password Field** | `JPasswordField` | Hides input for password entry                         |
| **Text Area**      | `JTextArea`      | Multi-line text input                                  |
| **Check Box**      | `JCheckBox`      | Allows selecting or deselecting options (multiple)     |
| **Radio Button**   | `JRadioButton`   | Allows selecting one option from a group               |
| **Combo Box**      | `JComboBox`      | Drop-down list of items                                |
| **List**           | `JList`          | Displays list of items in a box                        |
| **Panel**          | `JPanel`         | Generic container to group other components            |
| **Frame**          | `JFrame`         | Top-level main application window                      |
| **Scroll Pane**    | `JScrollPane`    | Adds scrolling to components like `JTextArea`, `JList` |
| **Table**          | `JTable`         | Displays tabular data (rows and columns)               |

---

### **4. Description and Syntax of Basic Widgets**

---

#### **(i) JLabel**

* Used to **display static text or images**.

```java
JLabel label = new JLabel("Enter Name:");
```

---

#### **(ii) JButton**

* Used to **perform an action** on click.

```java
JButton btn = new JButton("Submit");
```

---

#### **(iii) JTextField**

* For **single-line text input**.

```java
JTextField tf = new JTextField(20);  // 20 columns width
```

---

#### **(iv) JPasswordField**

* Hides the characters as they are typed.

```java
JPasswordField pf = new JPasswordField(20);
```

---

#### **(v) JTextArea**

* For **multi-line** input.

```java
JTextArea ta = new JTextArea(5, 20);  // 5 rows, 20 columns
```

---

#### **(vi) JCheckBox**

* Used to select **multiple independent options**.

```java
JCheckBox cb1 = new JCheckBox("Java");
JCheckBox cb2 = new JCheckBox("Python");
```

---

#### **(vii) JRadioButton**

* Used for **mutually exclusive selection**.

```java
JRadioButton rb1 = new JRadioButton("Male");
JRadioButton rb2 = new JRadioButton("Female");

ButtonGroup bg = new ButtonGroup();
bg.add(rb1);
bg.add(rb2);
```

---

#### **(viii) JComboBox**

* A **drop-down menu**.

```java
String[] languages = { "C", "Java", "Python" };
JComboBox<String> cb = new JComboBox<>(languages);
```

---

#### **(ix) JList**

* Displays a list of items.

```java
String[] items = { "Apple", "Banana", "Mango" };
JList<String> list = new JList<>(items);
```

---

#### **(x) JScrollPane**

* Adds scrolling to long components like `JTextArea` or `JList`.

```java
JTextArea ta = new JTextArea(10, 30);
JScrollPane sp = new JScrollPane(ta);
```

---

#### **(xi) JTable**

* Used to display **tabular data** (rows and columns).

```java
String[][] data = {
    {"1", "Alice", "A"},
    {"2", "Bob", "B"}
};

String[] column = {"ID", "Name", "Grade"};

JTable table = new JTable(data, column);
```

---

### **5. Sample Program with Basic Widgets**

```java
import javax.swing.*;

public class BasicWidgetsExample {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Basic Widgets");

        JLabel label = new JLabel("Name:");
        label.setBounds(30, 30, 100, 30);

        JTextField tf = new JTextField();
        tf.setBounds(100, 30, 150, 30);

        JButton btn = new JButton("Submit");
        btn.setBounds(100, 80, 100, 30);

        frame.add(label);
        frame.add(tf);
        frame.add(btn);

        frame.setSize(300, 200);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
```

---

### **6. Summary Table of Constructors**

| Component      | Constructor Syntax                  |
| -------------- | ----------------------------------- |
| `JLabel`       | `JLabel(String text)`               |
| `JButton`      | `JButton(String text)`              |
| `JTextField`   | `JTextField(int columns)`           |
| `JTextArea`    | `JTextArea(int rows, int columns)`  |
| `JCheckBox`    | `JCheckBox(String text)`            |
| `JRadioButton` | `JRadioButton(String text)`         |
| `JComboBox`    | `JComboBox<String>(String[] items)` |
| `JList`        | `JList<String>(String[] items)`     |

---

### **7. Conclusion**

* Java Swing provides a rich set of **pre-built widgets** to build interactive user interfaces.
* These widgets are **flexible**, **customizable**, and **event-driven**, enabling creation of powerful GUI applications.

### **Java Swing Applications (Java Swing Apps)**

---

### **1. What is a Java Swing Application?**

* A **Java Swing Application** is a **Graphical User Interface (GUI)** program developed using the **Swing toolkit**.
* It uses **Swing components** (widgets) to create **interactive desktop applications** such as forms, calculators, text editors, etc.

---

### **2. Key Components of a Swing Application**

| Component         | Purpose                                                           |
| ----------------- | ----------------------------------------------------------------- |
| `JFrame`          | Main application window (top-level container)                     |
| `JPanel`          | Sub-container to organize components logically                    |
| `JComponent`      | Base class for all Swing UI elements (like JButton, JLabel, etc.) |
| `Event Listeners` | Respond to user actions like button clicks, selections, etc.      |

---

### **3. Basic Structure of a Swing Application**

```java
import javax.swing.*;

public class MySwingApp {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My Swing App");

        JButton button = new JButton("Click Me");
        button.setBounds(50, 100, 100, 40);

        frame.add(button);

        frame.setSize(300, 300);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
```

---

### **4. Lifecycle of a Swing Application**

| Step | Description                                       |
| ---- | ------------------------------------------------- |
| 1    | Import Swing packages                             |
| 2    | Create main container (`JFrame`)                  |
| 3    | Create and configure components (`JButton`, etc.) |
| 4    | Add components to container                       |
| 5    | Set properties (size, layout, visibility)         |
| 6    | Handle events using listeners                     |
| 7    | Launch the application                            |

---

### **5. Example: Simple Login Form**

```java
import javax.swing.*;

public class LoginApp {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Login Form");

        JLabel l1 = new JLabel("Username:");
        l1.setBounds(50, 50, 100, 30);
        JTextField tf = new JTextField();
        tf.setBounds(150, 50, 150, 30);

        JLabel l2 = new JLabel("Password:");
        l2.setBounds(50, 100, 100, 30);
        JPasswordField pf = new JPasswordField();
        pf.setBounds(150, 100, 150, 30);

        JButton loginBtn = new JButton("Login");
        loginBtn.setBounds(150, 150, 100, 30);

        frame.add(l1);
        frame.add(tf);
        frame.add(l2);
        frame.add(pf);
        frame.add(loginBtn);

        frame.setSize(400, 300);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
```

---

### **6. Event Handling Example (Button Click)**

```java
import javax.swing.*;
import java.awt.event.*;

public class ClickApp {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Event Example");
        JButton btn = new JButton("Click");
        btn.setBounds(100, 100, 80, 30);

        btn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(frame, "Button Clicked");
            }
        });

        frame.add(btn);
        frame.setSize(300, 200);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
```

---

### **7. Recommended Practices**

| Practice                            | Description                                             |
| ----------------------------------- | ------------------------------------------------------- |
| Use **Event Dispatch Thread (EDT)** | To create/update GUI components in thread-safe way      |
| Use **Layout Managers**             | To control GUI layout dynamically instead of hardcoding |
| Use **Modular Code**                | Separate GUI creation, logic, and event handling        |

---

### **8. Real-World Examples of Swing Apps**

* **Login System**
* **Student Management System**
* **Notepad Clone**
* **Calculator**
* **Employee Payroll System**

---

### **9. Advantages of Swing Applications**

* **Platform-independent**
* **Customizable appearance (Look & Feel)**
* **Rich set of components**
* **MVC architecture** for clean separation of logic and UI

---

### **10. Conclusion**

A **Java Swing Application** allows developers to build **desktop-based GUIs** using ready-made widgets and event-driven programming.
It provides a **flexible, powerful, and consistent** way to design interactive applications across different platforms.

### **Layout Managers in Java Swing**

---

### **1. What is a Layout Manager?**

* A **Layout Manager** in Java is an object that **controls the positioning and sizing** of components inside a **container** (like `JFrame`, `JPanel`).
* It determines **how GUI elements are arranged** and adjusts them **automatically** when the window is resized.

---

### **2. Purpose of Layout Managers**

* Avoids manual positioning (`setBounds()`).
* Provides **dynamic, platform-independent** layouts.
* Supports **flexible design** for various screen sizes and resolutions.

---

### **3. Commonly Used Layout Managers**

| Layout Manager     | Class Name      | Behavior Description                                               |
| ------------------ | --------------- | ------------------------------------------------------------------ |
| **Flow Layout**    | `FlowLayout`    | Left to right in a row; wraps to next line                         |
| **Border Layout**  | `BorderLayout`  | Divides container into 5 regions: North, South, East, West, Center |
| **Grid Layout**    | `GridLayout`    | Divides container into equal-sized rows and columns                |
| **GridBag Layout** | `GridBagLayout` | Flexible and complex grid-based layout                             |
| **Box Layout**     | `BoxLayout`     | Arranges components in horizontal or vertical lines                |
| **Group Layout**   | `GroupLayout`   | Arranges components hierarchically (used in GUI builders)          |
| **Card Layout**    | `CardLayout`    | Allows switching between multiple components like cards            |
| **Null Layout**    | —               | No layout manager; manual positioning with `setBounds()`           |

---

### **4. FlowLayout**

* **Default layout** for `JPanel`.
* Components are placed **left to right**, then wrap to the next line.

```java
JPanel panel = new JPanel(new FlowLayout());
panel.add(new JButton("One"));
panel.add(new JButton("Two"));
```

---

### **5. BorderLayout**

* Divides the container into **five regions**:

  * `BorderLayout.NORTH`
  * `BorderLayout.SOUTH`
  * `BorderLayout.EAST`
  * `BorderLayout.WEST`
  * `BorderLayout.CENTER`

```java
JFrame frame = new JFrame();
frame.setLayout(new BorderLayout());
frame.add(new JButton("North"), BorderLayout.NORTH);
frame.add(new JButton("South"), BorderLayout.SOUTH);
frame.add(new JButton("Center"), BorderLayout.CENTER);
```

---

### **6. GridLayout**

* Divides container into **equal cells** (rows × columns).
* Components fill cells **row-wise**.

```java
JPanel panel = new JPanel(new GridLayout(2, 3)); // 2 rows, 3 columns
panel.add(new JButton("1"));
panel.add(new JButton("2"));
panel.add(new JButton("3"));
panel.add(new JButton("4"));
panel.add(new JButton("5"));
```

---

### **7. GridBagLayout**

* Most **powerful and flexible** layout.
* Allows setting **constraints** for each component (position, width, height, weight).

```java
JPanel panel = new JPanel(new GridBagLayout());
GridBagConstraints gbc = new GridBagConstraints();
gbc.gridx = 0;
gbc.gridy = 0;
panel.add(new JButton("Button"), gbc);
```

---

### **8. BoxLayout**

* Arranges components in **single row or column**.

```java
JPanel panel = new JPanel();
panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS)); // Vertical layout
panel.add(new JButton("Button 1"));
panel.add(new JButton("Button 2"));
```

---

### **9. CardLayout**

* Allows multiple components to occupy the **same space**, one at a time.
* Used for **wizard-style interfaces or tab panels**.

```java
JPanel cardPanel = new JPanel(new CardLayout());
cardPanel.add(new JButton("Card 1"), "card1");
cardPanel.add(new JButton("Card 2"), "card2");
```

---

### **10. Null Layout (Manual Positioning)**

* You **disable layout manager** and use `setBounds()` to place components manually.

```java
JFrame frame = new JFrame();
frame.setLayout(null);
JButton b = new JButton("Click");
b.setBounds(100, 100, 80, 30);
frame.add(b);
```

> ⚠️ Not recommended for large apps. No automatic resizing support.

---

### **11. Summary Table**

| Layout        | Resizes | Flexible  | Region/Grid Based   | Use Case                         |
| ------------- | ------- | --------- | ------------------- | -------------------------------- |
| FlowLayout    | No      | Medium    | No                  | Simple row layout                |
| BorderLayout  | Yes     | High      | 5 regions           | Main windows                     |
| GridLayout    | Yes     | Medium    | Uniform grid        | Keypads, tabular input           |
| GridBagLayout | Yes     | Very High | Complex grid        | Advanced layout control          |
| BoxLayout     | Yes     | High      | Vertical/Horizontal | Form-like layouts                |
| CardLayout    | No      | High      | Layered             | Tab switch, multiple views       |
| Null Layout   | No      | None      | Manual              | Quick small UIs, prototypes only |

---

### **12. Conclusion**

* Layout Managers make GUI development in Java **flexible**, **resizable**, and **platform-independent**.
* Use the appropriate layout depending on your application's **complexity and layout needs**.

### **Introduction to JDBC (Java Database Connectivity)**

---

### **1. What is JDBC?**

* **JDBC** stands for **Java Database Connectivity**.
* It is a **Java API (Application Programming Interface)** that enables Java programs to **connect to and interact with databases**.
* JDBC is used for **executing SQL queries**, **retrieving results**, **updating data**, and **managing transactions**.

---

### **2. Purpose of JDBC**

* To allow Java applications to perform:

  * **Database connection**
  * **CRUD operations** (Create, Read, Update, Delete)
  * **Transaction management**
  * **Stored procedure execution**

---

### **3. JDBC Architecture**

#### **a) Two-tier Architecture**

* Java application connects directly to the database.

```
Java App  -->  JDBC API  -->  DB Driver  -->  Database
```

#### **b) Three-tier Architecture**

* Java application communicates with a **middleware** or **application server**, which interacts with the database.

---

### **4. JDBC API Components**

| Component           | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `DriverManager`     | Manages list of database drivers and connects to the database |
| `Connection`        | Interface for establishing database connection                |
| `Statement`         | Interface to execute static SQL queries                       |
| `PreparedStatement` | Executes parameterized SQL queries (precompiled)              |
| `ResultSet`         | Holds data returned by a query (table-like structure)         |
| `SQLException`      | Handles errors during database operations                     |

---

### **5. JDBC Interfaces and Classes**

| Interface/Class     | Use                                      |
| ------------------- | ---------------------------------------- |
| `DriverManager`     | Loads and registers the driver           |
| `Connection`        | Represents a connection to the database  |
| `Statement`         | Executes SQL statements                  |
| `PreparedStatement` | Executes parameterized queries safely    |
| `ResultSet`         | Contains result of SQL SELECT queries    |
| `CallableStatement` | Executes stored procedures               |
| `SQLException`      | Exception class for handling JDBC errors |

---

### **6. Steps to Use JDBC**

1. **Import JDBC package**

   ```java
   import java.sql.*;
   ```

2. **Load the JDBC driver**

   ```java
   Class.forName("com.mysql.cj.jdbc.Driver");
   ```

3. **Establish a connection**

   ```java
   Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/dbname", "username", "password");
   ```

4. **Create statement**

   ```java
   Statement stmt = con.createStatement();
   ```

5. **Execute query**

   ```java
   ResultSet rs = stmt.executeQuery("SELECT * FROM users");
   ```

6. **Process result**

   ```java
   while(rs.next()) {
       System.out.println(rs.getInt(1) + " " + rs.getString(2));
   }
   ```

7. **Close connection**

   ```java
   con.close();
   ```

---

### **7. Example: Basic JDBC Program**

```java
import java.sql.*;

public class JDBCExample {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/mydb", "root", "password");

            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM employee");

            while (rs.next()) {
                System.out.println(rs.getInt(1) + " " + rs.getString(2));
            }

            con.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

---

### **8. Types of JDBC Drivers**

| Driver Type        | Description                                 | Example                        |
| ------------------ | ------------------------------------------- | ------------------------------ |
| Type 1 (JDBC-ODBC) | Bridge driver to ODBC                       | `sun.jdbc.odbc.JdbcOdbcDriver` |
| Type 2             | Native-API driver (requires native library) | Oracle OCI                     |
| Type 3             | Network Protocol driver (middleware server) | WebLogic                       |
| Type 4             | Pure Java driver (direct to DB)             | MySQL, PostgreSQL JDBC         |

> ✅ **Type 4** is most commonly used today.

---

### **9. Advantages of JDBC**

* Platform-independent database access from Java
* Supports most popular RDBMS (MySQL, Oracle, PostgreSQL, etc.)
* Secure database connectivity
* Supports **transaction management**
* Uses **standard SQL syntax**

---

### **10. Limitations of JDBC**

* Requires detailed knowledge of SQL
* Connection management must be handled manually
* Less abstract compared to higher-level frameworks (e.g., Hibernate, JPA)

---

### **11. Conclusion**

JDBC provides a **standard interface** for Java programs to perform **database operations** in a **portable, secure, and efficient way**.
It forms the **foundation of all Java-based database programming**.

 ### **JDBC Drivers**

---

### **1. What is a JDBC Driver?**

* A **JDBC Driver** is a **software component** that enables **Java applications to interact with a database**.
* It acts as a **translator** between the **Java program** and the **Database Management System (DBMS)**.

---

### **2. Role of JDBC Driver**

* Converts **JDBC API calls** into **database-specific calls**.
* Enables communication between **Java application** and **database server**.
* Responsible for:

  * Establishing connection
  * Executing SQL queries
  * Returning results to the Java program

---

### **3. Types of JDBC Drivers**

Java defines **4 types** of JDBC drivers:

---

#### **Type 1 – JDBC-ODBC Bridge Driver**

| Feature            | Description                                                     |
| ------------------ | --------------------------------------------------------------- |
| Name               | JDBC-ODBC Bridge                                                |
| Working Mechanism  | Translates JDBC calls into ODBC calls, then into database calls |
| Dependency         | Requires ODBC driver installed on client                        |
| Platform-Dependent | Yes                                                             |
| Performance        | Low (due to multiple layers)                                    |
| Example            | `sun.jdbc.odbc.JdbcOdbcDriver` (Deprecated)                     |

**Diagram:**

```
Java App → JDBC API → JDBC-ODBC Driver → ODBC → Database
```

> ❌ **Obsolete. Removed from Java 8 onwards.**

---

#### **Type 2 – Native-API Driver**

| Feature            | Description                                          |
| ------------------ | ---------------------------------------------------- |
| Name               | Native-API driver                                    |
| Working Mechanism  | Converts JDBC calls into **native C/C++ API** calls  |
| Dependency         | Requires **native library** specific to the database |
| Platform-Dependent | Yes                                                  |
| Performance        | Better than Type 1                                   |
| Example            | Oracle OCI driver                                    |

**Diagram:**

```
Java App → JDBC API → Native Driver (C/C++) → Database
```

> ✅ Suitable for large enterprise apps that require high performance and use specific databases.

---

#### **Type 3 – Network Protocol Driver**

| Feature            | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| Name               | Network Protocol (Middleware) Driver                              |
| Working Mechanism  | Sends JDBC calls to a **middleware server**, which forwards to DB |
| Dependency         | Requires **middleware service**                                   |
| Platform-Dependent | No (pure Java)                                                    |
| Performance        | Good, scalable                                                    |
| Example            | IBM WebSphere, BEA WebLogic                                       |

**Diagram:**

```
Java App → JDBC API → Type 3 Driver → Middleware Server → Database
```

> ✅ Suitable for large **distributed systems**.

---

#### **Type 4 – Thin Driver (Pure Java Driver)**

| Feature            | Description                                                      |
| ------------------ | ---------------------------------------------------------------- |
| Name               | Thin Driver / Direct-to-Database Driver                          |
| Working Mechanism  | Converts JDBC calls **directly into database-specific protocol** |
| Dependency         | No native libraries required                                     |
| Platform-Dependent | No (written entirely in Java)                                    |
| Performance        | High                                                             |
| Example            | MySQL Connector/J, Oracle JDBC Thin Driver, PostgreSQL JDBC      |

**Diagram:**

```
Java App → JDBC API → Type 4 Driver → Database
```

> ✅ **Most commonly used** in modern Java applications.

---

### **4. Comparison Table of JDBC Driver Types**

| Feature                 | Type 1         | Type 2 | Type 3  | Type 4        |
| ----------------------- | -------------- | ------ | ------- | ------------- |
| Platform Independent    | ❌              | ❌      | ✅       | ✅             |
| Requires Native Library | ✅ (ODBC)       | ✅      | ❌       | ❌             |
| Middleware Required     | ❌              | ❌      | ✅       | ❌             |
| Performance             | Low            | Medium | High    | Very High     |
| Portability             | Poor           | Poor   | Good    | Excellent     |
| Use Today               | ❌ (Deprecated) | Rare   | Limited | ✅ Most Common |

---

### **5. Examples of Popular Type 4 JDBC Drivers**

| Database   | JDBC Driver Class                              | Jar File                         |
| ---------- | ---------------------------------------------- | -------------------------------- |
| MySQL      | `com.mysql.cj.jdbc.Driver`                     | `mysql-connector-java-x.x.x.jar` |
| PostgreSQL | `org.postgresql.Driver`                        | `postgresql-x.x.x.jar`           |
| Oracle     | `oracle.jdbc.driver.OracleDriver`              | `ojdbc8.jar`, `ojdbc11.jar`      |
| SQLite     | `org.sqlite.JDBC`                              | `sqlite-jdbc-x.x.x.jar`          |
| SQL Server | `com.microsoft.sqlserver.jdbc.SQLServerDriver` | `sqljdbc4.jar`                   |

---

### **6. How to Load a JDBC Driver**

```java
Class.forName("com.mysql.cj.jdbc.Driver");  // MySQL Driver
```

> For newer versions of JDBC (Java 6+), **automatic loading** happens via **Service Provider Interface (SPI)**.

---

### **7. Conclusion**

* JDBC Drivers are the **core link between Java code and databases**.
* **Type 4 (Thin Drivers)** are **preferred** in most real-world applications due to their **performance, portability, and ease of use**.

### **Database (DB) Connectivity Steps in Java using JDBC**

---

### **1. Overview**

To connect a Java application with a database (like MySQL, Oracle, PostgreSQL), you follow **a standard set of JDBC steps**. These steps include:

1. Loading the driver
2. Establishing the connection
3. Creating a statement
4. Executing SQL queries
5. Processing the result
6. Closing the connection

---

### **2. Step-by-Step Explanation**

---

#### **Step 1: Import JDBC Packages**

* Required to use JDBC classes such as `Connection`, `Statement`, `ResultSet`.

```java
import java.sql.*;
```

---

#### **Step 2: Load and Register the JDBC Driver**

* The driver must be **registered with the DriverManager**.
* Use `Class.forName()` to load the class dynamically.

```java
Class.forName("com.mysql.cj.jdbc.Driver"); // For MySQL
```

> For newer JDBC versions (Java 6+), this step is optional for some drivers due to auto-loading.

---

#### **Step 3: Establish the Database Connection**

* Use `DriverManager.getConnection()` to connect to the database.

```java
Connection con = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/mydatabase",
    "username",
    "password"
);
```

**Parameters:**

* URL format:
  `jdbc:<dbms>://<host>:<port>/<database_name>`
* Username: DB username
* Password: DB password

---

#### **Step 4: Create Statement or PreparedStatement**

##### **Using Statement (for static SQL):**

```java
Statement stmt = con.createStatement();
```

##### **Using PreparedStatement (for dynamic queries):**

```java
PreparedStatement pstmt = con.prepareStatement("SELECT * FROM users WHERE id = ?");
pstmt.setInt(1, 101);
```

---

#### **Step 5: Execute SQL Query**

##### **For SELECT queries (returns ResultSet):**

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM users");
```

##### **For INSERT, UPDATE, DELETE (returns update count):**

```java
int rowsAffected = stmt.executeUpdate("INSERT INTO users VALUES (101, 'John')");
```

---

#### **Step 6: Process the Result**

##### **For SELECT queries:**

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
    System.out.println(id + " " + name);
}
```

---

#### **Step 7: Close the Connection**

* Always close resources to **prevent memory leaks**.

```java
rs.close();           // Close ResultSet
stmt.close();         // Close Statement
con.close();          // Close Connection
```

> Best done inside `finally` block or using **try-with-resources** (Java 7+).

---

### **3. Complete JDBC Example**

```java
import java.sql.*;

public class DBConnectionExample {
    public static void main(String[] args) {
        try {
            // Step 1: Load Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Step 2: Establish Connection
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/testdb",
                "root",
                "password"
            );

            // Step 3: Create Statement
            Statement stmt = con.createStatement();

            // Step 4: Execute Query
            ResultSet rs = stmt.executeQuery("SELECT * FROM users");

            // Step 5: Process Results
            while (rs.next()) {
                System.out.println(rs.getInt(1) + " " + rs.getString(2));
            }

            // Step 6: Close resources
            rs.close();
            stmt.close();
            con.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

---

### **4. Additional Notes**

| Topic                  | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- |
| **Driver JAR file**    | Must be in classpath (e.g., `mysql-connector-java.jar`)              |
| **Exception Handling** | Wrap JDBC code in `try-catch` blocks (check for `SQLException`)      |
| **try-with-resources** | Automatically closes resources (from Java 7 onwards)                 |
| **Transactions**       | For atomic operations, use `con.setAutoCommit(false)` and `commit()` |

---

### **5. Summary of JDBC Connectivity Steps**

| Step No | Description                    | Method/Interface Used                      |
| ------- | ------------------------------ | ------------------------------------------ |
| 1       | Import JDBC packages           | `import java.sql.*;`                       |
| 2       | Load the driver                | `Class.forName()`                          |
| 3       | Create DB connection           | `DriverManager.getConnection()`            |
| 4       | Create statement object        | `Statement` / `PreparedStatement`          |
| 5       | Execute query                  | `executeQuery()`, `executeUpdate()`        |
| 6       | Process results                | `ResultSet` methods (`next()`, `getXXX()`) |
| 7       | Close connection and resources | `close()` methods                          |

---

### **6. Conclusion**

These **7 standardized JDBC steps** are essential for any Java application to **interact with a relational database** effectively and safely.
They provide full control over **connection, query execution, and data handling**.

### **Connectivity with Various Databases using JDBC**

---

### **1. Overview**

Java programs can connect to multiple types of **Relational Database Management Systems (RDBMS)** using **JDBC drivers**.
Each database has its own **JDBC driver**, **connection URL format**, and **specific configurations**.

---

### **2. General JDBC Connection Steps**

1. Load the JDBC driver class
2. Establish the connection using `DriverManager.getConnection()`
3. Execute SQL using `Statement` or `PreparedStatement`
4. Process the `ResultSet`
5. Close resources

---

### **3. Connecting to Common Databases**

---

#### **A. MySQL**

* **Driver Class**: `com.mysql.cj.jdbc.Driver`

* **JAR**: `mysql-connector-java-x.x.x.jar`

* **Connection URL**:

  ```java
  jdbc:mysql://<host>:<port>/<database>
  ```

* **Example Code**:

```java
Class.forName("com.mysql.cj.jdbc.Driver");
Connection con = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/testdb", "root", "password");
```

---

#### **B. Oracle**

* **Driver Class**: `oracle.jdbc.driver.OracleDriver`

* **JAR**: `ojdbc8.jar` or `ojdbc11.jar`

* **Connection URL**:

  ```java
  jdbc:oracle:thin:@<host>:<port>:<SID>
  ```

* **Example Code**:

```java
Class.forName("oracle.jdbc.driver.OracleDriver");
Connection con = DriverManager.getConnection(
    "jdbc:oracle:thin:@localhost:1521:xe", "system", "oracle");
```

---

#### **C. PostgreSQL**

* **Driver Class**: `org.postgresql.Driver`

* **JAR**: `postgresql-x.x.x.jar`

* **Connection URL**:

  ```java
  jdbc:postgresql://<host>:<port>/<database>
  ```

* **Example Code**:

```java
Class.forName("org.postgresql.Driver");
Connection con = DriverManager.getConnection(
    "jdbc:postgresql://localhost:5432/mydb", "postgres", "password");
```

---

#### **D. SQLite**

* **Driver Class**: `org.sqlite.JDBC`

* **JAR**: `sqlite-jdbc-x.x.x.jar`

* **Connection URL**:

  ```java
  jdbc:sqlite:<path_to_db_file>
  ```

* **Example Code**:

```java
Class.forName("org.sqlite.JDBC");
Connection con = DriverManager.getConnection("jdbc:sqlite:test.db");
```

---

#### **E. Microsoft SQL Server**

* **Driver Class**: `com.microsoft.sqlserver.jdbc.SQLServerDriver`

* **JAR**: `sqljdbc4.jar`

* **Connection URL**:

  ```java
  jdbc:sqlserver://<host>:<port>;databaseName=<dbname>
  ```

* **Example Code**:

```java
Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
Connection con = DriverManager.getConnection(
    "jdbc:sqlserver://localhost:1433;databaseName=TestDB", "sa", "password");
```

---

### **4. Summary Table**

| Database   | Driver Class                                   | URL Format Example                                    |
| ---------- | ---------------------------------------------- | ----------------------------------------------------- |
| MySQL      | `com.mysql.cj.jdbc.Driver`                     | `jdbc:mysql://localhost:3306/dbname`                  |
| Oracle     | `oracle.jdbc.driver.OracleDriver`              | `jdbc:oracle:thin:@localhost:1521:xe`                 |
| PostgreSQL | `org.postgresql.Driver`                        | `jdbc:postgresql://localhost:5432/dbname`             |
| SQLite     | `org.sqlite.JDBC`                              | `jdbc:sqlite:C:/db/mydb.db`                           |
| SQL Server | `com.microsoft.sqlserver.jdbc.SQLServerDriver` | `jdbc:sqlserver://localhost:1433;databaseName=dbname` |

---

### **5. Required JAR Files**

| Database   | JDBC Driver JAR file                   |
| ---------- | -------------------------------------- |
| MySQL      | `mysql-connector-java-x.x.x.jar`       |
| Oracle     | `ojdbc8.jar`, `ojdbc11.jar`            |
| PostgreSQL | `postgresql-x.x.x.jar`                 |
| SQLite     | `sqlite-jdbc-x.x.x.jar`                |
| SQL Server | `sqljdbc4.jar`, `mssql-jdbc-x.x.x.jar` |

---

### **6. JDBC URL Components Explained**

For a typical URL:

```
jdbc:<subprotocol>:<subname>
```

* `jdbc`: Standard prefix
* `<subprotocol>`: Database type (e.g., mysql, postgresql, oracle)
* `<subname>`: Hostname, port, database name, and parameters

Example:

```java
jdbc:mysql://localhost:3306/mydb?useSSL=false
```

---

### **7. Notes**

* Always ensure the **JDBC JAR is added to the classpath**.
* If connection fails, check:

  * Driver loaded?
  * Host/port/database name correct?
  * User credentials valid?
  * JDBC JAR present?

---

### **8. Conclusion**

JDBC enables seamless connectivity between Java applications and various **popular databases**.
By using **correct drivers, URLs, and credentials**, Java can connect to **any RDBMS** that supports JDBC.

