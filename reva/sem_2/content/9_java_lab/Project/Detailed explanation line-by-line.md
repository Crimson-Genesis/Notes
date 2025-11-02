
---

# 🔹 Sections of the Code

### **Section 1: Setup & UI Initialization**

* **Imports**
* **Class declaration & global fields**
* **Constructor**
* **`initUI()` method** (building filters, table, form, and layout)

---

### **Section 2: Database Operations**

* **`initDB()`** (create table, alter table if missing columns)
* **CRUD operations:**

  * `addEntryToDB(...)`
  * `updateEntryInDB(...)`
  * `deleteEntryFromDB(int id)`

---

### **Section 3: Application Logic & Event Handling**

* **Loading & filtering entries:** `loadEntries(...)`
* **Apply/Clear filters**
* **Update totals**
* **Form actions:**

  * `onAdd()`
  * `onUpdate()`
  * `clearForm()`
  * `loadSelectedRowToForm()`
* **Helper method `refreshAndTotals()`**
* **`main()` method**

---

So basically:

* **Section 1 = UI + Setup**
* **Section 2 = Database**
* **Section 3 = Logic & Events**

---
# 🔹 Section 1: Setup & UI Initialization

## 1. Imports

```java
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.io.FileWriter;
import java.io.PrintWriter;
```

### Explanation:

* `javax.swing.*;` → Imports all Swing classes (JFrame, JPanel, JButton, JTable, etc.).
* `javax.swing.border.EmptyBorder;` → For adding empty spacing around UI components.
* `javax.swing.table.DefaultTableModel;` → Used for handling JTable’s data (rows/columns).
* `java.awt.*;` → For layouts, colors, dimensions (from AWT).
* `java.awt.event.*;` → For handling events like button clicks, mouse events.
* `java.sql.*;` → For JDBC database operations (Connection, Statement, ResultSet).
* `java.text.DecimalFormat;` and `NumberFormat;` → For formatting numbers (like 1000.50).
* `java.text.SimpleDateFormat;` → For handling date strings (yyyy-MM-dd).
* `java.util.Date;` → Represents the current date/time.
* `java.io.FileWriter;` & `PrintWriter;` → For writing to files (e.g., CSV export).

---

## 2. Class Declaration & Global Variables

```java
public class PersonalFinanceTracker extends JFrame {
    private static final String DB_URL = "jdbc:sqlite:finance.db";

    private DefaultTableModel tableModel;
    private JTable table;

    // Form fields (right column)
    private JComboBox<String> cbType, cbCategory, cbPayment;
    private JFormattedTextField tfAmount;
    private JTextField tfDescription, tfDate, tfTags;
    private JCheckBox cbRecurring;
    private JTextArea taNotes;

    // Filter fields (top)
    private JComboBox<String> fType, fCategory;
    private JTextField fDateFrom, fDateTo, fSearch, fMinAmt, fMaxAmt;

    private JLabel lblIncomeTotal, lblExpenseTotal, lblBalance, lblStatus;
```

### Explanation:

* `public class PersonalFinanceTracker extends JFrame` → Our class **is a JFrame** (main application window).
* `DB_URL` → Database connection string → tells JDBC to use SQLite DB file `finance.db`.
* `tableModel` → Holds transaction data (rows/columns).
* `table` → JTable UI element that shows transactions.
* Form fields: `cbType`, `cbCategory`, `cbPayment` → Drop-down menus.

  * Example: Type = Expense/Income.
* `tfAmount` → Formatted text field for money amounts.
* `tfDescription`, `tfDate`, `tfTags` → Normal text fields.
* `cbRecurring` → Checkbox (for recurring entries).
* `taNotes` → Text area for writing notes.
* Filter fields (fType, fCategory, etc.) → Search bar fields in the top filter section.
* Labels (`lblIncomeTotal`, `lblExpenseTotal`, `lblBalance`, `lblStatus`) → Show totals & status bar at the bottom.

---

## 3. Constructor

```java
public PersonalFinanceTracker() {
    super("Personal Finance Tracker");
    initDB();
    initUI();
    loadEntries("", "", "", "", "");
    updateTotals();
}
```

### Explanation:

* `super("Personal Finance Tracker")` → Calls JFrame constructor and sets **window title**.
* `initDB()` → Prepares the database (creates table if missing).
* `initUI()` → Builds all UI components (filters, table, form, status bar).
* `loadEntries("", "", "", "", "")` → Loads all entries into the table (no filters at first).
* `updateTotals()` → Calculates and displays totals (Income, Expense, Balance).

So the constructor sets up **database + UI + first data load**.

---

## 4. initUI() — Frame Setup

```java
private void initUI() {
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setSize(1200, 720);
    setLocationRelativeTo(null);
```

### Explanation:

* `setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)` → App closes when user clicks the X button.
* `setSize(1200, 720)` → Window size set to 1200px width × 720px height.
* `setLocationRelativeTo(null)` → Centers the window on screen.

---

## 5. initUI() — Top Filter Bar

```java
JPanel top = new JPanel(new GridBagLayout());
top.setBorder(BorderFactory.createCompoundBorder(
    BorderFactory.createLineBorder(Color.LIGHT_GRAY), 
    new EmptyBorder(8,8,8,8))
);
GridBagConstraints tc = new GridBagConstraints();
tc.insets = new Insets(4,6,4,6);
tc.anchor = GridBagConstraints.WEST;
```

* Creates a `JPanel` for the **top filter bar**.
* Uses `GridBagLayout` → flexible layout for aligning filters.
* Adds borders: gray line + empty padding.
* `GridBagConstraints tc` → defines padding & alignment for components.

```java
fType = new JComboBox<>(new String[]{"All","Expense","Income"});
fCategory = new JComboBox<>(new String[]{"All","Food","Transport","Bills","Salary","Entertainment","Other"});
fDateFrom = new JTextField(8); fDateTo = new JTextField(8);
fDateFrom.setToolTipText("YYYY-MM-DD (start)");
fDateTo.setToolTipText("YYYY-MM-DD (end)");
fSearch = new JTextField(12);
fSearch.setToolTipText("Search description or tags");
fMinAmt = new JTextField(6); fMaxAmt = new JTextField(6);
```

