If you have made two commits in Git but haven't pushed them yet, you can easily remove them using the following steps:

### To remove the most recent commit:
1. **Use `git reset`**:
   ```bash
   git reset --soft HEAD~1
   ```
   This will remove the last commit but keep the changes in the staging area, allowing you to modify them or recommit if needed.

---

### To remove the last two commits:
1. **Use `git reset`**:
   ```bash
   git reset --soft HEAD~2
   ```
   This will remove the last two commits, keeping the changes staged.

---

### To discard the commits and the changes:
1. Use the `--hard` option if you want to completely discard the commits and their changes:
   ```bash
   git reset --hard HEAD~2
   ```
   ⚠️ This will permanently delete the changes, so be cautious.

---

### To safely keep the changes but remove commits:
1. Use the `--mixed` option to keep the changes unstaged (in the working directory):
   ```bash
   git reset --mixed HEAD~2
   ```

---

### For safety:
- If you're unsure, you can create a backup branch before resetting:
  ```bash
  git branch backup-branch-name
  ```

Would you like to proceed with any of these, or do you need further assistance?
