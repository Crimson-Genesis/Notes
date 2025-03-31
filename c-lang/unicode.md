You can find all **box-drawing characters** in the **Unicode Box Drawing** block. Here’s where to look:

### **1. Unicode Table**
Visit [Unicode Box Drawing Characters](https://www.unicode.org/charts/PDF/U2500.pdf) (Official Unicode PDF) to see all available characters.

### **2. Wikipedia**
Check out the [Box-drawing characters](https://en.wikipedia.org/wiki/Box-drawing_character) page on Wikipedia.

### **3. Copy from Online Unicode Tools**
You can copy characters from:
- [Unicode Table](https://www.unicode-table.com/en/blocks/box-drawing/)  
- [Compart Box Drawing Characters](https://www.compart.com/en/unicode/block/U+2500)

### **4. Unicode Code Points**
If you want to insert these characters in C using their Unicode values, you can use `\u` or `\x` escape sequences in `wprintf` (for wide characters).

#### **Common Box-Drawing Characters**
| Character | Unicode | Description |
|-----------|---------|-------------|
| `─` | `\u2500` | Horizontal line |
| `│` | `\u2502` | Vertical line |
| `┌` | `\u250C` | Top-left corner |
| `┐` | `\u2510` | Top-right corner |
| `└` | `\u2514` | Bottom-left corner |
| `┘` | `\u2518` | Bottom-right corner |
| `├` | `\u251C` | Left tee |
| `┤` | `\u2524` | Right tee |
| `┬` | `\u252C` | Top tee |
| `┴` | `\u2534` | Bottom tee |
| `┼` | `\u253C` | Cross |

### **5. Typing in Linux Terminal**
- In **GTK apps** (like Gedit, Terminal), press `Ctrl+Shift+U`, then type the **Unicode code** (`250C` for `┌`) and press `Enter`.
- In **Vim/Neovim**, insert Unicode by typing `Ctrl+V u250C`.
- In **Alacritty, Kitty, or other Unicode-supported terminals**, you can directly copy-paste these characters.