* Creates filter inputs:

  * `fType` → Drop-down (All/Expense/Income).
  * `fCategory` → Drop-down for categories.
  * `fDateFrom` & `fDateTo` → Text fields for date range.
  * `fSearch` → Search text field.
  * `fMinAmt` & `fMaxAmt` → Range of amounts.

```java
JButton btnApplyFilter = new JButton("Apply Filters");
JButton btnClearFilter = new JButton("Clear Filters");
```

* Buttons to **apply or clear filters**.

```java
int gx=0;
tc.gridx = gx++; tc.gridy=0; top.add(new JLabel("Type:"), tc);
tc.gridx = gx++; top.add(fType, tc);
// ... (similar lines for Category, Date, etc.)
```

* Adds labels + filter inputs to `top` panel row by row.

---
## 6. Left Table (3/4 of screen)

```java
String[] cols = new String[]{"ID","Date","Type","Category","Amount","Payment","Tags","Recurring","Description"};
tableModel = new DefaultTableModel(cols, 0) { 
    public boolean isCellEditable(int r,int c){return false;} 
};
table = new JTable(tableModel);
table.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
table.setFillsViewportHeight(true);
table.getColumnModel().getColumn(0).setMaxWidth(60);
JScrollPane tableScroll = new JScrollPane(table);
JPanel leftPanel = new JPanel(new BorderLayout());
leftPanel.add(tableScroll, BorderLayout.CENTER);
leftPanel.setBorder(new EmptyBorder(6,6,6,6));
```

### Explanation:

* Defines **columns** for the JTable: `ID, Date, Type, Category, Amount, Payment, Tags, Recurring, Description`.
* `DefaultTableModel(cols, 0)` → table with headers, **0 rows initially**.
* `isCellEditable(...)` overridden → makes table **read-only**.
* `table = new JTable(tableModel);` → Creates the actual JTable UI.
* `setSelectionMode(SINGLE_SELECTION)` → Only one row can be selected at a time.
* `setFillsViewportHeight(true)` → Table fills vertical space even if empty.
* `getColumnModel().getColumn(0).setMaxWidth(60)` → Shrinks ID column.
* Wrapped in `JScrollPane` → Scrollable.
* Added into `leftPanel` with `BorderLayout.CENTER`.
* `leftPanel` also has padding.

---

## 7. Right Form (1/4 of screen)

```java
JPanel form = new JPanel(new GridBagLayout());
form.setBorder(BorderFactory.createCompoundBorder(
    BorderFactory.createLineBorder(Color.LIGHT_GRAY), 
    new EmptyBorder(12,12,12,12))
);
GridBagConstraints c = new GridBagConstraints();
c.insets = new Insets(6,6,6,6);
c.anchor = GridBagConstraints.WEST;
c.fill = GridBagConstraints.HORIZONTAL;
```

* Creates the **form panel**.
* Uses `GridBagLayout` → allows structured placement of labels & inputs.
* Adds border with gray line + padding.
* Sets constraints (spacing, alignment).

```java
cbType = new JComboBox<>(new String[]{"Expense","Income"});
cbCategory = new JComboBox<>(new String[]{"Food","Transport","Bills","Salary","Entertainment","Other"});
cbPayment = new JComboBox<>(new String[]{"Cash","Card","UPI","NetBanking","Other"});
```

* Combo boxes for selecting **Type, Category, Payment Method**.

```java
NumberFormat nf = DecimalFormat.getNumberInstance();
nf.setMinimumFractionDigits(2); nf.setMaximumFractionDigits(2);
tfAmount = new JFormattedTextField(nf);
tfAmount.setColumns(10); tfAmount.setValue(0.00);
```

* `tfAmount` is a **formatted text field** → ensures valid decimal number input.

```java
tfDescription = new JTextField(12);
tfDate = new JTextField(12); 
tfDate.setText(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));
tfTags = new JTextField(12);
cbRecurring = new JCheckBox("Recurring");
taNotes = new JTextArea(4,12);
taNotes.setLineWrap(true); taNotes.setWrapStyleWord(true);
JScrollPane notesScroll = new JScrollPane(taNotes);
```

* Extra form fields:

  * `tfDescription` → Short text.
  * `tfDate` → Default today’s date (`yyyy-MM-dd`).
  * `tfTags` → Keywords.
  * `cbRecurring` → Checkbox.
  * `taNotes` → Multi-line notes field (scrollable).

---

### Adding Form Components Row by Row

```java
int row = 0;
c.gridx=0; c.gridy=row; form.add(new JLabel("Type:"), c);
c.gridx=1; form.add(cbType, c);
// ... (same style for Category, Amount, Payment, Date, Tags, Recurring, Description, Notes)
```

* Uses `GridBagLayout` → Each row has **Label** on left, **Input** on right.
* Each field is added row by row.

---

### Buttons in Form

```java
row++; 
c.gridx=0; c.gridy=row; c.gridwidth=2; c.anchor = GridBagConstraints.CENTER;
JPanel fp = new JPanel();
JButton btnAdd = new JButton("Add");
JButton btnUpdate = new JButton("Update");
JButton btnClear = new JButton("Clear");
fp.add(btnAdd); fp.add(btnUpdate); fp.add(btnClear);
form.add(fp, c);
```

* Adds **Add, Update, Clear** buttons inside the form.
* Buttons placed in a separate small panel `fp`.

---

## 8. Split Pane

```java
JSplitPane split = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT, leftPanel, form);
split.setResizeWeight(0.75);
split.setDividerSize(6);
```

* Splits screen **horizontally**:

  * Left side = table (75%).
  * Right side = form (25%).
* `DividerSize(6)` → Thin divider between them.

---

## 9. Bottom Status Bar

