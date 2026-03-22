function Table({ data}) {
  const renderedRows = data.map((fruit) => {
    return (
      <tr className="border-b" key={fruit.name}>
        <td className="p-3">{fruit.name}</td>
        <td className="p-3">
            <div className={`p-3 m-2 ${fruit.color}`}></div>
        </td>
        <td className="p-3">{fruit.score}</td>
      </tr>
    )
  })

  return (
    <table className="table-auto border-spacing-2">
        <thead>
            <tr className="border-b-2">
                <th>Fruits</th>
                <th>Color</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>
            {renderedRows}
        </tbody>
    </table>
  )
}

export default Table;