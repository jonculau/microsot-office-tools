# unknow_pass
Unprotected-Sheet Script: This script is designed to remove the password protection from all sheets within a workbook. Additionally, it creates a recovery.json file containing XML protection tags for each sheet. To use this script, execute the following command:
```bash
py unprotected-sheet.py <file.xlsx>
```
The second script, protected-sheet.py, uses the recovery.json file generated by the first script to restore the password protection for each sheet within the workbook. To utilize this script, run the following command:
```bash
py protected-sheet.py <file.xlsx> <recovery.json>
```