```java
JPanel status = new JPanel(new BorderLayout());
JPanel totals = new JPanel(new FlowLayout(FlowLayout.RIGHT));
lblIncomeTotal = new JLabel("Income: 0.00");
lblExpenseTotal = new JLabel("Expense: 0.00");
lblBalance = new JLabel("Balance: 0.00");
totals.add(lblIncomeTotal); 
totals.add(Box.createHorizontalStrut(12)); 
totals.add(lblExpenseTotal); 
totals.add(Box.createHorizontalStrut(12)); 
totals.add(lblBalance);
lblStatus = new JLabel("Ready");
status.add(lblStatus, BorderLayout.WEST);
status.add(totals, BorderLayout.EAST);
status.setBorder(new EmptyBorder(6,8,6,8));
```

* Creates **status panel** at bottom.
* Left side: status message (e.g., “Ready”, “Added entry”).
* Right side: totals (Income, Expense, Balance).
* `Box.createHorizontalStrut(12)` → Adds space between labels.

---

## 10. Event Wiring

```java
btnApplyFilter.addActionListener(e -> applyFilters());
btnClearFilter.addActionListener(e -> clearFilters());
btnAdd.addActionListener(e -> onAdd());
btnClear.addActionListener(e -> clearForm());
btnUpdate.addActionListener(e -> onUpdate());

table.addMouseListener(new MouseAdapter() { 
    public void mouseClicked(MouseEvent e){ 
        if (e.getClickCount()==2) loadSelectedRowToForm(); 
    } 
});
```

* **Apply Filters** button → calls `applyFilters()`.
* **Clear Filters** button → calls `clearFilters()`.
* **Add** → calls `onAdd()`.
* **Update** → calls `onUpdate()`.
* **Clear** → resets form.
* **Table double-click** → loads that row into the form for editing.

---

## 11. Add Components to Frame

```java
getContentPane().setLayout(new BorderLayout());
getContentPane().add(top, BorderLayout.NORTH);
getContentPane().add(split, BorderLayout.CENTER);
getContentPane().add(status, BorderLayout.SOUTH);
```

* Places panels in **main JFrame**:

  * Top filter bar (`NORTH`)
  * Split (table + form) (`CENTER`)
  * Status bar (`SOUTH`)

---
# Section 2 — Database Operations

We’ll cover these methods:

1. `initDB()` — create table and add missing columns
2. `addEntryToDB(...)` — insert a row
3. `updateEntryInDB(...)` — update an existing row
4. `deleteEntryFromDB(int id)` — delete by id

---

## 1) `initDB()`

```java
private void initDB() {
    try (Connection conn = DriverManager.getConnection(DB_URL)) {
        Statement st = conn.createStatement();
        st.execute("CREATE TABLE IF NOT EXISTS entries ("
                +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                +"date TEXT,"
                +"type TEXT,"
                +"category TEXT,"
                +"amount REAL,"
                +"description TEXT"
                +")");

        // add extra columns if missing
        ResultSet rs = st.executeQuery("PRAGMA table_info(entries)");
        java.util.Set<String> cols = new java.util.HashSet<>();
        while (rs.next()) cols.add(rs.getString("name"));
        if (!cols.contains("payment_method")) st.execute("ALTER TABLE entries ADD COLUMN payment_method TEXT");
        if (!cols.contains("tags")) st.execute("ALTER TABLE entries ADD COLUMN tags TEXT");
        if (!cols.contains("recurring")) st.execute("ALTER TABLE entries ADD COLUMN recurring INTEGER DEFAULT 0");
        if (!cols.contains("notes")) st.execute("ALTER TABLE entries ADD COLUMN notes TEXT");

    } catch (SQLException ex) {
        JOptionPane.showMessageDialog(this, "DB init failed: "+ex.getMessage());
    }
}
```

### Line-by-line explanation

* `private void initDB() {`
  Declares the method — private because only this class needs it.

* `try (Connection conn = DriverManager.getConnection(DB_URL)) {`
  Opens a JDBC connection to the SQLite file defined by `DB_URL`. The try-with-resources ensures the connection is closed automatically at the end of the block.

* `Statement st = conn.createStatement();`
  Create a `Statement` object used to execute SQL statements. We use this for DDL (CREATE/ALTER) and simple queries.

* `st.execute("CREATE TABLE IF NOT EXISTS entries (... )");`
  Runs SQL to create the `entries` table if it doesn't exist. The columns defined here are the minimum required by older versions of the app (`id`, `date`, `type`, `category`, `amount`, `description`). Using `IF NOT EXISTS` prevents errors if the table already exists.

* `ResultSet rs = st.executeQuery("PRAGMA table_info(entries)");`
  SQLite-specific query: `PRAGMA table_info(table)` returns metadata about the columns present in the table. We use it to inspect which columns already exist.

* `java.util.Set<String> cols = new java.util.HashSet<>();`
  Prepare a `Set` to collect column names for quick lookup.

* `while (rs.next()) cols.add(rs.getString("name"));`
  Iterate through the `ResultSet` and add each column name to the set. `rs.getString("name")` returns the column name in the schema row.

* `if (!cols.contains("payment_method")) st.execute("ALTER TABLE entries ADD COLUMN payment_method TEXT");`
  For each new column we want (payment_method, tags, recurring, notes), check if it exists; if not, `ALTER TABLE ... ADD COLUMN ...`. This keeps older databases compatible and upgrades schema on first run.

  Important detail: SQLite supports `ALTER TABLE ADD COLUMN` but it only allows adding columns at the end and they will be null/default for existing rows. Also `DEFAULT` is used for `recurring` so older rows get `0`.

* (similar `if` checks for `tags`, `recurring`, `notes`)

* `} catch (SQLException ex) {`
  Catch any SQL errors (permission issues, malformed SQL, file locked, etc.)

* `JOptionPane.showMessageDialog(this, "DB init failed: "+ex.getMessage());`
  Show a dialog to the user if DB initialization fails — useful for debugging/teaching in viva.

**Why this approach?**

* Keeps the app backward-compatible: if you change the code later and add fields, existing `finance.db` files won't break — `initDB()` will add missing columns automatically.
* Try-with-resources avoids leaks.

**Gotchas to tell your teammate**

* If `finance.db` is opened by another process or is read-only, `CREATE` / `ALTER` can fail.
* `PRAGMA table_info` is SQLite-specific (works fine here).
* `ALTER TABLE` won't add NOT NULL columns without defaults — we avoid that complexity.

---

