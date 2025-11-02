# MCA Semester 2 Mini Project Report

## Project Title

**Personal Finance Tracker using Java Swing and SQLite**

---

## Abstract

The project is a **desktop-based finance management application** developed in **Java Swing** with an embedded **SQLite database**. It allows users to add, update, delete, and view personal financial transactions, filter them by multiple criteria, and view overall summaries such as total income, expenses, and balance. The project demonstrates skills in **GUI programming, event-driven design, and database integration**.

---

## Objectives

1. To design a user-friendly desktop application for personal finance management.
2. To provide essential features like adding, editing, and deleting entries.
3. To support filtering based on type, category, date, tags, and amount range.
4. To maintain persistence using an embedded SQLite database.
5. To calculate totals of income, expenses, and balance in real time.
6. To apply **Java Swing concepts** and **JDBC connectivity** in a practical project.

---

## Technologies Used

* **Programming Language:** Java (JDK 8+)
* **GUI Toolkit:** Java Swing (AWT & Swing components)
* **Database:** SQLite (via JDBC driver)
* **IDE/Editor:** Any Java-compatible IDE (IntelliJ, Eclipse, VS Code, or CLI tools)
* **OS Environment:** Platform-independent (tested on Linux - Arch/Hyprland)

---

## System Requirements

### Hardware

* Processor: Minimum Dual-Core
* RAM: 2 GB minimum
* Disk Space: ~50 MB

### Software

* JDK 8 or higher
* SQLite JDBC Driver (e.g., sqlite-jdbc-3.36.0.3.jar)
* SQLite CLI (optional, for debugging database)

---

## System Design

### Architecture

* **Layer 1 (UI Layer):** Implemented with Swing components (JFrame, JPanel, JTable, JTextField, etc.).
* **Layer 2 (Event Handling):** ActionListeners and MouseListeners handle user input.
* **Layer 3 (Database Layer):** SQLite database connected via JDBC.

(*Insert Architecture Diagram here*)

### Database Schema

The application stores data in a single table `entries` with the following fields:

* `id` (INTEGER, Primary Key, Auto Increment)
* `date` (TEXT, format: YYYY-MM-DD)
* `type` (TEXT: Income/Expense)
* `category` (TEXT)
* `amount` (REAL)
* `description` (TEXT)
* `payment_method` (TEXT: Cash/Card/UPI/NetBanking/Other)
* `tags` (TEXT)
* `recurring` (INTEGER: 0 or 1)
* `notes` (TEXT)

(*Insert ER Diagram here*)

### Data Flow Diagram (DFD)

* **Level 0 DFD:** User ↔ Application ↔ Database
* **Level 1 DFD:** Shows processes such as Add Entry, Update Entry, Delete Entry, Filter Entries, View Totals.

(*Insert DFD diagrams here*)

### Use Case Diagram

Actors: User

Use Cases: Add Entry, Update Entry, Delete Entry, Filter Entries, View Totals.

(*Insert Use Case Diagram here*)

### Application Layout

1. **Top Section (Filters):**

   * Filter by Type, Category, Date Range, Search Text, Min/Max Amount.
   * Buttons: Apply Filters, Clear Filters.

2. **Left Section (Table - 3/4 screen):**

   * JTable displaying all transactions with columns for ID, Date, Type, Category, Amount, Payment, Tags, Recurring, Description.

3. **Right Section (Form - 1/4 screen):**

   * Form fields: Type, Category, Amount, Payment Method, Date, Tags, Recurring (checkbox), Description, Notes.
   * Buttons: Add, Update, Clear.

4. **Bottom Section (Summary Bar):**

   * Labels showing Income, Expense, Balance.
   * Status label showing the latest action performed.

(*Insert UI Layout Diagram here*)

---

## Implementation

### Execution Flow

1. The JVM starts with the `main` method.
2. Constructor initializes the database and builds the UI.
3. `setVisible(true)` displays the JFrame.
4. Application enters the event-driven loop:

   * User interacts via buttons, filters, or table rows.
   * Listeners trigger methods (onAdd, onUpdate, loadEntries, etc.).
   * Database is updated accordingly.

(*Insert Flowchart of Execution Flow here*)

### Features Implemented

* **Add Entry:** Add a new transaction with all fields.
* **Update Entry:** Double-click a row to load, then modify and update.
* **Delete Entry:** Remove selected entry from database.
* **Filters:** Narrow data by type, category, date, amount, or tags.
* **Totals:** Real-time income, expense, and balance calculation.
* **Notes & Tags:** Allow extra details for transactions.
* **Recurring Flag:** Identify fixed recurring expenses/income.

---

## Screenshots

(*Insert screenshots here*)

* Screenshot 1: Application Home Screen (UI with table and form)
* Screenshot 2: Adding a New Transaction
* Screenshot 3: Filtering Data by Category/Date
* Screenshot 4: Updating an Existing Record
* Screenshot 5: Totals Display (Income, Expense, Balance)

---

## Testing & Validation

* **Unit Testing:** Verified CRUD operations on database.
* **Integration Testing:** Ensured filters work correctly with multiple conditions.
* **Usability Testing:** Checked UI layout on Linux (Arch with Hyprland).
* **Validation:** Form prevents invalid input (negative/empty amounts).

(*Insert Test Case Table Diagrammatically here*)

---

## Advantages

* Lightweight, runs without external DB installation.
* Portable across operating systems.
* Easy-to-use interface.
* Provides both data entry and analytical summaries.

---

## Limitations

* No support for multiple users or authentication.
* No graphical charts (only text-based totals).
* Basic error handling for invalid dates.

---

## Future Enhancements

1. Add graphical charts (monthly expense pie chart, line graphs).
2. Support for exporting reports in PDF.
3. User authentication with login system.
4. Option to categorize recurring payments automatically.
5. Dark mode UI.

---

## Conclusion

The **Personal Finance Tracker** project successfully demonstrates the application of **Java Swing** and **SQLite database integration** in building a real-world desktop finance application. It fulfills the requirements of the mini-project by implementing **CRUD operations, filtering, real-time totals, and a structured UI layout**. With further enhancements, it can evolve into a complete personal finance manager.

---

## References

* Java Swing Documentation: [https://docs.oracle.com/javase/tutorial/uiswing/](https://docs.oracle.com/javase/tutorial/uiswing/)
* SQLite Documentation: [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)
* JDBC Tutorial: [https://docs.oracle.com/javase/tutorial/jdbc/](https://docs.oracle.com/javase/tutorial/jdbc/)

---

## Student Details

* **Name:** [Your Name]
* **USN/ID:** [Your University ID]
* **Course:** MCA Semester 2
* **Institution:** Reva University, Bengaluru

---

(*Add signatures, approval, and submission pages as per university format*)
