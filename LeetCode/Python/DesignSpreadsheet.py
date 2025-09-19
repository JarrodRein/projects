class Spreadsheet:
    def __init__(self, rows: int):
        # Keep only the explicitly set values. Unset cells are implicitly 0.
        self.cells = {}   # key: cell string like "A1", value: int

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        # Reset to 0 (considered explicitly set to 0)
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        # formula is always "X+Y"
        formula = formula.lstrip('=')
        left, right = formula.split('+', 1)

        def eval_term(t: str) -> int:
            t = t.strip()
            # If it has any letter, we treat it as a cell reference
            if any(ch.isalpha() for ch in t):
                return self.cells.get(t, 0)
            # Otherwise it must be an integer (may have + or - sign)
            return int(t)

        return eval_term(left) + eval_term(right)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)