## 2) `addEntryToDB(...)`

```java
private void addEntryToDB(String date, String type, String category, double amount, String desc, String payment, String tags, boolean recurring, String notes) {
    String sql = "INSERT INTO entries(date,type,category,amount,description,payment_method,tags,recurring,notes) VALUES(?,?,?,?,?,?,?,?,?)";
    try (Connection conn = DriverManager.getConnection(DB_URL);
         PreparedStatement ps = conn.prepareStatement(sql)) {
        ps.setString(1, date);
        ps.setString(2, type);
        ps.setString(3, category);
        ps.setDouble(4, amount);
        ps.setString(5, desc);
        ps.setString(6, payment);
        ps.setString(7, tags);
        ps.setInt(8, recurring ? 1 : 0);
        ps.setString(9, notes);
        ps.executeUpdate();
    } catch (SQLException ex) {
        JOptionPane.showMessageDialog(this, "Insert failed: "+ex.getMessage());
    }
}
```

### Line-by-line explanation

* `private void addEntryToDB(... ) {`
  Method signature — parameters are the form fields to persist.

* `String sql = "INSERT INTO entries(... ) VALUES(?,?,?,?,?,?,?,?,?)";`
  Use a parameterized INSERT statement with `?` placeholders to avoid SQL injection and to let JDBC handle escaping.

* `try (Connection conn = DriverManager.getConnection(DB_URL); PreparedStatement ps = conn.prepareStatement(sql)) {`
  Try-with-resources opening a connection and preparing a statement. This ensures both resources close automatically.

* `ps.setString(1, date);` ... `ps.setString(9, notes);`
  Bind each method parameter into the prepared statement in sequence:

  1. date → TEXT
  2. type → TEXT
  3. category → TEXT
  4. amount → REAL (setDouble)
  5. desc → TEXT
  6. payment → TEXT
  7. tags → TEXT
  8. recurring → INTEGER (we set 1 or 0)
  9. notes → TEXT

* `ps.executeUpdate();`
  Executes the INSERT. For DML statements `executeUpdate()` returns the number of affected rows (we ignore it).

* `} catch (SQLException ex) { JOptionPane.showMessageDialog(this, "Insert failed: "+ex.getMessage()); }`
  If insertion fails (constraint, disk full, bad types), show an error dialog.

**Why prepared statements?**

* Prevent SQL injection and handle quoting.
* Slight performance benefit for repeated operations.
* Cleaner binding of Java types to SQL types.

**Gotchas**

* If `date` is empty or malformed, it will still be stored as TEXT; you may want validation before calling this method.
* If `amount` is NaN/Infinity or driver can't handle value, `setDouble` may fail — but we validate in UI (`tfAmount`) so it's typically okay.

---

## 3) `updateEntryInDB(...)`

```java
private void updateEntryInDB(int id, String date, String type, String category, double amount, String desc, String payment, String tags, boolean recurring, String notes) {
    String sql = "UPDATE entries SET date=?,type=?,category=?,amount=?,description=?,payment_method=?,tags=?,recurring=?,notes=? WHERE id=?";
    try (Connection conn = DriverManager.getConnection(DB_URL);
         PreparedStatement ps = conn.prepareStatement(sql)) {
        ps.setString(1, date); ps.setString(2, type); ps.setString(3, category); ps.setDouble(4, amount); ps.setString(5, desc);
        ps.setString(6, payment); ps.setString(7, tags); ps.setInt(8, recurring?1:0); ps.setString(9, notes); ps.setInt(10, id);
        ps.executeUpdate();
    } catch (SQLException ex) {
        JOptionPane.showMessageDialog(this, "Update failed: "+ex.getMessage());
    }
}
```

### Line-by-line explanation

* `private void updateEntryInDB(int id, ... ) {`
  Update method receives the `id` of the row to modify plus the new column values.

* `String sql = "UPDATE entries SET ... WHERE id=?";`
  Parameterized UPDATE statement. The `WHERE id=?` ensures only the intended row is updated.

* `try (Connection conn = DriverManager.getConnection(DB_URL); PreparedStatement ps = conn.prepareStatement(sql)) {`
  Open connection & prepare statement using try-with-resources.

* `ps.setString(1, date); ... ps.setInt(10, id);`
  Bind parameters in the exact order of `?` placeholders. Note: `id` is the **last** parameter (10th).

* `ps.executeUpdate();`
  Runs the UPDATE; returns count of updated rows.

* `} catch (SQLException ex) { JOptionPane.showMessageDialog(this, "Update failed: "+ex.getMessage()); }`
  Error handling.

**Why check order carefully?**

* Parameter index must match `?` order; mixing them up results in wrong values or SQL errors.

**Gotchas**

* If the `id` doesn't exist, no row will be updated; you might want to check `int updated = ps.executeUpdate();` and alert if `updated == 0`.
* Concurrent edits: two clients editing same row could cause last-writer-wins; for this app that's acceptable.

---

## 4) `deleteEntryFromDB(int id)`

```java
private void deleteEntryFromDB(int id) {
    String sql = "DELETE FROM entries WHERE id=?";
    try (Connection conn = DriverManager.getConnection(DB_URL);
         PreparedStatement ps = conn.prepareStatement(sql)) {
        ps.setInt(1, id);
        ps.executeUpdate();
    } catch (SQLException ex) {
        JOptionPane.showMessageDialog(this, "Delete failed: "+ex.getMessage());
    }
}
```

### Line-by-line explanation

* `private void deleteEntryFromDB(int id) {`
  Delete a row identified by `id`.

* `String sql = "DELETE FROM entries WHERE id=?";`
  Parameterized DELETE to avoid string concatenation mistakes.

* `try (Connection conn = DriverManager.getConnection(DB_URL); PreparedStatement ps = conn.prepareStatement(sql)) {`
  Open connection & prepare statement.

* `ps.setInt(1, id);`
  Bind the id.

* `ps.executeUpdate();`
  Execute the delete; returns number of deleted rows.

* `} catch (SQLException ex) { JOptionPane.showMessageDialog(this, "Delete failed: "+ex.getMessage()); }`
  Show error if deletion fails.

