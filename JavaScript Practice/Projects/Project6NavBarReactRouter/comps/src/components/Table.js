function Table({ data, config }) {

  const renderedHeaders = config.map((column) => {
    return <th key={column.label}>{column.label}</th>
  })

  const renderedRows = data.map((fruit) => {
    return (
      <tr className="border-b" key={fruit.name}>
        <td className="p-3">{config[0].render(fruit)}</td>
        <td className="p-3">{config[1].render(fruit)}</td>
        <td className="p-3">{config[2].render(fruit)}</td>
      </tr>
    )
  })

  return (
    <table className="table-auto border-spacing-2">
        <thead>
            <tr className="border-b-2">
                {renderedHeaders}
            </tr>
        </thead>
        <tbody>
            {renderedRows}
        </tbody>
    </table>
  )
}

export default Table;