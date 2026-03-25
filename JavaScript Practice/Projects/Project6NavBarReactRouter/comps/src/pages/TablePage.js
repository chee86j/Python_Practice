import Table from '../components/Table'

/* TablePage provides row data plus a column config object to the reusable Table component.
   Each config item defines a label, a render function for cell content, and an optional custom header.
   keyFn returns a stable unique value for each row so React can track row updates correctly. 
*/
function TablePage() {
  const data = [
    {name: 'Orange', color: 'bg-orange-500', score: 5},
    {name: 'Apple', color: 'bg-red-500', score: 3},
    {name: 'Banana', color: 'bg-yellow-500', score: 1},
    {name: 'Lime', color: 'bg-green-500', score: 4},
  ]

  /* The purpose of the config array is to define how each column in the table should be rendered. 
  Each object in the config array represents a column and contains:
- label: The header text for the column.
- render: A function that takes a data item (in this case, a fruit) and returns the content to be displayed in the cell for that column.
- header (optional): A function that returns custom JSX for the column header, allowing for more complex header designs beyond just text.
*/
  const config = [
    { 
        label: 'Name',
        render: (fruit) => fruit.name
     },
    { 
        label: 'Color',
        render: (fruit) => <div className={`p-3 m-2 ${fruit.color}`} />
    },
    { 
        label: 'Score',
        render: (fruit) => fruit.score,
        header: () => <th className="bg-red-500">Score</th>,
    },
  ]

  const keyFn = (fruit) => {
    return fruit.name
  }

  return (
    <div>
        <Table data={data} config={config} keyFn={keyFn} />
    </div>
    )
}

export default TablePage