**Notes**

* No confirm logic in DB method — confirmation happens in UI before calling delete.
* If `id` doesn't exist, `executeUpdate()` returns 0 — safe but silent; UI code should ensure user selected an existing row.

---
# Section 3 — Application Logic & Event Handling

We'll cover these methods in order:

* `loadEntries(String search, String dateFrom, String dateTo, String minAmt, String maxAmt)`
* `applyFilters()`
* `clearFilters()`
* `updateTotals()`
* `onAdd()`
* `onUpdate()`
* `clearForm()`
* `loadSelectedRowToForm()`
* `refreshAndTotals()`
* `main(String[] args)`

---

## 1) `loadEntries(...)`

```java
private void loadEntries(String search, String dateFrom, String dateTo, String minAmt, String maxAmt) {
    tableModel.setRowCount(0);
    StringBuilder sql = new StringBuilder("SELECT id,date,type,category,amount,payment_method,tags,recurring,description FROM entries");
    java.util.List<String> where = new java.util.ArrayList<>();
    if (search != null && !search.isEmpty()) where.add("(description LIKE ? OR tags LIKE ?)");
    if (dateFrom != null && !dateFrom.isEmpty()) where.add("date >= ?");
    if (dateTo != null && !dateTo.isEmpty()) where.add("date <= ?");
    if (minAmt != null && !minAmt.isEmpty()) where.add("amount >= ?");
    if (maxAmt != null && !maxAmt.isEmpty()) where.add("amount <= ?");

    // Type & category filters from comboboxes (applied separately)
    String typeFilter = (String) fType.getSelectedItem();
    String catFilter = (String) fCategory.getSelectedItem();
    if (!"All".equalsIgnoreCase(typeFilter)) where.add("type = '"+typeFilter+"'");
    if (!"All".equalsIgnoreCase(catFilter)) where.add("category = '"+catFilter+"'");

    if (!where.isEmpty()) {
        sql.append(" WHERE ");
        sql.append(String.join(" AND ", where));
    }
    sql.append(" ORDER BY date DESC");

    try (Connection conn = DriverManager.getConnection(DB_URL);
         PreparedStatement ps = conn.prepareStatement(sql.toString())) {
        int idx = 1;
        if (search != null && !search.isEmpty()) { ps.setString(idx++, "%"+search+"%"); ps.setString(idx++, "%"+search+"%"); }
        if (dateFrom != null && !dateFrom.isEmpty()) ps.setString(idx++, dateFrom);
        if (dateTo != null && !dateTo.isEmpty()) ps.setString(idx++, dateTo);
        if (minAmt != null && !minAmt.isEmpty()) ps.setString(idx++, minAmt);
        if (maxAmt != null && !maxAmt.isEmpty()) ps.setString(idx++, maxAmt);

        ResultSet rs = ps.executeQuery();
        while (rs.next()) {
            Object[] row = new Object[]{ rs.getInt("id"), rs.getString("date"), rs.getString("type"), rs.getString("category"), String.format("%.2f", rs.getDouble("amount")), rs.getString("payment_method"), rs.getString("tags"), rs.getInt("recurring")==1?"Yes":"No", rs.getString("description") };
            tableModel.addRow(row);
        }
    } catch (SQLException ex) {
        JOptionPane.showMessageDialog(this, "Load failed: "+ex.getMessage());
    }
}
```

### Explanation — block / line by line

* `private void loadEntries(...) {`
  Method loads rows from DB into the `tableModel`. Called from UI actions (constructor, applyFilters, clearFilters, onAdd, onUpdate, refresh).

* `tableModel.setRowCount(0);`
  Clears the current table rows. Reset before re-populating to avoid duplicates.

* `StringBuilder sql = new StringBuilder("SELECT ... FROM entries");`
  Base SQL selecting fields we want to show. We use `StringBuilder` since we will append WHERE clauses dynamically.

* `java.util.List<String> where = new java.util.ArrayList<>();`
  A list of WHERE clause snippets to concatenate later. Using a list avoids dealing with leading `AND`/`WHERE` logic.

* `if (search != null && !search.isEmpty()) where.add("(description LIKE ? OR tags LIKE ?)");`
  If search text was provided, add a condition that checks description or tags using `LIKE`. We use `?` placeholders to bind values later (prevents SQL injection).

* Date & amount filters add conditions similarly (`date >= ?`, `amount >= ?`, etc.).
  Note: Dates are compared lexicographically since stored as `YYYY-MM-DD` — this works correctly for date ranges.

* `String typeFilter = (String) fType.getSelectedItem();`
  Read the Type combobox from the UI (top filters). This is applied directly into the WHERE list **as a literal** below.

* `if (!"All".equalsIgnoreCase(typeFilter)) where.add("type = '"+typeFilter+"'");`
  If the user selected a specific Type (not All), we append a condition for `type`. **Important:** here we inject the filter value directly into SQL string (not via `?`). This is safe because the combobox values are hard-coded (All, Expense, Income). If you later make combobox editable, change to parameterized binding.

* Same for category filter.

* `if (!where.isEmpty()) { sql.append(" WHERE "); sql.append(String.join(" AND ", where)); }`
  If there are any conditions, append them joined by `AND`. This produces a valid WHERE clause with multiple conditions.

* `sql.append(" ORDER BY date DESC");`
  Orders most recent entries first.

* `try (Connection conn = DriverManager.getConnection(DB_URL); PreparedStatement ps = conn.prepareStatement(sql.toString())) {`
  Open connection & prepare statement. Using try-with-resources so both close automatically.

* `int idx = 1;`
  Parameter index for `ps.setX(...)` calls — JDBC is 1-based.

* For each optional parameter, if present, bind it to the prepared statement in the same order they were added to `where`. Example:

  * `ps.setString(idx++, "%"+search+"%");` twice for the two `LIKE` placeholders.
  * Dates and amounts bound as strings (we use `setString` for amounts too — it works, but `setDouble` would also be fine if we converted).

* `ResultSet rs = ps.executeQuery();`
  Execute SELECT and get results.

