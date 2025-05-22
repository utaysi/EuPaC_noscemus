## Brief overview
This rule outlines preferences for interacting with Jupyter Notebooks (`.ipynb` files). The primary goal is to avoid the generation of output cells or execution counts by Cline, as the user will run the notebooks themselves to produce these. This helps in keeping the notebook files clean and reduces unnecessary resource usage during generation.

## Jupyter Notebook Development
- When adding new code cells to a Jupyter Notebook:
  - Only provide the `source` content for the new cell.
  - Set `outputs` to an empty list (`[]`).
  - Set `execution_count` to `null` (or omit it if the schema allows, but `null` is safer for existing structures).
  - A new `id` for the cell can be generated (e.g., using a pattern like `cline-new-cell-<timestamp>`).
- When modifying existing code cells using `replace_in_file`:
  - Focus changes on the `source` array.
  - If the `SEARCH` block includes `outputs` or `execution_count`, the `REPLACE` block should generally preserve these as they are unless the specific instruction is to clear them. The main objective is to not *introduce new* or *regenerate existing* outputs.
- **Example of a new code cell to be added:**
  ```json
  {
   "cell_type": "code",
   "id": "cline-new-cell-example",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"This is a new cell added by Cline.\")"
   ],
   "execution_count": null
  }
  ```
- **Avoid generating content for `outputs` or setting a numerical `execution_count` for any cells you introduce or modify unless explicitly asked to reproduce a specific state that includes them.**