* `while (rs.next()) { Object[] row = ...; tableModel.addRow(row); }`
  For each result row, read fields by column name and format amount as `String.format("%.2f", rs.getDouble("amount"))`. Convert `recurring` integer to `"Yes"`/`"No"` for display. Then add the resulting `Object[]` to `tableModel`.

* `} catch (SQLException ex) { JOptionPane.showMessageDialog(this, "Load failed: "+ex.getMessage()); }`
  Show an error dialog if anything goes wrong (SQL syntax, DB locked, etc.).

### Notes & gotchas

* **Parameter order matters**: the code sets parameters in the same logical order as `where` entries were added. If you change `where` order, update bindings accordingly.
* **Type safety**: amounts are compared using numeric operators in SQL, but you bind as string; SQLite will do type coercion. Safer to use `ps.setDouble(...)` for numeric parameters.
* **Combo filters injected as literals**: safe here because values are controlled; if you make them editable, switch to `?` parameters to avoid SQL injection.
* **Performance**: For many rows, consider pagination. For now this is fine for small datasets.

---

## 2) `applyFilters()` and `clearFilters()`

```java
private void applyFilters() {
    String search = fSearch.getText().trim();
    String from = fDateFrom.getText().trim();
    String to = fDateTo.getText().trim();
    String min = fMinAmt.getText().trim();
    String max = fMaxAmt.getText().trim();
    loadEntries(search, from, to, min, max);
    lblStatus.setText("Filters applied");
    updateTotals();
}
```

### Explanation

* `String search = fSearch.getText().trim();` — read top filter fields from UI components and trim whitespace.
* `loadEntries(search, from, to, min, max);` — call `loadEntries()` passing these values to re-query DB and refresh table.
* `lblStatus.setText("Filters applied");` — update the status bar so the user knows action succeeded.
* `updateTotals();` — recalc and update totals based on the entire DB (note: `updateTotals()` currently uses the whole `entries` table, not the visible subset — we’ll note that behavior later).

```java
private void clearFilters() {
    fType.setSelectedIndex(0); fCategory.setSelectedIndex(0); fDateFrom.setText(""); fDateTo.setText(""); fSearch.setText(""); fMinAmt.setText(""); fMaxAmt.setText("");
    loadEntries("", "", "", "", "");
    lblStatus.setText("Filters cleared");
    updateTotals();
}
```

### Explanation

* Reset all filter UI components to defaults (Type=All, Category=All, empty date/amount/search).
* `loadEntries("", "", "", "", "");` — reloads full dataset.
* Update status & totals.

### Notes

* If you want totals to reflect the current filtered view instead of full DB, you can modify `updateTotals()` to accept optional filter parameters and compute totals on the same WHERE clause (simple enhancement).

---

## 3) `updateTotals()`

```java
private void updateTotals() {
    double income = 0.0, expense = 0.0;
    String sql = "SELECT type, SUM(amount) as total FROM entries GROUP BY type";
    try (Connection conn = DriverManager.getConnection(DB_URL);
         Statement st = conn.createStatement();
         ResultSet rs = st.executeQuery(sql)) {
        while (rs.next()) {
            String type = rs.getString("type");
            double t = rs.getDouble("total");
            if ("Income".equalsIgnoreCase(type)) income = t;
            else if ("Expense".equalsIgnoreCase(type)) expense = t;
        }
    } catch (SQLException ex) {
        // ignore
    }
    lblIncomeTotal.setText(String.format("Income: %.2f", income));
    lblExpenseTotal.setText(String.format("Expense: %.2f", expense));
    lblBalance.setText(String.format("Balance: %.2f", income - expense));
}
```

### Explanation

* `double income = 0.0, expense = 0.0;` — initialize accumulators.
* `String sql = "SELECT type, SUM(amount) as total FROM entries GROUP BY type";` — get aggregated totals grouped by `type`.
* `try (Connection conn = ...; Statement st = conn.createStatement(); ResultSet rs = st.executeQuery(sql)) {` — open connection, execute query.
* `while (rs.next()) { String type = rs.getString("type"); double t = rs.getDouble("total"); ... }` — pick totals for Income and Expense and assign to variables.
* `lblIncomeTotal.setText(...)` etc. — update UI labels with formatted totals.

### Notes & gotchas

* This computes totals across all DB records (not filtered). If you want filtered totals, build a similar query using the same WHERE clause as `loadEntries()`.
* If you store amounts with inconsistent signs (e.g., negative expenses instead of type), this grouping may not work — current design stores type separately and stores positive amounts.

---

## 4) `onAdd()`

```java
private void onAdd() {
    String type = (String) cbType.getSelectedItem();
    String category = (String) cbCategory.getSelectedItem();
    Number num = (Number) tfAmount.getValue(); double amount = (num==null)?0.0:num.doubleValue();
    if (amount <= 0) { JOptionPane.showMessageDialog(this, "Enter a positive amount"); return; }
    String payment = (String) cbPayment.getSelectedItem();
    String date = tfDate.getText().trim();
    String tags = tfTags.getText().trim();
    boolean recurring = cbRecurring.isSelected();
    String desc = tfDescription.getText().trim();
    String notes = taNotes.getText().trim();

    addEntryToDB(date, type, category, amount, desc, payment, tags, recurring, notes);
    loadEntries("", "", "", "", ""); updateTotals(); lblStatus.setText("Added entry"); clearForm();
}
```

### Explanation

* Reads all form input fields into local variables.
* `Number num = (Number) tfAmount.getValue(); double amount = (num==null)?0.0:num.doubleValue();` — reads formatted amount safely and converts to `double`. If no value, default 0.
* `if (amount <= 0) { ... return; }` — basic validation to prevent zero/negative amounts. Shows dialog and aborts add if invalid.
* `addEntryToDB(...)` — call DB method to insert the new row.
* `loadEntries("", "", "", "", "")` — reload table to show new row.
* `updateTotals()` — recompute totals.
* `lblStatus.setText("Added entry")` — show message.
* `clearForm()` — reset UI form to defaults.

### Notes

* Additional validation you could add: date format check, max description length, tags format, etc.
* `addEntryToDB(...)` will throw SQLException which is handled inside that method — UI method just assumes success. You may want to check and show a message based on insertion success.

---

## 5) `onUpdate()`

```java
private void onUpdate() {
    int row = table.getSelectedRow();
    if (row == -1) { JOptionPane.showMessageDialog(this, "Select a row to update (double-click to load)"); return; }
    int id = Integer.parseInt(tableModel.getValueAt(row, 0).toString());
    String type = (String) cbType.getSelectedItem();
    String category = (String) cbCategory.getSelectedItem();
    Number num = (Number) tfAmount.getValue(); double amount = (num==null)?0.0:num.doubleValue();
    String payment = (String) cbPayment.getSelectedItem();
    String date = tfDate.getText().trim();
    String tags = tfTags.getText().trim();
    boolean recurring = cbRecurring.isSelected();
    String desc = tfDescription.getText().trim();
    String notes = taNotes.getText().trim();

    updateEntryInDB(id, date, type, category, amount, desc, payment, tags, recurring, notes);
    loadEntries("", "", "", "", ""); updateTotals(); lblStatus.setText("Updated id="+id); clearForm();
}
```

### Explanation

* `int row = table.getSelectedRow();` — get currently selected row index in the table.
* If no row selected, show dialog and return.
* `int id = Integer.parseInt(tableModel.getValueAt(row, 0).toString());` — read the ID from the selected table row (first column). This `id` maps to DB primary key.
* Read form fields same as in `onAdd()`.
* `updateEntryInDB(...)` — call DB update method, passing `id` + new values.
* After update, reload entries, update totals, set status, and clear form.

### Notes & gotchas

* Typical flow: the user double-clicks a row (`loadSelectedRowToForm()` loads fields), then edits fields and clicks **Update**.
* If the user edits fields without loading a row, `onUpdate()` will fail because no row selected.
* You might want to warn user if `amount <= 0` similarly to `onAdd()` — current code doesn’t re-check that; you can add validation.

---

## 6) `clearForm()`

```java
private void clearForm() {
    cbType.setSelectedIndex(0);
    cbCategory.setSelectedIndex(0);
    cbPayment.setSelectedIndex(0);
    tfAmount.setValue(0.00);
    tfDescription.setText("");
    tfDate.setText(new SimpleDateFormat("yyyy-MM-dd").format(new Date()));
    tfTags.setText("");
    cbRecurring.setSelected(false);
    taNotes.setText("");
}
```

### Explanation

* Reset every form field to sensible defaults:

  * Combo boxes to first item (usually Expense/Cash).
  * Amount to 0.00.
  * Description, tags, notes cleared.
  * Date reset to today's date.
  * Recurring unchecked.

This is used after Add/Update or when user clicks Clear.

---

## 7) `loadSelectedRowToForm()`

```java
private void loadSelectedRowToForm() {
    int row = table.getSelectedRow(); if (row == -1) return;
    int id = Integer.parseInt(tableModel.getValueAt(row, 0).toString());
    try (Connection conn = DriverManager.getConnection(DB_URL);
         PreparedStatement ps = conn.prepareStatement("SELECT * FROM entries WHERE id=?")) {
        ps.setInt(1, id);
        ResultSet rs = ps.executeQuery();
        if (rs.next()) {
            cbType.setSelectedItem(rs.getString("type"));
            cbCategory.setSelectedItem(rs.getString("category"));
            tfAmount.setValue(rs.getDouble("amount"));
            cbPayment.setSelectedItem(rs.getString("payment_method")!=null?rs.getString("payment_method"):"Cash");
            tfDate.setText(rs.getString("date"));
            tfTags.setText(rs.getString("tags"));
            cbRecurring.setSelected(rs.getInt("recurring")==1);
            tfDescription.setText(rs.getString("description"));
            taNotes.setText(rs.getString("notes"));
            lblStatus.setText("Loaded id="+id+" into form");
        }
    } catch (SQLException ex) { JOptionPane.showMessageDialog(this, "Load row failed: "+ex.getMessage()); }
}
```

### Explanation

* Get selected table row; if none selected, return.
* Read `id` from first column.
* Query DB for the full row matching `id` using parameterized query `"SELECT * FROM entries WHERE id=?"`.
* `ps.setInt(1, id);` — bind id.
* `ResultSet rs = ps.executeQuery(); if (rs.next()) { ... }` — if row exists, populate form fields from DB columns (type, category, amount, payment_method, date, tags, recurring, description, notes).
* For `payment_method` we handle potential `null` by defaulting to `"Cash"` when `rs.getString(...)` returns null.
* `cbRecurring.setSelected(rs.getInt("recurring")==1);` — convert stored integer to boolean.
* Update `lblStatus` to reflect the loaded id.

### Notes

* This method is bound to the JTable double-click mouse handler (so user double-clicks a row to start editing).
* Good UX tip: after loading into form, you might focus the first input or scroll to the right panel.

---

## 8) `refreshAndTotals()` and `main()`

```java
public void refreshAndTotals() { loadEntries("", "", "", "", ""); updateTotals(); }
```

* Simple helper to reload full dataset and recompute totals. Used when you want a quick refresh.

```java
public static void main(String[] args) {
    SwingUtilities.invokeLater(() -> new PersonalFinanceTracker().setVisible(true));
}
```

### Explanation

* `SwingUtilities.invokeLater(...)` schedules the Runnable on Swing's Event Dispatch Thread (EDT). All Swing UI operations must happen on EDT to avoid concurrency bugs.
* Inside the Runnable we create a new `PersonalFinanceTracker()` instance (constructor runs initDB, initUI, loadEntries, updateTotals) and then call `.setVisible(true)` to show the frame.

---
# 1) Field mapping table

| UI label / location                  |                                  Java variable (in code) | DB column name   | Notes                                 |
| ------------------------------------ | -------------------------------------------------------: | ---------------- | ------------------------------------- |
| Type (Expense/Income) — form (right) |                      `cbType.getSelectedItem()` → `type` | `type`           | stored as TEXT                        |
| Category — form                      |              `cbCategory.getSelectedItem()` → `category` | `category`       | TEXT                                  |
| Amount — form                        |       `(Number) tfAmount.getValue()` → `amount` (double) | `amount`         | REAL                                  |
| Description — form                   |                       `tfDescription.getText()` → `desc` | `description`    | TEXT                                  |
| Payment Method — form                |                `cbPayment.getSelectedItem()` → `payment` | `payment_method` | TEXT                                  |
| Tags — form                          |                              `tfTags.getText()` → `tags` | `tags`           | TEXT (comma/space separated)          |
| Recurring — form                     | `cbRecurring.isSelected()` → `recurring` (boolean → 1/0) | `recurring`      | INTEGER (1 for true, 0 for false)     |
| Notes — form                         |                            `taNotes.getText()` → `notes` | `notes`          | TEXT                                  |
| Date — form                          |        `tfDate.getText()` → `date` (string `YYYY-MM-DD`) | `date`           | TEXT; current design stores as string |

---

# 2) Exact parameter order — **INSERT** (addEntryToDB)

SQL used:

```sql
INSERT INTO entries(date,type,category,amount,description,payment_method,tags,recurring,notes)
VALUES(?,?,?,?,?,?,?,?,?)
```

Parameter binding order (index → value):

1. `ps.setString(1, date);`             // `date`
2. `ps.setString(2, type);`             // `type`
3. `ps.setString(3, category);`         // `category`
4. `ps.setDouble(4, amount);`           // `amount`
5. `ps.setString(5, desc);`             // `description`
6. `ps.setString(6, payment);`          // `payment_method`
7. `ps.setString(7, tags);`             // `tags`
8. `ps.setInt(8, recurring ? 1 : 0);`   // `recurring` (int)
9. `ps.setString(9, notes);`            // `notes`

````

So the call in `onAdd()` should gather the variables in exactly that order and call `addEntryToDB(date,type,category,amount,desc,payment,tags,recurring,notes)`.

---

# 3) Exact parameter order — **UPDATE** (updateEntryInDB)

SQL used:
```sql
UPDATE entries
SET date=?,type=?,category=?,amount=?,description=?,payment_method=?,tags=?,recurring=?,notes=?
WHERE id=?
````

Parameter binding order (index → value):

1. `ps.setString(1, date);`
2. `ps.setString(2, type);`
3. `ps.setString(3, category);`
4. `ps.setDouble(4, amount);`
5. `ps.setString(5, desc);`
6. `ps.setString(6, payment);`
7. `ps.setString(7, tags);`
8. `ps.setInt(8, recurring ? 1 : 0);`
9. `ps.setString(9, notes);`
10. `ps.setInt(10, id);` // WHERE id = ?

So in `onUpdate()` be sure to read the selected row's `id` (first column of table) and pass it as the **last** parameter.

---

# 4) How `loadEntries(...)` parameter binding works (filters)

`loadEntries(String search, String dateFrom, String dateTo, String minAmt, String maxAmt)` builds WHERE parts dynamically and binds `?` in the same order they were added.

Important details (the code logic you already have):

* The WHERE parts are added in this order (if the filter value is present):

  1. `(description LIKE ? OR tags LIKE ?)` — **two placeholders**, bound as `%search%`, then `%search%`
  2. `date >= ?` — bound as `dateFrom`
  3. `date <= ?` — bound as `dateTo`
  4. `amount >= ?` — bound as `minAmt` (string currently; consider using `setDouble`)
  5. `amount <= ?` — bound as `maxAmt`
* **Plus** two possible literal filters appended directly:

  * `type = 'Expense'` or `type = 'Income'` — if `fType` is not `All` (these are inserted directly as string literals because combobox values are controlled)
  * `category = 'Food'` etc. — if `fCategory` is not `All`

So the binding loop does:

```java
int idx = 1;
if (search not empty) { ps.setString(idx++, "%"+search+"%"); ps.setString(idx++, "%"+search+"%"); }
if (dateFrom not empty) ps.setString(idx++, dateFrom);
if (dateTo not empty) ps.setString(idx++, dateTo);
if (minAmt not empty) ps.setString(idx++, minAmt); // consider ps.setDouble
if (maxAmt not empty) ps.setString(idx++, maxAmt);
```

**Key point:** If you change which `where.add(...)` lines appear or their order, you MUST change the binding order accordingly. Always keep generation order == binding order.

---

# 5) Practical example — full flow when user clicks **Add**

1. User fills form: chooses Type, Category, sets Amount, Date, Payment, Tags, toggles Recurring, types Notes/Description.
2. `onAdd()` reads values:

   ```java
   String type = (String) cbType.getSelectedItem();
   String category = (String) cbCategory.getSelectedItem();
   Number num = (Number) tfAmount.getValue();
   double amount = (num == null) ? 0.0 : num.doubleValue();
   String desc = tfDescription.getText().trim();
   String date = tfDate.getText().trim();
   String payment = (String) cbPayment.getSelectedItem();
   String tags = tfTags.getText().trim();
   boolean recurring = cbRecurring.isSelected();
   String notes = taNotes.getText().trim();
   ```
3. `onAdd()` validates `amount > 0` (and any other rules you add).
4. Calls `addEntryToDB(date, type, category, amount, desc, payment, tags, recurring, notes);`
5. `addEntryToDB(...)` prepares the INSERT and binds parameters 1..9 in *exact* order shown above, then `executeUpdate()`.
6. After success, UI reloads table: `loadEntries("", "", "", "", "");` and `updateTotals();`; status label updated.

---

# 6) Practical example — full flow when user clicks **Update**

1. User double-clicks a table row → `loadSelectedRowToForm()`:

   * It reads the `id` from the selected row: `int id = Integer.parseInt(tableModel.getValueAt(row, 0).toString());`
   * Queries DB: `SELECT * FROM entries WHERE id=?` and fills the form fields with DB values.
2. User edits fields (eg. amount or notes).
3. Click **Update** → `onUpdate()`:

   * Reads the form fields (same as Add).
   * Reads `id` from selected row again (important!).
   * Calls `updateEntryInDB(id, date, type, category, amount, desc, payment, tags, recurring, notes)` — note parameter order: id passed last.
4. `updateEntryInDB(...)` binds values 1..10 per the UPDATE parameter list and executes.

---
